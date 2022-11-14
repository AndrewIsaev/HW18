from flask_restx import Namespace, Resource

from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace("genres")
genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()


@genre_ns.route("/")
class GenresView(Resource):
    def get(self):
        return genres_schema.dump(genre_service.get_all())


@genre_ns.route("/<int:did>")
class GenreView(Resource):
    def get(self, did):
        return genre_schema.dump(genre_service.get_one(did))
