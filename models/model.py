import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from database.database import engine

Base = declarative_base()


class EmployeeDetailModel(Base):
    __tablename__ = "register"
    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True)
    f_name = Column(String)
    l_name = Column(String)
    contact = Column(BigInteger)
    SecurityQ = Column(String)
    SecurityA = Column(String)
    password = Column (String)


Base.metadata.create_all(engine)
    