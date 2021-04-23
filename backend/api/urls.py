from django.urls import path
from .views import ListMerchant, ListItem, DetailMerchant, DetailItem

# path so far "api/"
urlpatterns = [
    path("item/", ListItem.as_view()),
    path("item/<int:pk>", DetailItem.as_view()),
    path("merchant/", ListMerchant.as_view()),
    path("merchant/<int:pk>", DetailMerchant.as_view())
]
