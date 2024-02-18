#!/usr/bin/python3
"""
class definition of a State and an instance Base
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    id (integer): unique integet auto-generated
    name (str): the name of state
    """
    __tablename__ = "states"
    id = Column(Integer,
                autoincrement=True,
                primary_key=True,
                nullable=False)
    name = Column(String(128), nullable=False)
