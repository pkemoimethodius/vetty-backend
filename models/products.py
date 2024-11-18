from flask_sqlalchemy import SQLAlchemy
from db import db

# db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    imageSrc = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stars = db.Column(db.Integer, nullable=False)
    rates = db.Column(db.Integer, nullable=False)
    discount = db.Column(db.String(50), nullable=True)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    type = db.Column(db.String(50), nullable=False)
    details = db.Column(db.String(500), nullable=True)

    # Define a one-to-many relationship with the Review model
    reviews = db.relationship('Review', back_populates='product')

    def __repr__(self):
        return f"Product(id={self.id}, title='{self.title}', price={self.price}, stars={self.stars}, quantity={self.quantity})"
