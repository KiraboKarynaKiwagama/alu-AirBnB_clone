#!/usr/bin/python3
"""Unit tests for the BaseModel class in models/base_model.py."""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_id_is_string(self):
        """Check that id is a string."""
        self.assertIsInstance(BaseModel().id, str)

    def test_unique_ids(self):
        """Check that two instances get different ids."""
        self.assertNotEqual(BaseModel().id, BaseModel().id)

    def test_created_at_is_datetime(self):
        """Check that created_at is a datetime object."""
        self.assertIsInstance(BaseModel().created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Check that updated_at is a datetime object."""
        self.assertIsInstance(BaseModel().updated_at, datetime)

    def test_str_format(self):
        """Check that __str__ uses the required format."""
        model = BaseModel()
        expected = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), expected)

    def test_save_updates_updated_at(self):
        """Check that save() changes updated_at but not created_at."""
        model = BaseModel()
        old_updated = model.updated_at
        old_created = model.created_at
        model.save()
        self.assertGreater(model.updated_at, old_updated)
        self.assertEqual(model.created_at, old_created)

    def test_to_dict_type(self):
        """Check that to_dict() returns a dictionary."""
        self.assertIsInstance(BaseModel().to_dict(), dict)

    def test_to_dict_has_class_key(self):
        """Check that to_dict() adds the __class__ key."""
        self.assertEqual(BaseModel().to_dict()["__class__"], "BaseModel")

    def test_to_dict_keys(self):
        """Check that to_dict() contains the expected keys."""
        keys = BaseModel().to_dict().keys()
        for key in ["id", "created_at", "updated_at", "__class__"]:
            self.assertIn(key, keys)

    def test_to_dict_dates_are_iso_strings(self):
        """Check that to_dict() converts the dates to ISO strings."""
        model = BaseModel()
        data = model.to_dict()
        self.assertIsInstance(data["created_at"], str)
        self.assertIsInstance(data["updated_at"], str)
        self.assertEqual(data["created_at"], model.created_at.isoformat())
        self.assertEqual(data["updated_at"], model.updated_at.isoformat())

    def test_to_dict_includes_custom_attributes(self):
        """Check that attributes added later appear in to_dict()."""
        model = BaseModel()
        model.name = "My First Model"
        model.my_number = 89
        data = model.to_dict()
        self.assertEqual(data["name"], "My First Model")
        self.assertEqual(data["my_number"], 89)

    def test_to_dict_does_not_change_instance(self):
        """Check that to_dict() leaves the real attributes untouched."""
        model = BaseModel()
        model.to_dict()
        self.assertIsInstance(model.created_at, datetime)
        self.assertNotIn("__class__", model.__dict__)

    def test_init_from_dict_copies_values(self):
        """Check that an instance built from a dict keeps its values."""
        model = BaseModel()
        model.name = "My_First_Model"
        model.my_number = 89
        new_model = BaseModel(**model.to_dict())
        self.assertEqual(new_model.id, model.id)
        self.assertEqual(new_model.name, "My_First_Model")
        self.assertEqual(new_model.my_number, 89)

    def test_init_from_dict_converts_dates(self):
        """Check that date strings become datetime objects."""
        model = BaseModel()
        new_model = BaseModel(**model.to_dict())
        self.assertIsInstance(new_model.created_at, datetime)
        self.assertIsInstance(new_model.updated_at, datetime)
        self.assertEqual(new_model.created_at, model.created_at)
        self.assertEqual(new_model.updated_at, model.updated_at)

    def test_init_from_dict_skips_class_key(self):
        """Check that __class__ is not added as an attribute."""
        new_model = BaseModel(**BaseModel().to_dict())
        self.assertNotIn("__class__", new_model.__dict__)

    def test_init_from_dict_is_new_object(self):
        """Check that the new instance is a different object."""
        model = BaseModel()
        new_model = BaseModel(**model.to_dict())
        self.assertIsNot(model, new_model)

    def test_init_ignores_args(self):
        """Check that positional arguments are not used."""
        model = BaseModel("ignored", 42)
        self.assertIsInstance(model.id, str)
        self.assertNotIn("ignored", model.__dict__.values())

    def test_round_trip_to_dict(self):
        """Check that to_dict() gives the same result after a round trip."""
        model = BaseModel()
        model.name = "Round"
        new_model = BaseModel(**model.to_dict())
        self.assertEqual(new_model.to_dict(), model.to_dict())

    def test_init_without_kwargs_creates_new(self):
        """Check that no kwargs creates id and dates as before."""
        model = BaseModel()
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, "updated_at"))


if __name__ == "__main__":
    unittest.main()
