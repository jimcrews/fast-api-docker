import databases
import ormar
import sqlalchemy

from .config import settings

database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()


ormar_base_config = ormar.OrmarConfig(
    database=database, metadata=metadata
)


class User(ormar.Model):
    ormar_config = ormar_base_config.copy(tablename="users")

    id: int = ormar.Integer(primary_key=True)
    email: str = ormar.String(max_length=128, unique=True, nullable=False)
    active: bool = ormar.Boolean(default=True, nullable=False)


# ormar is built on SQLAlchemy core. so you can use alembic to provide database migrations.
# For tests and basic applications, sqlalchemy is more than enough

engine = sqlalchemy.create_engine(settings.db_url)
metadata.create_all(engine)