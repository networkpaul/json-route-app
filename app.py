from flask import Flask, request, jsonify, render_template_string, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)

# Directory for storing route files
ROUTES_DIR = 'routes'

# Ensure the routes directory exists
if not os.path.exists(ROUTES_DIR):
    os.makedirs(ROUTES_DIR)

# Load existing data from files
data_store = {}
for filename in os.listdir(ROUTES_DIR):
    if filename.endswith('.json'):
        with open(os.path.join(ROUTES_DIR, filename), 'r') as f:
            key = filename[:-5]  # Remove '.json' from filename
            data_store[key] = json.load(f)

# Save data to file
def save_data(key, data):
    filepath = os.path.join(ROUTES_DIR, f"{key}.json")
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

# Delete data file
def delete_data(key):
    filepath = os.path.join(ROUTES_DIR, f"{key}.json")
    if os.path.exists(filepath):
        os.remove(filepath)
        data_store.pop(key, None)

# Home route to render the form and list all routes
@app.route('/')
def home():
    routes_list = list(data_store.keys())
    return render_template_string('''
        <!doctype html>
        <title>JSON Input</title>
        <h1>Post JSON Data</h1>
        <form action="/post-json" method="post">
            <textarea name="json_data" rows="10" cols="50" placeholder="Enter JSON here"></textarea><br>
            <input type="submit" value="Submit">
        </form>
        <h2>Available Routes</h2>
        <ul>
            {% for route in routes %}
                <li>
                    <a href="/{{ route }}">{{ route }}</a>
                    <form action="/delete-json/{{ route }}" method="post" style="display:inline;">
                        <input type="submit" value="Delete" onclick="return confirm('Are you sure you want to delete this route?');">
                    </form>
                </li>
            {% endfor %}
        </ul>
    ''', routes=routes_list)

# Route to handle JSON data submission
@app.route('/post-json', methods=['POST'])
def post_json():
    try:
        json_data = request.form['json_data']
        parsed_json = json.loads(json_data)

        # Create a unique key with the original key and a timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        original_key = list(parsed_json.keys())[0]
        key_with_timestamp = f"{original_key}_{timestamp}"
        data_store[key_with_timestamp] = parsed_json

        # Save data to a JSON file
        save_data(key_with_timestamp, parsed_json)

        return jsonify({"message": f"JSON stored under key '{key_with_timestamp}'", "data": data_store}), 200

    except (json.JSONDecodeError, IndexError) as e:
        return jsonify({"error": "Invalid JSON"}), 400

# Dynamic route to return JSON data
@app.route('/<key>')
def get_json(key):
    data = data_store.get(key)
    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "Not found"}), 404

# Route to handle JSON data deletion
@app.route('/delete-json/<key>', methods=['POST'])
def delete_json(key):
    delete_data(key)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
