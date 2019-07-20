import django.conf
from django.utils.translation import gettext_lazy as _


class AppSettings(object):
    """
    A holder for app-specific default settings that allows overriding via
    the project's settings.
    """

    def __getattribute__(self, attr):
        if attr == attr.upper():
            try:
                return getattr(django.conf.settings, attr)
            except AttributeError:
                pass
        return super(AppSettings, self).__getattribute__(attr)


class Settings(AppSettings):
    EASY_SUBSCRIPTION_VALIDATE_EMAIL = False
    """
    Whether to validate the email address with the MX server.
    """

    EASY_SUBSCRIPTION_UPLOAD_SUBSCRIBERS = False
    """
    Whether to upload subscribers data.
    """

    EASY_SUBSCRIPTION_INTEGRATION = None
    """
    The integration to use to upload subscribers.
    """

    EASY_SUBSCRIPTION_INTEGRATION_CREDENTIALS = {}
    """
    A dictionary of the credentials to use with the selected integration.
    """

    EASY_SUBSCRIPTION_FORM_THANK_YOU_MESSAGE = _('Thank you for subscribing!')
    """
    Thank you message after user subscribed
    """


settings = Settings()
