from  django.urls import path
from pages import views



urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("service/", views.ServicePageView.as_view(), name="services"),

]