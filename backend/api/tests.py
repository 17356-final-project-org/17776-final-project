from django.test import TestCase
from .models import Item

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
    def setUpTestData(s):
        Item.objects.create(name = "soccer ball", nominal_price = 15,
                            lowest_price = 12, 
                            item_url = "http://amazon.com")

    def test_name(self):
        created_item = Item.objects.get(id = 1)
        item_name = f'{created_item.name}'
        self.assertEqual(item_name, "soccer ball")

    def test_nominal_price(self):
        created_item = Item.objects.get(id = 1)
        self.assertEqual(created_item.nominal_price, 15)

    def test_lowest_price(self):
        created_item = Item.objects.get(id = 1)
        self.assertEqual(created_item.lowest_price, 12)

    def test_item_url(self):
        created_item = Item.objects.get(id = 1)
        self.assertEqual(created_item.item_url, "http://amazon.com")
