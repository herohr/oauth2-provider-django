from django.db.models import *


class AllowedAPP(Model):
    READ = "R"
    WRITE = "W"
    READWRITE = "RW"

    app_id = AutoField(primary_key=True)
    app_secret = CharField(max_length=256)

    app_name = CharField(max_length=32)
    access = TextField(choices=((READ, "read"), (WRITE, 'write'), (READWRITE, "read and write")))

    def __str__(self):
        return "ID:{}, Name:{}".format(self.app_id, self.app_name)
