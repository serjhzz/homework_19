from flask_restx import Resource, Namespace
from flask import request

from implemented import auth_service


auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        username = req_json.get('username')
        password = req_json.get('password')
        if not all([username, password]):
            return '', 400
        tokens = auth_service.generate_tokens(username, password)
        return tokens, 201

    def put(self):
        req_json = request.json
        token = req_json.get('refresh_token')
        tokens = auth_service.approve_refresh_token(token)
        return tokens, 201
