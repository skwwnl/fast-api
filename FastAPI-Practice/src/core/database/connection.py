from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:"

engine = create_engine(DATABASE_URL)

SessionFactory = sessionmaker(
    autocommit=False, autoflush=False, expire_on_commit=False, bind=engine
)


def get_db():
    session = SessionFactory()
    try:
        yield session
    finally:
        session.close()
