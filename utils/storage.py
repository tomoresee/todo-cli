import json


def read_json():
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
            return tasks
    except FileNotFoundError:
        print("File tasks.json not found")
        return []
    except json.JSONDecodeError:
        print("Error in JSON file format")
        return []


def save_json(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, sort_keys=True, indent=2)
