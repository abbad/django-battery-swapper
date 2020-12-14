VEHICLE_FIXTURE = [
    {
        "id": 1,
        "license_plate": "NY0001",
        "battery_level": 90,
        "in_use": True,
        "model": "Niu",
        "location": [40.680245, -73.996955],
    },
    {
        "id": 2,
        "license_plate": "NY0002",
        "battery_level": 9,
        "in_use": False,
        "model": "Niu",
        "location": [40.684978,-73.998965],
    },
    {
        "id": 3,
        "license_plate": "NY0003",
        "battery_level": 65,
        "in_use": False,
        "model": "Niu",
        "location": [40.683574,-73.990715],
    },
    {
        "id": 4,
        "license_plate": "NY0004",
        "battery_level": 34,
        "in_use": False,
        "model": "Niu",
        "location": [40.67942,-73.983841],
    },
    {
        "id": 5,
        "license_plate": "NY0005",
        "battery_level": 20,
        "in_use": False,
        "model": "Niu",
        "location": [40.676695,-73.988838],
    },
    {
        "id": 6,
        "license_plate": "NY0006",
        "battery_level": 15,
        "in_use": False,
        "model": "Niu",
        "location": [40.675496,-73.99468],
    },
    {
        "id": 7,
        "license_plate": "NY0007",
        "battery_level": 90,
        "in_use": False,
        "model": "Niu",
        "location": [40.678274,-74.001642],
    },
    {
        "id": 8,
        "license_plate": "NY0008",
        "battery_level": 9,
        "in_use": False,
        "model": "Niu",
        "location": [40.678434,-73.997158],
    },
    {
        "id": 9,
        "license_plate": "NY0009",
        "battery_level": 90,
        "in_use": False,
        "model": "Niu",
        "location": [40.683456,-74.002047],
    },
    {
        "id": 10,
        "license_plate": "NY0010",
        "battery_level": 22,
        "in_use": True,
        "model": "Niu",
        "location": [40.677941,-73.982731],
    },
    {
        "id": 11,
        "license_plate": "NY0011",
        "battery_level": 76,
        "in_use": False,
        "model": "Niu",
        "location": [40.673533,-73.981992],
    },
    {
        "id": 12,
        "license_plate": "NY0012",
        "battery_level": 90,
        "in_use": False,
        "model": "Niu",
        "location": [40.668346,-73.976115],
    },
    {
        "id": 13,
        "license_plate": "NY0013",
        "battery_level": 2,
        "in_use": False,
        "model": "Niu",
        "location": [40.669861,-73.989846],
    },
    {
        "id": 14,
        "license_plate": "NY0014",
        "battery_level": 13,
        "in_use": False,
        "model": "Niu",
        "location": [40.673568,-74.000575],
    },
    {
        "id": 15,
        "license_plate": "NY0015",
        "battery_level": 17,
        "in_use": False,
        "model": "Niu",
        "location": [40.676001,-73.987382],
    },
]

from vehicles.models import Vehicle


class VehicleFixtures(object):
    """
        Fixture loader, I usually use factory boy.
    """
    model_to_int_mapper = {
        'Niu' : 1
    }
        
    def load_fixtures(self):
        for vehicle in VEHICLE_FIXTURE:
            Vehicle.objects.create(
                license_plate=vehicle['license_plate'],
                battery_level=vehicle['battery_level'],
                in_use=vehicle['in_use'],
                model=self.model_to_int_mapper[vehicle['model']],
                latitude=vehicle['location'][0],
                longitude=vehicle['location'][1]
            )
