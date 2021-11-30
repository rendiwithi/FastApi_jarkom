from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

products = Table('products',meta,
Column('id', Integer, primary_key=True,autoincrement=True),
Column('name', String(255)),
Column('type', String(255)),
Column('quantity', Integer),
)

meta.create_all(engine)