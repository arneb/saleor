from django import template

register = template.Library()


@register.inclusion_tag('product/_price_range.html')
def price_range(price_range):
    return {'price_range': price_range, 'method': 'gross'}


@register.inclusion_tag('product/_price_range.html')
def price_range_tax(price_range):
    return {'price_range': price_range, 'method': 'tax'}