from django.test import TestCase
from django.conf import settings
from django.urls import reverse


class TestLeague(TestCase):

    def test_detailview_deny_anonymous(self):
        url_to_view = reverse("leagues:league_detail", code=league.slug)
        response = self.client.get(url_to_view, follow=True)
        self.assertRedirects(response, settings.LOGIN_URL)
        response = self.client.post(url_to_view, follow=True)
        self.assertRedirects(response, settings.LOGIN_URL)
    
    def test_call_view_load(self):
        self.client.login(username='user', password='test')  # defined in fixture or with factory in setUp()
        response = self.client.get('/url/to/view')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'conversation.html')

    def test_call_view_fail_blank(self):
        self.client.login(username='user', password='test')
        response = self.client.post('/url/to/view', {}) # blank data dictionary
        self.assertFormError(response, 'form', 'some_field', 'This field is required.')
        # etc. ...

    def test_call_view_fail_invalid(self):
        # as above, but with invalid rather than blank data in dictionary
        pass

    def test_call_view_success_invalid(self):
        # same again, but with valid data, then
        self.assertRedirects(response, '/contact/1/calls/')