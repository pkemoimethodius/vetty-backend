from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from models import db, Service
from models import Customer, Location, Product, Review, Service
from db import db



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vetty.db'  # SQLite for simplicity, or your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disables track modifications (optional)
app.config['SQLALCHEMY_ECHO'] = True  # Optional: Prints SQL statements for debugging

db.init_app(app)
# db = SQLAlchemy(app)

migrate = Migrate(app, db)

def create_tables():
    db.create_all()


@app.route('/', methods=['GET'])
def hello():
    return "Hello, Welcome to the Flask API!"


if __name__ == '__main__':
    app.run(debug=True)
