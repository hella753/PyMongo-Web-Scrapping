

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
        author: str,
        description: str,
        ingredients: list,
        portions: int,
        preparation_steps: list,
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
        self.image_link: str = image_link
        self.recipe_title: str = recipe_title
        self.recipe_link: str = recipe_link
        self.category: dict = category
        self.subcategory: dict = subcategory
        self.ingredients: list = ingredients
        self.portions: int = portions
        self.author: str = author
        self.description: str = description
        self.preparation_steps: list = preparation_steps


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
            "author": self.author,
            "description": self.description,
            "ingredients": self.ingredients,
            "portions": self.portions,
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
            f"Author={self.author}, "
            f"Description={self.description}, "
            f"Ingredients={self.ingredients}, "
            f"Portions={self.portions}, "
            f"Preparation Steps={self.preparation_steps}"
        )
