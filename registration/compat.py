from django.conf import settings


__all__ = ['get_user_model', 'AUTH_USER_MODEL']


def get_user_model():
    """ Returns the appropriate User model class. As of Django 1.5, the use
    of custom user models was allowed by changing a setting. This method
    will no longer be required when Django 1.4 support is dropped.
    """
    try:
        # Django 1.5+
        from django.contrib.auth import get_user_model
        model = get_user_model()
    except IOError:
        # Django <= 1.4
        from django.contrib.auth.models import User
        model = User
    return model

# The Django docs recommend referencing all user FK's by string
# to avoid the issues caused by having initialization logic that
# depends on the pluggable user model (which may not have been read
# yet. This allows us to do so while keeping the extra code out of the way.
AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')
