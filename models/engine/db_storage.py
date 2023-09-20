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
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """ this class manage the db storage for hbnb clone"""
    __engine = None
    __session = None

    def __init__(self):
        """constructor for DBstorage class"""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, password, host, database),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)
            
    def all(self, cls=None):
        """query on the current database session,
        all objects depending of the class name"""
        session = self.__session
        dic = {}
        if not cls:
            tables = [User, State, City, Amenity, Place, Review]

        else:
            if type(cls) == str:
                cls = eval(csl)

            tables = [cls]

        for table in tables:
            query = session.query(table).all()

            for rows in query:
                key = "{}.{}".format(type(rows).__name__, rows.id)
                dic[key] = rows

        return dic
        
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
    
    def reload(self):
        """ create all tables in the database """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

        