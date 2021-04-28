from django.urls import path
from .views import ListItem, DetailItem

# path so far "api/"
urlpatterns = [
    path("item/", ListItem.as_view()),
    path("item/<str:itemName>", DetailItem.as_view()),
]
