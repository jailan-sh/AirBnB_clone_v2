#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base
import os

engine = create_engine(self.__engine)
class DBStorage(Base):
    """ this class manage the db storage for hbnb clone"""
    __engine = None
    __session = None
    def __init__(self):
        """ init method"""
        user =  os.environ.get('HBNB_MYSQL_USER')
        password = os.environ.get('HBNB_MYSQL_PWD')
        host =  os.environ.get('HBNB_MYSQL_HOST', 'localhost')
        database = os.environ.get('HBNB_MYSQL_DB')
        
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                               .format(user, password, host, database),
                               pool_pre_ping=True)
        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
        else:
            Base.metadata.create_all(self.__engine)
        