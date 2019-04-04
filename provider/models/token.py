import uuid

from django.db.models import *
from provider.models.user import User
from provider.models.allowedApp import AllowedApp
from provider.models.client import Client


class Token(Model):
    token_id = UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True)

    client = ForeignKey(Client, on_delete=CASCADE)
    app = ForeignKey(AllowedApp, on_delete=CASCADE)
    user = ForeignKey(User, on_delete=CASCADE)

    access_token = CharField(max_length=256)
    refresh_token = CharField(max_length=256, null=True)

    access_token_expiration = BigIntegerField()
    refresh_token_expiration = BigIntegerField()

    scope = CharField(max_length=32, verbose_name="Access range")
