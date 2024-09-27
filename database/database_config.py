from pymongo import MongoClient


class MongoDB:
    def __init__(self, uri="mongodb://localhost:27017/", database_name="mydatabase"):
        """
        Initializes the MongoDB connection and defines the database to use.

        :param uri: MongoDB URI to connect to (default is local MongoDB server).
        :param database_name: Name of the database to use.
        """
        self.client = MongoClient(uri)
        self.db = self.client[database_name]

    def get_collection(self, collection_name):
        """
        Get a collection by name.

        :param collection_name: The name of the collection to access.
        :return: The collection object.
        """
        return self.db[collection_name]

    def insert_one(self, collection_name, document):
        """
        Insert a single document into a collection.

        :param collection_name: The name of the collection.
        :param document: A dictionary representing the document to be inserted.
        :return: The result of the insertion.
        """
        collection = self.get_collection(collection_name)
        result = collection.insert_one(document)
        return result.inserted_id

    def insert_many(self, collection_name, documents):
        """
        Insert multiple documents into a collection.

        :param collection_name: The name of the collection.
        :param documents: A list of dictionaries representing the documents to be inserted.
        :return: The result of the insertion.
        """
        collection = self.get_collection(collection_name)
        result = collection.insert_many(documents)
        return result.inserted_ids

    def find_one(self, collection_name, query):
        """
        Find a single document that matches the query.

        :param collection_name: The name of the collection.
        :param query: A dictionary representing the query.
        :return: The first document that matches the query.
        """
        collection = self.get_collection(collection_name)
        return collection.find_one(query)

    def find_many(self, collection_name, query):
        """
        Find multiple documents that match the query.

        :param collection_name: The name of the collection.
        :param query: A dictionary representing the query.
        :return: A list of documents that match the query.
        """
        collection = self.get_collection(collection_name)
        return list(collection.find(query))

    def update_one(self, collection_name, query, update):
        """
        Update a single document in the collection that matches the query.

        :param collection_name: The name of the collection.
        :param query: A dictionary representing the query to find the document.
        :param update: A dictionary representing the update to be applied.
        :return: The result of the update operation.
        """
        collection = self.get_collection(collection_name)
        return collection.update_one(query, update)

    def update_many(self, collection_name, query, update):
        """
        Update multiple documents in the collection that match the query.

        :param collection_name: The name of the collection.
        :param query: A dictionary representing the query to find documents.
        :param update: A dictionary representing the update to be applied.
        :return: The result of the update operation.
        """
        collection = self.get_collection(collection_name)
        return collection.update_many(query, update)

    def delete_one(self, collection_name, query):
        """
        Delete a single document that matches the query.

        :param collection_name: The name of the collection.
        :param query: A dictionary representing the query.
        :return: The result of the deletion.
        """
        collection = self.get_collection(collection_name)
        return collection.delete_one(query)

    def delete_many(self, collection_name, query):
        """
        Delete multiple documents that match the query.

        :param collection_name: The name of the collection.
        :param query: A dictionary representing the query.
        :return: The result of the deletion.
        """
        collection = self.get_collection(collection_name)
        return collection.delete_many(query)

    def close(self):
        """
        Close the MongoDB connection.
        """
        self.client.close()
