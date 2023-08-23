#!/usr/bin/python3
'''
Defines the User class with various attributes
'''
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = 'users'

    if getenv('HBNB_TYPE_STORAGE') == 'db':

        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', cascade='all, delete', backref='user',
                              passive_deletes=True)
        reviews = relationship('Review', cascade='all, delete', backref='user',
                               passive_deletes=True)
        # Set default charset to match the db dump charset
        __table_args__ = {'mysql_default_charset': 'latin1'}
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''

    def __init__(self, *args, **kwargs):
        """Initializes a user"""
        super().__init__(*args, **kwargs)
