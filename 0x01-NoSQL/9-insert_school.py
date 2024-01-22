#!/usr/bin/env python3
""" Python Module """


def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document in a collection based on kwargs """

    insert = mongo_collection.insert_one(kwargs)
    return insert.inserted_id
