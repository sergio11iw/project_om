from django.shortcuts import render, redirect
from django.db.models import Count
from .models import Note
from .forms import UserModelForm

def main(request):
    notes = Note.objects.all()
    return render(request, 'main.html', {'notes': notes})

def produkts(request):
    notes = Note.objects.all()
    grop = request.GET.get('grop')
    sorter = request.GET.get('sorter')
    if grop:
        notes = notes.filter(name__istartswith=grop).values()
    if sorter:
        notes = notes.order_by(sorter).values()
    return render(request, 'produkts.html', {'notes': notes})

def produkt_list(request, list_id):
    list = Note.objects.get(id=list_id)
    if request.method == 'POST':
        list.save()
    return render(request, 'produkt_list.html', {'list': list})
def feedback(request):
    form = UserModelForm()
    print(form)
    if request.method == 'POST':
        form = UserModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')


    return render(request, 'main.html', {'form': form})




