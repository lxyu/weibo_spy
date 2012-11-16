# -*- coding: utf-8 -*-

"""
Only one public api here: track_user. Check examples for how to use.

Can either be used to crawl all user infos or as a background daemon to monitor
user changes in realtime.
"""

import logging
import datetime
import hashlib

from dateutil.parser import parse

from client import (
    get_statuses,
    get_comments,
)

from .mongo import db


def track_user(uid, page=1):
    statuses = get_statuses(uid, page)

    profile = statuses[0]['user']
    _track_profile(profile)

    for status in statuses:
        _track_status(status)


def _track_status(status):
    pstatus = db.status.find_one({'id': status['id']})

    if pstatus and pstatus['comments_count'] == status['comments_count']:
        return

    logging.debug("tracking status: %s" % status['id'])

    comments = get_comments(status['id'])
    for comment in comments:
        if db.comment.find({'id': comment['id']}).count():
            continue

        logging.debug("tracking comment: %s" % comment['id'])

        comment['status_id'] = status['id']
        comment.pop('idstr')
        comment.pop('status')
        if 'reply_comment' in comment:
            comment.pop('reply_comment')
        comment['created_at'] = parse(comment['created_at'])
        comment['updated_at'] = datetime.datetime.now()
        db.comment.insert(comment)

    status.pop('user')
    status.pop('idstr')
    status['created_at'] = parse(status['created_at'])
    if 'original_pic' in status:
        status['original_pic'] = _process_image(status['original_pic'])
    status['updated_at'] = datetime.datetime.now()
    db.status.insert(status)


def _track_profile(user):
    logging.debug("tracking user: %s" % user['id'])

    user['created_at'] = parse(user['created_at'])
    user['avatar_large'] = _process_image(user['avatar_large'])

    # if user exists, then track profile change.
    if db.user.find({'id': user['id']}).count():
        care_about = [
            'domain',
            'screen_name',
            'avatar_large',
            'description',
            'remark',
            'gender',
            'city',
            'province',
            'location',
            'follow_me',
            'lang',
            'weihao',
            'url',
            'profile_url',
        ]

        puser = db.user.find({'id': user['id']}).sort('updated_at')[0]
        updated = False
        for field in care_about:
            if user[field] != puser[field]:
                updated = True
                change = {
                    'field': field,
                    'from': puser[field],
                    'to': puser[field],
                    'created_at': datetime.datetime.now()
                }
                db.changelog.insert(change)

        if not updated:
            return

    user['updated_at'] = datetime.datetime.now()
    db.user.insert(user)


def _process_image(url):
    img_hash = hashlib.md5(url).hexdigest()
    if db.image.find({'hash': img_hash}).count() == 0:
        img = {
            'url': url,
            'hash': img_hash,
            'created_at': datetime.datetime.now(),
            'downloaded': False,
            'downloaded_at': None,
        }
        db.image.insert(img)
        logging.debug("processed image: %s => %s" % (img_hash, url))
    return img_hash
