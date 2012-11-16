#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Images were saved to mongo as md5(url) hash.
This script will download all images to local.
"""

import sys
sys.path.append("..")

import datetime
import os
import logging
import urllib

from spy.mongo import db


IMAGE_DIR = '../images'


def main():
    images = db.image.find({"downloaded": False})

    for image in images:
        logging.debug('downloading image: %s' % image['hash'])
        image_path = os.path.join(IMAGE_DIR, image['hash'] + '.jpg')
        urllib.urlretrieve(image['url'], image_path)

        image['downloaded'] = True
        image['downloaded_at'] = datetime.datetime.now()
        db.image.save(image)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
