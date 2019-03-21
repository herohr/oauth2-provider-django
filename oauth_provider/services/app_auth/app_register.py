from oauth_provider.models.AllowedApp import AllowedAPP


def register_client(app_name, app_secret, access):
    client = AllowedAPP(client_name=app_name, client_secret=app_secret, access=access)
    client.save()


def get_client(app_name, app_secret):
    try:
        client = AllowedAPP.objects.get(client_name=app_name, client_secret=app_secret)
        return client
    except AllowedAPP.DoesNotExist:
        return None
