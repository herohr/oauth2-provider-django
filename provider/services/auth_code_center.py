import time
import uuid
from threading import Lock


class CodeCenter:
    __instance__ = None
    __inited__ = False

    def __new__(cls, *args, **kwargs):
        if CodeCenter.__instance__ is None:
            instance = super().__new__(cls, *args, **kwargs)
            CodeCenter.__instance__ = instance
            return instance
        else:
            return CodeCenter.__instance__

    def __init__(self):
        if not CodeCenter.__inited__:
            self.codes = {}  # {"code" : Code}
            self.lock = Lock()
            CodeCenter.__inited__ = True

    def add_code(self, client_id, user_id, app_id, expire=60):
        code = uuid.uuid4()
        with self.lock:
            self.codes[code] = Code(client_id, user_id, app_id, code, expire)
        return self.codes[code]

    def check(self, client_id, user_id, app_id, code):
        with self.lock:
            signature = Code.generate_code_signature(client_id, user_id, app_id)
            result = self.codes.get(code, None)
            if result is None:
                return False
            if result.code_signature == signature:
                if not result.is_expire():  # 失效
                    return True
            return False


class Code:
    def __init__(self, client_id, user_id, app_id, code, expire=600, ):
        self.client_id = client_id
        self.user_id = user_id
        self.app_id = app_id

        self.expire = expire
        self.create_time = time.time()
        self.code = code

    def is_expire(self):
        now_time = time.time()
        if now_time - self.create_time < 0:
            return True
        else:
            return False

    @property
    def code_signature(self):
        return Code.generate_code_signature(self.client_id, self.user_id, self.app_id)

    @staticmethod
    def generate_code_signature(client_id, user_id, app_id):
        return "{}:{}:{}".format(client_id, user_id, app_id)
