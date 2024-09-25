# PyMongo & Web Scrapping

## Description
This project uses BeautifulSoup web scraping to extract data from a culinary website and then stores it in a
MongoDB database using PyMongo. The data is a list of georgian cuisine recipes with their information. The data
is easily accessible and can be used for further analysis. <br>

Database name: `georgian_cuisine` <br>
collection name: `recipes` <br>
Document structure: <br>
```
{
    "_id": id,
    "Title": "recipe title",
    "Link": "recipe url",
    "Category": "category",
    "Subcategory": "subcategory",
    "Image": "image url",
    "Description": "recipe description",
    "Author": "author",
    "Portions": "number of portions",
    "Ingredients": ["ingredient1", "ingredient2", ...],    
    "preparation": "preparation steps"
}
```

## Components
* **Database**: Handles the MongoDB database operations like initializing database, inserting and retrieving data. 
* **DataFetcher**: Handles usual and asynchronous data fetching from the website .
* **Recipe**: Recipe Object to store the recipe information.
* **Scraper**: Handles the web scraping operations with bs4.
* 
## **Features** ##
coming soon

### Provided Tasks
**Web-Scraping Tasks:**
- [x] Extract the recipe title,
- [x] Extract the recipe link,
- [x] category, 
- [x] subcategory,
- [x] image,
- [x] description,
- [x] author,
- [x] portions,
- [x] ingredients,
- [x] preparation steps.

**Database Tasks:**
- [x] Average of the number of ingredients in all recipes.
- [x] Average of the number of preparation steps in all recipes.
- [x] Maximum number of portions of a recipe. (recipe title, recipe url)
- [x] Author with the most recipes. 


## Usage
To run the application, use the following command in your terminal:
```bash
python main.py
```

## Dependencies
* **Python 3.X**
* **PyMongo**: Python distribution containing tools for working with MongoDB.
* **BeautifulSoup**: Python library for pulling data out of HTML and XML files.
* **AIOHTTP**: Asynchronous HTTP Client/Server for asyncio and Python.
* **requests**: HTTP client library for the Python.


#### Python Standard Library modules used:
* **asyncio**: framework for writing asynchronous programs using the async and await.

