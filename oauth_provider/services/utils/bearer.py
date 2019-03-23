import hmac
import base64


# 以:分割， 将客户端ID，APPID，用户ID，访问权限作为需要签名的字符串，并使用秘钥加密，将结果b64加密作为token

def get_prefix(client_id, app_id, user_id, _type="ACCESS-TOKEN"):
    return "{}:{}:{}:{}".format(client_id, app_id, user_id, _type)


def hmac_md5(prefix, secret_key):
    signature = hmac.new(secret_key.encode(), prefix.encode()).hexdigest()
    return signature


def generate_token_b64(client_id, app_id, user_id, secret_key, _type="ACCESS-TOKEN"):
    prefix = get_prefix(client_id, app_id, user_id, _type)
    signature = hmac_md5(prefix, secret_key)
    token = "{}:{}".format(prefix, signature)
    return base64.b64encode(token.encode()).decode()


def check_token(token, secret_key):
    token = base64.b64decode(token.encode()).decode()
    token = token.split(":")

    prefix = ":".join(token[:-1])
    signature = token[-1]

    hashed = hmac_md5(prefix, secret_key)
    if hashed == signature:
        return True
    return False


def test():
    client_id = 1
    app_id = 113123
    user_id = 1
    secret_key = "WTF"
    k = generate_token_b64(client_id, app_id, user_id, secret_key)
    print(k)
    print(check_token(k, secret_key))


if __name__ == "__main__":
    test()
