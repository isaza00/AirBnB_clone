#!/usr/bin/python3
"""
    Amenity (models/amenity.py):

    Public class attributes:
        name: string - empty string
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """ state class inherits from BaseModel """

    name = ""
