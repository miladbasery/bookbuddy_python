import json
from typing import Dict, Any

def save_data(data: Dict[str, Any], filename: str):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        raise Exception(f"Error saving data to JSON file {filename}: {e}")

def load_data(filename: str) -> Dict[str, Any]:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        raise Exception(f"File not found: {filename}")
    except json.JSONDecodeError:
        raise Exception(f"Error decoding JSON from file: {filename}")
    except IOError as e:
        raise Exception(f"Error loading data from JSON file {filename}: {e}")