from django.shortcuts import render, HttpResponse
from loans.models import Emprunt
from clients.models import Client

# Create your views here.
def home(request):
    emprunts = Emprunt.objects.all()
    clients = Client.objects.all()
    context = {
        'emprunts': emprunts,
        'clients': clients
    }
    return render(request, 'books/index.html', context=context)

def books_list(request):
    return render(request, 'books/books_list.html')
