from django.shortcuts import render, HttpResponse, redirect
from .models import Client
from .forms import ClientForm
from loans.filters import EmpruntFiltre

# Create your views here.
def clients_list(request, pk):
    client = Client.objects.get(id=pk)
    emprunt = client.emprunt_set.all()
    total_emprunts = emprunt.count()
    myFilter = EmpruntFiltre(request.GET, queryset=emprunt)
    emprunt = myFilter.qs
    context = {
        'client': client,
        'emprunt': emprunt,
        'total_emprunts': total_emprunts,
        'myFilter': myFilter
    }
    return render(request, 'clients/clients_list.html', context)

def ajout_client(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'clients/ajout_client.html', context)

def modif_client(request, pk):
    client = Client.objects.get(id=pk)
    form = ClientForm(instance=client)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'clients/ajout_client.html', context)

def supp_client(request, pk):
    client = Client.objects.get(id=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('/')
    context = {
        'item': client
    }
    return render(request, 'clients/supp_client.html', context)
