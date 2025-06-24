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
from app.services.users_service import Users
from app.models.user import User

router = APIRouter()

user_service = Users()

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
    return user_service.create_user(user.username, user.email)


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
    return users_service.get_user(username)
