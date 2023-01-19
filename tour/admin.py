from django.contrib import admin
from.models import Profile,Signup,Destination,Package,Amenities,Hotel,PackageBooking,HotelBooking

# Register your models here.
admin.site.register(Profile)
admin.site.register(Signup)
admin.site.register(Package)
admin.site.register(Amenities)
admin.site.register(Hotel)
admin.site.register(PackageBooking)
admin.site.register(HotelBooking)
admin.site.register(Destination)
def __str__(self) -> str:
        return self.destination_name
