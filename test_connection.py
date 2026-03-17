from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://siluni:SiluAbc@database-1.ct0qcsm60es8.us-east-2.rds.amazonaws.com:5432/amazon_rec"
)

print(engine.connect())