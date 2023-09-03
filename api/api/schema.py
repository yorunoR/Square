from graphene import Field, List, ObjectType, Schema, String
from graphene_django import DjangoObjectType

from account.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude = (
            "uid",
            "created_at",
            "updated_at",
            "deleted_at",
        )


class Query(ObjectType):
    ping = Field(String)
    users = List(UserType)

    def resolve_ping(self, info, **kwargs):
        return "pong"

    def resolve_users(self, info, **kwargs):
        return User.objects.all()


schema = Schema(query=Query)
