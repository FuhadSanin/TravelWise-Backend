from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ksrtc.views import BusTripViewSet, UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'bus-trips', BusTripViewSet , basename="bustrip")  # Register the viewset
router.register(r'users', UserViewSet, basename="users")  # Register the viewset

urlpatterns = [
    path('', include(router.urls)),  # Include DRF router URLs
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),  # Include DRF authentication URLs
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]