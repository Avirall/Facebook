from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/',views.loginPage,name='login'),
    path('loggedin/',views.loginUser,name='home'),
    path('signup/',views.registerUser,name='signup'),
    path('loggedin/<int:id>/', views.like, name='like'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)