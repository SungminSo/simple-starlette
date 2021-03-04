from starlette.requests import Request
from starlette.responses import JSONResponse


async def rest_example(request: Request):
    return JSONResponse({'msg': 'hello'})
