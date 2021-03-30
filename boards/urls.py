from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListBoard.as_view()),
    path('<int:pk>/', views.DetailBoard.as_view()),
]