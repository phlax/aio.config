import os
import unittest

from aio.testing import aiotest
from aio.config import parse_config, find_config

TEST_DIR = os.path.dirname(__file__)


class AioConfigTestCase(unittest.TestCase):

    @aiotest
    def test_parse_config(self):
        app_dir = os.path.join(
            TEST_DIR, "resources")
        config = yield from parse_config(app_dir=app_dir)
        self.assertEquals(config.sections(), ["section1"])        
        self.assertEquals(config["section1"]["result"], "1")    

    @aiotest
    def test_parse_custom_config(self):
        configfile = os.path.join(
            TEST_DIR, "resources", "test-1.conf")
        config = yield from parse_config(configfile)
        self.assertEquals(config.sections(), ["foo", "bar"])
        self.assertEquals(config["foo"]["bar"], "1")
        self.assertEquals(config["bar"]["foo"], "baz")

    def test_find_config(self):
        app_dir = os.path.join(
            TEST_DIR, "resources")
        self.assertEquals(
            find_config(app_dir),
            os.path.join(
                app_dir, 'aio.conf'))

    def test_find_config_etc(self):
        app_dir = os.path.join(
            TEST_DIR, "resources", "sub")
        self.assertEquals(
            find_config(app_dir),
            os.path.join(
                app_dir, "etc", 'aio.conf'))
