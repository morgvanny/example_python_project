from sqlalchemy import (PrimaryKeyConstraint, Column, Integer, String)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SuperHero(Base):

    __tablename__ = 'super_heroes'

    __table_args__ = (PrimaryKeyConstraint('id'), )

    id = Column(Integer())
    name = Column(String())
    power = Column(String())
