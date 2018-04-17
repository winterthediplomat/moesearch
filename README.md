MoeSearch
=========

A Python library for [desuarchive.org](https://desuarchive.org/) and [RebeccaBlackTech](https://rbt.asia) REST API.  
Theoretically, it should work with every installation of FoolFuuka, but 4plebs apparently needs to be fixed to their updated definition of the FoolFuuka API before it will work.

Helpful binaries included.

Disclaimer
------

This codebase was fixed from the [moesearch](https://pypi.org/project/moesearch/) library, which became broken due to a hardcoded domain. We made the URL a function argument (so you can use it with rbt.asia, though not warosu, which is fuuka). We also plan to make this compatible with [the 4plebs definition of the FoolFuuka API.](https://4plebs.tech/foolfuuka/) Finally we have to fix the unit tests to work on whatever method we use to set `archiver_url`.

This software is experimental, use it at your own risk.

Quickstart
--------

(You can check the executables in /bin folder).
FoolFuuka docs are available [at foolz.us](https://web.archive.org/web/20140728111047/http://www.foolz.us/docs/foolfuuka/documentation.html).  
```py
>>> import moesearch
>>> print(moesearch.search(archiver_url="https://desuarchive.org", board="a", text="woxxy")[2].comment)
>>112732805
Fuck Woxxy.
>>> print(archiver_url="https://desuarchive.org", moesearch.index("a", 1)["112834776"].op.media.media_link)
http://cdn2.desu-usergeneratedcontent.xyz/a/image/1366/74/1366741186747.jpg
>>> print(archiver_url="https://desuarchive.org", moesearch.post("a", 112766871).board.short_name)
a
>>> print(moesearch.thread(archiver_url="https://desuarchive.org", "a", 112800651).posts[0].comment)
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
