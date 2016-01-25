from django.core.urlresolvers import reverse
from django.db.models import Q
from rest_framework.test import APITestCase

from finance.tests.test_command import WithForm460ADataTest
from locality.models import City


class SupportingTests(WithForm460ADataTest, APITestCase):

    @classmethod
    def setUpClass(cls):
        WithForm460ADataTest.setUpClass()
        APITestCase.setUpClass()

    def test_supporting_list(self):
        # Get first city with non-None name
        city = City.objects.filter(~Q(name=None))[0]

        supporting_url = reverse('locality_supporting',
                                 kwargs={'locality_id': city.id})
        resp = self.client.get(supporting_url)
        self.assertTrue(len(resp.data) > 0)

        # TODO: replace dummy tests with live data tests.
        row = resp.data[0]
        self.assertIn('name', row)
        self.assertIn('contributions', row)
