from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class HomePageTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'store/store.html')


class CartPageTests(TestCase):
    def setUp(self):
        # Create user
        test_user = get_user_model().objects.create_user(
            username='testuser', password='testpassword'
        )
        test_user.save()

    def test_cart_page_status_code_as_anonymous_user(self):

        response = self.client.get('/cart')

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/users/login/')

    def test_view_url_by_name_as_anonymous_user(self):

        response = self.client.get(reverse('cart'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/users/login/')

    def test_view_uses_correct_template_as_logged_in_user(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('cart'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/cart.html')
