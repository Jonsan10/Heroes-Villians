from django.urls import path
from . import views

urlpatterns = [
    path('', views.hv_lists),
    path('<int:pk>/', views.hv_lists)
]