"""
User Routes Module

This module defines API endpoints for managing users.
Currently, uses an in-memory dictionary for demonstration purposes.

Routes:
- POST /user/         → Create a new user
- GET  /user/{username} → Retrieve user by username
"""

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    """
    Data model representing a user.
    """
    username: str
    email: str

# In-memory "database" for demonstration
fake_users_db = {}

@router.post("/")
def create_user(user: User):
    """
    Create a new user entry.

    Parameters:
    ----------
    user : User
        A Pydantic model representing the user data (username, email).

    Returns:
    -------
    dict
        A success message with user data, or an error if the user already exists.
    """
    if user.username in fake_users_db:
        return {"error": "User already exists"}
    fake_users_db[user.username] = user
    return {"message": "User created", "user": user}

@router.get("/{username}")
def get_user(username: str):
    """
    Retrieve an existing user by their username.

    Parameters:
    ----------
    username : str
        The username of the user to retrieve.

    Returns:
    -------
    dict or User
        The user data if found, otherwise an error message.
    """
    user = fake_users_db.get(username)
    if user:
        return user
    return {"error": "User not found"}
