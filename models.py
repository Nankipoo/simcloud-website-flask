

import datetime

from lib.google.cloud import ndb




class User(ndb.Model):
    email_address = ndb.StringProperty()
    cell_number = ndb.StringProperty()
    password = ndb.StringProperty()

##def list_books():
    ##with client.context():
     ##   books = Book.query()
     ##   for book in books:
        ##    print(book.to_dict())