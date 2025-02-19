from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ksrtc.views import BusTripViewSet, UserViewSet

router = DefaultRouter()
router.register(r'bus-trips', BusTripViewSet , basename="bustrip")  # Register the viewset
router.register(r'users', UserViewSet, basename="users")  # Register the viewset

urlpatterns = [
    path('', include(router.urls)),  # Include DRF router URLs
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),  # Include DRF authentication URLs
]