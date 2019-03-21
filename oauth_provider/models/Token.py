from django.db.models import *


class Token(Model):
    access_token = CharField(max_length=256, primary_key=True)
    refresh_token = CharField(max_length=256, null=True, unique=True)
    expires_in = IntegerField()
    scope = CharField(max_length=32, verbose_name="Access range")

    client = ForeignKey("oauth_provider.AllowedApp", on_delete=CASCADE)