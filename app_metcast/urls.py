from django.urls import path
from .views import metcast_view

urlpatterns = [
    path('', metcast_view),
]

