#!/usr/bin/python3
"""Amenity class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''Class for managing amenity objects'''
    name = ""

    def __init__(self, *args, **kwargs):
        '''Initializes attributes for the Amenity class'''
        super().__init__(*args, **kwargs)
