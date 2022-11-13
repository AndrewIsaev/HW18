from dao.movie import MovieDao


class MovieService:
    def __init__(self, dao: MovieDao):
        self.dao = dao

    def get_all(self, args):
        if "director_id" in args:
            return self.dao.get_by_director(director_id=args.get("director_id"))
        elif "genre_id" in args:
            return self.dao.get_by_genre(genre_id=args.get("genre_id"))
        elif "year" in args:
            return self.dao.get_by_year(year=args.get("year"))
        return self.dao.get_all(args)

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        self.dao.update(data)
        return self.dao

    def delete(self,mid):
        self.dao.delete(mid)