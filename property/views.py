from django.shortcuts import render
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        UpdateView,
        DeleteView
)



# Create your views here.

class PropertyListView(ListView): #scan ops
        template_name = "property/property_list.html"
        

class PropertyCreateView(CreateView): #create new records
        template_name = "property/property_new.html"
        
        

class PropertyUpdateView(UpdateView): #update current records
        template_name = "property/property_update.html"
    

class PropertyDetailView(DetailView): # read single, reads a single copy for read-only
        template_name = "property/property_detail.html"
        

