#!/usr/bin/python3

import requests
#from parser import Post, IndexResult
from .parser import IndexResult
from .exceptions import is_error, ExceptionFactory
#from json import loads
from pprint import pprint

def index(board, page):
  res = requests.get("http://api.archive.moe/index?board=%s&page=%d"%(board, page), stream=False).json()
  if is_error(res):
    #print(res)
    raise ExceptionFactory.generateException(res) #ValueError("got an error!")
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
  pass
