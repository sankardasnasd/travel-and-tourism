from django.urls import include, path 
from.import views

urlpatterns = [
    path('nav',views.nav,name='nav'),
    path('home',views.home,name='home'),
    path('home2',views.home2,name='home2'),
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('signout',views.signout,name='signout'),
    path('package',views.package,name='package'),
    path('hotel',views.hotel,name='hotel'),
    path('destinations',views.destinations,name='destinations'),
    path('hotel-detail<uid>/' ,views.hotel_detail , name="hotel_detail"),
    path('package-booking<uid>/' ,views.packagebooking , name="packagebooking"),
    
    
    
    

]