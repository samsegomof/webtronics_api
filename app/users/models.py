from datetime import datetime

from sqlalchemy import Column, Integer, String, TIMESTAMP

from app.database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)
