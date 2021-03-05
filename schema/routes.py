import graphene

from starlette.routing import Route
from starlette.graphql import GraphQLApp
from graphql.execution.executors.asyncio import AsyncioExecutor

from .graphql import Hello


graphql_routes = [
    Route('/graphql', GraphQLApp(
        schema=graphene.Schema(query=Hello),
        executor_class=AsyncioExecutor,
    )),
]
