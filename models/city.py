#!/usr/bin/python3
"""Defines the City class for the AirBnB clone."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city."""

    state_id = ""
    name = ""
