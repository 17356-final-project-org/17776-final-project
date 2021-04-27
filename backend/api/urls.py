from django.urls import path
from .views import ListItem, DetailItem

# path so far "api/"
urlpatterns = [
    path("item/", ListItem.as_view()),
    path("item/<str:name_of_item_scraped_from_frontend>", DetailItem.as_view()),
]
