#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import environ
import models


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))
class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place", cascade="all,delete")
        amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)
    else:
        @property
        def reviews(self):
            """ returns the list of Review instances
            with place_id equals to the current Place.id"""
            reviews_list = []
            for r in storage.all(Review).values():
                if r.place_id == Self.id:
                    reviews_list.append(r)
            return reviews_list

        @property
        def amenities(self):
            """ returns the list of Amenity instances
            based on the attribute amenity_ids that contains all Amenity.id linked to the Place
            """
            amenity_list = []
            amenity_ids = storage.all(Amenity)
            for a in amenity_ids.values():
                if a.place_id == self.id:
                    amenity_list.append(a)
            return amenity_list
        
        @setattr
        def amenities(self, amenity_obj):
            """
            handles append method for adding an Amenity.id
            """
            if isinstance(amenity_obj, Amenity):
                self.amenity_ids.append(obj.id)
