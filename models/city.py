#!/usr/bin/python3
"""
    City (models/city.py):

    Public class attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
"""


from models.base_model import BaseModel


class City(BaseModel):
    """ state class inherits from BaseModel """

    state_id = ""
    name = ""
