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
    owner = db.Column(db.String(120), db.ForeignKey('user.email'))
    nameFavorite = db.Column(db.String(30), unique=False, nullable=False)
    typeFavorite = db.Column(db.String(30), unique=False, nullable=False)
    relationFavorite = db.relationship("Favorite") 

    def serialize(self):
        return {
            "id": self.id,
            "owner": self.owner,
            "nameFavorite": self.nameFavorite,
            "typeFavorite": self.typeFavorite
        }

#    def __repr__(self):
#       return '<User %r>' % self.username
