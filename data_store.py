import json
import os

ROUTES_DIR = 'routes'
data_store = {}

# Load existing data from files
for filename in os.listdir(ROUTES_DIR):
    if filename.endswith('.json'):
        with open(os.path.join(ROUTES_DIR, filename), 'r') as f:
            key = filename[:-5]  # Remove '.json' from filename
            data_store[key] = json.load(f)

def save_data(key, data):
    filepath = os.path.join(ROUTES_DIR, f"{key}.json")
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def delete_data(key):
    filepath = os.path.join(ROUTES_DIR, f"{key}.json")
    if os.path.exists(filepath):
        os.remove(filepath)
        data_store.pop(key, None)
