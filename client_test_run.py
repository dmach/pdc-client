#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Red Hat
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#
import argparse
import sys
import platform

if platform.python_version() < '2.7':
    unittest = __import__('unittest2')
else:
    import unittest

"""
Use this script either without arguments to run all tests:
    python client_test_run.py
or with specific module/test to run only part of the test suite:
    python client_test_run.py pdc_client.tests.release.tests.ReleaseTestCase.test_list_all
"""

if __name__ == '__main__':
    parser = argparse.ArgumentParser('client_test_run.py')
    parser.add_argument('tests', metavar='TEST', nargs='*')
    options = parser.parse_args()
    loader = unittest.TestLoader()
    if options.tests:
        suite = loader.loadTestsFromNames(options.tests)
    else:
        suite = loader.discover('tests', top_level_dir='.')
    result = unittest.TextTestRunner().run(suite)
    if not result.wasSuccessful():
        sys.exit(1)
