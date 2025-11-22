import pickle
from typing import Dict, Any

def save_data(data: Dict[str, Any], filename: str):
    try:
        with open(filename, 'wb') as f:
            pickle.dump(data, f)
    except IOError as e:
        raise Exception(f"Error saving data to Pickle file {filename}: {e}")

def load_data(filename: str) -> Dict[str, Any]:
    try:
        with open(filename, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        raise Exception(f"File not found: {filename}")
    except pickle.UnpicklingError:
        raise Exception(f"Error decoding Pickle from file: {filename}")
    except IOError as e:
        raise Exception(f"Error loading data from Pickle file {filename}: {e}")