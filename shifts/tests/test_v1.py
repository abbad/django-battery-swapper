"""
    Simple tests to demo using the api endpoint v1.
"""
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from vehicles.loaders.vehicle_fixture_loader import VehicleFixtures

class TestShiftsV1(APITestCase):
    """
        These are tests for making sure that requirements are met. 
        When I write tests, I make them more comprehensive and I organize them differently, however for now all assertions are written in 
        one function.
    """
    API_BASE = '/api/v1/shifts/'

    @classmethod
    def setUpTestData(cls):
        VehicleFixtures().load_fixtures()

    def test_user_create_shifts(self):
        # - create shifts,
        response = self.client.post(self.API_BASE, data={
            'user': 'testuser'
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        shift_data = response.json()

        self.assertListEqual(list(shift_data.keys()), ['id', 'user', 'vehicles'])

        # - add vehicles to shifts
        response = self.client.post(F"{self.API_BASE}{shift_data['id']}/vehicles", data={
            'vehicles': [5,6,7]
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()['results']), 3)

        # - review all vehicles in a shift
        response = self.client.get(F"{self.API_BASE}{shift_data['id']}/vehicles")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()['results']), 3)

        # - complete a battery swap for a vehicle
        response = self.client.patch(F"{self.API_BASE}{shift_data['id']}/vehicles/5", data={
            'battery_swapped': True
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.json()['battery_swapped'])

        # - check if a swap has been completed for any vehicle in a shift
        response = self.client.get(F"{self.API_BASE}{shift_data['id']}/vehicles/5")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.json()['battery_swapped'])

        response = self.client.get(F"{self.API_BASE}{shift_data['id']}/vehicles/6")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(response.json()['battery_swapped'])

        # - query shift to see if all vehicles in the shift have had their battery swaps
        response = self.client.get(F"{self.API_BASE}{shift_data['id']}/vehicles?battery_swapped=True")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()['results']), 1)
