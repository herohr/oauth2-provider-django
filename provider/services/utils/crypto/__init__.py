import hmac


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
        :return: 二进制串
        """
        signature = hmac.new(secret.encode(), data.encode())
        return signature.hexdigest()


print(HmacCrypto.hmac_md5_hex("FUCKER", "SHITER"))
