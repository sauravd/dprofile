from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views
# from .views import HomePageView, MapView

app_name = 'dprofile'

urlpatterns = [
    path(' ', views.home, name='home'),
    path('accesstoroadnetwork/',views.AccessToRoadnetworkView, name="accesstoroadnetwork"),
    path('agrilivstkcooperative/',views.AgriLivstkCooperativesView, name="agrilivstkcooperative"),
    path('animalhusbandryfirms/',views.AnimalHusbandryFirmsView, name="animalhusbandryfirms"),
    path('personaleventdetails/',views.PersonalEventDetails, name="personaleventdetails"),
    path('map/', views.MapView, name='map'),

]