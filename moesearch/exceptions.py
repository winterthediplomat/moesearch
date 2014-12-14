#!/usr/bin/python3

from pprint import pprint

class ArchiveException(Exception):
  def __init__(self, response_dict):
    super(Exception, self).__init__(response_dict["error"], response_dict)

  @staticmethod
  def is_error(response_dict):
    try:
      return list(response_dict.keys()) == ["error"]
    except AttributeError: #that's a list, we're safe!
      return False
