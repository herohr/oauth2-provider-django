from provider.services.auth_code_center import CodeCenter


# from oauth_provider.models

def code_check(code, client_id, user_id, app_id):
    center = CodeCenter()
    if center.check(client_id, user_id, app_id, code):
        return True
    return False


def add_code(client_id, user_id, app_id):
    """
    :param client_id:
    :param user_id:
    :param app_id:
    :return: Code对象
    """
    center = CodeCenter()
    code = center.add_code(client_id, user_id, app_id)
    return code
