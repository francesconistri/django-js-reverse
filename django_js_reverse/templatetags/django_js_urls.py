from django.template import Library

from django_js_urls.views import get_template_context

register = Library()


@register.inclusion_tag("django_js_reverse/urls_js.tpl", takes_context=True)
def virtual_coins_widget(context):
    return get_template_context()
