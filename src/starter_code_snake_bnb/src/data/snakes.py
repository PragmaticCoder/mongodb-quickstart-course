import datetime

import mongoengine


class Snake(mongoengine.Document):
    name = mongoengine.StringField(required=True)
    species = mongoengine.StringField(required=True)

    length = mongoengine.FloatField(required=True, min_value=0.00)
    is_venomous = mongoengine.BooleanField(required=True)
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)

    meta_data = {
        'db_alias': 'core',
        'collection': 'snake',
    }
