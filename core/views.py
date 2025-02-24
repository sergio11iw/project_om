from django.shortcuts import render, redirect
from django.db.models import Count
from .models import Note, User, ShopUser
from .forms import UserModelForm
from django.contrib import messages

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
    if request.method == 'POST':
        form = UserModelForm(request.POST)
        if form.is_valid():
            form.save()
            print("Данные успешно сохранены")
            messages.success(request, 'Данные получены, мы свяжемся с вами в ближайшее время!')
            return redirect('main')
        else:
            print("Форма не валидна:", form.errors)
    else:
        form = UserModelForm()
    return render(request, 'main.html',{'form': form})
def create_order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        tel = request.POST.get('tel')
        email = request.POST.get('email')
        other = request.POST.get('other')

        order = ShopUser(name=name, tel=tel, email=email, other=other)
        order.save()  # Сохраняем заказ в базе данных

        messages.success(request, 'Ваш заказ принят, мы свяжемся с вами в ближайшее время!')
        return redirect('main')

    return render(request, 'main')
