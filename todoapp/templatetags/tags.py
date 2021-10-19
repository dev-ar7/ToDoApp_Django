# Only For To Look Forms Better And Cool
from django import template

register = template.Library()


@register.filter(name='add_css')
def add_css(field, css):
    # Removes All The Values Of Arg From The Given String
    return field.as_widget(attrs={'class': css})
