from flask_login import UserMixin

import datetime

from datastore_entity import DatastoreEntity, EntityValue

class User(DatastoreEntity):

    # specify a default value of 'None'
    email = EntityValue(None)
    # or provide no argument to imply 'None'
    password = EntityValue()
    cell_no = EntityValue(None)
    # default value of 1
    active = EntityValue(1)
    date_created = EntityValue(datetime.datetime.utcnow())

    # specify the name of the entity kind.
    # This is REQUIRED. Raises ValueError otherwise
    __kind__ = "User"

    # optionally add properties to exclude from datastore indexes
    __exclude_from_index__ = ['password']

    def get(self, value):
        return self.get_obj('username', value)
    # call the super class here
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)