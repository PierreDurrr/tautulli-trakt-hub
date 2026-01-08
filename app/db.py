from sqlalchemy import (
    create_engine, Column, Integer, String, Boolean, ForeignKey
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DB_PATH

engine = create_engine(f"sqlite:///{DB_PATH}")
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    plex_username = Column(String, unique=True)
    plex_user_id = Column(String)
    is_managed = Column(Boolean, default=False)
    enabled = Column(Boolean, default=True)

class TraktToken(Base):
    __tablename__ = "trakt_tokens"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    access_token = Column(String)
    refresh_token = Column(String)
    expires_at = Column(Integer)
    auto_refresh = Column(Boolean, default=True)

Base.metadata.create_all(engine)
