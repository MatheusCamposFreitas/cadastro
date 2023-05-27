from domain.user import User
from repositories.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def create_user(self, cpf, nome, email, pis, senha):
        # Lógica para criar um novo usuário
        # Pode incluir validações, criptografia de senha, etc.
        user = User(cpf=cpf, nome=nome, email=email, pis=pis, senha=senha)
        self.user_repository.create(user)

    def get_user_by_id(self, user_id):
        # Lógica para obter um usuário pelo ID
        user = self.user_repository.get_by_id(user_id)
        return user
