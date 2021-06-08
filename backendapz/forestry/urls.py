from django.urls import path

from . import views
from .views import ForestryViewSet

urlpatterns = [
    path('', ForestryViewSet.as_view({'get': 'list'}))
]