#!/usr/bin/python3
"""Base Model"""


import uuid
from datetime import datetime

class BaseModel():
	"""Class BaseModel creation"""
	def __init__(self):
		"""Task 3 - Initialization of instances"""
		self.id = str(uuid.uuid4())
		time = datetime.now()
		self.created_at = time
		self.updated_at = time

	def __str__(self):
		"""Task 3 - Method to print class name, 
		self.id and self.__dict__"""
		cl_name = "[" + __class__.__name__ + "]"
		id = " (" + self.id + ")"
		dictio = " "+str(self.__dict__)
		return cl_name + id + dictio

	def save(self):
		"""Task 3 - Method to update updated_at"""
		self.updated_at = datetime.now()

	def to_dict(self):
		"""Task 3 - Method to return a dict 
		with all keys/values"""
		dic = {}
		dic["__class__"] = __class__.__name__
		for key in self.__dict__:
			if key == "created_at" or key == "updated_at":
					dic[key] = self.__dict__[key].isoformat()
			else:
					dic[key] = self.__dict__[key]
		return dic


hola = BaseModel()
print(hola)
print(hola.created_at)
print(hola.created_at.isoformat())
print(hola.to_dict())
