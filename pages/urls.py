from  django.urls import path
from pages import views



urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("property/", views.PropertyPageView.as_view(), name="property"),
    path("remodel/", views.RemodelPageView.as_view(), name="remodel"),

]