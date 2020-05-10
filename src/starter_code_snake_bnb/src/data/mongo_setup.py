import os
import ssl

import mongoengine

alias_core = 'core'
db_name = 'snake_bnb'


def global_init():
    data = dict(
        username=os.environ.get('MONGODB_USERNAME', 'root'),
        password=os.environ.get('MONGODB_PASSWORD', ''),
        host=os.environ.get('MONGODB_HOST', '127.0.0.1'),
        port=os.environ.get('MONGODB_PORT', 27017),
        authentication_source='admin',
        authentication_mechanism='SCRAM-SHA-1',
        ssl=True,
        ssl_cert_reqs=ssl.CERT_NONE
    )
    mongoengine.register_connection(alias=alias_core, name=db_name, **data)
