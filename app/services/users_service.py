import json
import os
from app.models.user import User

USERS_FILE = "app/db/users.json"

class Users:
    """
    A simple file-based user management service.
    """

    def __init__(self, filepath=USERS_FILE):
        self.filepath = filepath

    def _load(self):
        """
        Load user data from the JSON file.

        Returns:
            dict: Dictionary where keys are usernames and values are user data.
        """
        try:
            if not os.path.exists(self.filepath):
                return {}
            with open(self.filepath, "r") as file:
                return json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading users: {e}")
            return {}

    def _save(self, users):
        """
        Save user data to the JSON file.

        Args:
            users (dict): Dictionary of all users to save.
        """
        try:
            with open(self.filepath, "w") as file:
                json.dump(users, file, indent=4)
        except IOError as e:
            print(f"Error saving users: {e}")

    def create_user(self, user: User):
        """
        Create a new user and save to the file.

        Args:
            user (User): User object to create.

        Returns:
            dict: Message and user info or error.
        """
        users = self._load()
        if user.name in users:
            return {"error": "User already exists"}
        users[user.name] = user.dict()
        self._save(users)
        return {"message": "User created", "user": user.dict()}

    def get_user(self, name: str):
        """
        Retrieve a user by their name.

        Args:
            name (str): Username to search for.

        Returns:
            User or dict: User object if found, or error dict.
        """
        users = self._load()
        data = users.get(name)
        if data:
            return User(**data)
        return {"error": "User not found"}
