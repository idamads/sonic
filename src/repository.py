import json
import os

FILE = "data/recipes.json"

def load():

    if not os.path.exists(FILE):
        return []

    with open(FILE, encoding="utf8") as f:
        return json.load(f)

def save(data):

    with open(FILE, "w", encoding="utf8") as f:
        json.dump(data, f, indent=4)
