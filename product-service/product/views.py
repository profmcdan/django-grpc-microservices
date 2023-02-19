from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer


class ProductViewSets(viewsets.ModelViewSet):
    """Product ViewSets"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

    # def get_serializer_class(self):
    #     if self.action in ['create', 'partial_update']:
    #         return CreateUserSerializer
    #     return super().get_serializer_class()

