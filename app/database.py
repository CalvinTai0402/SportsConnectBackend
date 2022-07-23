from sqlmodel import Session, create_engine
from .config import settings
from sqlmodel.sql.expression import Select, SelectOfScalar

SelectOfScalar.inherit_cache = True
Select.inherit_cache = True

SQLMODEL_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
engine = create_engine(SQLMODEL_DATABASE_URL)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()