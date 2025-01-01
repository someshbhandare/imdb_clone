from django.urls import re_path, include
from rest_framework.routers import DefaultRouter

from content.views import MovieViewSet

router = DefaultRouter()
router.register(r"movies", MovieViewSet, basename="movies")

urlpatterns = [
    re_path("", include(router.urls))
]

app_name = "content"