#!/usr/bin/python3
"""Defines the FileStorage class that saves objects to a JSON file."""
import json
import os


class FileStorage:
    """Serializes instances to a JSON file and back to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of all stored objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Store obj in the dictionary with the key <class name>.<id>."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize all stored objects to the JSON file."""
        data = {}
        for key, obj in FileStorage.__objects.items():
            data[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(data, file)

    def reload(self):
        """Deserialize the JSON file into objects, if the file exists."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        classes = {"BaseModel": BaseModel, "User": User, "State": State,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review}
        if not os.path.exists(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as file:
            data = json.load(file)
        for key, value in data.items():
            cls = classes[value["__class__"]]
            FileStorage.__objects[key] = cls(**value)
