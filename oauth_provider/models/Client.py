from django.db.models import *
from oauth_provider.models.AllowedApp import AllowedAPP


class Client(Model):
    client_id = CharField(max_length=256, primary_key=True)
    app = ForeignKey("oauth_provider.AllowedApp", on_delete=CASCADE)