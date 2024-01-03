import json
import os

def update_path(path) :
    if os.path.exists(path) :
        f = open('file_path.json',"r+")
        data = json.load(f)
        f.truncate(0)
        f.seek(0)
        print(data["path"])

        data["path"] = path
        json.dump(data, f, indent=4)
        # Closing file
        f.close()
        print("File updated")
    else:
        print('invalid path !!')

def get_path() :
    f = open('file_path.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)
    return (data["path"])

