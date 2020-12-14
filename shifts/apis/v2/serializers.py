from rest_framework import serializers
from shifts.models import Shift

class RequestShiftSerializer(serializers.Serializer):
    """
        User for serializing the request that come sto this endpoint. 
    """
    latitude = serializers.DecimalField(max_digits=9, decimal_places=6, required=True)
    longitude = serializers.DecimalField(max_digits=9, decimal_places=6, required=True)
    user = serializers.CharField(required=True)
    radius = serializers.IntegerField(default=5000)
    assignment_limit = serializers.IntegerField(default=20)

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = '__all__'
        depth = 1

    def to_representation(self, instance):
        """
            Restructure json to be as a vehicles related to a shift.
        """
        representation = super().to_representation(instance)
        return representation
