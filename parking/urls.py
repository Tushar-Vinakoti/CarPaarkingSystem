from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-vehicle/', views.add_vehicle, name='add_vehicle'),
    path('view-vehicles/', views.view_vehicles, name='view_vehicles'),
    path('payment/<int:vehicle_id>/', views.payment, name='payment'),
]