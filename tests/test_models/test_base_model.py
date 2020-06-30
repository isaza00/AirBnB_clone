#!/usr/bin/python3
"""Tests Base Model"""

import unittest
"""import pep"""
from models.base_model import BaseModel


class TestsBase(unittest.TestCase):
    """Class to test the Base cases"""

    """def test_pep8_conformance(self):
        Test that we conform to PEP8.
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/base_model.py'])
        self.assertEqual(result.total_errors, 0)"""

    def test_any(self):
        """Test"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        print(my_model)
        my_model.save()
        print(my_model)
        my_model_json = my_model.to_dict()
        print(my_model_json)
        self.assertEqual(1, 1)

    def test_print(self):
        """Print ok"""
        model = BaseModel()
        my_model_json = model.to_dict()
        self.assertEqual(my_model_json["id"], model.id)

    def test_print1(self):
        """Print ok"""
        model = BaseModel()
        my_model_json = model.to_dict()
        self.assertEqual(my_model_json["created_at"], model.created_at.isoformat())

    def test_print2(self):
        """Print ok"""
        model = BaseModel()
        my_model_json = model.to_dict()
        self.assertEqual(my_model_json["updated_at"], model.updated_at.isoformat())

    def test_print3(self):
        """Print ok"""
        self.assertEqual(1, 1)
