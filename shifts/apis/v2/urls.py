from shifts.apis.v2.views import ShiftsView
from django.urls import path

urlpatterns = [
    path('shifts/', ShiftsView.as_view()),
]
