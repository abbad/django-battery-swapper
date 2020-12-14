from django.db import transaction
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from django.db.models.query import RawQuerySet
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import HttpRequest
from rest_framework import status

from shifts.models import Shift
from vehicles.models import Vehicle
from shifts.apis.v2.serializers import ShiftSerializer, RequestShiftSerializer


class ShiftsView(generics.ListCreateAPIView):
    """
        Responsible for creating automatic shifts, you can also use it to return lists.
    """
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer

    def post(self, request: HttpRequest) -> Response:
        """
            Takes a lat lng, and a user --> creates a new list with 20 nearest vehicles. 
        """
        serialized_request = self._serialize_request()
        
        response_data = {
            'user': serialized_request['user'],
            'vehicles': []
        }

        vehicles = nearby_vehicles(
            serialized_request['latitude'], 
            serialized_request['longitude'], 
            radius=serialized_request['radius'],
            limit=serialized_request['assignment_limit']
        )

        with transaction.atomic():
            shift = Shift.objects.create(user=serialized_request['user'])
            response_data['id'] = shift.id
            for vehicle in vehicles:
                shift.vehicles.add(vehicle)
                response_data['vehicles'].append(
                    model_to_dict(vehicle)
                )
        
        return Response(data=response_data, status=status.HTTP_201_CREATED)

    def _serialize_request(self):
        serialized_request = RequestShiftSerializer(data=self.request.data)
        serialized_request.is_valid(raise_exception=True)
        return serialized_request.data 


class NearbyVehiclesSerivce():


    def __init__(self):
        pass



    def nearby_vehicles(self, lat: float, lng: float, radius: int, limit: int=20) -> RawQuerySet:
        """
        Usually I create a service and encapsulate this logic there. 
        http://en.wikipedia.org/wiki/Haversine_formula
        """
        earth_radius = 6371 # (kms)
        radius = float(radius) / 1000.0 # Distance radius convert m to km

        query = F"""SELECT id FROM
                    (SELECT id, latitude, longitude, ({earth_radius} * acos(CAST((cos(radians({lat})) * cos(radians(latitude)) *
                                                        cos(radians(longitude) - radians({lng})) +
                                                        sin(radians({lat})) * sin(radians(latitude))) AS DECIMAL)))
                        AS distance
                        FROM vehicles_vehicle) AS distances
                    WHERE distance < {radius}
                    ORDER BY distance
                    OFFSET 0
                    LIMIT {limit}"""

        return Vehicle.objects.raw(query)
