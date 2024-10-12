from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.views.generic import TemplateView
# Create your views here.


class HomePageView(TemplateView):
    template_name = "pages/home.html"

class ServicePageView(TemplateView):
    template_name = "pages/services.html"






def contact_view(request):
    if request.method == "POST":
        #send message
        

        form = ContactForm(request.POST) #to validate the information

        if form.is_valid():
            print("Sending")

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            email_message = f"Name: {name}\nEmail: {email}\nMessage:\n {message}"

            send_mail(
                "Email from: " + name,
                email_message,
                email,
                ["christina.nkya@sdgku.edu"]

            )

        else:
            print("Invalid Form")
    else:
        #display form
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})
