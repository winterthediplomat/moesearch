#!/usr/bin/env python

from .api import *

def file_extension(filename):
  return filename.split(".")[-1]

def media_in_thread(thread_to_harvest):
  yield thread_to_harvest.op.media
  for post in thread_to_harvest.posts:
    if post.has_media:
      yield post.media

def filter_by_type(posts, ok_types=None, not_ok_types=None):
  for media in posts:
    if ( file_extension(media.media_filename) in ok_types and
         file_extension(media.media_filename) not in not_ok_types):
         yield media
