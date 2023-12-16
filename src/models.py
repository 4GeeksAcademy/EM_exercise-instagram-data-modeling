import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    posts = Column(String(250), nullable=False)
    activity = Column(String(250), nullable=False)
    followers = Column(String(250), nullable=False)
    following = Column(String(250), nullable=False)
    likes = Column(String(250), nullable=False)
    histories = Column(String(250), nullable=False)

class Posts(Base):
    __tablename__ = 'posts'

    chat_id = Column(Integer, primary_key=True)
    group_id = Column(String(250),ForeignKey('user'))
    following_status = Column(String(250)), ForeignKey('user.following')
    message_requests = Column(String(250), nullable=False)
    calls = Column(Integer)

class Comments(Base):
    __tablename__ = 'comments'

    comments = Column(Integer, primary_key=True)
    tags = Column(String(250),ForeignKey('posts'))
    follows = Column(String(250))
    follows_requests = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
