from django.core.management import BaseCommand
from vehicles.loaders.vehicle_fixture_loader import VehicleFixtures

class Command(BaseCommand):

    def handle(self, *args, **options): #pylint: disable=too-many-locals
        VehicleFixtures().load_fixtures()
