from sqlalchemy import create_engine, String, Integer, Column, Boolean, DateTime
from fastapi import FastAPI
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Person(Base):
    __tablename__ = 'customer'
    id = Column('id', Integer, primary_key=True)
    firstname = Column('first_name', String(128))
    lastname = Column('last_name', String(128))
    password = Column('password', String(60))
    phone = Column('phone', String(15))
    email = Column('email', String(319))
    is_verified = Column(Boolean)
    created_at = Column(DateTime)

    def __init__(self, id, firstname, lastname, password, phone, email, is_verified, created_at):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.phone = phone
        self.email = email
        self.is_verified = is_verified
        self.created_at = created_at

    def repr(self):
        return f"({self.id} {self.firstname} {self.lastname} ({self.password} {self.phone} {self.email} {self.is_verified} {self.created_at})"
    