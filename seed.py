#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Cake, Review, FavoriteCake, Order, OrderCake

fake = Faker()

def create_users():
    users = []
    usernames = []
    emails = []
    for _ in range(10):
        username = fake.first_name()
        while username in usernames:
            username = fake.first_name()
        usernames.append(username)

        email = fake.email()
        while email in emails:
            email = fake.email()
        emails.append(email)

        user = User(
            username=username,
            email=email
        )

        user.password_hash = user.username + "hello"
        users.append(user)
    db.session.add_all(users)
    db.session.commit()

def create_cakes():
    cakes = []
    cake_names = [
    'Chocolate Cake',
    'Vanilla Cake',
    'Strawberry Cake',
    'Red Velvet Cake',
    'Rainbow Cake',
    'Great British Baking Show Cake',
    'Princess Cake',
    'Holiday Cake',
    'Cup Cake']

    for i in range(len(cake_names)):
        cake = Cake(
            name=cake_names[i],
            price=randint(20, 50),
            description=fake.paragraph(nb_sentence=10),
            image=fake.image_url()
        )
        cakes.append(cake)

    db.session.add_all(cakes)
    db.session.commit()

def create_reviews():
    pass

def create_favorites():
    pass

def create_orders():
    pass

def create_order_cakes():
    pass


if __name__ == '__main__':

    with app.app_context():
        print("Starting seed...")
        User.query.delete()
        Cake.query.delete()
        Review.query.delete()
        FavoriteCake.query.delete()
        Order.query.delete()
        OrderCake.query.delete()
