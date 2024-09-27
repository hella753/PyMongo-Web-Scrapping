from pymongo import MongoClient, errors


class MongoDB:
    def __init__(self, uri="mongodb://localhost:27017/", database_name="mydatabase"):
        """
        Initializes the MongoDB connection and defines the database to use.

        :param uri: MongoDB URI to connect to (default is local MongoDB server).
        :param database_name: Name of the database to use.
        """
        try:
            self.client = MongoClient(
                uri, serverSelectionTimeoutMS=5000
            )  # 5-second timeout for connection
            self.client.server_info()  # Trigger connection check
            self.db = self.client[database_name]
        except errors.ServerSelectionTimeoutError as err:
            print(f"Failed to connect to server: {err}")
            raise

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
        try:
            collection = self.get_collection(collection_name)
            result = collection.insert_one(document)
            return result.inserted_id
        except errors.PyMongoError as e:
            print(f"Error inserting document: {e}")
            return None

    def insert_many(self, collection_name, documents):
        """
        Insert multiple documents into a collection.

        :param collection_name: The name of the collection.
        :param documents: A list of dictionaries representing the documents to be inserted.
        :return: The result of the insertion.
        """
        try:
            collection = self.get_collection(collection_name)
            result = collection.insert_many(documents)
            return result.inserted_ids
        except errors.BulkWriteError as e:
            print(f"Error inserting multiple documents: {e}")
            return None

    def find_one(self, collection_name, query):
        """
        Find a single document that matches the query.

        :param collection_name: The name of the collection.
        :param query: A dictionary representing the query.
        :return: The first document that matches the query.
        """
        try:
            collection = self.get_collection(collection_name)
            return collection.find_one(query)
        except errors.PyMongoError as e:
            print(f"Error finding document: {e}")
            return None

    def find_many(self, collection_name, query):
        """
        Find multiple documents that match the query.

        :param collection_name: The name of the collection.
        :param query: A dictionary representing the query.
        :return: A list of documents that match the query.
        """
        try:
            collection = self.get_collection(collection_name)
            return list(collection.find(query))
        except errors.PyMongoError as e:
            print(f"Error finding documents: {e}")
            return None

    def update_one(self, collection_name, query, update):
        """
        Update a single document in the collection that matches the query.

        :param collection_name: The name of the collection.
        :param query: A dictionary representing the query to find the document.
        :param update: A dictionary representing the update to be applied.
        :return: The result of the update operation.
        """
        try:
            collection = self.get_collection(collection_name)
            return collection.update_one(query, update)
        except errors.PyMongoError as e:
            print(f"Error updating document: {e}")
            return None

    def update_many(self, collection_name, query, update):
        """
        Update multiple documents in the collection that match the query.

        :param collection_name: The name of the collection.
        :param query: A dictionary representing the query to find documents.
        :param update: A dictionary representing the update to be applied.
        :return: The result of the update operation.
        """
        try:
            collection = self.get_collection(collection_name)
            return collection.update_many(query, update)
        except errors.PyMongoError as e:
            print(f"Error updating documents: {e}")
            return None

    def delete_one(self, collection_name, query):
        """
        Delete a single document that matches the query.

        :param collection_name: The name of the collection.
        :param query: A dictionary representing the query.
        :return: The result of the deletion.
        """
        try:
            collection = self.get_collection(collection_name)
            return collection.delete_one(query)
        except errors.PyMongoError as e:
            print(f"Error deleting document: {e}")
            return None

    def delete_many(self, collection_name, query):
        """
        Delete multiple documents that match the query.

        :param collection_name: The name of the collection.
        :param query: A dictionary representing the query.
        :return: The result of the deletion.
        """
        try:
            collection = self.get_collection(collection_name)
            return collection.delete_many(query)
        except errors.PyMongoError as e:
            print(f"Error deleting documents: {e}")
            return None

    def close(self):
        """
        Close the MongoDB connection.
        """
        self.client.close()
