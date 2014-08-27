#!/usr/bin/python3

from pprint import pprint
from .exceptions import ExceptionFactory
from collections import namedtuple

Board = namedtuple("Board", "short_name name")

class Post(object):
  def __init__(self, post_dict):
    #print("[Post.init]", post_dict)
    for post_key in post_dict:
      if post_key == "media":
        self.__dict__[post_key] = Media(post_dict[post_key])
      elif post_key == "board":
        self.__dict__[post_key] = Board(post_dict[post_key]["shortname"],
                                        post_dict[post_key]["name"])
      else:
        self.__dict__[post_key] = post_dict[post_key]

  def __repr__(self):
    return repr(self.__dict__)

class Thread(object):
  def __init__(self, thread_dict):
    #print("[Thread.init]", list(thread_dict.keys()))
    try:
      self.thread_number = -1
      self.build_thread(thread_dict)
    except KeyError:
      #when requesting with /thread?, we have {"threadnum": threadobj}
      #when working on /index? results, it seems not.
      #print("[Thread.gotKeyError]")
      self.thread_number = list(thread_dict.keys())[0]
      self.build_thread(thread_dict[self.thread_number])

  def build_thread(self, thread_dict):
    #print("[Thread.build_thread]")
    self.op = Post(thread_dict["op"])
    try:
      #AH FUCKING PY3K, FUCK YOU AND YOUR FUCKING BROKEN MAP
      thread_dict["posts"] = [Post(post_obj) for post_num, post_obj in thread_dict["posts"].items()]
    except KeyError:
      thread_dict["posts"] = list()
    self.posts = thread_dict["posts"]

  def __repr__(self):
    return repr(self.__dict__)

class IndexResult(Thread):
  def __init__(self, thread_dict):
    if "error" in thread_dict:
      raise ExceptionFactory.generateException(thread_dict)
    Thread.__init__(self, thread_dict)
    self.omitted = thread_dict["omitted"]
    self.images_omitted = thread_dict["images_omitted"]

class Media(object):
  def __init__(self, post_dict):
    #if the post has no image/video, post_dict is None.
    for post_key in (post_dict or dict()):
      self.__dict__[post_key] = post_dict[post_key]   

  def __repr__(self):
    return repr(self.__dict__)
