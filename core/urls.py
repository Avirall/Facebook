from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginPage,name='main'),
    path('loggedin/',views.loginUser,name='home'),
]
