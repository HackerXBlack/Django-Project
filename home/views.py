from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.shortcuts import redirect
from django.shortcuts import render


def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def external_link(request):
    # Define the URL of the external website
    external_url = "https://www.nike.com/in/"

    # Redirect the user to the external website
    return redirect(external_url)

def my_view(request):
    # Your view logic here
    return render(request, 'index.html')


# Create your views here.
def index(request):
    context = {
        'variable': "hello guys"
    }
    return render(request, 'index.html', context)

def about(request): 
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html') 

def saveForm(request):
    if request.method=="POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name = name, phone = phone, email = email, desc = desc, date = datetime.today())
        contact.save()
    return render(request, 'contact.html')

def search(request):
    return render(request, 'search.html')

