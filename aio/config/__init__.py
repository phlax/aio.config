__version__ = "0.0.1"
import os
import asyncio
from configparser import ConfigParser, ExtendedInterpolation


@asyncio.coroutine
def parse_config(config=None, app_dir=None):
    if not config:

        if not app_dir:
            app_dir = os.getcwd()

        _config = os.path.join(app_dir, 'aio.conf')
        if os.path.exists(_config):
            config = _config
        else:
            _config = os.path.join(app_dir, 'etc', 'aio.conf')
            if os.path.exists(_config):
                config = _config
            else:
                _config = os.path.join(app_dir, '/etc', 'aio.conf')
                if os.path.exists(_config):
                    config = _config
                else:
                    raise Exception('no configuration file found')

    parser = ConfigParser(interpolation=ExtendedInterpolation())
    parser.read_file(open(config))

    return parser

