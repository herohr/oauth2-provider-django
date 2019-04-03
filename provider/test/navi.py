from django.test import TestCase
from provider.services import code as code_service
from provider.models import AllowedApp, Client, User


class ServiceTest(TestCase):
    app = AllowedApp(app_secret="APP_SERCRET", app_name="TestName", access=AllowedApp.READWRITE)
    client = Client(app=app)
    user = User(username="TestUserName", password="Test")

    @staticmethod
    def get_code_by_user(app, client, user):
        # login ...

        code = code_service.add_code(client.client_id, user.user_id, app.app_id)
        result = code_service.code_check(code.code, client.client_id, user.user_id, app.app_id)
        assert result
        return code  # Code Object

    @staticmethod
    def get_authorization_by_app(app, client_id, user_id):
        


    @staticmethod
    def test():
        app = ServiceTest.app
        client = ServiceTest.client
        user = ServiceTest.user

        code = ServiceTest.get_code_by_user(app, client, user)
