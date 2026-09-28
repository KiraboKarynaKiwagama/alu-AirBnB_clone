#!/usr/bin/python3
"""Unit tests for the Review class in models/review.py."""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_inherits_from_base_model(self):
        """Check that Review is a subclass of BaseModel."""
        self.assertIsInstance(Review(), BaseModel)

    def test_string_defaults(self):
        """Check that all attributes are empty strings by default."""
        review = Review()
        for name in ["place_id", "user_id", "text"]:
            self.assertEqual(getattr(review, name), "")

    def test_to_dict_class_name(self):
        """Check that to_dict() stores the class name Review."""
        self.assertEqual(Review().to_dict()["__class__"], "Review")

    def test_from_dict(self):
        """Check that a Review can be rebuilt from its dictionary."""
        review = Review()
        review.text = "Great stay"
        new_review = Review(**review.to_dict())
        self.assertEqual(new_review.id, review.id)
        self.assertEqual(new_review.text, "Great stay")


if __name__ == "__main__":
    unittest.main()
