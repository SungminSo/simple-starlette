import uvicorn

from starlette.applications import Starlette
from starlette.routing import Route

from api import *


routes = [
    Route('/', rest_example),
]

app = Starlette(routes=routes)

if __name__ == '__main__':
    uvicorn.run(app)
