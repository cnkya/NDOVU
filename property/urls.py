from  django.urls import path
from property import views



urlpatterns = [
path("property/", views.PropertyListView.as_view(), name="property_list"),
path("<int:pk>/", views.PropertyDetailView.as_view(), name="property_detail"),
path("new/", views.create_property_page, name="property_new"),
path("save_property/", views.create_property, name="save_property"),
path("<int:pk>/update_property/", views.PropertyUpdateDetailView.as_view(), name="property_update"), 
path('save_changes/', views.update_property, name='save_changes'),
]