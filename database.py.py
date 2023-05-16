from fastapi import FastAPI
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, String, Integer, Column, Boolean, DateTime


app = FastAPI()

engine = create_engine("mysql+mysqlconnector://root:root@localhost:3306/web_site")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()




Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()



