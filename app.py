import uvicorn

from starlette.applications import Starlette

from settings.config import config
from api.routes import rest_routes
from schema.routes import graphql_routes
from exceptions import exception_handlers


app = Starlette(routes=graphql_routes + rest_routes, exception_handlers=exception_handlers)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port="8000", debug=(config.MODE == 'dev'))
