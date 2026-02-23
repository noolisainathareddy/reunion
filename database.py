from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm import declarative_base
from get_db_credentials import get_db_pass, db_pass

print("Printing db password : " , db_pass)
DATABASE_URL = f'postgresql://postgres:{db_pass}@localhost/reunion'

engine = create_engine(DATABASE_URL,echo=True,pool_size=10,max_overflow=20)

SessionLocal = sessionmaker(bind=engine,class_=Session,expire_on_commit=False, autoflush=False)

Base = declarative_base()


