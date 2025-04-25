import datetime
import enum
import sqlalchemy as sa
import sqlalchemy.orm as orm

import strings
from .db_session import SqlAlchemyBase
from .user import User


class SubscriptionLevel(enum.Enum):
    BASIC = strings.SUBSCRIPTION.BASIC
    MEDIUM = strings.SUBSCRIPTION.MEDIUM
    PREMIUM = strings.SUBSCRIPTION.PREMIUM


class SubscriptionType(SqlAlchemyBase):
    __tablename__ = "subscription_types"

    id = sa.Column(sa.Integer, primary_key=True)
    level = sa.Column(sa.Enum(SubscriptionLevel), unique=True, nullable=False)

    def __repr__(self):
        return f"<SubscriptionType(level='{self.level.name}')>"


class UserSubscription(SqlAlchemyBase):
    __tablename__ = "user_subscription"

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey(User.id), nullable=False)
    subscription_id = sa.Column(sa.Integer, sa.ForeignKey(SubscriptionType.id), nullable=False)
    expires_at = sa.Column(sa.DateTime, nullable=False)

    user = orm.relationship(User, back_populates="subscriptions")
    subscription = orm.relationship(SubscriptionType)

    def is_active(self):
        return self.expires_at > datetime.datetime.now()

    def extend(self, duration: datetime.timedelta):
        self.expires_at += duration

    def __repr__(self):
        status = 'active' if self.is_active() else 'inactive'
        return (f"<UserSubscription(user_id='{self.user_id}', sub_id={self.subscription_id}, expires='{self.expires_at}',"
                f" status='{status}'>")