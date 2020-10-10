import sys

import uvicorn
from starlette.applications import Starlette

import settings
from middlewares import middleware
from events import on_startup, on_shutdown
from routes import routes

app = Starlette(middleware=middleware, on_startup=on_startup, on_shutdown=on_shutdown, routes=routes)


if __name__ == '__main__':
    """."""

    try:
        uvicorn.run(
            app='main:app',
            host=settings.HOST,
            port=settings.PORT,
            debug=settings.DEBUG,
            reload=settings.RELOAD
        )
    except Exception as exc:
        tc, te, tb = sys.exc_info()
        print(f'Class: {tc.__name__} | Exception: {exc} | Line Number: {tb.tb_lineno} | File: {__name__}')
