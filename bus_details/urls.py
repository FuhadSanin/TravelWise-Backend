from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ksrtc.views import BusTripViewSet

router = DefaultRouter()
router.register(r'bus-trips', BusTripViewSet)  # Register the viewset

urlpatterns = [
    path('', include(router.urls)),  # Include DRF router URLs
]