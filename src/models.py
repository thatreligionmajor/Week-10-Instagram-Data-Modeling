import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    firstname = Column(String(30), nullable=False)
    lastname = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False)

    def serialize(self):
        return{
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
        }


class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    following_user_id = Column(Integer, ForeignKey('user.id'))
    followed_user_id = Column(Integer, ForeignKey('user.id'))

    def serialize(self):
        return {
            #nothing, I believe
        }

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = relationship(User)
    post_date = Column(Integer, nullable=False)
    post_time = Column(Integer, nullable=False)
    caption = Column(String, nullable=True)

    def serialize(self):
        return {
            "post_date": self.post_date,
            "post_time": self.post_time,
            "caption": self.caption,
        }

class Filter(Base):
    __tablename__ = 'filter'
    id = Column(Integer, primary_key=True)
    media_id = Column(Integer, ForeignKey('media.id'))
    filter_name = Column(String, nullable=True)

    def serialize(self):
        return {
            "filter_name": self.filter_name,
        }

class Media(Base):
    __tablename__ = 'media'
    post_id = Column(Integer, ForeignKey('post.id'))
    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    url = Column(String, nullable=False)
    filter_id = relationship(Filter)
    post_position = Column(Integer, nullable=False)
    latitude = Column(String, nullable=True)
    longitude = Column(String, nullable=True)

    def serialize(self):
        return {
            "type": self.type,
            "url": self.url,
            "post_position": self.post_position,
            "latitude": self.latitude,
            "longitude": self.longitude
        } 

class Media_Effects(Base):
    __tablename__ = 'media_effects'
    id = Column(Integer, primary_key=True)
    media_relationship = relationship(Media)
    media_id = Column(Integer, ForeignKey('media.id'))
    scale = Column(Integer, nullable=True)

    def serialize(self):
        return {
            "effect_id": self.effect_id,
            "scale": self.scale
        }

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String, nullable=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    comment_date = Column(String, nullable=True)
    comment_time = Column(String, nullable=True)

    def serialize(self):
        return {
            "comment_text": self.comment_text,
            "author_id": self.author_id,
            "post_id": self.post_id,
            "comment_date": self.comment_date,
            "comment_time": self.comment_time,
        }

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
