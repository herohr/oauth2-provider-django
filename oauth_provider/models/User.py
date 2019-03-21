from django.db.models import *


class User(Model):
    user_id = AutoField(primary_key=True)

    username = CharField(max_length=32, null=False)  # Keyword null default is false
    password = CharField(max_length=32)

