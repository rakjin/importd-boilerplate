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
    # django-nose
    TEST_RUNNER='django_nose.NoseTestSuiteRunner',
)

if __name__ == '__main__':
    d.main()
