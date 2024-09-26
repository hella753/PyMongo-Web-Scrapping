import json


def recipes_to_json(recipes):
    """
    Convert a list of recipes to JSON format.

    Args:
        recipes (list): A list of dictionaries containing recipe data.

    Returns:
        str: JSON formatted string of the recipes.
    """
    try:
        # Convert the list of recipes (which are dictionaries) to JSON string
        json_data = json.dumps(recipes, ensure_ascii=False, indent=4)
        return json_data
    except Exception as e:
        return f"Error converting to JSON: {e}"
