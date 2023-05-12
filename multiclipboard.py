import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

def saveData(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def loadData(filepath):
    # handle err if file doesn't exist
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

if len(sys.argv) == 2:
    command = sys.argv[1]
    # attempt to load file
    data = loadData(SAVED_DATA)

    if command == "save":
        key = input("Enter a key to save: ")
        # store inside of data dictionary
        data[key] = clipboard.paste()
        saveData(SAVED_DATA, data)
        print("Data saved.")
    elif command == "load":
        key = input("Enter a key to load: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard.")
        else:
            print("Key does not exist.")
    elif command == "list":
        print("list")
    else:
        print("Unknown command")
else:
    print("Please pass exactly one command.")