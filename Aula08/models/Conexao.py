from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
#DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/pw2";
DATABASE_URL = "sqlite:///project.db";
Base = declarative_base()
engine = create_engine(DATABASE_URL)
