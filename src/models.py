from flask_sqlalchemy import SQLAlchemy
# db == base de datos
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }


class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(120), db.ForeignKey('user.id'))
    nameFavorite = db.Column(db.String(30), unique=False, nullable=False)
    typeFavorite = db.Column(db.String(30), unique=False, nullable=False)
    relationUser = db.relationship("User") 
    


    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "nameFavorite": self.nameFavorite,
            "typeFavorite": self.typeFavorite
        }

class Personajes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    homeworld = db.Column(db.String(30), unique=False)
    age = db.Column(db.Integer)
    vehicle = db.Column(db.String(30), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "homeworld": self.homeworld,
            "age": self.age,
            "vehicle": self.vehicle,
        }
#    def __repr__(self):
#       return '<User %r>' % self.username
