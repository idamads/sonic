def summary(recipes):

    favorites = sum(
        1
        for recipe in recipes
        if recipe.get("favorite")
    )

    return {
        "recipes": len(recipes),
        "favorites": favorites
    }
