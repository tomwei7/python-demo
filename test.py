#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

import unittest

from app import app


class TimeTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_time(self):
        rv = self.app.get('/api/datetime')
        assert rv.status_code == 200


if __name__ == '__main__':
    unittest.main()
