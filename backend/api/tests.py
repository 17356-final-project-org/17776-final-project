from django.test import TestCase
from .models import Item
from django.contrib.auth.models import User

# testing reference: https://docs.djangoproject.com/en/3.2/topics/testing/overview/

class ApiResponsesTest(TestCase):
    def test_api_item_response_code(self):
        response = self.client.get("/api/item/")
        self.assertEqual(response.status_code, 200)

    def test_api_root_link_response_code(self):
        response = self.client.get("/api/")
        self.assertEqual(response.status_code, 404)

    def test_api_nonexistent_link_response_code(self):
        response = self.client.get("/api/random/")
        self.assertEqual(response.status_code, 404)

    
class ItemTest(TestCase):

    @classmethod
    def setUpTestData(self):
        user = User.objects.create_user(username='testuser', password='12345')
        Item.objects.create(seller = user, name = "adidas soccer ball f50", nominal_price = 15,
                            lowest_price = 12, 
                            item_url = "http://amazon.com")

    def test_name(self):
        created_item = Item.objects.get(id = 1)
        item_name = f'{created_item.name}'
        self.assertEqual(item_name, "adidas soccer ball f50")

    def test_nominal_price(self):
        created_item = Item.objects.get(id = 1)
        self.assertEqual(created_item.nominal_price, 15)

    def test_lowest_price(self):
        created_item = Item.objects.get(id = 1)
        self.assertEqual(created_item.lowest_price, 12)

    def test_item_url(self):
        created_item = Item.objects.get(id = 1)
        self.assertEqual(created_item.item_url, "http://amazon.com")

    def test_api_query_look_up(self):
        response = self.client.get("/api/item/adidas soccer ball")
        self.assertEqual(response.status_code, 200)
    
    def test_api_query_not_in_database(self):
        response = self.client.get("/api/item/not here")
        self.assertEqual(response.status_code, 404)

