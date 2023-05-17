from django.urls import path
from hpme import views

urlpatterns = [
    path("", views.index,name='hpme'),
    path("about", views.about,name='about'),
    path("services", views.services,name='services'),
    path("contact", views.contact,name='contact')
]
