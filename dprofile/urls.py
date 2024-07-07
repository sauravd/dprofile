from django.urls import path
from . import views
from .views import HomePageView, MapView

app_name = 'dprofile'

urlpatterns = [
    path('dprofile/', HomePageView.as_view(), name='index'),
    path('accesstoroadnetwork/',views.AccessToRoadnetworkView, name="accesstoroadnetwork"),
    path('agrilivstkcooperative/',views.AgriLivstkCooperativesView, name="agrilivstkcooperative"),
    path('animalhusbandryfirms/',views.AnimalHusbandryFirmsView, name="animalhusbandryfirms"),
    path('personaleventdetails/',views.PersonalEventDetails, name="personaleventdetails"),
    path('map/', MapView.as_view(), name='map'),

]