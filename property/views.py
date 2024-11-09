from django.shortcuts import render, redirect
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        UpdateView,
        
)

from .models import PropertyManagement, PropertyFinance, PropertyTenantInfo, PropertyMaintenanceInfo

# Create your views here.

class PropertyListView(ListView): #scan ops
        template_name = "property/property_list.html"
        model = PropertyManagement
        #context_object_name = 'properties'
        

#class PropertyCreateView(CreateView): #create new records
        #template_name = "property/property_new.html"
        #model = PropertyManagement

        #def get_success_url(self) -> str:
                #return super().get_success_url()


        
        

#class PropertyUpdateView(UpdateView): #update current records
        #template_name = "property/property_update.html"
        #model = PropertyManagement
        #get the property
        # property = self.object
        # load related models
                

        #return redirect('property_detail')
                

class PropertyDetailView(DetailView): # read single, reads a single copy for read-only
        template_name = "property/property_detail.html"
        model = PropertyManagement

        def get_context_data(self, **kwargs):
                # get the context
                context = super().get_context_data(**kwargs)

                # get the property 
                property = self.object

                # load related models.
                finance = PropertyFinance.objects.filter(property=property).first()
                context["propertyfinance"] = finance

                tenant =  PropertyTenantInfo.objects.filter(property=property).first()
                context["propertytenantinfo"] = tenant

                maintenance = PropertyMaintenanceInfo.objects.filter(property=property).first()
                context["propertymaintenanceinfo"] = maintenance
                return context
        
        



        
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

        return redirect('property_list')



class PropertyUpdateDetailView(DetailView): # read single, reads a single copy for read-only
        template_name = "property/property_update.html"
        model = PropertyManagement

        def get_context_data(self, **kwargs):
                # get the context
                context = super().get_context_data(**kwargs)

                # get the property 
                property = self.object

                # load related models.
                finance = PropertyFinance.objects.filter(property=property).first()
                context["propertyfinance"] = finance

                tenant =  PropertyTenantInfo.objects.filter(property=property).first()
                context["propertytenantinfo"] = tenant

                maintenance = PropertyMaintenanceInfo.objects.filter(property=property).first()
                context["propertymaintenanceinfo"] = maintenance
                return context
        


def update_property(request):
        
        # get property
        property_id = request.POST.get('property_id')

        #get related data fields/models
        property = PropertyManagement.objects.get(id=property_id)
        property.property_name = request.POST.get('property_name')
        property.image = request.POST.get('image')
        property.address= request.POST.get('address')
        property.property_type= request.POST.get('property_type')
        property.number_of_units= request.POST.get('number_of_units')
        property.year_built= request.POST.get('year_built')
        property.square_footage= request.POST.get('square_footage')
        property.acquired_date= request.POST.get('acquired_date')

        #save the data
        property.save()

        #get related data fields/models
        finance = PropertyFinance.objects.filter(property=property).first()
        finance.purchase_price = request.POST.get('purchase_price')
        finance.market_value = request.POST.get('market_value')
        finance.monthly_rent = request.POST.get('monthly_rent')
        finance.operating_expenses = request.POST.get('operating_expenses')
        finance.mortgage_details = request.POST.get('mortgage_details')

        #save the data
        finance.save()

        #get related data fields/models
        tenant = PropertyTenantInfo.objects.filter(property=property).first()
        tenant.name = request.POST.get('name')
        tenant.lease_terms = request.POST.get('lease_terms')
        tenant.rent_payment_status =request.POST.get('rent_payment_status')

        #save the data
        tenant.save()
        

        #get related data fields/models
        maintenance = PropertyMaintenanceInfo.objects.filter(property=property).first()
        maintenance.scheduled_maintenance = request.POST.get('scheduled_maintenance')
        maintenance.vendor = request.POST.get('vendor')
        maintenance.cost = request.POST.get('cost')

        #save the data
        maintenance.save()

        # redirect user to deails page after update
        return redirect('property_detail')
