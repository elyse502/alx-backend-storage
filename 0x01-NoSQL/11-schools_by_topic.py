#!/usr/bin/env python3
""" Python Module """


def schools_by_topic(mongo_collection, topic):
    """ Returns the list of school with a specific topic """
    return [x for x in mongo_collection.find({"topics": topic})]
