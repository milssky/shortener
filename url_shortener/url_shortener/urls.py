from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shortener.urls', namespace='shortener')),
    path('api/', include('api.urls', namespace='api_shortener'))
]
