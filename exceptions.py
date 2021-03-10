from starlette.responses import JSONResponse
from starlette.exceptions import HTTPException


class BadRequest(HTTPException):
    pass


async def invalid_request_error(request, exc):
    return JSONResponse({
        "detail": "invalid request body or query",
    }, status_code=400)


class InternalError(HTTPException):
    pass


async def server_error(request, exc):
    return JSONResponse({
        "detail": str(exc),
    }, status_code=500)


exception_handlers = {
    BadRequest: invalid_request_error,
    InternalError: server_error,
    500: server_error,
}
