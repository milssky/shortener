from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UrlsViewSet


app_name = 'api_shortener'

api_router = DefaultRouter()
api_router.register('url', UrlsViewSet)

urlpatterns = [
    path('', include(api_router.urls)),
]
