from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('principal/', include('principal.urls')),
]