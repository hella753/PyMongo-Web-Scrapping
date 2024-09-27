from database.database_config import MongoDB
from pymongo import errors


class RecipeQueries(MongoDB):
    def __init__(self, uri="mongodb://localhost:27017/", database_name="mydatabase"):
        super().__init__(uri, database_name)

    def avg_ingredients(self, collection_name="recipies"):
        """
        Calculates the average number of ingredients in all recipes in the specified collection.

        :param collection_name: The name of the collection to query (default is "recipes").
        :return: A list containing the average number of ingredients, or None if an error occurs.
        """
        try:
            collection = self.get_collection(collection_name)
            avg_ingredients = collection.aggregate(
                [
                    {"$project": {"num_ingredients": {"$size": "$ingredients"}}},
                    {
                        "$group": {
                            "_id": None,
                            "avgIngredients": {"$avg": "$num_ingredients"},
                        }
                    },
                ]
            )
            avg_value = next(avg_ingredients, None)
            if avg_value is not None:
                return round(avg_value["avgIngredients"])
            return None
        except errors.PyMongoError as e:
            print(f"Error calculating average ingredients: {e}")
            return None

    def avg_stages(self, collection_name="recipies"):
        """
        Calculates the average number of cooking stages (preparation steps) in all recipes.

        :param collection_name: The name of the collection to query (default is "recipes").
        :return: The rounded average number of cooking stages, or None if an error occurs.
        """
        try:
            collection = self.get_collection(collection_name)
            avg_stages = collection.aggregate(
                [
                    {
                        "$project": {
                            "num_stages": {
                                "$size": {"$objectToArray": "$preparation Steps"}
                            }
                        }
                    },
                    {"$group": {"_id": None, "avgStages": {"$avg": "$num_stages"}}},
                ]
            )

            avg_value = next(avg_stages, None)
            if avg_value is not None:
                return round(avg_value["avgStages"], 2)
            return None
        except errors.PyMongoError as e:
            print(f"Error calculating average cooking stages: {e}")
            return None

    def most_beneficial_recipe(self, collection_name="recipies"):
        """
        Finds the first recipe with the maximum portions and returns its title and link.

        :param collection_name: The name of the collection to query (default is "recipes").
        :return: A dictionary containing the title and link of the recipe with the most portions, or None if an error occurs.
        """
        try:
            collection = self.get_collection(collection_name)

            recipe = collection.find_one(
                filter={"portions": {"$ne": None}},
                sort=[("portions", -1)],
                projection={"title": 1, "link": 1},
            )
            return recipe
        except errors.PyMongoError as e:
            print(f"Error finding recipe with max portions: {e}")
            return None

    def top_author(self, collection_name="recipies"):
        """
        Finds the author who has posted the most recipes.

        :param collection_name: The name of the collection to query (default is "recipes").
        :return: A list containing the top author and the count of their recipes, or None if an error occurs.
        """
        try:
            collection = self.get_collection(collection_name)
            author = collection.aggregate(
                [
                    {"$group": {"_id": "$author", "recipeCount": {"$sum": 1}}},
                    {"$sort": {"recipeCount": -1}},
                    {"$limit": 1},
                ]
            )
            return list(author)
        except errors.PyMongoError as e:
            print(f"Error finding top author: {e}")
            return None
