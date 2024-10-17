from  django.urls import path
from property import views



urlpatterns = [
path("", views.PropertyListView.as_view(), name="propertylist"),
path("<int:pk>/", views.PropertyDetailView.as_view(), name="propertydetail"),
path("new/", views.PropertyCreateView.as_view(), name="propertynew"),
]