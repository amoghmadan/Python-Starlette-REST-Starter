from starlette.routing import Route
from controllers.hello_world import HelloWorld

routes = [
    Route('/', endpoint=HelloWorld, methods=['GET']),
]
