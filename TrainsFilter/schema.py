import graphene
from TFilter.schema import TrainsQuery


class Query(TrainsQuery, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
