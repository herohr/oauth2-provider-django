from django.db.models import *


class User(Model):
    user_id = AutoField(primary_key=True)

    username = CharField(max_length=32)
    password = CharField(max_length=32)

