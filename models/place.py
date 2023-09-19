#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("userss.id"), nullable=False)
    name = column(string(128), nullable=False)
    description = column(String(1024), nullable=False)
    number_rooms = column(Integer, nullable=False, default=0)
    number_bathrooms = column(Integer, nullable=False, default=0)
    max_guest = column(Integer, nullable=False, default=0)
    price_by_night = column(Integer, nullable=False, default=0)
    latitude = column(Float, nullable=False)
    longitude = column(Float, nullable=False)
    
