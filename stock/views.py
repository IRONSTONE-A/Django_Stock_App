
from rest_framework import viewsets, filters
from .models import(
    Category,
    Brand,
    Product,
    Firm,
    Transaction
)

from.serilaizers import (
    CategorySerializer,
    BrandSerializer,
    ProductSerializer
)

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends =[filters.SearchFilter]
    search_fields = ["name"]
    
class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends =[filters.SearchFilter]
    search_fields = ["name"]
    
class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    