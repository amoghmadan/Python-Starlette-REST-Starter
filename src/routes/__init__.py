from starlette.routing import Mount
from . import hello_world

routes = [
    Mount('/api/hello_world', routes=hello_world.routes),
]
