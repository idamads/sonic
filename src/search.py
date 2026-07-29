def by_ingredient(recipes, ingredient):

    return [
        recipe
        for recipe in recipes
        if ingredient.lower() in
        " ".join(recipe["ingredients"]).lower()
    ]
