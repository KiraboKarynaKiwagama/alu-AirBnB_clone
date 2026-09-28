#!/usr/bin/python3
"""Defines the Review class for the AirBnB clone."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review of a place."""

    place_id = ""
    user_id = ""
    text = ""
