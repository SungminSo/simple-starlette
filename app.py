import uvicorn

from starlette.applications import Starlette

from api.routes import rest_routes
from schema.routes import graphql_routes


app = Starlette(routes=graphql_routes + rest_routes)

if __name__ == '__main__':
    uvicorn.run(app)
