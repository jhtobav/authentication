# app/models.py

from app import db


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

    def validate_password(self, password):
        return self.password_hash == password


    def __str__(self):
        return "User: {} {}".format(self.name, self.last_name) 
