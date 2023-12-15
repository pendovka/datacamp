from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base

engine = create_engine("postgresql+psycopg2://pendovka:e1b58k@localhost:5432/apps")
session = Session(engine)
Base = declarative_base()
