#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response, session
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

# Local imports
from config import app, db, api
from models import db, User, Cake, Review, FavoriteCake, Order, OrderCake

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
        return {'error': '401 Unauthorized'}, 401

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
        return {'error': '401 Unauthorized'}, 401

class Cakes(Resource):
    def get(self):
        cakes = Cake.query.all()
        cakes_serialized = [cake.to_dict(only=("id", "name", "price", "description", "image", "reviews")) for cake in cakes]
        return cakes_serialized, 200

class CakesById(Resource):
    def get(self, id):
        cake = Cake.query.filter_by(id=id).first()
        if cake:
            return cake.to_dict(only=("id", "name", "price", "description", "image", "reviews")), 200
        return {'error': 'Cake not found'}, 404

class Order(Resource):
    pass


class Reviews(Resource):
    def get(self):
        if session.get('user_id'):
            reviews = Review.query.all()
            reviews_serialized = [review.to_dict(only=('id', 'content', 'user.username', 'cake.name')) for review in reviews]
            return reviews_serialized, 200
        return {'error' : '401 Unauthorized'}, 401

    def post(self):
        if session.get('user_id'):
                cake_id = request.get_json()['cake_id']
                cake = Cake.query.filter_by(id = cake_id).first()
                if cake:
                    new_review = Review(
                        content = request.get_json()['content'],
                        user_id = session['user_id'],
                        cake_id = request.get_json()['cake_id']
                    )
                    db.session.add(new_review)
                    db.session.commit()
                    return new_review.to_dict(), 201
                else: 
                    return {'error': "Cake does not exist."}, 422
        return {'error' : '401 Unauthorized'}, 401

class ReviewsById(Resource):
    def get(self, id):
        if session.get('user_id'):
            review = Review.query.filter_by(id=id).first()
            if review:
                return review.to_dict(only=('id', 'content', 'user', 'cake')), 200
            return {'error' : 'Review not found'}, 404
        return {'error' : '401 Unauthorized'}, 401
    
    def patch(self,id):
        if session.get('user_id'):
            review = Review.query.filter_by(id=id).first()
            if review:
                for attr in request.get_json():
                    setattr(review, attr, request.json[attr])
                db.session.add(review)
                db.session.commit()
                return review.to_dict(), 200
            return {'error' : 'Review not found'}, 404
        
        return {'error' : '401 Unauthorized'}, 401
    
    def delete(self,id):
        if session.get('user_id'):
            review = Review.query.filter_by(id=id).first()
            if review:
                db.session.delete(review)
                db.session.commit()
                return {'message': 'record successfully deleted'}, 204
            return {'error' : 'Review not found'}, 404
        return {'error' : '401 Unauthorized'}, 401
            

    
    
api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')
api.add_resource(Cakes, '/cakes', endpoint='cakes')
api.add_resource(CakesById, '/cakes/<int:id>', endpoint='/cakes/<int:id>')
api.add_resource(Reviews, '/reviews', endpoint = '/reviews')
api.add_resource(ReviewsById, '/reviews/<int:id>', endpoint = '/reviews/<int:id>')



if __name__ == '__main__':
    app.run(port=5555, debug=True)
