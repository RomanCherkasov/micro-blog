from django import template

register = template.Library()

# this userfilter get access to edit css properties
@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})