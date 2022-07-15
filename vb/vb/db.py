from peewee import *

versions_db = SqliteDatabase('versions.db')

class Version(Model):
    software_name = CharField()
    release_name = CharField(NULL=True)
    version = CharField()
    major = CharField(NULL=True)
    minor = CharField(NULL=True)
    patch = CharField(NULL=True)

    class Meta:
        database = versions_db


versions_db.create_tables([Version])

# version = Version.create(software_name="aaaaA",release_name="woooo", version="aaaa", major="gggg", minor="qqqq",patch="aaaA")
# version.save()
#list(version.select())[0].__dict__
#{'__data__': {'id': 1, 'software_name': 'aaaaA', 'release_name': 'woooo', 'version': 'aaaa', 'major': 'gggg', 'minor': 'qqqq', 'patch': 'aaaA'}, '_dirty': set(), '__rel__': {}}
