from flask_sqlalchemy import SQLAlchemy
from db import db

# db = SQLAlchemy()

class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    link = db.Column(db.String(255), nullable=True)
    order = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    is_featured = db.Column(db.Boolean, default=False)
    image = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.String(50), nullable=False)

    # Many-to-many relationship with categories (assuming the existence of a Category model)
    categories = db.Column(db.PickleType, nullable=False)

    def __init__(self, name, description, link, order, status, is_featured, image, categories, created_at):
        self.name = name
        self.description = description
        self.link = link
        self.order = order
        self.status = status
        self.is_featured = is_featured
        self.image = image
        self.categories = categories
        self.created_at = created_at

    def __repr__(self):
        return f"Location(id={self.id}, name='{self.name}', description='{self.description}', link='{self.link}', " \
               f"order={self.order}, status='{self.status}', is_featured={self.is_featured}, image='{self.image}', " \
               f"categories={self.categories}, created_at='{self.created_at}')"
