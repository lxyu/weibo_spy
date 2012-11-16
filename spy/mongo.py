# -*- coding: utf-8 -*-

import pymongo

from settings import (
    MONGO_HOST,
    MONGO_PORT,
    MONGO_DB,
)

connection = pymongo.Connection(MONGO_HOST, MONGO_PORT)
db = getattr(connection, MONGO_DB)
