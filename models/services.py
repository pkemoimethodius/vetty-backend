from flask_sqlalchemy import SQLAlchemy
from db import db

# db = SQLAlchemy()

class Service(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"Service(id={self.id}, name='{self.name}', price={self.price}, type='{self.service_type}')"
