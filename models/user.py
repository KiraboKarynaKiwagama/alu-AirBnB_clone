#!/usr/bin/python3
"""Defines the User class for the AirBnB clone."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user of the AirBnB clone."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
