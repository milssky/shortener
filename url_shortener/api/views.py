from rest_framework.viewsets import ModelViewSet

from .serializers import UrlsSerializer
from shortener.models import Urls


class UrlsViewSet(ModelViewSet):
    queryset = Urls.objects.all()
    serializer_class = UrlsSerializer
