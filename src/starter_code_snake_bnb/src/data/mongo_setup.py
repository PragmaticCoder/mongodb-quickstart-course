import os

import mongoengine

alias_core = 'core'
db_name = 'snake_bnb'


def global_init():
    data = dict(
        username=os.environ.get('MONGODB_USERNAME', 'root'),
        password=os.environ.get('MONGODB_PASSWORD', ''),

        host=os.environ.get('MONGODB_HOST', 'localhost'),
        port=os.environ.get('MONGODB_PORT', 27017),
    )
    mongoengine.register_connection(alias=alias_core, name=db_name, **data)
