#!/usr/bin/env python
# -*- coding: utf-8 -*-
from importd import d
from jinja2 import Environment
from django.core.urlresolvers import reverse

from sella import filters


d(
    DEBUG=True,
    INSTALLED_APPS=[
        'django.contrib.auth',
        'django.contrib.staticfiles',

        # external library
        'django_nose',
        'debug_toolbar',

        'sella',
        'demo',
    ],
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
        {
            'BACKEND': 'django.template.backends.jinja2.Jinja2',
            'DIRS': ['jinja2'],
            'APP_DIRS': True,
            'OPTIONS': {
                'environment': 'manage.jinja2_environment',
            },
        },
    ],
    # django-nose
    TEST_RUNNER='django_nose.NoseTestSuiteRunner',

    mounts={'demo': '/demo/'},
)

from django.contrib.staticfiles.storage import staticfiles_storage


def jinja2_environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    env.filters.update({
        'tojson': filters.tojson,
    })
    return env

if __name__ == '__main__':
    d.main()
