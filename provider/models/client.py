from django.db.models import *
from provider.models import AllowedApp


class Client(Model):
    client_id = AutoField(primary_key=True)
    app = ForeignKey(AllowedApp, on_delete=CASCADE)
