Weibo Spy
=========

An demo weibo user timeline crawler and monitor build on top of `weibo <http://lxyu.github.com/weibo/>`_.

Can either be used to crawl all user infos or as a background daemon to monitor user changes in realtime.

Features
--------

1. Crawl all user infos, including statuses timeline, comments, user profile based on uid.
2. Smart detect new statuses/comments and user profile changes, and avoid duplicate requests.
3. Record a changelog on user profile about what changed and when.
4. Use mongodb as backend for easy data query and retrival.


Usage
-----

1. Copy `settings.py.sample` to `settings.py`.
2. Edit `settings.py` settings. Refer to `weibo <http://lxyu.github.com/weibo/>`_ for more info.
3. The 3 scripts inside `examples/` will work now, get your hand on it and try.


Disclaimer
----------

This project is just a demo mainly for personal use.
