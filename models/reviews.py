from flask_sqlalchemy import SQLAlchemy
from db import db

# db = SQLAlchemy()

class Review(db.Model):
    __tablename__ = 'reviews'

    review_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    customer_id = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    review_text = db.Column(db.String(500), nullable=False)
    review_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(50), nullable=False)

    # Define the relationship to the Product model
    product = db.relationship('Product', back_populates='reviews')

    def __repr__(self):
        return f"Review(review_id={self.review_id}, product_id={self.product_id}, customer_id={self.customer_id}, " \
               f"rating={self.rating}, review_text='{self.review_text}', review_date='{self.review_date}', status='{self.status}')"
