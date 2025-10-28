from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # Strona główna
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Ścieżka logowania
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Ścieżka wylogowania
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('add/', views.add_transaction, name='add_transaction'),
]