from .models import Item
from rest_framework import generics
from .serializers import ItemSerializer

class ListItem(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class DetailItem(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = "itemName"

    def get_object(self):
        print(self.kwargs[self.lookup_field])
        return bestKeywordMatch(self.kwargs[self.lookup_field])

def bestKeywordMatch(queryItem, minMatches=3):
    """
    Finds item whose name most closely matches query item. Since some keywords may exist in
    two items that are not the same, a minimum threshold of matches must be met to get a result.
    @param queryItem: name of query item
    @param minMatches: minimum number of keyword matches to return a result
    """
    mostMatches = float("-inf")
    bestMatch = None
    for item in Item.objects.all():
        matches = getNumMatchingKeywords(queryItem, item.name)
        if mostMatches < matches:
            mostMatches = matches
            bestMatch = item

    if mostMatches >= minMatches:
        return bestMatch
    else:
        return None

def getNumMatchingKeywords(queryName, itemName):
    """
    Returns the number of matching keywords between two names.
    """
    matches = 0
    queryWords = set(queryName.split(" "))

    for word in itemName.split(" "):
        if word in queryWords:
            matches += 1

    return matches
