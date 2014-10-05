# Django Modules
# from django.test import TestCase

# Third Party Modules
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

# App Modules
from accounts.factory import UserFactory
from measurements.models import Measurement


class APITest(APITestCase):

    def setUp(self):
        self.user = UserFactory.create()
        self.apiclient = APIClient()
        self.apiclient.login(username=self.user.username, password=UserFactory.DEFAULT_PASSWORD)
        self.measurement = Measurement.objects.create(user=self.user, gps="xyz", bpm=50, hr_max=30, effort=10, recovery=10, status="ok", details="all ok", raw="lorem ipsum")

    def test_all_measurements(self):
        try:
            data = {"user": "1", "gps": "xyz", "bpm": "50", "hr_max": "30", "effort": "10", "recovery": "10", "status": "ok", "details": "all ok", "raw": "lorem ipsum"}
            url = '/api/v1/measurements/'
            response = self.apiclient.get(url, data, format='json')
            self.assertEqual(response.status_code, 200, response.content)
            print(response.content)
        except Exception as e:
            print(e)
            raise
