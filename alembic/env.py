import sys
import os
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

sys.path.append(os.getcwd())

from db.base import Base
from db import *

target_metadata = Base.metadata

config = context.config
fileConfig(config.config_file_name)

config.set_main_option("sqlalchemy.url", os.environ["POSTGRES_URL"])

url = config.get_main_option("sqlalchemy.url")
connectable = engine_from_config(
    config.get_section(config.config_ini_section), prefix="sqlalchemy.", poolclass=pool.NullPool
)

with connectable.connect() as connection:
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()
