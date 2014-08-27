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
      self.build_thread(thread_dict)
    except KeyError:
      #when requesting with /thread?, we have {"threadnum": threadobj}
      #when working on /index? results, it seems not.
      #print("[Thread.gotKeyError]")
      self.build_thread(list(thread_dict.values())[0]) #at least, we have an object.

  def build_thread(self, thread_dict):
    #print("[Thread.build_thread]")
    self.op = Post(thread_dict["op"])
    try:
      #AH FUCKING PY3K, FUCK YOU AND YOUR FUCKING BROKEN MAP
      thread_dict["posts"] = [Post(post_obj) for post_num, post_obj in sorted(thread_dict["posts"].items())]
    except AttributeError:
      thread_dict["posts"] = [Post(post_obj) for post_obj in thread_dict["posts"]]
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
  DEFAULTS = [
  "media_id", "spoiler", "preview_orig", "media", "preview_op",
  "preview_reply", "preview_w",  "preview_h", "media_filename",
  "media_w", "media_h", "media_size", "media_hash", "media_orig",
  "exif", "total", "banned", "media_status", "safe_media_hash",
  "remote_media_link", "media_link", "thumb_link", "media_filename_processed"]
  def __init__(self, post_dict):
    #if the post has no image/video, post_dict is None.
    post_dict = post_dict or self.default_dict()
    for post_key in (post_dict):
      self.__dict__[post_key] = post_dict[post_key]   

  def default_dict(self):
    d_ = {}
    for key in self.DEFAULTS: d_[key] = None
    return d_ 

  def __repr__(self):
    return repr(self.__dict__)
