from django.shortcuts import render

# Create your views here.

def assets_view(request):
    return render(request, 'post/assets.html')