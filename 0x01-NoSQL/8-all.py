#!/usr/bin/env python3
""" Python Module """
import pymongo


def list_all(mongo_collection):
    """ Lists all documents in a collection """
    cursor = mongo_collection.find({})
    return cursor
