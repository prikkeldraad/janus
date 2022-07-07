from peewee import *

versions_db = SqliteDatabase('versions.db')

class Person(Model):
    software_name = CharField()
    release_name = CharField()
    version = CharField()
    major = CharField()
    minor = CharField()
    patch = CharField()

    class Meta:
        database = versions_db