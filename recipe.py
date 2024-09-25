

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
        image_link: str
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

    def to_dict(self) -> dict:
        """
        Converts the Recipe instance into a dictionary format.

        :return: dict: A dictionary containing the recipe information.
        """
        return {
            "Title": self.recipe_title,
            "Link": self.recipe_link,
            "Category": self.category,
            "Subcategory": self.subcategory,
            "Image": self.image_link,
        }

    def __repr__(self) -> str:
        """
        Returns a string representation of the Recipe instance.

        :return: str: A string that provides a clear representation
        of the recipe object.
        """
        return (
            f"Recipe(Title='{self.recipe_title}', Link={self.recipe_link}, "
            f" Category={self.category}, Subcategory={self.subcategory}, "
            f"Image={self.image_link}, "
        )
