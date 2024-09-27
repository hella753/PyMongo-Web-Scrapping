# PyMongo & Web Scrapping

## Description
This project uses BeautifulSoup for web scraping to extract data from a culinary website and then stores it in a
MongoDB database using PyMongo. The data is a list of georgian cuisine recipes with their information. It
is easily accessible and can be used for further analysis. <br>

Database name: `mydatabase` <br>
Collection name: `recipies` <br>
Document structure: <br>
```
{
    "_id": id,
    "title": "recipe title",
    "link": "recipe url",
    "category": "category",
    "subcategory": "subcategory",
    "image": "image url",
    "description": "recipe description",
    "author": "author",
    "portions": "number of portions",
    "ingredients": ["ingredient1", "ingredient2", ...],    
    "preparation": "preparation steps"
}
```

## Components
* **MongoDB**: Handles the MongoDB database CRUD operations.
* **DataFetcher**: Handles usual and asynchronous data fetching from the website.
* **Recipe**: Recipe Object to store the recipe information.
* **Scraper**: Handles the web scraping operations with bs4.
* **RecipeQueries**: Handles the database queries for data analysis.


## **Features** ##
Application provides the following functionalities:
* **Web Scraping**: `get_recipe_info` with the help of other methods in the scraper class extracts the recipe information from the website.
* **Database Operations**: `insert_one` and `insert_many` in `database_config.py` stores the extracted data in the MongoDB database.
`find_one` and `find_many` finds the documents in the collection. `get_collection` gets the collection by the name.
* **Data Analysis**: `avg_ingredients`, `avg_stages`, `most_beneficial_recipe` and `top_author` provides some basic analysis on the stored data for the provided tasks.
* **Asynchronous Data Fetching**: `fetch_async` and `fetch_async_all` fetches the data asynchronously using aiohttp.


### Provided Tasks
**Web-Scraping Tasks:**
- [x] Extract the recipe title
- [x] Extract the recipe link
- [x] Extract the category
- [x] Extract the subcategory
- [x] Extract the image
- [x] Extract the description
- [x] Extract the author
- [x] Extract the portions
- [x] Extract the ingredients
- [x] Extract the preparation steps

**Database Tasks:**
- [x] Print average of the number of ingredients in all recipes
- [x] Print average of the number of preparation steps in all recipes
- [x] Print maximum number of portions of a recipe. (recipe title, recipe url)
- [x] Print author with the most recipes


## Usage
To run the application, use the following command in your terminal:
```bash
python main.py
```

## Dependencies
* **Python 3.x**
* **PyMongo**: Python distribution containing tools for working with MongoDB.
* **BeautifulSoup**: Python library for pulling data out of HTML and XML files.
* **AIOHTTP**: Asynchronous HTTP Client/Server for asyncio and Python.
* **requests**: HTTP client library for the Python.


#### Python Standard Library modules used:
* **asyncio**: framework for writing asynchronous programs using the async and await.

