from django.shortcuts import render

# Create your views here.


def index_page(request):
    return render(request, 'index.html')

def about_page(request):
     return render(request, 'about.html')

def contacts_page(request):
     return render(request, 'contacts.html')

def phones_page(request):
     return render(request, 'phones.html')