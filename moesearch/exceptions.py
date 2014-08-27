#!/usr/bin/python3

from pprint import pprint

def is_error(error_dict):
  return "error" in error_dict

class ExceptionFactory(object):
  @classmethod
  def generateException(self, error_dict):
    #print("[ExceptionFactory.generateException] error_dict", error_dict)
    #print(type(error_dict))
    if error_dict["error"] == "No board selected.":
      return BoardNotFound("You have not selected a board, or the board you're looking for does not exist")
    else:
      return GenericError("Ehm... Please, go search some Jibril posts on /a/ while I figure it out.")

class ArchiveException(Exception):
  pass

class BoardNotFound(ArchiveException):
  """ the selected board does not exist """

class GenericError(ArchiveException):
  """ ask Woxxy about this. """
