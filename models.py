from database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__  = "my_posts"
    zipcode = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    place = Column(String, unique=True, index=True)

