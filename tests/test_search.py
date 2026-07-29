from src.search import by_ingredient

def test_search():

    recipes = [
        {
            "ingredients": ["Milk", "Eggs"]
        }
    ]

    assert len(by_ingredient(recipes, "milk")) == 1
