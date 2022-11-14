from flask_restx import Namespace, Resource

from dao.model.director import DirectorSchema
from implemented import director_service

director_ns = Namespace("directors")
directors_schema = DirectorSchema(many=True)
director_schema = DirectorSchema()


@director_ns.route("/")
class DirectorsView(Resource):
    def get(self):
        return directors_schema.dump(director_service.get_all())


@director_ns.route("/<int:did>")
class DirectorView(Resource):
    def get(self, did):
        return director_schema.dump(director_service.get_one(did))
