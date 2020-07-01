#!/usr/bin/python3
"""Tests Base Model"""

import unittest
from models.base_model import BaseModel
from models import storage
import os


class TestsBase(unittest.TestCase):
    """Class to test the Base cases"""

    """def test_pep8_conformance(self):
        Test that we conform to PEP8.
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/base_model.py'])
        self.assertEqual(result.total_errors, 0)"""

    """def test_any(self):
        model = BaseModel()
        str1 = "[BaseModel] "
        str2 = "(" + model.id + ") "
        str3 = str(model.__dict__)
        string = str1 + str2 + str3
        self.assertEqual(model.__str__(), string)

    def test_print(self):
        model = BaseModel()
        my_model_json = model.to_dict()
        self.assertEqual(my_model_json["id"], model.id)

    def test_print1(self):
        model = BaseModel()
        my_model_json = model.to_dict()
        self.assertEqual(my_model_json["created_at"], model.created_at.isoformat())

    def test_print2(self):
        model = BaseModel()
        my_model_json = model.to_dict()
        self.assertEqual(my_model_json["updated_at"], model.updated_at.isoformat())
    """
    
    def test_print3(self):
        """Print ok"""
        
        model = BaseModel()
        model.save()
        dic = storage.all()
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print(dic)
        new_model = BaseModel(**dic)
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print(model)
        print(new_model)
        self.assertEqual(model.to_dict(), new_model.to_dict())
        self.assertNotEqual(model, new_model)
