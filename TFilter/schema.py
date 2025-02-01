import graphene
from graphene import ObjectType
from graphene_django.types import DjangoObjectType
from elasticsearch_dsl import Search
from django_elasticsearch_dsl.search import Search as ElasticsearchSearch
from elasticsearch import Elasticsearch
from datetime import datetime


# GraphQL ObjectTypes for related models
class TrainType(graphene.ObjectType):
    pass


class RailwayCompanyType(graphene.ObjectType):
    pass


class StationType(graphene.ObjectType):
    pass


# GraphQL ObjectType for Flight with necessary fields
class TrainHallType(graphene.ObjectType):
    pass


# Base Filter Strategy
class FilterStrategy:
    def apply_filter(self, search, value):
        pass


# Strategy for applying dynamic filters based on parameters
class DepartureStationFilter(FilterStrategy):
    def apply_filter(self, search, value):
        pass


class ArrivalStationFilter(FilterStrategy):
    def apply_filter(self, search, value):
        pass


class DepartureDateFilter(FilterStrategy):
    def apply_filter(self, search, value):
        pass


class TrainCapacityFilter(FilterStrategy):
    def apply_filter(self, search, value):
        pass


class TrainTypeFilter(FilterStrategy):
    def apply_filter(self, data, value):
        pass


class RailwayCompanyFilter(FilterStrategy):
    def apply_filter(self, data, value):
        pass


class TrainHallFilter(FilterStrategy):
    def apply_filter(self, search, value):
        pass


class DepartureTimeFilter(FilterStrategy):
    def apply_filter(self, data, value):
        pass


# Advanced Filters for Step 2
# Advanced Filters for Step 2 (Merged into one class)
class AdvancedTrainFilters:
    @staticmethod
    def filter_by_price(Trains, min_price=None, max_price=None):
        pass

    @staticmethod
    def filter_fastest_train(Trains):
        pass

    @staticmethod
    def filter_earliest_train(Trains):
        pass

    @staticmethod
    def filter_latest_train(Trains):
        pass

    @staticmethod
    def filter_stars_train(Trains):
        pass


# Main GraphQL Query
class TrainsQuery(ObjectType):

    def resolve_trains(self, info):
        pass