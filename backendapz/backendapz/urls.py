from rest_framework.authtoken import views
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

urlpatterns = [
    path("feeders/", views.FeederListView.as_view()),
    path("animals/", views.AnimalsListView.as_view()),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
]
