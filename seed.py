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
    'Cup Cake',
    'Cheese Cake']

    for i in range(len(cake_names)):
        cake = Cake(
            name=cake_names[i],
            price=randint(20, 50),
            description=fake.paragraph(nb_sentences=10),
            image=fake.image_url()
        )
        cakes.append(cake)

    db.session.add_all(cakes)
    db.session.commit()

def create_reviews():
    reviews = []
    for i in range(30):
        review = Review(
            cake_id = randint(1,11),
            user_id = randint(1,11),
            content = fake.paragraph(nb_sentences=10)
        )
        reviews.append(review)

    db.session.add_all(reviews)
    db.session.commit()

def create_favorites():
    favs = []
    for i in range(10):
        fav = FavoriteCake(
            cake_id = randint(1, 10),
            user_id = randint(1, 10)
        )
        favs.append(fav)
    db.session.add_all(favs)
    db.session.commit()

def create_orders():
    orders = []
    for i in range(10):
        order = Order(
            user_id = randint(1,10)
        )
        orders.append(order)
        # db.session.add(order)
        # db.session.commit()
        # order.total_price = sum([oc.price for oc in order.order_cakes])
        # db.session.add(order)
        # db.session.commit()
    db.session.add_all(orders)
    db.session.commit()
    return orders

def create_order_cakes():
    for i in range(50):
        oc = OrderCake(
            quantity = randint(1, 5),
            order_id = randint(1, 10),
            cake_id = randint(1, 10)
        )

        #too many commits?
        db.session.add(oc)
        db.session.commit()
        oc.price = oc.quantity * oc.cake.price
        db.session.add(oc)
        db.session.commit()

def update_orders_total_price(orders):
    for order in orders:
        order.total_price = sum([oc.price for oc in order.order_cakes])
        db.session.add(order)
        db.session.commit()

if __name__ == '__main__':

    with app.app_context():
        print("Starting seed...")
        User.query.delete()
        Cake.query.delete()
        Review.query.delete()
        FavoriteCake.query.delete()
        Order.query.delete()
        OrderCake.query.delete()


        create_users()
        create_cakes()
        create_reviews()
        create_favorites()
        orders = create_orders()
        create_order_cakes()
        update_orders_total_price(orders)
