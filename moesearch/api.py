#!/usr/bin/python3

import requests
from .parser import *
from .exceptions import is_error, ExceptionFactory
from pprint import pprint

def index(board, page):
  res = requests.get("http://api.archive.moe/index?board=%s&page=%d"%(board, int(page)), stream=False).json()
  if is_error(res):
    raise ExceptionFactory.generateException(res)
  for thread_num in res:
    res[thread_num] = IndexResult(res[thread_num])
  return res 

def search(board, *args):
  defaults = {"email":"", "username":"",
  "tripcode":"", "capcode":"", "subject":"",
  "text":"", "filename":"", "filehash":"",
  "deleted":-1, "ghost":-1, "filter":-1,
  "date_start":"", "date_end":"", "order":""}
  pass
  

def thread(board, thread_num, latest_doc_id=-1, last_limit=-1):
  pass

def post(board, post_num):
  res = requests.get("http://api.archive.moe/post?board=%s&num=%d"%(board, int(post_num)), stream=False)
  if is_error(res):
    raise ExceptionFactory.generateException(res)
  return Post(res)
