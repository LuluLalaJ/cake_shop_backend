#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response, session
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

# Local imports
from config import app, db, api
from models import db, User, Cake, Review, FavoriteCake, Order, OrderCake

@app.before_request
def check_if_logged_in():
    if not session.get('user_id') \
        and request.endpoint != 'signup' \
        and request.endpoint != 'login':
        return {'error': '401 Unauthorized'}, 401

#endpoints for everyone
class Signup(Resource):
    def post(self):
        user_input = request.get_json()
        username = user_input.get('username')
        email = user_input.get('email')
        password = user_input.get('password')

        if username and email and password:
            user = User(
                username=username,
                email=email
            )

            user.password_hash = password
            try:
                db.session.add(user)
                db.session.commit()
                session['user_id'] = user.id
                #not sure why there's recursion error;
                return user.to_dict(), 201

            except IntegrityError:
                return {'error': 'invalid input; username and email must be unique'}, 422

        return {'error': 'username, email, and password cannot be empty'}, 400

class CheckSession(Resource):
    def get(self):
        if session.get('user_id'):
            user = User.query.filter_by(id=session['user_id']).first()
            return user.to_dict(), 200

class Login(Resource):
    def post(self):

        user_input = request.get_json()

        username = user_input.get('username')
        password = user_input.get('password')

        user = User.query.filter_by(username=username).first()

        if user and user.authenticate(password):
            session['user_id'] = user.id
            return user.to_dict(), 200

        return {'error': '401 Unauthorized'}, 401

class Logout(Resource):
    def delete(self):
        if session.get('user_id'):
            session['user_id'] = None
            return {}, 204

api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
