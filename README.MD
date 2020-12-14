## Tasks

1. Implement Battery Swapping Shift

     one of the main tasks for operations is keeping our vehicles charged.  We do that with a van full of batteries that drives around and swaps out the batteries for vehicles.  Swapping is done in shifts by one employee for a set number of vehicles.  We need to create the basic endpoints that allow us to manage shifts and the swaps on them.

    Requirements

    - create shifts
    - add vehicles to shifts
    - review all vehicles in a shift
    - complete a battery swap for a vehicle
    - check if a swap has been completed for any vehicle in a shift
    - query shift to see if all vehicles in the shift have had their battery swaps

    Design and implement the database and api for the above

2. Implement automatic shift creation. Automatic shift creation should take a lat long that it uses as a start point.  Your vehicle selection should select the 20 closest vehicles to that point.  The vehicles should be in the order that they should be visited to reduce the amount of distance traveled. e.g. the first vehicle in the list should be the first vehicle that should be visited the second the second and so on. Please use euclidian distance vs drive distance for simplicity.


# Solution

## DB design

I created `Shift` table that has a many to many relation to the `Vehicle` table. This many to many relation has a through (junction table) that dictate whether a battery has been swapped or not per shift. 

You can assign the same vehicle to a different shift assuming that shifts could be created for a future schedule. Thus the solution does not prevent assigning the same vehicle to multiple shifts. The solution solves the problem for creating shifts for a user and adding any vehicle to that shift, even if the battery was 100 percent. 

User is a unique field, I did not create a user table to minimize scope. 

Postgres was used but with no support for GIS, finding the nearest 20 vehicles in the current solution depends on the haversine algorithm. 
I would use GeoDjango https://docs.djangoproject.com/en/3.1/ref/contrib/gis/ for production and something similiar to direction 
https://developers.google.com/maps/documentation/directions/start for optimizing users route.  

## API Design 
I conformed to using Django-Rest-Framework Generic Views for creating the endpoints. I used regular URLs to expose them. 

V1
```
urlpatterns = [
    path('shifts/', ShiftsView.as_view()), # GET for retriving all shifts, POST for creating a new shift
    path('shifts/<int:shift_id>/vehicles', VehiclesShiftDetailView.as_view()), # GET for retrieving a list of vehicles, this filter can accept 
    battery_swapped url param (boolean)
    # POST for adding vehicles(s) 
    path('shifts/<int:pk>/vehicles/<int:vehicle_id>', VehicleShiftDetailView.as_view()) # GET for retriving # PUT/PATCH To mark batteries as swapped. 
]
```

v2 
```
urlpatterns = [
    path('shifts/', ShiftsView.as_view()), # GET for retriving all shifts, POST for creating a new shift with the closest 20 vehicles.
]
```

## Outlines

1. Used Docker to spin Postgres and the Django web-server.
2. Used Django-Rest-Framework for building the endpoints.
3. Django admin has been set to help in managing the data if needed. (You can use it to accomplish the same tasks but via the admin)
4. Created an Mgmt command for populating vehicles `./manage.py populate_vehicles`
5. V1 endpoints used for creating shifts, adding vehicles to a shift, and reviewing vehicles in a shift.
6. V2 used for creating an automated shift.

## How To Run Application 
1. Make sure that you have docker and docker-compose installed. 
2. run docker-compose up --build
3. run docker-compose exec web bash --> ./manage.py createsuperuser  # in order to access the django admin interface.
4. run docker-compose exec web bash --> ./manage.py populate_vehicles # for populating Vehicle model with data. 
5. run docker-compose exec web bash --> ./manage.py test # for running tests
