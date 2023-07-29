from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.Cepx import Cepx

class FindCepx:
    def __init__(self, code) -> None:
        self.code = code
        self.engine = create_engine("sqlite:///datacode.db")
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def SearchCode(self):
       query = self.session.query(Cepx).filter(Cepx.cpex == self.code).first()

       if query:
           return True
       else:
           return False 
