from provider.models import AllowedApp


def register_client(app_name, app_secret, access):
    client = AllowedApp(client_name=app_name, client_secret=app_secret, access=access)
    client.save()


def get_client(app_name, app_secret):
    try:
        client = AllowedApp.objects.get(client_name=app_name, client_secret=app_secret)
        return client
    except AllowedApp.DoesNotExist:
        return None
