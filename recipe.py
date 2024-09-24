

class Recipe:
    def __init__(
        self,
        recipe_title: str,
        recipe_link: str,
        category: dict,
        subcategory: dict,
        image_link: str
    ) -> None:
        self.image_link: str = image_link
        self.recipe_title: str = recipe_title
        self.recipe_link: str = recipe_link
        self.category: dict = category
        self.subcategory: dict = subcategory

    def __repr__(self):
        return (f"Recipe(Title='{self.recipe_title}', Link={self.recipe_link}, "
                f" Category={self.category}, Subcategory={self.subcategory}, "
                f"Image={self.image_link})")

