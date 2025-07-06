"""
User data model definition.
===========================
This module defines the User class used throughout the application for
representing basic user identity and contact information. The model leverages
Pydantic for validation and serialization, ensuring data integrity.

Classes
-------
User : pydantic.BaseModel
    Defines user information with name and email validation.
"""

from pydantic import BaseModel, EmailStr

class User(BaseModel):
    """
    Data model for representing a user.

    Attributes
    ----------
    name : str
        The full name of the user.
    email : EmailStr
        A valid email address for the user.
    """
    name: str
    email: EmailStr
