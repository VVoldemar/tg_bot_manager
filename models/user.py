import datetime
import sqlalchemy as sa
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = "user"

    id = sa.Column(sa.Integer, primary_key=True)
    register_date = sa.Column(sa.DateTime, nullable=False)
    subscription_type = sa.Column(sa.String, default=None, nullable=True)
    subscription_expiration = sa.Column(sa.DateTime, default=None, nullable=True)
    is_banned = sa.Column(sa.Boolean, default=False, nullable=False)