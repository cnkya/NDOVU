from  django.urls import path
from projects import views



urlpatterns = [
path("", views.ProjectListView.as_view(), name="list"),
path("<int:pk>/", views.ProjectDetailView.as_view(), name="detail"),
path("new/", views.ProjectCreateView.as_view(), name="new"),
path("<int:pk>/update/", views.ProjectUpdateView.as_view(), name="update"),
]