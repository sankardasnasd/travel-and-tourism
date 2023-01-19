from django.shortcuts import render,redirect
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from tour.models import Profile
from django.contrib import messages,auth
from django.contrib.auth import authenticate,login,logout
from.models import Destination,Package,Amenities,Hotel,HotelBooking,PackageBooking
from django.db.models import Q
# Create your views here.
def nav(request):
    return render(request,'nav.html')

def home(request):
    return render(request,'home.html')

def home2(request):
    return render(request,'home2.html')




def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        myuser=User.objects.create_user(username,email,password)
        myuser.firstname = firstname
        myuser.lastname= lastname
        myuser.save()

        messages.success(request,'your account  successfully created')
        return redirect('signin')

    return render(request,'signup.html')

def signin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user= authenticate(username=username,password=password)


        if user is not None:
            login(request,user)
            firstname=user.first_name
            return render(request,'home.html',{'firstname':firstname})

            
        else:
            messages.error(request,'bad credentials')
            return redirect('home2')


    return render(request,'signin.html')

def signout(request):
    logout(request)
    messages.success(request,'logged out successfully')
    return redirect('home')

def destinations(request):
    
    dict_dest = {
        'dest' : Destination.objects.all()
    }
    return render(request,'destinations.html',dict_dest)

def hotel(request):
    amenities_objs = Amenities.objects.all()
    hotels_objs = Hotel.objects.all()
    

    sort_by = request.GET.get('sort_by')
    search = request.GET.get('search')
    amenities = request.GET.getlist('amenities')
    print(amenities)

    if sort_by:

        
        if sort_by == 'ASC':
            hotels_objs = hotels_objs.order_by('hotel_price')
        elif sort_by == 'DSC':
            hotels_objs = hotels_objs.order_by('-hotel_price')  


    
    if search:
        hotels_objs = hotels_objs.filter(
            Q(hotel_name__icontains = search) |
            Q(description__icontains = search) )

    if len(amenities):
        hotels_objs=hotels_objs.filter(amenities__amenity_name__in = amenities).distinct()

    
    
    context = {'amenities_objs' : amenities_objs , 'hotels_objs' : hotels_objs , 'sort_by' : sort_by 
    , 'search' : search,'amenities':amenities }
    return render(request,'hotel.html',context)

# hotel booking step=2
def check_booking(start_date  , end_date ,uid , room_count):
    qs = HotelBooking.objects.filter(
        start_date__lte=start_date,
        end_date__gte=end_date,
        hotel__uid = uid
        )
    
    if len(qs) >= room_count:
        return False
    
    return True

def hotel_detail(request,uid):
    hotel_obj = Hotel.objects.get(uid = uid)
    

# hotel booking calling get via name stp=1
    if request.method == 'POST':
        checkin = request.POST.get('checkin')
        checkout= request.POST.get('checkout')
        hotel = Hotel.objects.get(uid = uid)
        if not check_booking(checkin ,checkout  , uid , hotel.room_count):
            messages.warning(request, 'Hotel is already booked in these dates ')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        HotelBooking.objects.create(hotel=hotel , user = request.user , start_date=checkin
        , end_date = checkout , booking_type  = 'Pre Paid', user_address = ' user_address')
        
        messages.success(request, 'Your booking has been saved')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


    
    return render(request , 'hotel_detail.html' ,{
        'hotels_obj' :hotel_obj
    })


def packagebooking(request,uid):
    package_obj = Package.objects.get(uid = uid)
    
   
    context = {'package_obj':package_obj}
    return render(request , 'packagebooking.html',context )

def package(request):
    package_objs = Package.objects.all()
    search = request.GET.get('search')

    if search:
        package_objs = package_objs.filter(
            Q(package_name__icontains = search) |
            Q(Package_description__icontains = search))
            
    context = {'package_objs':package_objs,'search' : search}
   
    return render(request,'package.html',context)



