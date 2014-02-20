#-*- coding: utf-8 -*-
import re

from django.core import urlresolvers
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render

from django_js_reverse.conf import JS_VAR_NAME


def get_template_context():
    if not re.match(r'^[$A-Z_][\dA-Z_$]*$', JS_VAR_NAME.upper()):
        raise ImproperlyConfigured(
            'JS_REVERSE_JS_VAR_NAME setting "%s" is not a valid javascript identifier.' % (JS_VAR_NAME))

    url_patterns = list(urlresolvers.get_resolver(None).reverse_dict.items())
    url_list = [(url_name, url_pattern[0][0]) for url_name, url_pattern in url_patterns if
                (isinstance(url_name, str) or isinstance(url_name, unicode))]
    ctx = {
        'urls': url_list,
        'url_prefix': urlresolvers.get_script_prefix(),
        'js_var_name': JS_VAR_NAME
    }
    return ctx


def urls_js(request):
    template = 'django_js_reverse/urls_js.tpl'
    ctx = get_template_context()
    return render(request, template, ctx, mimetype='application/javascript')
