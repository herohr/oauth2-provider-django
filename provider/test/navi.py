import json

from django.test import TestCase
from provider.services import code as code_service, authorization as authorization_service
from provider.models import AllowedApp, Client, User


class ServiceTest(TestCase):

    @staticmethod
    def get_code_by_user(app, client, user):
        # login ...

        code = code_service.add_code(client.client_id, user.user_id, app.app_id)
        result = code_service.code_check(code.code, client.client_id, user.user_id, app.app_id)
        assert result
        return code  # Code Object

    @staticmethod
    def get_authorization_by_app(app, client_id, user_id, secret_key):
        token = authorization_service.generate_token(client_id, user_id, app.app_id, "R", secret_key)
        return token

    def test_shit(self):
        app = AllowedApp(app_secret="APP_SERCRET", app_name="TestName", access=AllowedApp.READWRITE)
        app.save()
        client = Client(app_id=app.app_id)
        client.app_id = app.app_id
        user = User(username="TestUserName", password="Test")
        client.save()
        user.save()

        code = ServiceTest.get_code_by_user(app, client, user)
        result = code_service.code_check(code.code, client.client_id, user.user_id, app.app_id)
        assert result

        token = ServiceTest.get_authorization_by_app(app, client.client_id, user.user_id, "WTF")
        data_dict = {"fuck": "here", "Lamer": "fucker"}
        data = json.dumps(data_dict)
        from provider.utils.crypto import HmacCrypto
        signature = HmacCrypto.hmac_md5_hex(data, token.access_token)

        result = authorization_service.verify_data(token_id=token.token_id, data=data, signature=signature)
        assert result