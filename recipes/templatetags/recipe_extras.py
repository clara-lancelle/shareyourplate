from django import template

register = template.Library()
 
@register.filter
def bg_color(value):
    color = ''
    if value == 'Facile' or value == 'Faible':
        color = 'green'
    elif value == 'Moyen':
        color = 'yellow'
    else:
        color = 'pink'

    display = '<span class="recipe__badge bg-{color}-100 text-{color}-800">{value}</span>'.format(color=color, value=value)
    return display

@register.simple_tag(takes_context=True)
def display_author(context, user):
    if user == context['user']:
        return 'Vous'
    return user.username    
