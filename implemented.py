# файл для создания DAO и сервисов чтобы импортировать их везде
from dao.movie import MovieDao
from dao.services.movie import MovieService
from setup_db import db

movie_dao = MovieDao(session=db.session)
movie_service = MovieService(dao=movie_dao)
#
# review_dao = ReviewDAO(db.session)
# review_service = ReviewService(dao=review_dao)