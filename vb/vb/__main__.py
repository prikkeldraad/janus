from aiohttp import web

from vb.db import *
from vb.app import create_app

if __name__ == "__main__":
    web.run_app(create_app())
