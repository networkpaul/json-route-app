from flask import Flask
import os

app = Flask(__name__)

# Directory for storing route files
ROUTES_DIR = 'routes'

# Ensure the routes directory exists
if not os.path.exists(ROUTES_DIR):
    os.makedirs(ROUTES_DIR)

from routes import home, post_json, get_json, delete_json

app.add_url_rule('/', 'home', home)
app.add_url_rule('/post-json', 'post_json', post_json, methods=['POST'])
app.add_url_rule('/<key>', 'get_json', get_json)
app.add_url_rule('/delete-json/<key>', 'delete_json', delete_json, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)
