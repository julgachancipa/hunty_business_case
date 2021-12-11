from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Float
from config.db import meta, engine

vacancies = Table(
    "vacancies",
    meta,
    Column("id", Integer, primary_key=True),
    Column("position_name", String(50)),
    Column("vacancy_link", String(200)),
    Column("company_id", Integer),
    Column("salary", Float),
    Column("skills", String(500)),
    Column("min_experience", Integer),
    Column("max_experience", Integer),
)

meta.create_all(engine)
