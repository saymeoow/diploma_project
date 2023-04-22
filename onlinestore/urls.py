from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('support', views.support,
         name='support'),
    path('', views.sneakers_list,
         name='sneakers_list'),
    path('<slug:company_slug>/', views.sneakers_list,
         name='sneakers_by_company'),
    path('<int:id>/<slug:slug>', views.sneakers_detail,
         name='sneakers_detail'),
]
