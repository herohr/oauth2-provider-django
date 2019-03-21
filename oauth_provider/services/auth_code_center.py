import time
import uuid
from threading import Lock


class CodeCenter:
    __instance__ = None

    def __new__(cls, *args, **kwargs):
        if CodeCenter.__instance__ is None:
            return super().__new__(*cls, **kwargs)
        else:
            return CodeCenter.__instance__

    def __init__(self):
        self.codes = {}
        self.lock = Lock()

    def add_code(self, client_id, expire=60):
        code = uuid.uuid4()

        with self.lock.acquire():
            self.codes[client_id] = Code(client_id, expire, code)

    def check(self, client_id, code):
        with self.lock.acquire():
            result = self.codes.get(client_id, None)
            if result is None:
                return False
            if result.code == code:
                if not result.is_expire():
                    return True
            return False


class Code:
    def __init__(self, client_id, expire, code):
        self.client_id = client_id
        self.expire = expire
        self.create_time = time.time()
        self.code = code

    def is_expire(self):
        now_time = time.time()
        if now_time - self.create_time < 0:
            return True
        else:
            return False
