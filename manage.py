#!/usr/bin/env python
# -*- coding: utf-8 -*-
from importd import d


d(
    DEBUG=True,
    INSTALLED_APPS=[
        'django.contrib.auth',
    ],
)

if __name__ == '__main__':
    d.main()
