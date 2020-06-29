#!/usr/bin/python3
from models.base_model import BaseModel
from models.user import User
from models.place import Place


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