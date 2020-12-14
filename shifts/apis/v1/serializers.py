from vehicles.models import Vehicle
from rest_framework import serializers
from shifts.models import Shift, VehicleShift

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = '__all__'
        depth = 1



class VehicleShiftRequestSerializer(serializers.Serializer):
    vehicles = serializers.PrimaryKeyRelatedField(required=True, many=True, queryset=Vehicle.objects.all())

class VehicleShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleShift
        fields = ['vehicle', 'battery_swapped']
        depth = 1

    def to_representation(self, instance):
        """
            Restructure json to be as a vehicles related to a shift.
        """
        representation = super().to_representation(instance)

        representation['vehicle']['battery_swapped'] = instance.battery_swapped

        return representation['vehicle']
