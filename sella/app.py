#!/usr/bin/env python
#-*- coding: utf-8 -*-
from importd import d

d(
    DEBUG=True,
    INSTALLED_APPS=(
        # external library
        'django_nose',

        # django rest framework
        'rest_framework',
        'rest_framework.authtoken',

        'sella',
        'demo',
        'api',
    ),
    # django-jinja
    DEFAULT_JINJA2_TEMPLATE_EXTENSION='.jinja2',
    TEMPLATE_LOADERS=(
        # django-jinja
        'django_jinja.loaders.AppLoader',
        'django_jinja.loaders.FileSystemLoader',
        # django
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ),
    # django-nose
    TEST_RUNNER='django_nose.NoseTestSuiteRunner',

    mounts={"demo": "/demo/", 'rest_framework': '/api/'}
)

if __name__ == "__main__":
    d.main()
