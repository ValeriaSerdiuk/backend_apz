from rest_framework.authtoken import views
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from forestry.views import ForestryViewSet, AnimalViewSet, FeederViewSet, VaccinationViewSet

from backendapz.views import index

router = SimpleRouter()

router.register(r'forestry', ForestryViewSet)
router.register(r'animal', AnimalViewSet)
router.register(r'feeder', FeederViewSet)
router.register(r'vaccination', VaccinationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('checkserver/', index, name='index'),
    path('auth/', include('accounts.urls')),
    path('api/', include('api.urls', namespace='api')),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    path('db/v1', include('forestry.urls')),
]

urlpatterns += router.urls

