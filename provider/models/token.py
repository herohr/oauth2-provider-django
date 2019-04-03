from django.db.models import *
from . import AllowedApp, Client


class Token(Model):
    client = ForeignKey(Client, on_delete=CASCADE)
    app = ForeignKey(AllowedApp, on_delete=CASCADE)

    access_token = CharField(max_length=256)
    refresh_token = CharField(max_length=256, null=True)

    access_token_expiration = BigIntegerField()
    refresh_token_expiration = BigIntegerField()

    scope = CharField(max_length=32, verbose_name="Access range")
