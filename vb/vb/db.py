from peewee import *

versions_db = SqliteDatabase('versions.db')


class Software(Model):
    vendor = CharField()
    name = CharField()
    class Meta:
        database = versions_db


class Version(Model):
    ForeignKeyField(Software, backref='versions')
    release_name = CharField(null=True)
    version = CharField()
    major = CharField(null=True)
    minor = CharField(null=True)
    patch = CharField(null=True)

    class Meta:
        database = versions_db


versions_db.create_tables([Software, Version])

# version = Version.create(software_name="aaaaA",release_name="woooo", version="aaaa", major="gggg", minor="qqqq",patch="aaaA")
# version.save()
#list(version.select())[0].__dict__
#{'__data__': {'id': 1, 'software_name': 'aaaaA', 'release_name': 'woooo', 'version': 'aaaa', 'major': 'gggg', 'minor': 'qqqq', 'patch': 'aaaA'}, '_dirty': set(), '__rel__': {}}
