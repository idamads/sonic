import json

def export(recipes):

    with open(
        "data/exports/recipes.json",
        "w",
        encoding="utf8"
    ) as f:

        json.dump(recipes, f, indent=4)
