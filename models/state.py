#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state',
                          cascade="all, delete-orphan")

    @property
    def cities(self):
        """Getter method for class attr cities."""
        from models import storage
        from models.city import City
        cities = storage.all(City)
        cities_list = []
        for i in cities.values():
            if self.id == i.state_id:
                cities_list.append(i)
        return cities_list
