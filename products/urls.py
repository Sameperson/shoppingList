from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductListViewSet, ProductEntryViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'product_lists', ProductListViewSet)
router.register(r'entries', ProductEntryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
