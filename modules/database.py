import json


def read_json(filename):
    """Read JSON data from a file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None


def write_json(filename, data):
    """Write data to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def append_history(filename, user, assistant):
    """Append a conversation to the history file."""
    history = read_json(filename)

    if history is None:
        history = []

    history.append({
        "user": user,
        "assistant": assistant
    })

    write_json(filename, history)