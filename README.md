MoeSearch
=========

A stupid Python library for [archive.moe](https://archive.moe) (ex FoolzArchive) REST API.

Useless binaries included.

BEWARE
------

This software is experimental, use it at your own risk.
For those who want to try this...  
[PyPI archive](https://pypi.python.org/pypi/moesearch/)

Quickstart
--------

(You can check the executables in /bin folder).
FoolFuuka docs are [at foolz.us](http://www.foolz.us/docs/foolfuuka/documentation.html#rest-api)
```py
>>> import moesearch
>>> print(moesearch.search(board="a", text="woxxy")[2].comment)
>>112732805
Fuck Woxxy.
>>> print(moesearch.index("a", 1)["112834776"].op.media.media_link)
http://data.archive.moe/board/a/image/1366/74/1366741186747.jpg
>>> print(moesearch.post("a", 112766871).board.short_name)
a
>>> print(moesearch.thread("a", 112800651).posts[0].comment)
>>112800651
I fucking went grocery shopping all the time when I was a kid. I didn't have qt lesbian friends to go with though.
```
