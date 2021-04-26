from .models import Item
from rest_framework import generics
from .serializers import ItemSerializer

class ListItem(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class DetailItem(generics.RetrieveAPIView):
    # TODO (Diego): this view is passed in the name of the item that got scraped
    # by the front end. It gets passed in the name through the url like so:
    # api/item/<str:name_of_item_scraped_from_frontend>
    # see the urls.py file in this app for details. It then needs to use this
    # passed in string to do the keyword search.
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
