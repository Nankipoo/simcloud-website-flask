

import datetime

from lib.google.cloud import ndb

import os
import sys
import io
import csv


class User(ndb.Model):
    name = ndb.StringProperty()
    surname = ndb.StringProperty()
    cell_number = ndb.StringProperty()
    id_number = ndb.StringProperty()
    email_address = ndb.StringProperty()
    business_address = ndb.StringProperty()
    business_registration_number = ndb.StringProperty()
    vat_number = ndb.StringProperty()
    address = ndb.StringProperty()
    password = ndb.StringProperty()
    confirm_password = ndb.StringProperty()

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