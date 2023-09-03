from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from default.views import top

from .middlewares.auth import JWTAuthenticationMiddleware

urlpatterns = [
    path("admin/", admin.site.urls),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True, middleware=[JWTAuthenticationMiddleware()]))),
    path("", top, name="top"),
]
