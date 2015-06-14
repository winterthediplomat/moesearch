#!/usr/bin/python3

import requests
from .parser import *
from .exceptions import ArchiveException
from pprint import pprint

#disabling warnings about unverified SSL certificates
#as urllib3 is embedded, we don't have to worry about
#urllib3 being missing.
requests.packages.urllib3.disable_warnings()

def index(board, page=1):
  req = requests.get("https://api.archive.moe/index",
          stream=False, verify=True,
          params = {"board": str(board), "page": int(page)})
  res = req.json()
  if ArchiveException.is_error(res):
    raise ArchiveException(res)
  for thread_num in res:
    res[thread_num] = IndexResult(res[thread_num])
  return res 

def search(board, **kwargs):
  url = "https://api.archive.moe/search"
  try:
    kwargs["boards"] = board.lower() #it's a string?
  except AttributeError: 
    #https://github.com/FoolCode/FoolFuuka/blob/master/src/Controller/Api/Chan.php#L337
    kwargs["boards"] = ".".join([str(b) for b in board]) #we got a list of boards!
  except TypeError: #it's not an iterable (probably a Board object): try to convert it
    kwargs["boards"] = str(board)
  req = requests.get(url, stream=False, verify=True, params=kwargs)
  res = req.json()
  if ArchiveException.is_error(res):
    raise ArchiveException(res)
  res = res[0]
  return [Post(post_obj) for post_obj in res["posts"]]

def thread(board, thread_num, latest_doc_id=-1, last_limit=-1):
  url = "https://api.archive.moe/thread"
  payload = {"board": str(board), "num": thread_num}
  if(latest_doc_id != -1):
    payload["latest_doc_id"] = (int(latest_doc_id))
  if(last_limit != -1):
    payload["last_limit"] = (int(last_limit))
  req = requests.get(url, stream=False, verify=True, params=payload)
  res = req.json()
  if ArchiveException.is_error(res):
    raise ArchiveException(res)
  return Thread(res)

def post(board, post_num):
  req = requests.get("https://api.archive.moe/post", verify=True,  stream=False,
                  params={"board":str(board), "num":post_num})
  res = req.json()
  if ArchiveException.is_error(res):
    raise ArchiveException(res)
  return Post(res)
