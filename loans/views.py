from django.shortcuts import render, HttpResponse, redirect
from .forms import EmpruntForm
from .models import Emprunt

# Create your views here.
def loans_list(request):
    return render(request, 'loans/loans_list.html')

def ajout_emprunt(request):
    form = EmpruntForm()
    if request.method == 'POST':
        form = EmpruntForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'loans/ajout_emprunt.html', context)

def modif_emprunt(request, pk):
    emprunt = Emprunt.objects.get(id=pk)
    form = EmpruntForm(instance=emprunt)
    if request.method == 'POST':
        form = EmpruntForm(request.POST, instance=emprunt)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'loans/ajout_emprunt.html', context)

def supp_emprunt(request, pk):
    emprunt = Emprunt.objects.get(id=pk)
    if request.method == 'POST':
        emprunt.delete()
        return redirect('/')
    context = {
        'item': emprunt
    }
    return render(request, 'loans/supp_emprunt.html', context)
