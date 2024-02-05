from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime

class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    testimonials = db.relationship('Testimonial', backref='user')
    
class Barber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    information = db.Column(db.String(128), nullable=False)
    
    # Relationship with Booking model
    bookings = db.relationship('Booking', backref='barber')

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Integer, nullable=False)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    barber_id = db.Column(db.Integer, db.ForeignKey('barber.id'), nullable=False)
    service = db.Column(db.String(128), nullable=False)
    date = db.Column(db.String(10), nullable=False)  # You may want to use Date type
    time = db.Column(db.String(8), nullable=False)  # You may want to use Time type
    phone_number = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    
    def __repr__(self):
        return f"Booking(id={self.id}, barber_id={self.barber_id}, service={self.service}, date={self.date}, time={self.time}, phone_number={self.phone_number})"
