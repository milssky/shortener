import django


from django.urls import path

from . import views

app_name = 'shortener'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.redirect_to_http_url),
]

