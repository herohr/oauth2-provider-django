import time

from provider.models import Token, Client, User, AllowedApp
from provider.utils.crypto import HmacCrypto


def generate_token(client_id, user_id, app_id, scope, secret_key, access_expire=600, refresh_expire=6000):
    try:
        client = Client.objects.get(client_id=client_id)
        user = User.objects.get(user_id=user_id)
        app = AllowedApp.objects.get(app_id=app_id)
    except User.DoesNotExist or Client.DoesNotExist or AllowedApp.DoesNotExist:
        raise Exception("WTF APP")

    access_token_signature = HmacCrypto.generate_token_b64(client_id, user_id, app_id, secret_key)
    refresh_token_signature = HmacCrypto.generate_token_b64(client_id, user_id, app_id, secret_key,
                                                            _type="REFRESH-TOKEN")

    now_time = int(time.time())
    access_token = Token(client=client, user=user, app=app,
                         access_token=access_token_signature,
                         refresh_token=refresh_token_signature,
                         access_token_expiration=now_time + access_expire,
                         refresh_token_expiration=now_time + refresh_expire,
                         scope=scope
                         )
    access_token.save()
    return access_token


def verify_data(token_id, data, signature):
    try:
        token = Token.objects.get(token_id=token_id)
    except Token.DoesNotExist as e:
        raise e

    access_token = token.access_token
    verified_signature = HmacCrypto.hmac_md5_hex(data, access_token)
    return signature == verified_signature