#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
from warnings import filterwarnings


class Orm(object):
    """Class for simple imitation ORM"""
    # Define error message
    error_message = "An error occurred with database"

    def __init__(self, *credentials):
        # Open connection
        self.connection = MySQLdb.connect(*credentials)
        self.cursor = self.connection.cursor()

    def _execute_query(self, query, message='Success'):
        if query:
            try:
                self.cursor.execute(query)
                self.connection.commit()
                print message
            except:
                self.connection.rollback()
                print self.error_message

    def create(self, table, columns):
        """
        Table create method.
        It takes two str attributes: first name of table,
        second should be columns with the data_types parameters
        example:
        instant.create('table_name', 'col_1 varchar(80), col_2 int')
        """
        # define query strings
        _query = "CREATE TABLE %s\
                  (ID int NOT NULL AUTO_INCREMENT, %s, PRIMARY KEY (ID))"\
                  % (table, columns)
        _drop_query = "DROP TABLE IF EXISTS %s" % table
        message = "Table `%s` was successfully created" % table

        filterwarnings('ignore', category = MySQLdb.Warning)

        # delete table if exists
        self.cursor.execute(_drop_query)

        # implement query
        self._execute_query(_query, message)

    def insert(self, table, values, columns=''):
        """
        Insert entries method
        example of calling:
        instant.insert('table_name', ('value1', 2), 'Col_1, Col_2')
        """
        # define query strings
        _query = "INSERT INTO %s (%s) VALUES %s" % (table, columns, values)
        message = "Data was successfully inserted into `%s`" % table

        # implement query
        self._execute_query(_query, message)

    def update(self, table, values, condition):
        """
        Update method
        example of calling:
        instant.update('table_name', 'Col_n = "some"', 'id=1')
        """
        # define query strings
        _query = "UPDATE %s SET %s WHERE %s" % (table, values, condition)
        message = "Table `%s` was successfully updated" % table

        # implement query
        self._execute_query(_query, message)

    def read(self, table, columns, condition=''):
        """
        Method to select data from a database.
        example of calling:
        instant.read('table_name', 'col_1, col_n', 'col_n>2')
        third argument(condition) isn't necessary
        """
        # define query strings
        error_empty = "Unable to fecth data."

        if condition:
            _query = "SELECT %s FROM %s WHERE %s" % (columns, table, condition)
        else:
            _query = "SELECT %s FROM %s" % (columns, table)

        self.cursor.execute(_query)

        results = self.cursor.fetchall()

        if results != ():
            for result in results:
                print result
        else:
            print error_empty

    def close(self):
        self.connection.close()


if __name__ == "__main__":
    e = Orm('localhost', 'testuser', 'q1234567890', 'test_db')
    #e.create('new_table', 'Title varchar(12), NextCol int')
    e.insert('new_table', ('newnew22', 112), 'Title, NextCol')
    #e.update('new_table', 'NextCol = 32', 'id=1')
    e.read('new_table', 'Title, NextCol', 'id>0')
    #e.close()
