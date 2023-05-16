from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Product, ProductList, ProductEntry
from .serializers import ProductSerializer, ProductListSerializer, ProductEntrySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductEntryViewSet(viewsets.ModelViewSet):
    queryset = ProductEntry.objects.all()
    serializer_class = ProductEntrySerializer

    def create(self, request, *args, **kwargs):
        product_list_id = request.data.get('product_list_id')
        product_list = ProductList.objects.filter(id=product_list_id).first()

        if product_list is None:
            return Response({'error': 'ProductList not found'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ProductListViewSet(viewsets.ModelViewSet):
    queryset = ProductList.objects.all().prefetch_related('entries')
    serializer_class = ProductListSerializer
