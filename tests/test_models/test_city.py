#!/usr/bin/python3
"""Unit tests for the City class in models/city.py."""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_inherits_from_base_model(self):
        """Check that City is a subclass of BaseModel."""
        self.assertIsInstance(City(), BaseModel)

    def test_state_id_default(self):
        """Check that state_id is an empty string by default."""
        self.assertEqual(City().state_id, "")

    def test_name_default(self):
        """Check that name is an empty string by default."""
        self.assertEqual(City().name, "")

    def test_to_dict_class_name(self):
        """Check that to_dict() stores the class name City."""
        self.assertEqual(City().to_dict()["__class__"], "City")

    def test_from_dict(self):
        """Check that a City can be rebuilt from its dictionary."""
        city = City()
        city.name = "San Francisco"
        city.state_id = "abc"
        new_city = City(**city.to_dict())
        self.assertEqual(new_city.id, city.id)
        self.assertEqual(new_city.name, "San Francisco")
        self.assertEqual(new_city.state_id, "abc")


if __name__ == "__main__":
    unittest.main()
