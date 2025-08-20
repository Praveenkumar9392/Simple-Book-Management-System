from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from books.models import Book
from django.contrib.auth import get_user_model

class BookAPITests(APITestCase):
    def setUp(self):
        self.list_url = reverse('book-list')
        # Create a test user
        self.user = get_user_model().objects.create_user(
            username="tester", password="pass1234"
        )
        # Authenticate the client
        self.client.force_authenticate(user=self.user)

    def test_create_and_retrieve_book(self):
        payload = {
            "title": "Clean Code",
            "author": "Robert C. Martin",
            "published_date": "2008-08-01",
            "is_available": True
        }
        # Create
        res = self.client.post(self.list_url, payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        book_id = res.data["id"]

        # Retrieve
        detail_url = reverse('book-detail', args=[book_id])
        res_get = self.client.get(detail_url)
        self.assertEqual(res_get.status_code, status.HTTP_200_OK)
        self.assertEqual(res_get.data["title"], "Clean Code")

    def test_filtering(self):
        Book.objects.create(title="A", author="Alice", is_available=True)
        Book.objects.create(title="B", author="Bob", is_available=False)
        res = self.client.get(self.list_url + "?author=ali&available=true")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["count"], 1)
