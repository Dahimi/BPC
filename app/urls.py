from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('Home/', views.Home, name='home'),
    path('Problem/<int:id>/my-ajax-test/', views.Lunch_Tests),
    path('', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('Problem/<int:id>/', views.Play, name='Problem'),
    path('Ranking/', views.Ranking, name='ranking'),
]