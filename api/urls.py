from django.urls import path

from . import views

urlpatterns = [
    path('', views.Email_Sender.as_view(), name='email'),
    path('game', views.GameScheduleView.as_view(), name='game'),
    path('search/', views.Search.as_view(), name='search'),
    path('login', views.LoginView.as_view(), name='login'),
    path('signup', views.Signup.as_view(), name='signup'),
    path('migration/', views.migration, name='migrations'),
]
