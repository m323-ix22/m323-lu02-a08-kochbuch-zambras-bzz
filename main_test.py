import main

def test_adjust_recipe():
    original_recipe = {"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}
    num_people = 2
    adjusted_recipe = main.adjust_recipe(original_recipe, num_people)
    assert adjusted_recipe == {"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 200, "Tomato Sauce": 150, "Minced Meat": 250}, "servings": 2}

def test_load_recipe():
    json_string = '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}'
    loaded_recipe = main.load_recipe(json_string)
    assert loaded_recipe == {"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}