from django.urls import path
from Madhumitha import views
urlpatterns=[
path('rt/',views.home,name="home"),
path('demo/',views.chk),
path('hm/',views.homepage),
path('lg/',views.lgn),
path('rg/',views.reg),
path('',views.bthm),
path('about/',views.about,name="about"),
path('contact/',views.contact,name="contact"),
path('registration',views.registration,name="registration"),
]