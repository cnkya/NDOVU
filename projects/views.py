from django.shortcuts import render
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        UpdateView,
        DeleteView
)

from .models import Project

# Create your views here.

class ProjectListView(ListView): #scan ops
        template_name = "projects/projects_list.html"
        model = Project

class ProjectCreateView(CreateView): #create new records
        template_name = "projects/new_project.html"
        model = Project
        fields = ["name", "image", "tasks", "vendor", "total_cost", "start_date", "complete_date", "comments" ]
        

class ProjectUpdateView(UpdateView): #update current records
        template_name = "projects/update_project.html"
        model = Project
        fields = ["name", "image", "tasks", "vendor", "total_cost", "start_date", "complete_date", "comments" ]

class ProjectDetailView(DetailView): # read single, reads a single copy for read-only
        template_name = "projects/detail_project.html"
        model = Project

        
