from django.urls import path
from . import views

urlpatterns = [
    path('', views.detail_list, name='detail_list'),
    path('<int:pk>/', views.detail_view, name='detail_view'),
    path('new/', views.detail_create, name='detail_create'),
    path('<int:pk>/edit/', views.detail_update, name='detail_update'),
    path('<int:pk>/delete/', views.detail_delete, name='detail_delete'),
]
