#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The spy function is smart enough to avoid duplicate requests,
if you only watch one user, 60 wait time is far more than enough.
Tune wait time higher if you need to watch more.
"""

import sys
sys.path.append("..")

import logging
import time

import spy


UID = 1282440983
WAIT = 60


def main():
    while True:
        spy.track_user(UID)
        time.sleep(WAIT)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
