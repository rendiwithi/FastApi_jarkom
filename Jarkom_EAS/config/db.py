from sqlalchemy import create_engine, MetaData, engine

engine = create_engine('mysql+pymysql://duck:@localhost:3306/ets_jarkom')
meta = MetaData()
conn = engine.connect()