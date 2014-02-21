from django.template import Library

from django_js_reverse.views import get_template_context

register = Library()


@register.inclusion_tag("django_js_reverse/urls_js.tpl")
def django_urls():
    return get_template_context()
