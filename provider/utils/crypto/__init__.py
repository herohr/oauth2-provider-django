import base64
import hmac

"""
Example:
    client_id = 1
    user_id = 1
    app_id = 1
    secret_key = "SECRET"
    
    token = HmacCrypto.generate_token_b64(client_id, user_id, app_id, secret_key)
    print(token)
    print(HmacCrypto.check_token(token, secret_key))
"""


class HmacCrypto:
    @staticmethod
    def hmac_md5(data, secret):
        """
        :param data: 数据 字符串
        :param secret: 秘钥 字符串
        :return: 二进制串
        """
        signature = hmac.new(secret.encode(), data.encode())
        return signature.digest()

    @staticmethod
    def hmac_md5_hex(data, secret):
        """
        :param data: 数据 字符串
        :param secret: 秘钥 字符串
        :return: 16进制字符串
        """
        signature = hmac.new(secret.encode(), data.encode())
        return signature.hexdigest()

    @staticmethod
    def get_prefix(client_id, app_id, user_id, _type="ACCESS-TOKEN"):
        return "{}:{}:{}:{}".format(client_id, app_id, user_id, _type)

    @staticmethod
    def generate_token_b64(client_id, user_id, app_id, secret_key, _type="ACCESS-TOKEN"):
        """
        :param client_id:
        :param app_id:
        :param user_id:
        :param secret_key:
        :param _type:
        :return: 返回的是base64 urlsafe的字符串
        """
        prefix = HmacCrypto.get_prefix(client_id, app_id, user_id, _type)
        signature = HmacCrypto.hmac_md5_hex(prefix, secret_key)
        token = "{}:{}".format(prefix, signature)
        return base64.urlsafe_b64encode(token.encode()).decode()

    @staticmethod
    def check_token(token, secret_key):
        token = base64.b64decode(token.encode()).decode()
        token = token.split(":")

        prefix = ":".join(token[:-1])
        signature = token[-1]

        hashed = HmacCrypto.hmac_md5_hex(prefix, secret_key)
        if hashed == signature:
            return True
        return False