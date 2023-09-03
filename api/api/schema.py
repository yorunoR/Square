from functools import wraps

from graphene import Field, List, Mutation, ObjectType, Schema, String
from graphene_django import DjangoObjectType
from graphql import GraphQLError

from account.models import User


def require_user(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        info = args[1]  # 通常、リゾルバの第二引数は`info`です
        if not info.context.user:
            raise GraphQLError("Authentication required")
        return func(*args, **kwargs)

    return wrapper


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

    @require_user
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
