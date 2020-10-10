from starlette.endpoints import HTTPEndpoint
from starlette.responses import JSONResponse


class HelloWorld(HTTPEndpoint):
    """."""

    async def get(self, request, *args, **kwargs):
        """."""

        return JSONResponse({'hello': 'World'})
