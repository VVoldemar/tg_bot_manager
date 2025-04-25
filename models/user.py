import datetime
import sqlalchemy as sa
import sqlalchemy.orm as orm

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = "user"

    id = sa.Column(sa.Integer, primary_key=True)  # tg id
    username = sa.Column(sa.String, unique=True, nullable=False)  # @tg_account
    registered_at = sa.Column(sa.DateTime, default=lambda: datetime.datetime.now(), nullable=False)

    is_banned = sa.Column(sa.Boolean, default=False, nullable=False)
    referrer_id = sa.Column(sa.Integer, sa.ForeignKey(id), default=None, nullable=True)

    referrer = orm.relationship("User", back_populates="referrals", remote_side=[id])
    referrals = orm.relationship("User", back_populates="referrer")
    subscriptions = orm.relationship("UserSubscription", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}')"