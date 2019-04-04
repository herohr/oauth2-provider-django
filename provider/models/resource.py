from django.db.models import *
from provider.models import User


class Resource(Model):
    resource_id = AutoField(primary_key=True)
    context = TextField("Jesus of Context")

    user_id = ForeignKey(User, on_delete=CASCADE)