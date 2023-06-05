from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    cpf = Column(String(20), primary_key=True)
    nome = Column(String(20))
    email = Column(String(20))
    pis = Column(String(20))
    senha = Column(String(20))

    def to_dict(self):
        return {
            'cpf': self.cpf,
            'nome': self.nome,
            'email': self.email,
            'pis': self.pis,
            'senha': self.senha
        }