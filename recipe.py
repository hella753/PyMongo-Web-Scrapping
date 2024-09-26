

class Recipe:
    """
    Recipe class to store recipe information
    """
    def __init__(
        self,
        recipe_title: str,
        recipe_link: str,
        category: dict,
        subcategory: dict,
        image_link: str,
        description: str,
        author: str,
        portions: int,
        ingredients: list,
        preparation_steps: dict,
    ) -> None:
        """
        Initializes a Recipe instance.

        :param recipe_title: str: The title of the recipe.
        :param recipe_link: str: The URL link to the recipe.
        :param category: dict: The category of the recipe
        (e.g., dessert, main course).
        :param subcategory: dict: The subcategory of the recipe.
        :param image_link: str: The URL link to the recipe's image.
        """
        self.recipe_title: str = recipe_title
        self.recipe_link: str = recipe_link
        self.category: dict = category
        self.subcategory: dict = subcategory
        self.image_link: str = image_link
        self.description: str = description
        self.author: str = author
        self.portions: int = portions
        self.ingredients: list = ingredients
        self.preparation_steps: dict = preparation_steps


    def to_dict(self) -> dict:
        """
        Converts the Recipe instance into a dictionary format.

        :return: dict: A dictionary containing the recipe information.
        """
        return {
            "title": self.recipe_title,
            "link": self.recipe_link,
            "category": self.category,
            "subcategory": self.subcategory,
            "image": self.image_link,
            "description": self.description,
            "author": self.author,
            "portions": self.portions,
            "ingredients": self.ingredients,
            "preparation Steps": self.preparation_steps,
        }

    def __repr__(self) -> str:
        """
        Returns a string representation of the Recipe instance.

        :return: str: A string that provides a clear representation
        of the recipe object.
        """
        return (
            f"Recipe(Title='{self.recipe_title}', "
            f"Link={self.recipe_link}, "
            f"Category={self.category}, "
            f"Subcategory={self.subcategory}, "
            f"Image={self.image_link}, "
            f"Description={self.description}, "
            f"Author={self.author}, "
            f"Portions={self.portions}, "
            f"Ingredients={self.ingredients}, "
            f"Preparation Steps={self.preparation_steps}"
        )
