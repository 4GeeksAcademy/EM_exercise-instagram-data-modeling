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
    username = Column(String(250), ForeignKey('messages'),ForeignKey('notifications'),ForeignKey('feed'), nullable=False)
    name = Column(String(250), nullable=False)
    posts = Column(String(250), nullable=False)
    activity = Column(String(250), nullable=False)
    followers = Column(String(250), nullable=False)
    following = Column(String(250), nullable=False)
    likes = Column(String(250), nullable=False)
    histories = Column(String(250), nullable=False)

class Messages(Base):
    __tablename__ = 'messages'

    chat_id = Column(Integer, primary_key=True)
    group_id = Column(String(250))
    following_status = Column(String(250)), ForeignKey('user.following')
    message_requests = Column(String(250), nullable=False)
    calls = Column(Integer)

class Notifications(Base):
    __tablename__ = 'notifications'

    comments = Column(Integer, primary_key=True)
    tags = Column(String(250))
    follows = Column(String(250))
    follows_requests = Column(String(250), nullable=False)

class Feed(Base):
    __tablename__ = 'feed'

    following_posts = Column(Integer, primary_key=True)
    ads_posts = Column(Integer), ForeignKey('user.activity')
    comments = Column(String(250))
    likes = Column(String(250), nullable=False)








    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
