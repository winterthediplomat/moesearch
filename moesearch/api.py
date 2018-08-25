#!/usr/bin/python3

import requests
from .parser import *
from .exceptions import ArchiveException
from pprint import pprint

#disabling warnings about unverified SSL certificates
#as urllib3 is embedded, we don't have to worry about
#urllib3 being missing.
requests.packages.urllib3.disable_warnings()

# archiver_url is now an argument, so you can use https://archived.moe, https://rbt.asia, or https://4plebs.org
#archiver_url = "https://desuarchive.org"
FOOLFUUKA_API_URL = "%s/_/api/chan"

def index(archiver_url, board, page=1):
  req = requests.get("{}/index".format(FOOLFUUKA_API_URL % archiver_url),
          stream=False, verify=False,
          params = {"board": str(board), "page": int(page)})
  #print(req.content)
  res = req.json()
  if ArchiveException.is_error(res):
    raise ArchiveException(res)
  for thread_num in res:
    res[thread_num] = IndexResult(res[thread_num])
  return res 

def search(archiver_url, board, **kwargs):
  url = "{}/search".format(FOOLFUUKA_API_URL % archiver_url)
  try:
    kwargs["boards"] = board.lower() #it's a string?
  except AttributeError:
    try: 
    #https://github.com/FoolCode/FoolFuuka/blob/master/src/Controller/Api/Chan.php#L328
      kwargs["boards"] = ".".join([str(b) for b in board]) #we got a list of boards!
    except TypeError: #it's not an iterable (probably a Board object): try to convert it
      kwargs["boards"] = str(board)
  req = requests.get(url, stream=False, verify=True, params=kwargs)
  res = req.json()
  if ArchiveException.is_error(res):
    raise ArchiveException(res)
  res = res['0']
  return [Post(post_obj) for post_obj in res["posts"]]

def thread(archiver_url, board, thread_num, latest_doc_id=-1, last_limit=-1):
  url = "{}/thread".format(FOOLFUUKA_API_URL % archiver_url)
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

def post(archiver_url, board, post_num):
  req = requests.get("{}/post".format(FOOLFUUKA_API_URL % archiver_url),
                  verify=True,  stream=False,
                  params={"board":str(board), "num":post_num})
  res = req.json()
  if ArchiveException.is_error(res):
    raise ArchiveException(res)
  return Post(res)
