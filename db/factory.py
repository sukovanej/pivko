from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def db_session_factory(postgres_url: str):
    some_engine = create_engine(postgres_url)
    Session = sessionmaker(bind=some_engine)
    return Session()
