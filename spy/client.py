#!/usr/bin/env python

"""
The weibo client was activated directly by token info.
"""

import weibo

from settings import (
    WEIBO_API_KEY,
    WEIBO_API_SECRET,
    WEIBO_REDIRECT_URI,
    WEIBO_ACCESS_TOKEN,
    WEIBO_EXPIRES_AT,
)

c = weibo.Client(
    WEIBO_API_KEY, WEIBO_API_SECRET, WEIBO_REDIRECT_URI,
    access_token=WEIBO_ACCESS_TOKEN, expires_at=WEIBO_EXPIRES_AT)


def get_statuses(uid, page):
    res = c.get('statuses/user_timeline',
                uid=uid,
                page=page,
                count=100)
    return res['statuses']


def get_comments(status_id):
    res = c.get('comments/show', id=status_id, count=100)
    return res['comments']
