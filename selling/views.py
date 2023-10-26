from .models import *
from .serializer import *
from rest_framework import viewsets
from django.http import JsonResponse


class CustomerModelViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ItemModelViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer


class ShopcardModelViewSet(viewsets.ModelViewSet):
    queryset = Shopcard.objects.all()
    serializer_class = ShopcardSerializer


def customer_purchase_history(request, pk):

    shop_card = Items.objects.all()
    customer_card = shop_card.filter(owner_id=pk)
    serializer = ShopcardSerializer(customer_card.data, many=True)
    return JsonResponse({"customer_card": serializer})


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
