#!/usr/bin/python3
"""Unit tests for the FileStorage class in models/engine/file_storage.py."""
import json
import os
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Start each test with no stored objects and no JSON file."""
        FileStorage._FileStorage__objects.clear()
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Remove the JSON file and stored objects after each test."""
        FileStorage._FileStorage__objects.clear()
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_storage_is_file_storage(self):
        """Check that storage is a FileStorage instance."""
        self.assertIsInstance(storage, FileStorage)

    def test_file_path(self):
        """Check that the private file path is file.json."""
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")

    def test_all_returns_dict(self):
        """Check that all() returns a dictionary."""
        self.assertIsInstance(storage.all(), dict)

    def test_all_returns_objects(self):
        """Check that all() returns the private __objects dictionary."""
        self.assertIs(storage.all(), FileStorage._FileStorage__objects)

    def test_new_adds_object(self):
        """Check that new() stores the object."""
        model = BaseModel()
        FileStorage._FileStorage__objects.clear()
        storage.new(model)
        self.assertIn(model, storage.all().values())

    def test_new_key_format(self):
        """Check that the key is <class name>.<id>."""
        model = BaseModel()
        key = "BaseModel.{}".format(model.id)
        self.assertIn(key, storage.all())
        self.assertIs(storage.all()[key], model)

    def test_save_creates_file(self):
        """Check that save() creates the JSON file."""
        BaseModel()
        storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_save_file_content(self):
        """Check that the JSON file holds the dictionary of the object."""
        model = BaseModel()
        model.name = "Saved"
        storage.save()
        with open("file.json", "r") as file:
            data = json.load(file)
        key = "BaseModel.{}".format(model.id)
        self.assertEqual(data[key], model.to_dict())

    def test_reload_restores_objects(self):
        """Check that reload() rebuilds objects from the JSON file."""
        model = BaseModel()
        model.name = "Reloaded"
        model.save()
        FileStorage._FileStorage__objects.clear()
        storage.reload()
        key = "BaseModel.{}".format(model.id)
        self.assertIn(key, storage.all())
        self.assertIsInstance(storage.all()[key], BaseModel)
        self.assertEqual(storage.all()[key].to_dict(), model.to_dict())

    def test_reload_without_file(self):
        """Check that reload() does nothing if the file does not exist."""
        storage.reload()
        self.assertEqual(storage.all(), {})

    def test_base_model_registers_in_storage(self):
        """Check that a new BaseModel is added to storage."""
        model = BaseModel()
        self.assertIn("BaseModel.{}".format(model.id), storage.all())

    def test_base_model_save_writes_file(self):
        """Check that BaseModel.save() writes the JSON file."""
        BaseModel().save()
        self.assertTrue(os.path.exists("file.json"))

    def test_base_model_from_dict_not_registered(self):
        """Check that an instance made from a dict is not added again."""
        model = BaseModel()
        data = model.to_dict()
        FileStorage._FileStorage__objects.clear()
        BaseModel(**data)
        self.assertEqual(storage.all(), {})

    def test_reload_restores_user(self):
        """Check that reload() rebuilds a User from the JSON file."""
        user = User()
        user.first_name = "Betty"
        user.save()
        FileStorage._FileStorage__objects.clear()
        storage.reload()
        key = "User.{}".format(user.id)
        self.assertIn(key, storage.all())
        self.assertIsInstance(storage.all()[key], User)
        self.assertEqual(storage.all()[key].first_name, "Betty")

    def test_reload_restores_all_classes(self):
        """Check that reload() rebuilds every class from the JSON file."""
        objs = [State(), City(), Amenity(), Place(), Review()]
        for obj in objs:
            obj.save()
        FileStorage._FileStorage__objects.clear()
        storage.reload()
        for obj in objs:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.assertIn(key, storage.all())
            self.assertIsInstance(storage.all()[key], obj.__class__)


if __name__ == "__main__":
    unittest.main()
