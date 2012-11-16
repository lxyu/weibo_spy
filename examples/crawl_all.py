#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Due to the stupid 150 user-requests per hour limit, crawl all may take
very long time.
Blame sina for this.
"""

import sys
sys.path.append("..")

import logging
import time

import spy


UID = 1282440983
MAX_PAGE = 500


def main():
    for i in range(0, 500):
        logging.debug('working...')
        try:
            spy.track_user(UID, i)
        except:
            logging.debug('sleeping...')
            time.sleep(60 * 10)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
