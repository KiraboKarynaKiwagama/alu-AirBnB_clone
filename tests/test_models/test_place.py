#!/usr/bin/python3
"""Unit tests for the Place class in models/place.py."""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def test_inherits_from_base_model(self):
        """Check that Place is a subclass of BaseModel."""
        self.assertIsInstance(Place(), BaseModel)

    def test_string_defaults(self):
        """Check that the string attributes are empty strings."""
        place = Place()
        for name in ["city_id", "user_id", "name", "description"]:
            self.assertEqual(getattr(place, name), "")

    def test_integer_defaults(self):
        """Check that the integer attributes are 0."""
        place = Place()
        for name in ["number_rooms", "number_bathrooms", "max_guest",
                     "price_by_night"]:
            self.assertEqual(getattr(place, name), 0)
            self.assertIsInstance(getattr(place, name), int)

    def test_float_defaults(self):
        """Check that latitude and longitude are 0.0 floats."""
        place = Place()
        for name in ["latitude", "longitude"]:
            self.assertEqual(getattr(place, name), 0.0)
            self.assertIsInstance(getattr(place, name), float)

    def test_amenity_ids_default(self):
        """Check that amenity_ids is an empty list."""
        self.assertEqual(Place().amenity_ids, [])

    def test_to_dict_class_name(self):
        """Check that to_dict() stores the class name Place."""
        self.assertEqual(Place().to_dict()["__class__"], "Place")

    def test_from_dict(self):
        """Check that a Place can be rebuilt from its dictionary."""
        place = Place()
        place.name = "Cozy Cabin"
        place.max_guest = 4
        new_place = Place(**place.to_dict())
        self.assertEqual(new_place.id, place.id)
        self.assertEqual(new_place.name, "Cozy Cabin")
        self.assertEqual(new_place.max_guest, 4)


if __name__ == "__main__":
    unittest.main()
