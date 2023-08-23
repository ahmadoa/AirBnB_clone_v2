#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    # For DBStorage
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade="all,\
            delete-orphan", backref="state")
