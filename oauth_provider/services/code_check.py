from oauth_provider.services.auth_code_center import CodeCenter, Code

def code_check(code, client_id):
    center = CodeCenter()
    if center.check(client_id, code)
        authorize_product
