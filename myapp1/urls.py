
from django.urls import path
from . import views

app_name="myapp1"

urlpatterns = [
    path('',views.home1,name='home1'),
    path('turn_on/',views.turn_on,name='turn_on'),
    path('register/',views.register,name='register'),
    path('user_logout/',views.user_logout,name='logout'),
    path('user_login/',views.user_login,name='user_login'),
    path('home2/',views.home2,name='home2'),
    path('get_status/',views.get_status,name='get_status'),
    #path('controllight/',views.controllight,name='controllight'),
]
