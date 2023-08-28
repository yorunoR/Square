from django.contrib import admin
from django.urls import path

from default.views import top

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", top, name="top"),
]
