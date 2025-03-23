from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Count, Q
from .models import Note, User, ShopUser
from .forms import UserModelForm
from django.contrib import messages
from django.http import Http404, JsonResponse

def main(request):
    notes = Note.objects.all()
    return render(request, 'main.html', {'notes': notes})
def contacts(request):
    return render(request, 'contacts.html',)
def produkts(request):
    notes = Note.objects.all()
    page_number = request.GET.get('page', 1)
    grop = request.GET.get('grop')
    sorter = request.GET.get('sorter')
    if grop:
        notes = notes.filter(name__istartswith=grop).values()
    if sorter:
        notes = notes.order_by(sorter).values()
    paginator = Paginator(notes, 6)
    page_obj = paginator.get_page(page_number)
    return render(request, 'produkts.html', {'notes': notes, 'page_obj': page_obj, 'grop': grop, 'sorter': sorter})

def produkt_search(request):
    text = request.GET.get('text', '').strip()
    # Поиск с учетом регистра
    produkts_case_sensitive = Note.objects.filter(Q(name__contains=text) | Q(descr__contains=text))
    # Поиск без учета регистра
    produkts_case_insensitive = Note.objects.filter(Q(name__icontains=text) | Q(descr__icontains=text))
    # Объединяем результаты
    produkts = produkts_case_sensitive | produkts_case_insensitive
    # Пагинация
    paginator = Paginator(produkts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'produkt_search.html', { 'page_obj': page_obj, 'text': text})

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
# def create_order(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         tel = request.POST.get('tel')
#         email = request.POST.get('email')
#         other = request.POST.get('other')
#         order = ShopUser(name=name, tel=tel, email=email, other=other)
#         order.save()
#         return JsonResponse({'success': True})
#     return JsonResponse({'success': False, 'error': 'Неверный метод запроса'})