from django.shortcuts import get_object_or_404
from django.db import transaction
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from shifts.models import Shift, VehicleShift
from vehicles.models import Vehicle
from shifts.apis.v1.serializers import ShiftSerializer, VehicleShiftSerializer, VehicleShiftRequestSerializer


class ShiftsView(generics.ListCreateAPIView):
    """
        Responsible for listing and creating shifts.
    """
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
 

class VehiclesShiftDetailView(generics.ListCreateAPIView):
    """
        Repsonsible for showing a list of vehicles in a shift or adding vehicle(s) to a shift. 
        Accepts url param battery_swapped. 
    """
    queryset = VehicleShift.objects.all()
    serializer_class = VehicleShiftSerializer
    filterset_fields = ['battery_swapped']

    def post(self, request, shift_id):
        """
            Takes list of vehicle(s) ids to be added. 
        """
        serialized_request = VehicleShiftRequestSerializer(data=request.data)
        serialized_request.is_valid(raise_exception=True)

        vehicles = Vehicle.objects.filter(id__in=serialized_request.data['vehicles'])
        with transaction.atomic():
            for vehicle in vehicles:
                vehicle_shift = VehicleShift(shift_id=shift_id, vehicle=vehicle).save()

        return self.get(request, shift_id)

    def get_queryset(self):
        shift = get_object_or_404(Shift, pk=self.kwargs['shift_id'])

        return VehicleShift.objects.filter(shift=shift)


class VehicleShiftDetailView(generics.RetrieveUpdateAPIView):
    """
        Responsible for marking a battery as swapped in a shift.
    """
    queryset = VehicleShift.objects.all()
    serializer_class = VehicleShiftSerializer

    def get_object(self):
        shift_id = self.kwargs['pk']
        vehicle_id = self.kwargs['vehicle_id']
        
        return get_object_or_404(VehicleShift, shift_id=shift_id, vehicle_id=vehicle_id)
