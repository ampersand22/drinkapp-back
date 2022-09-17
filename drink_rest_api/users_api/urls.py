from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from users_api import views as user_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('api/useraccount', views.UserAccountList.as_view(), name='useraccount_list'),
    path('api/useraccount/<int:pk>', views.UserAccountDetail.as_view(), name='useraccount_detail'),
    path('api/useraccount/login', csrf_exempt(views.check_login), name="check_login"), # api/useraccount/login will be routed to the check_login function for auth
    path('api/profiles', views.ProfileList.as_view(), name='profile_list'),
    path('api/profiles/<int:pk>', views.ProfileDetail.as_view(), name='profile_detail'),
]