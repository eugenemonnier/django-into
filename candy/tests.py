from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.

class CandyTests(SimpleTestCase):
  def test_page_statuses(self):
    url_list = ['home','about']
    for url in url_list:
      url = reverse(url)
      response = self.client.get(url)
      actual = response.status_code
      expected = 200
      assert actual == expected

  def test_page_templates(self):
    url_list = ['home','about']
    for url in url_list:
      reverse_url = reverse(url)
      response = self.client.get(reverse_url)
      self.assertTemplateUsed(response, url + '.html')
      self.assertTemplateUsed(response, 'base.html')