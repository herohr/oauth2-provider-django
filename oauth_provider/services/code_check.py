from oauth_provider.services.auth_code_center import CodeCenter, Code
# from oauth_provider.models

def code_check(code, client_id):
    center = CodeCenter()
    if center.check(client_id, code):
        return True
    return False

