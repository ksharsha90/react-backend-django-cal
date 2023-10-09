from django.urls import path
from rest_framework.routers import DefaultRouter
from . views import CustomerViewSet

router = DefaultRouter()
router.register('customers', CustomerViewSet )

urlpatterns = [
    # path('customers', customers)
] + router.urls