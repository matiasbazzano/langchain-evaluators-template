import json, os


def load_dataset(path):
    if not os.path.exists(path):
        print(f"Dataset not found: {path}")
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
