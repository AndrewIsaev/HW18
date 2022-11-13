from flask import request
from flask_restx import Namespace, Resource

from dao.model.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace("movies")
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route("/")
class MoviesView(Resource):

    def get(self):
        director_id = request.args.get("director_id")
        genre_id = request.args.get("genre_id")
        year = request.args.get("year")

        args = {
            "director_id": director_id,
            "genre_id": genre_id,
            "year": year
        }
        return movies_schema.dump(movie_service.get_all(args))

    def post(self):
        req_json = request.json
        movie_service.create(req_json)
        return "", 201


@movie_ns.route("/<int:mid>")
class MovieView(Resource):
    def get(self, mid):
        return movie_schema.dump(movie_service.get_one(mid))

    def put(self, mid):
        req_json = request.json
        req_json["id"] = mid
        movie_service.update(req_json)
        return "", 204

    def delete(self, mid):
        movie_service.delete(mid)
        return "", 204
