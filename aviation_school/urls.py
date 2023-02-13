from django.urls import path
from . import views

app_name='aviation_school'

urlpatterns = [
    path('', views.home, name='home'),
    path('become-a-pilot/', views.become_pilot, name='become_a_pilot'),
    path('sightseeing-tour/', views.sightseeing_tour, name='sightseeing_tour'),
    path('our-aircraft/', views.our_aircraft, name='our_aircraft'),
    path('book-flight/', views.book_flight, name='book_flight'),
]
