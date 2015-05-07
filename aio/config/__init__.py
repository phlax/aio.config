__version__ = "0.0.1"
import os
import asyncio
from configparser import ConfigParser, ExtendedInterpolation


def find_config(app_dir=None):    
    if not app_dir:
        app_dir = os.getcwd()
    config = os.path.join(app_dir, 'aio.conf')
    if os.path.exists(config):
        return config
    config = os.path.join(app_dir, 'etc', 'aio.conf')
    if os.path.exists(config):
        return config
    config = os.path.join(app_dir, '/etc', 'aio.conf')
    if os.path.exists(config):
        return config
    raise Exception('no configuration file found')


@asyncio.coroutine
def parse_config(config=None, app_dir=None):
    parser = ConfigParser(interpolation=ExtendedInterpolation())
    parser.read_file(open(config or find_config(app_dir)))
    return parser

