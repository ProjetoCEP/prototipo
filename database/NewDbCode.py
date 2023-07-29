from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.Cepx import Cepx

class AcessDbForInsert:
    def __init__(self, code) -> None:
        self.code = code
        self.engine = create_engine("sqlite:///datacode.db")
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def InsertCode(self):
        novo_item = Cepx(cpex=self.code)
        self.session.add(novo_item)
        self.session.commit()
