#!/usr/bin/python3

"""
these tests are archive.moe-oriented
"""

import unittest
import moesearch as foolz

def select_first_couple(dict_):
  return list(dict_.items())[0]

class TestIndex(unittest.TestCase):
  def setUp(self):
    self.a_index = foolz.index("a", 1)
  
  def test_boardexception(self):
    self.assertRaises(foolz.exceptions.BoardNotFound,
                      foolz.index,
                      #parameters
                      "welovewoxxy", 1
                    )
  
  def test_call_a(self):
    res = self.a_index
    self.assertIsInstance(res, dict)
    self.assertIsInstance(select_first_couple(res)[1], foolz.parser.IndexResult)
  
  def test_isrequestedboard(self):
    """ check the results are from the board we asked for """
    self.assertEqual(0, 
         sum(1 for post_num, post in self.a_index.items() if post.op.board.short_name != 'a')
         )

class TestThread(unittest.TestCase):
  def setUp(self):
    self.muh_thread = foolz.thread('a', 112800651)

  def test_isthatyou(self):
    self.assertEqual(112800651, int(self.muh_thread.op.thread_num))
    self.assertIsInstance(self.muh_thread, foolz.parser.Thread)

  def test_thread_isnota_indexresult(self):
    #http://stackoverflow.com/a/2267788
    self.assertRaises(AttributeError, lambda: self.muh_thread.omitted)
    self.assertRaises(AttributeError, lambda: self.muh_thread.images_omitted)

class TestPost(unittest.TestCase):
  def setUp(self):
    self.media_post      = foolz.post('v', 260289496)
    self.no_media_post   = foolz.post('v', 260289610)
    self.no_comment_post = foolz.post('v', 260289384)

  def test_isthatyou(self):
    """ check the response is the one we're looking for. """
    self.assertEqual('v', self.media_post.board.short_name)
    self.assertEqual('v', self.no_media_post.board.short_name)
    self.assertEqual(260289384, int(self.no_comment_post.num))
    self.assertEqual(260289496, int(self.media_post.num))
    self.assertEqual(260289610, int(self.no_media_post.num))
  
  def test_nomedia_hasattributes(self):
    """ don't crash when asking media data to a no-media post """
    self.assertIsInstance(self.no_media_post.media, foolz.parser.Media)
    self.assertEqual(None, self.no_media_post.media.media_link)
    self.assertEqual(None, self.no_media_post.media.exif)

  def test_media_data(self):
    """ check media data are correct for the media post """
    self.assertEqual("http://data.archive.moe/board/v/image/1401/68/1401683960835.jpg", self.media_post.media.media_link)

  def test_no_comment(self):
    """ if a post has no comment, it has to have an image/webm! """
    self.assertEqual(None, self.no_comment_post.comment)
    self.assertNotEqual(None, self.no_comment_post.media.media_link)

class TestSearch(unittest.TestCase):
  def setUp(self):
    #even though the doc says "board" is required, we can omit it.
    self.muh_vampire_search = foolz.search(subject='vampires')

  def test_aretheyvampires(self):
    pass
    #self.assertEqual(0, sum(1 for post in self.muh_vampire_search if post.title.count("vampires")==0))

if __name__ == "__main__":
  unittest.main()
