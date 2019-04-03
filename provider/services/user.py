from provider.models import User


def check_user_pw(username, password):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist as e:
        return False

    if user.password == password:
        return True
