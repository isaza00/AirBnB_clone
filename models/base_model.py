#!/usr/bin/python3
"""Base Model"""


import uuid
from datetime import datetime
import json
from models.__init__ import storage


class BaseModel():
    """Class BaseModel creation"""
    def __init__(self, *args, **kwargs):
        """Task 3 - Initialization of instances"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.strptime(value,
                                "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Task 3 - Method to print class name,
        self.id and self.__dict__"""
        new_dic = {}

        cl_name = "[" + self.__class__.__name__ + "]"
        id = " (" + self.id + ")"
        dictio = " " + str(self.__dict__)
        return cl_name + id + dictio

    def save(self):
        """Task 3 - Method to update updated_at"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Task 3 - Method to return a dict
        with all keys/values"""
        new_dic = {}
        members = [attr for attr in dir(self)
                   if not callable(getattr(self, attr)) and not
                   attr.startswith("__")]
        new_dic["__class__"] = self.__class__.__name__

        for key in self.__dict__:
            if key == "created_at" or key == "updated_at":
                new_dic[key] = self.__dict__[key].isoformat()
            else:
                new_dic[key] = self.__dict__[key]

        for key in self.__class__.__dict__:
            if key in members:
                    new_dic[key] = self.__class__.__dict__[key]
        return new_dic
