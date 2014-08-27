#!/usr/bin/python3

"""
these tests are archive.moe-oriented
"""

import unittest
import moesearch as foolz

def select_first_couple(dict_):
  return list(dict_.items())[0]

class TestIndex(unittest.TestCase):
  def test_boardexception(self):
    self.assertRaises(foolz.exceptions.BoardNotFound,
                      foolz.index,
                      #parameters
                      "alfateam123", 1
                    )
  
  def test_call_a(self):
    res = foolz.index("a", 1)
    self.assertIsInstance(res, dict)
    self.assertIsInstance(select_first_couple(res)[1], foolz.parser.IndexResult)


if __name__ == "__main__":
  unittest.main()
