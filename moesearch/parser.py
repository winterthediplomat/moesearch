#!/usr/bin/python3

from pprint import pprint
from .exceptions import ExceptionFactory

class Post(object):
  def __init__(self, post_dict):
    for post_key in post_dict:
      if post_key == "media":
        self.__dict__[post_key] = Media(post_dict[post_key])
      else:
        self.__dict__[post_key] = post_dict[post_key]

class Thread(object):
  def __init__(self, thread_dict):
    self.op = Post(thread_dict["op"])
    try:
      thread_dict["posts"] = map(Post,thread_dict["posts"]) 
    except KeyError:
      thread_dict["posts"] = list()
    self.posts = thread_dict["posts"]

class IndexResult(Thread):
  def __init__(self, thread_dict):
    if "error" in thread_dict:
      raise ExceptionFactory.generateException(thread_dict)
    Thread.__init__(self, thread_dict)
    self.omitted = thread_dict["omitted"]
    self.images_omitted = thread_dict["images_omitted"]

class Media(object):
  def __init__(self, post_dict):
    for post_key in post_dict:
      self.__dict__[post_key] = post_dict[post_key]   
