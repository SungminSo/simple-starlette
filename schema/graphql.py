import graphene

from graphql.execution.base import ResolveInfo


class Hello(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))

    async def resolve_hello(self, info: ResolveInfo, name: str):
        return "Hello " + name
