from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse


class Hello(HTTPEndpoint):
    async def get(self, request: Request):
        return JSONResponse({'msg': 'hello'})
