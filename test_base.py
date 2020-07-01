#!/usr/bin/python3
from models.base_model import BaseModel
from models.place import Place

place = Place()
print(place)
print()
print(place.to_dict())
place.save()
print(getattr(place, "longitude", False))
setattr(Place, "longitude", 8374)
print(place.to_dict())
