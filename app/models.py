# app/models.py

from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    """
    User representation on MySQL
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)  

    def set_password_hash(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __str__(self):
        return "User: {} {}".format(self.name, self.last_name) 
