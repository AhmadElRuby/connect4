from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("connect4_UI.urls")),
    path("admin/", admin.site.urls),
]