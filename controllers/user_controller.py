from flask import Blueprint, request, jsonify
from services.user_service import UserService
from repositories.user_repository import UserRepository

user_blueprint = Blueprint('user', __name__)
user_repository = UserRepository()


@user_blueprint.route('/users', methods=['POST'])
def create_user():
    cpf = request.json.get('cpf')
    nome = request.json.get('nome')
    email = request.json.get('email')
    pis = request.json.get('pis')
    senha = request.json.get('senha')
    # data = request.get_json()
    # Validações dos dados recebidos (opcional)
    # ...

    user_service = UserService(user_repository)
    user_service.create_user(cpf, nome, email, pis, senha)

    return jsonify(message='User created successfully'), 201


@user_blueprint.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user_service = UserService(user_repository)
    user = user_service.get_user_by_id(user_id)

    if user:
        return jsonify(user), 200
    else:
        return jsonify(message='User not found'), 404
