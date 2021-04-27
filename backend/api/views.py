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

    # TODO: How to return item returned from bestKeywordMatch?

    def bestKeywordMatch(self, queryItem, minMatches=1):
        """
        Finds item whose name most closely matches query item. Since some keywords may exist in
        two items that are not the same, a minimum threshold of matches must be met to get a result.
        @param queryItem: name of query item
        @param minMatches: minimum number of keyword matches to return a result
        """
        queryWords = set(queryItem.split(" "))

        for item in Item.objects.all():
            matches = self.getNumMatchingKeywords(queryItem, item.name)
            if mostMatches is None or mostMatches < matches:
                mostMatches = matches
                bestMatch = item

        if mostMatches >= minMatches:
            return bestMatch
        else:
            return None

    def getNumMatchingKeywords(self, queryName, itemName):
        """
        Returns the number of matching keywords between two names.
        """
        matches = 0
        queryWords = set(queryName.split(" "))

        for word in itemName.split(" "):
            if word in queryWords:
                matches += 1

        return matches
