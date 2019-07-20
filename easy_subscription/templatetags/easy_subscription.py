from django import template
from ..forms import SubscriberForm

register = template.Library()


@register.inclusion_tag('easy_subscription/subscription_form.html')
def subscription_form():
    return {
        'form': SubscriberForm()
    }
