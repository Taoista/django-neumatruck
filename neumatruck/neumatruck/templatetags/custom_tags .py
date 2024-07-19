from django import template
from neumatruck.helpers import say_hello


register = template.Library()

@register.simple_tag
def hello_tag():
    return say_hello()