from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

DATABASE_URL = "mysql+pymysql://root:root@localhost:3307/pw2";
Base = declarative_base()
engine = create_engine(DATABASE_URL)
