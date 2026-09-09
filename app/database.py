from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql://postgres:passwordlocalhost:5432/fastapi todo"

engine = create_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)