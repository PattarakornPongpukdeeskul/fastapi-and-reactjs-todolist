import pymongo
from dotenv import load_dotenv
import os
import uuid

load_dotenv()
SECRET_KEY = os.getenv("DATABASE_URL")
database_client = pymongo.MongoClient(SECRET_KEY)
database = database_client["python_react_login"]
user_collection = database.user
authentication_collection = database["authentication"]


class User:

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def query(self):
        email_query = {"email": self.email}
        collection = user_collection.find(email_query)
        if user_collection.count_documents(email_query) != 0:
            return collection[0]
        return {}

    def create(self, name):  # register
        user_data = {"email": self.email, "password": self.password,
                     "_id": str(uuid.uuid4()), "name": name}
        user_document = user_collection.insert_one(user_data)
        return user_document.inserted_id

    def delete(self):  # delete account
        user_data = {"email": self.email, "password": self.password}
        user_collection.insert_one(user_data)


class Authentication:

    def __init__(self, email):
        self.email = email

    def query(self, email):
        access_token_query = {"access_token": access_token}
        collection = authentication_collection.find(access_token_query)
        if authentication_collection.count_documents(access_token_query) != 0:
            return collection[0]
        return {}

    def create(self):  # login
        authentication_data = {"user_id": self.user_id, "refresh_token": refresh_token, "access_token": access_token,
                               "expired_at": expired_at, "is_active": True, "created_date": created_date, "updated_date": updated_date}
        authentication_collection.insert_one(authentication_data)

    def delete(self, id):  # logout
        authentication_collection.delete_one(id)
