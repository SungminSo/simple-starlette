import uvicorn

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def example(request):
    return JSONResponse({'msg': 'hello'})

routes = [
    Route('/', example),
]

app = Starlette(routes=routes)

if __name__ == '__main__':
    uvicorn.run(app)
