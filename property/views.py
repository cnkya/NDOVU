from django.shortcuts import render, redirect
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        UpdateView,
        DeleteView
)

from .models import PropertyManagement, PropertyFinance, PropertyTenantInfo, PropertyMaintenanceInfo

# Create your views here.

class PropertyListView(ListView): #scan ops
        template_name = "property/property_list.html"
        model = PropertyManagement
        

#class PropertyCreateView(CreateView): #create new records
        #template_name = "property/property_new.html"
        #model = PropertyManagement

        #def get_success_url(self) -> str:
                #return super().get_success_url()


        
        

class PropertyUpdateView(UpdateView): #update current records
        template_name = "property/property_update.html"
        

class PropertyDetailView(DetailView): # read single, reads a single copy for read-only
        template_name = "property/property_detail.html"
        
def create_property_page(request):
        return render(request, "property/property_new.html")

def create_property(request):
        # Create record
        property = PropertyManagement.objects.create(
                property_name = request.POST.get('property_name'),
                image = request.POST.get('image'),
                address= request.POST.get('address'),
                property_type= request.POST.get('property_type'),
                number_of_units= request.POST.get('number_of_units'),
                year_built= request.POST.get('year_built'),
                square_footage= request.POST.get('square_footage'),
                acquired_date= request.POST.get('acquired_date'),
        )
        
        property.save()

        finance = PropertyFinance.objects.create(
                purchase_price = request.POST.get('purchase_price'),
                market_value = request.POST.get('market_value'),
                monthly_rent = request.POST.get('monthly_rent'), 
                operating_expenses = request.POST.get('operating_expenses'),
                mortgage_details = request.POST.get('mortgage_details'),
                
                property = property
        )


        finance.save()

        tenant = PropertyTenantInfo.objects.create(
                name = request.POST.get('name'),
                lease_terms = request.POST.get('lease_terms'),
                rent_payment_status =request.POST.get('rent_payment_status'),

                property = property
                )
        tenant.save()
        

        maintenance = PropertyMaintenanceInfo.objects.create(
                scheduled_maintenance = request.POST.get('scheduled_maintenance'),
                vendor = request.POST.get('vendor'),
                cost = request.POST.get('cost'),

                property = property
        )
        maintenance.save()

        return redirect('propertylist')