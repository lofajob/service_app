#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint

from pymongo import MongoClient


class MongoOrm(object):
    """#"""

    def __init__(self, host='localhost', port=27017, database='test_database'):
        self.host = host
        self.port = port
        self.database = database

    def _get_uri(self):
        uri = "mongodb://%s:%s/" % (self.host, self.port)
        return uri

    def connect_to_db(self):
        """
        Method makes a connection with MongoClient
        and returns a database
        """
        client = MongoClient(self._get_uri())
        db = client[self.database]
        return db

    def switch_collection(self, collection):
        """
        ###
        """
        self.coll = self.connect_to_db()[collection]

    def select_all(self):
        """
        This method selects all entries
        and shows all fields of it's
        """
        return pprint(list(self.coll.find()))

    def select(self, **kwargs):
        """
        ###
        """
        return list(self.coll.find(kwargs))

    def select_all_and_format(self):
        """
        This method selects all entries
        and returns all fields except '_id'
        """
        json = []
        for doc in self.coll.find():
            del(doc['_id'])
            json.append(doc)
        return pprint(json)

    def insert(self, **kwargs):
        """
        ###
        """
        dictionary = dict(**kwargs)
        self.coll.insert(dictionary)

    def del_(self, **kwargs):
        """
        ###
        """
        query = dict(**kwargs)
        self.coll.remove(query)

    def update(self, find={}, set=dict()):
        self.coll.update(find,set)

if __name__ == "__main__":
    s = MongoOrm(database='unicorns')
    s.connect_to_db()
    s.switch_collection('unicorns')
