from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self, args):
        if args.get("director_id") is not None:
            return self.dao.get_by_director(director_id=args.get("director_id"))
        elif args.get("genre_id") is not None:
            return self.dao.get_by_genre(genre_id=args.get("genre_id"))
        elif args.get("year") is not None:
            return self.dao.get_by_year(year=args.get("year"))
        else:
            return self.dao.get_all()

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        self.dao.update(data)
        return self.dao

    def delete(self, mid):
        self.dao.delete(mid)
