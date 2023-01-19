from django.db import models
from django.contrib.auth import get_user_model
import uuid
from django.contrib.auth.models import User


# Create your models here.


class Basemodel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4  ,editable=False,primary_key=True)
    created_at=models.DateField(auto_now=True)
    updated_at=models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Profile(models.Model):
    username = models.CharField(max_length=50)
    name = models.TextField()
    last_name = models.TextField()
    location = models.CharField(max_length=100,blank=True)
    age = models.IntegerField()
    bio = models.TextField(blank= True)

    def __str__(self):
        return self.user.username

class Signup(Basemodel):
    username= models.CharField(max_length=20)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email = models.EmailField()
    password=models.TextField()
    password2= models.TextField()

    def __str__(self):
        return self.username
        
class Destination(Basemodel):
    destination_name = models.CharField(max_length=100)
    destination_description = models.CharField(max_length=500)
    destination_images = models.ImageField(upload_to="destination") 

    def __str__(self) -> str:
        return self.destination_name

class Amenities(Basemodel):
    amenity_name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.amenity_name



    

class Package(Basemodel):
    package_name = models.CharField(max_length=50)
    Package_description = models.CharField(max_length=200)
    package_images = models.ImageField(upload_to="package")
    package_price = models.IntegerField()
    package_amenity_name = models.CharField(max_length=100)
    package_days = models.IntegerField()
    def __str__(self) -> str:
        return self.package_name

class Hotel(Basemodel):
    hotel_name = models.CharField(max_length=100)
    hotel_images = models.ImageField(upload_to="hotels")
    hotel_price = models.IntegerField()
    description = models. TextField()
    amenities =models.ManyToManyField(Amenities)
    room_count = models.IntegerField(default=10)

    def __str__(self) -> str:
        return self.hotel_name
class HotelBooking(Basemodel):
    hotel = models.ForeignKey(Hotel,related_name="hotel_booking",on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name="user_booking",on_delete=models.CASCADE)
    user_address = models.CharField(max_length=250)
    user_phone  = models.TextField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()
    booked_on = models.DateField(auto_now = True)
    booking_type= models.CharField(max_length=100,choices=(('Pre Paid' , 'Pre Paid') , ('Post Paid' , 'Post Paid')))


class PackageBooking(Basemodel):
    package_name =models.ForeignKey(Package,related_name="package_booking",on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name="user_package_booking",on_delete=models.CASCADE)
    user_address = models.CharField(max_length=250)
    user_phone  = models.TextField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()
    booked_on = models.DateField(auto_now = True)
    booking_type= models.CharField(max_length=100,choices=(('Pre Paid' , 'Pre Paid') , ('Post Paid' , 'Post Paid')))


    

