from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

from config import db, bcrypt

class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    serialize_rules = ("-cakes.users",
                       "-reviews.user",
                       "-favorite_cakes.user",
                       "-orders.user",
                       "-reviews.cake",
                       "-favorite_cakes.cake",
                       "-orders.order_cakes")

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String)

    reviews = db.relationship('Review', back_populates="user", cascade="all, delete-orphan")
    favorite_cakes = db.relationship('FavoriteCake', back_populates="user", cascade="all, delete-orphan")
    orders = db.relationship('Order', back_populates="user", cascade="all, delete-orphan")

    cakes = association_proxy('reviews', 'cake', creator=lambda cake_obj: Review(cake=cake_obj))

    @hybrid_property
    def password_hash(self):
        raise AttributeError("Password hashes can't be viewed")

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8') )
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8')
        )

    def __repr__(self):
        return f'<User: {self.id} {self.username}'

class Cake(db.Model, SerializerMixin):
    __tablename__ = "cakes"

    serialize_rules = ("-users.cakes",
                       "-reviews.cake",
                       "-favorite_cakes.cake",
                       "-order_cakes.cake",
                       "-orders.cakes",
                       "-reviews.user"
                       )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.Numeric(8, 2), nullable=False)
    description = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)

    reviews = db.relationship('Review', back_populates="cake", cascade="all, delete-orphan")
    favorite_cakes = db.relationship('FavoriteCake', back_populates="cake", cascade="all, delete-orphan")
    order_cakes = db.relationship('OrderCake', back_populates="cake", cascade="all, delete-orphan")

    users = association_proxy('reviews', 'user', creator=lambda user_obj: Review(user=user_obj))
    orders = association_proxy('order_cakes', 'order', creator=lambda order_obj: OrderCake(order=order_obj))

    @validates('description')
    def check_length(self, key, description):
        if len(description) >= 50:
            return description
        raise ValueError('Description needs to be longer than 250 chars')

    def __repr__(self):
        return f'<Cake: {self.id} {self.name}>'


class Review(db.Model, SerializerMixin):
    __tablename__ = "reviews"

    serialize_rules = ("-cake.reviews", "-user.reviews",)

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    cake_id = db.Column(db.Integer, db.ForeignKey('cakes.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', back_populates="reviews")
    cake = db.relationship('Cake', back_populates="reviews")


    def __repr__(self):
        return f'Review: {self.id}'

class FavoriteCake(db.Model, SerializerMixin):
    __tablename__ = "favorite_cakes"

    serialize_rules = ("-cake.favorite_cakes", "-user.favorite_cakes",)

    id = db.Column(db.Integer, primary_key=True)

    cake_id = db.Column(db.Integer, db.ForeignKey('cakes.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', back_populates="favorite_cakes")
    cake = db.relationship('Cake', back_populates="favorite_cakes")

    def __repr__(self):
        return f'<FavoriteCake: {self.id} {self.cake.name}>'

class Order(db.Model, SerializerMixin):
    __tablename__ = "orders"

    serialize_rules = ("-user.orders", "-order_cakes.order", "-cakes.orders")

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    total_price = db.Column(db.Numeric(8, 2), default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', back_populates="orders")
    order_cakes = db.relationship('OrderCake', back_populates="order", cascade="all, delete-orphan")

    cakes = association_proxy('order_cakes', 'cake', creator=lambda cake_obj: OrderCake(cake=cake_obj))

    def __repr__(self):
        return f'<Order: {self.id}>'

class OrderCake(db.Model, SerializerMixin):
    __tablename__ = "order_cakes"

    serialize_rules = ("-order.order_cakes", "-cake.order_cakes",)

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, default=0)

    price = db.Column(db.Numeric(8, 2), default=0)

    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    cake_id = db.Column(db.Integer, db.ForeignKey('cakes.id'))

    order = db.relationship('Order', back_populates="order_cakes")
    cake = db.relationship('Cake', back_populates="order_cakes")

    def __repr__(self):
        return f'<OrderCake: {self.id}>'
