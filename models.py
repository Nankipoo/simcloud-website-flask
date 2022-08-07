

import datetime

from lib.google.cloud import ndb

import os
import sys
import io
import csv


class User(ndb.Model):
    email_address = ndb.StringProperty()
    cell_number = ndb.StringProperty()
    password = ndb.StringProperty()
    @property
    def is_authenticated(self):
        """
        Needed by Flask-login
        :return:
        """
        return True

    def is_active(self):
        """
        Needed by Flask-login
        :return:
        """
        return True

    def is_anonymous(self):
        """
        Needed by Flask-login
        :return:
        """
        return False

    def get_id(self):
        """
        Needed by Flask-login
        :return:
        """
        return str(self.key.id()).encode()
##def list_books():
    ##with client.context():
     ##   books = Book.query()
     ##   for book in books:
        ##    print(book.to_dict())