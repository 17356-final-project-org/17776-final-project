from .models import Merchant, Item
from rest_framework import generics
from .serializers import MerchantSerializer, ItemSerializer

class ListMerchant(generics.ListAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer

class DetailMerchant(generics.RetrieveAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer

class ListItem(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class DetailItem(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
