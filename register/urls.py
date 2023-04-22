from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login,
         name='login'),
    path('logout/', views.logouts,
         name='logouts'),
    path('register/', views.register,
         name='register'),
    path('edit_profile/', views.edit,
         name='edit'),
    path('profile', views.profile,
         name='profile'),
    path('profile_personal', views.profile_personal,
         name='profile_personal'),
]