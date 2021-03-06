from flask import request, jsonify, make_response
from flask_restful import abort

from models.user import User
from resources.base_handler import BaseHandler


class UsersHandler(BaseHandler):

    def post(self):
        username = request.get_json().get('username')
        password = request.get_json().get('password')
        if username is None or password is None:
            abort(400, error='No input parameters')
        if User.query.filter_by(username=username).first() is not None:
            abort(400, error='User already exists')
        user_id = self.repository.users.user_create(username, password)
        return make_response(jsonify({'username': username, 'user_id': user_id}), 201)
