from django.test import TestCase
from oauth_provider.services.app_auth import app_register
from oauth_provider.models.AllowedApp import AllowedClient


class ServiceTest(TestCase):
    def a_test(self):
        a = app_register.register_client("NAME", "SEC", 'READ')
        c1 = AllowedClient.objects.get(client_name="NAME")
        print(c1)