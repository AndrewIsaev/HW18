from dao.model.movie import Movie


class MovieDao:
    def __init__(self, session):
        self.session = session

    def get_all(self, args):

        return self.session.query(Movie).all()

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_by_director(self, director_id):
        return self.session.query(Movie).filter(Movie.director_id == director_id)

    def get_by_genre(self, genre_id):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id)

    def get_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year)

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, data):
        mid = data.get("id")
        movie = self.get_one(mid)

        movie.id = data.get("id")
        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id ")
        movie.director_id = data.get("director_id")
        self.session.add(movie)
        self.session.commit()



    def delete(self, mid):
        movie = self.get_one(mid)

        self.session.delete(movie)
        self.session.commit()
