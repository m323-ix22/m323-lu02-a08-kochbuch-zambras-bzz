"""
Dieses Modul enthält Funktionen zum Bearbeiten von Rezepten, die in JSON-Format vorliegen.
Es ermöglicht das Laden eines Rezepts aus einem JSON-String und das Anpassen der Mengenangaben
für eine bestimmte Anzahl von Personen.
"""
import json

def adjust_recipe(recipe, num_people):
    """
    Passt die Mengenangaben in einem Rezept an die angegebene Anzahl von Personen an.
    :param recipe: Das Originalrezept als Dictionary
    :param num_people: Die Anzahl der Personen, für die das Rezept angepasst werden soll
    :return: Ein neues Rezept, angepasst für die angegebene Anzahl an Personen
    """
    adjustment_factor = num_people / recipe['servings']
    adjusted_recipe = {
        'title': recipe['title'],
        'ingredients': {
            ingredient: amount * adjustment_factor
            for ingredient, amount in recipe['ingredients'].items()
        },
        'servings': num_people
    }
    return adjusted_recipe

def load_recipe(json_string):
    """
    Lädt ein Rezept aus einem JSON-String und gibt es als Dictionary zurück.
    :param json_string: JSON-kodierter String, der das Rezept enthält
    :return: Das Rezept als Python-Dictionary
    """
    return json.loads(json_string)

if __name__ == '__main__':
    recipe_json_str = '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, ' \
                      '"Minced Meat": 500}, "servings": 4} '
    recipe_dict = load_recipe(recipe_json_str)
    adjusted_recipe_dict = adjust_recipe(recipe_dict, 2)
    print(json.dumps(adjusted_recipe_dict, indent=4))
