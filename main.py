import os
import json

# Paths
images_folder = r"C:\Users\owner\Desktop\Project\reaction-shop\images"
json_file = r"C:\Users\owner\Desktop\Project\reaction-shop\images.json"

# Load existing JSON
if os.path.exists(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []
else:
    data = []

# Build a set of existing filenames to avoid duplicates
existing_files = {item['file'] for item in data}

# Scan folder and add new images
new_entries = []
for filename in os.listdir(images_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')) and filename not in existing_files:
        name = os.path.splitext(filename)[0]  # Use file name as default name
        entry = {"name": name, "file": filename, "tags": []}  # tags empty for now
        data.append(entry)
        new_entries.append(filename)

# Write back updated JSON
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print(f"Added {len(new_entries)} new images: {new_entries}" if new_entries else "No new images to add.")