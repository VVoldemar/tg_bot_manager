import logging

import models.db_session
import models.user


def get_or_create(target_user: models.user.User) -> models.user.User:
    session = models.db_session.get_session()

    try:
        with models.db_session.get_session() as session:
            user = session.query(models.user.User).filter(models.user.User.id == target_user.id)
            if not user:
                session.add(target_user)
                session.commit()
                return target_user

            return user
    except Exception as error:
        logging.warn(f"Error: {error}")
        session.rollback()
        raise
