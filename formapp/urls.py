from django.urls import path


from . import views

app_name = 'formapp'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='HomePage'),
    path('FirstPage/', views.FirstPage, name='FirstPage'),
    path('SecondPage/', views.SecondPage, name='SecondPage'),
    path('ThirdPage/', views.ThirdPage, name='ThirdPage'),
]