from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField


class Subscriber(models.Model):
    first_name = models.CharField(_('first name'), max_length=25)
    last_name = models.CharField(_('last name'), max_length=25)
    email = models.EmailField(_('email'), unique=True)
    language = models.CharField(_('language'), max_length=2)
    country = CountryField(_('country'))
    subscribed = models.BooleanField(_('subscribed'), default=True)
    uploaded = models.BooleanField(_('uploaded'), default=False)
    created = models.DateTimeField(_('created'), auto_now_add=True)

    class Meta:
        ordering = ('-created', )
        verbose_name = _('subscriber')
        verbose_name_plural = _('subscribers')

    def __str__(self):
        return '{} {} <{}>'.format(self.first_name, self.last_name, self.email)
