from dao.model.director import Director
from dao.model.genre import Genre
from setup_db import db
from marshmallow import Schema, fields


class Movie(db.Model):

    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    description = db.Column(db.String(500))
    trailer = db.Column(db.String(500))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.Foreignkey(Genre.id))
    director_id = db.Column(db.Integer, db.Foreignkey(Director.id))


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float
    genre_id = fields.Int()
    director_id = fields.Int()
