#!/usr/bin/python3
from models.base_model import BaseModel
from models.user import User
from models.place import Place

my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print(my_model)
print("______________")
user = User()
print("--")
print(user)
print("--")
print(user.to_dict())
print()
place = Place()
print(place)
print("--")
print(place.to_dict())