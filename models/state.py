#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = column(string(128), nullable=False)
    cities = relationship(City, cascade="all, delete, delete_orphan", backref="state")
    @property
    def cities (self):
        return (city for city in self.cities if State.id = city.state_id)