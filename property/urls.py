from  django.urls import path
from property import views



urlpatterns = [
path("property/", views.PropertyListView.as_view(), name="propertylist"),
path("<int:pk>/", views.PropertyDetailView.as_view(), name="propertydetail"),
path("new/", views.create_property_page, name="propertynew"),
path("save_property/", views.create_property, name="save_property"),
]