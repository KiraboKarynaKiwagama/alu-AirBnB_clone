#!/usr/bin/python3
"""Unit tests for the State class in models/state.py."""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_inherits_from_base_model(self):
        """Check that State is a subclass of BaseModel."""
        self.assertIsInstance(State(), BaseModel)

    def test_name_default(self):
        """Check that name is an empty string by default."""
        self.assertEqual(State().name, "")

    def test_to_dict_class_name(self):
        """Check that to_dict() stores the class name State."""
        self.assertEqual(State().to_dict()["__class__"], "State")

    def test_from_dict(self):
        """Check that a State can be rebuilt from its dictionary."""
        state = State()
        state.name = "California"
        new_state = State(**state.to_dict())
        self.assertEqual(new_state.id, state.id)
        self.assertEqual(new_state.name, "California")


if __name__ == "__main__":
    unittest.main()
