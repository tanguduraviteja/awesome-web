from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.index, name='index'),
    path('<int:id>/', views.fetchDetails),
]