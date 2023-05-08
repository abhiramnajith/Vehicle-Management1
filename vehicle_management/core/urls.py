from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from .views import VehicleList, VehicleDeleteView, VehicleUpdateView,VehicleCreateView
urlpatterns = [
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', VehicleList.as_view(), name='home'),
    path('create/',VehicleCreateView.as_view(),name='create_vehicle'),
    path('edit/<int:pk>/', VehicleUpdateView.as_view(), name='edit_vehicle'),
    path('delete/<int:pk>/', VehicleDeleteView.as_view(), name='delete_vehicle'),
]
