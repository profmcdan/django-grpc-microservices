from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSets

app_name = 'user'

router = DefaultRouter()
router.register('', UserViewSets)

urlpatterns = [
    path('', include(router.urls)),
]
