import uvicorn

from starlette.applications import Starlette
from starlette.routing import Route
from starlette.graphql import GraphQLApp
from graphql.execution.executors.asyncio import AsyncioExecutor

from api import *


routes = [
    Route('/graphql', GraphQLApp(
        schema=graphene.Schema(query=Hello),
        executor_class=AsyncioExecutor,
    )),
    Route('/hello', rest_example),
]

app = Starlette(routes=routes)

if __name__ == '__main__':
    uvicorn.run(app)
