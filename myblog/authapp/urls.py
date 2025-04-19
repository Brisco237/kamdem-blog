from django.urls import path
from authapp.views import home,register,login_user, logout_user

urlpatterns = [

    # User urls views
    path('', home, name='home'),
    path('authapp/register/', register, name='register'),
    path('authapp/login_user/', login_user, name='login_user'),
    path('authapp/logout_user/', logout_user, name='logout_user'),
]
