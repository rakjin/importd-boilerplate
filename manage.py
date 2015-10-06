#!/usr/bin/env python
# -*- coding: utf-8 -*-
from importd import d
from jinja2 import Environment


d(
    DEBUG=True,
    INSTALLED_APPS=[
        'django.contrib.auth',

        # external library
        'django_nose',

        'sella',
    ],
    TEMPLATES=[
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
)

from django.contrib.staticfiles.storage import staticfiles_storage


def jinja2_environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
    })
    return env

if __name__ == '__main__':
    d.main()
