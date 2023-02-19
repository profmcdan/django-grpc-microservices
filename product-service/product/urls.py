from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewSets

app_name = 'product'

router = DefaultRouter()
router.register('', ProductViewSets)

urlpatterns = [
    path('', include(router.urls)),
]
