#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""

from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


class DBStorage:
    """ this class manage the db storage for hbnb clone"""
    __engine = None
    __session = None

    def __init__(self):
        """constructor for DBstorage class"""
        user =  os.environ.get('HBNB_MYSQL_USER')
        password = os.environ.get('HBNB_MYSQL_PWD')
        host =  os.environ.get('HBNB_MYSQL_HOST')
        database = os.environ.get('HBNB_MYSQL_DB')
        
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, password, host, database),
                                      pool_pre_ping=True)
        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)
            
    def all(self, cls=None):
        """query on the current database session,
        all objects depending of the class name"""
        session = self.__session
        
    def new(self, obj):
        """ add the object to the current database session """
        if obj:
            self.__session.add(obj)
    
    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()
    
    def delete(self, obj=None):
        """ delete from module import symbol
        the current database session obj if not None """
        if obj:
            self.__session.delete(obj)
    
    

        