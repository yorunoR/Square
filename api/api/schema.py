from graphene import Field, List, Mutation, ObjectType, Schema, String
from graphene_django import DjangoObjectType
from graphql import GraphQLError

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


class SigninUserMutation(Mutation):
    user = Field(UserType)

    @classmethod
    def mutate(cls, root, info):
        try:
            user = User.objects.filter(uid=info.context.uid).first()
            if user is None:
                user = User.objects.create(uid=info.context.uid, email=info.context.email, name=info.context.name, activated=True)
        except Exception as e:
            raise GraphQLError("Invalid user.") from e

        return SigninUserMutation(user=user)


class Mutation(ObjectType):
    signin_user = SigninUserMutation.Field()


schema = Schema(query=Query, mutation=Mutation)
