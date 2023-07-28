from time import timezone
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import pytz

Base = declarative_base()

class Cepx(Base):
    __tablename__ = 'code'
    cpex = Column(String, primary_key=True)
    creation_date = Column(DateTime, default=lambda: datetime.now(pytz.timezone('America/Sao_Paulo')))