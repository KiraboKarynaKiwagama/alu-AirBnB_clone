#!/usr/bin/python3
"""Unit tests for the Amenity class in models/amenity.py."""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_inherits_from_base_model(self):
        """Check that Amenity is a subclass of BaseModel."""
        self.assertIsInstance(Amenity(), BaseModel)

    def test_name_default(self):
        """Check that name is an empty string by default."""
        self.assertEqual(Amenity().name, "")

    def test_to_dict_class_name(self):
        """Check that to_dict() stores the class name Amenity."""
        self.assertEqual(Amenity().to_dict()["__class__"], "Amenity")

    def test_from_dict(self):
        """Check that an Amenity can be rebuilt from its dictionary."""
        amenity = Amenity()
        amenity.name = "Wifi"
        new_amenity = Amenity(**amenity.to_dict())
        self.assertEqual(new_amenity.id, amenity.id)
        self.assertEqual(new_amenity.name, "Wifi")


if __name__ == "__main__":
    unittest.main()
