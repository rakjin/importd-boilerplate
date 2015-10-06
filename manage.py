#!/usr/bin/env python
# -*- coding: utf-8 -*-
from importd import d


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
            'APP_DIRS': True,
        },
    ],
    # django-nose
    TEST_RUNNER='django_nose.NoseTestSuiteRunner',
)

if __name__ == '__main__':
    d.main()
