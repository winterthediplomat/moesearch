MoeSearch
=========

A Python library for [desuarchive.org](https://desuarchive.org/), [RebeccaBlackTech](https://rbt.asia), [archive.4plebs.org](https://archive.4plebs.org) REST API.  

Helpful binaries included.

Quickstart
--------

(You can check the executables in /bin folder).
FoolFuuka API docs are available [at 4plebs.org.](https://4plebs.tech/foolfuuka/).  
```py
>>> import moesearch
>>> print(moesearch.search(archiver_url="https://desuarchive.org", board="a", text="woxxy")[2].comment)
>>112732805
Fuck Woxxy.
>>> print(moesearch.index("https://desuarchive.org", "a", 1)["112834776"].op.media.media_link)
http://cdn2.desu-usergeneratedcontent.xyz/a/image/1366/74/1366741186747.jpg
>>> print(moesearch.post("https://desuarchive.org, ""a", 112766871).board.short_name)
a
>>> print(moesearch.thread("https://desuarchive.org", "a", 112800651).posts[0].comment)
>>112800651
I fucking went grocery shopping all the time when I was a kid. I didn't have qt lesbian friends to go with though.
```

LICENSE
-------

```
        DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
                    Version 2, December 2004 

 Copyright (C) 2004 Sam Hocevar <sam@hocevar.net> 

 Everyone is permitted to copy and distribute verbatim or modified 
 copies of this license document, and changing it is allowed as long 
 as the name is changed. 

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION 

  0. You just DO WHAT THE FUCK YOU WANT TO.
```
