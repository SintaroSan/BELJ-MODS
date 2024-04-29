import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Mods(SqlAlchemyBase):
    __tablename__ = 'mods'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    author_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    game_image = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    game_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    visible_game_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    mod_name = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True)
    visible_mod_name = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True)
    game_version = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    about_mod = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    download_guide = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    game_link = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)