#!/usr/bin/python3
"""Unit tests for the User class in models/user.py."""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_inherits_from_base_model(self):
        """Check that User is a subclass of BaseModel."""
        self.assertIsInstance(User(), BaseModel)

    def test_email_default(self):
        """Check that email is an empty string by default."""
        self.assertEqual(User.email, "")

    def test_password_default(self):
        """Check that password is an empty string by default."""
        self.assertEqual(User.password, "")

    def test_first_name_default(self):
        """Check that first_name is an empty string by default."""
        self.assertEqual(User.first_name, "")

    def test_last_name_default(self):
        """Check that last_name is an empty string by default."""
        self.assertEqual(User.last_name, "")

    def test_attributes_are_strings(self):
        """Check that all four attributes are strings."""
        user = User()
        for name in ["email", "password", "first_name", "last_name"]:
            self.assertIsInstance(getattr(user, name), str)

    def test_has_id_and_dates(self):
        """Check that a User gets an id and both dates."""
        user = User()
        self.assertIsInstance(user.id, str)
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_unique_ids(self):
        """Check that two users get different ids."""
        self.assertNotEqual(User().id, User().id)

    def test_to_dict_class_name(self):
        """Check that to_dict() stores the class name User."""
        self.assertEqual(User().to_dict()["__class__"], "User")

    def test_str_starts_with_class_name(self):
        """Check that str() starts with [User]."""
        self.assertTrue(str(User()).startswith("[User] ("))

    def test_from_dict(self):
        """Check that a User can be rebuilt from its dictionary."""
        user = User()
        user.first_name = "Betty"
        new_user = User(**user.to_dict())
        self.assertEqual(new_user.id, user.id)
        self.assertEqual(new_user.first_name, "Betty")
        self.assertEqual(new_user.to_dict(), user.to_dict())


if __name__ == "__main__":
    unittest.main()
