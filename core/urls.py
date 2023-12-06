from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('loggedin/',views.loginUser,name='home'),
    path('signup/',views.registerUser,name='signup'),
    path('loggedin/<int:id>/', views.like, name='like'),
    path('loggedin/comments/<int:id>/', views.comment, name='comment'),
    path('loggedin/posts/', views.createpost, name='posts'),
    path('loggedin/friends/', views.addFriend, name='friends'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)