from sqlalchemy import Table, Column
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import Integer, String, Float, DateTime
from config.db import meta, engine

companies = Table(
    "companies",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("link", String(200)),
    Column("country", String(50)),
    Column("city", String(50)),
    Column("date_added", DateTime(), server_default=func.now()),
    Column("contact_first_name", String(50)),
    Column("contact_last_name", String(50)),
    Column("contact_phone_number", String(50)),
    Column("contact_email", String(50)),
)

meta.create_all(engine)
