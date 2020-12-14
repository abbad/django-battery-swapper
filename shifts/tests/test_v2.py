"""
    Simple tests to demo using the api endpoint v2.
"""
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from vehicles.loaders.vehicle_fixture_loader import VehicleFixtures

class TestShiftsV1(APITestCase):
    """
        Test to make sure v2 requirements are met.
    """
    API_BASE = '/api/v2/shifts/'

    @classmethod
    def setUpTestData(cls):
        VehicleFixtures().load_fixtures()

    def test_user_create_shifts(self):
        # - create shifts,
        response = self.client.post(self.API_BASE, data={
            'user': 'testuser', 
            'latitude': '40.673568',
            'longitude': '-74.000575'
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        expected_license_plates = [
            'NY0014',
            'NY0007',
            'NY0006',
            'NY0008',
            'NY0001',
            'NY0013',
            'NY0005',
            'NY0009',
            'NY0015',
            'NY0002',
            'NY0003',
            'NY0004',
            'NY0011',
            'NY0010',
            'NY0012',
        ]

        actual_license_plates = [vehicle['license_plate'] for vehicle in response.json()['vehicles']]
        self.assertListEqual(expected_license_plates, actual_license_plates)

