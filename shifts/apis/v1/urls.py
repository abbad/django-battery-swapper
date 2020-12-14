from shifts.apis.v1.views import ShiftsView, VehiclesShiftDetailView, VehicleShiftDetailView
from django.urls import path

urlpatterns = [
    path('shifts/', ShiftsView.as_view()),
    path('shifts/<int:shift_id>/vehicles', VehiclesShiftDetailView.as_view()),
    path('shifts/<int:pk>/vehicles/<int:vehicle_id>', VehicleShiftDetailView.as_view())
]
