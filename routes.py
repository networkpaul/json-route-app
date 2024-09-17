from flask import request, jsonify, render_template_string, redirect, url_for
import json
from datetime import datetime
from data_store import data_store, save_data, delete_data

def home():
    grouped_routes = {}
    for key in data_store:
        prefix = key.split('_')[0]
        if prefix not in grouped_routes:
            grouped_routes[prefix] = []
        grouped_routes[prefix].append(key)

    return render_template_string('''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>JSON Input</title>
            <script src="https://cdn.tailwindcss.com"></script>
            <style>
                .git-diff {
                    font-family: monospace;
                    white-space: pre-wrap;
                }
                .diff-add {
                    color: green;
                }
                .diff-del {
                    color: red;
                }
            </style>
        </head>
        <body class="bg-gray-100 font-sans leading-normal tracking-normal">
            <div class="container mx-auto px-4">
                <div class="w-full max-w-2xl mx-auto bg-white shadow-lg rounded-lg mt-10 p-8">
                    <h1 class="text-2xl font-bold mb-6">Post JSON Data</h1>
                    <form action="/post-json" method="post">
                        <textarea name="json_data" rows="10" class="w-full p-4 border rounded-lg mb-4" placeholder="Enter JSON here"></textarea>
                        <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                            Submit
                        </button>
                    </form>

                    <h2 class="text-xl font-bold mt-8">Available Routes</h2>
                    {% for category, routes in grouped_routes.items() %}
                        <h3 class="text-lg font-semibold mt-4">{{ category | capitalize }}</h3>
                        <ul class="mt-2">
                            {% for route in routes %}
                                <li class="flex items-center justify-between bg-gray-100 p-2 rounded-lg mb-2">
                                    <a href="/{{ route }}" class="text-blue-500 hover:underline">{{ route }}</a>
                                    <form action="/delete-json/{{ route }}" method="post" style="display:inline;">
                                        <button type="submit" class="bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-3 rounded" onclick="return confirm('Are you sure you want to delete this route?');">
                                            Delete
                                        </button>
                                    </form>
                                </li>
                            {% endfor %}
                        </ul>
                    {% endfor %}
                </div>
            </div>
        </body>
        </html>
    ''', grouped_routes=grouped_routes, data_store=data_store)

def post_json():
    try:
        json_data = request.form['json_data']
        parsed_json = json.loads(json_data)

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        original_key = list(parsed_json.keys())[0]
        key_with_timestamp = f"{original_key}_{timestamp}"
        data_store[key_with_timestamp] = parsed_json

        save_data(key_with_timestamp, parsed_json)

        return redirect(url_for('home'))

    except (json.JSONDecodeError, IndexError) as e:
        return jsonify({"error": "Invalid JSON"}), 400

def get_json(key):
    data = data_store.get(key)
    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "Not found"}), 404

def delete_json(key):
    delete_data(key)
    return redirect(url_for('home'))
