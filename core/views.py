from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Count, Q
from .models import Note, User, ShopUser, Order, OrderItem
from .forms import UserModelForm
from django.contrib import messages
import json
from .cart import Cart
from django.http import JsonResponse
def main(request):
    notes = Note.objects.all()
    return render(request, 'main.html', {'notes': notes})
def contacts(request):
    return render(request, 'contacts.html')
def adminus(request):
    shopUser = ShopUser.objects.all()
    user = User.objects.all()
    orders = Order.objects.all()
    return render(request, 'adminus.html', {'shopUser': shopUser, 'user': user, 'orders': orders})


def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    total_items_price = sum(item.total_price for item in order.items.all())
    return render(request, 'order_detail.html', {
        'order': order,
        'total_items_price': total_items_price
    })
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
        product_name = request.POST.get('product_name')
        product_color = request.POST.get('product_color')
        product_count = request.POST.get('product_count')
        product_total = request.POST.get('product_total')
        print(
            f"Name: {name}, Tel: {tel}, Email: {email}, Product Name: {product_name}, Product Color: {product_color}, Product Count: {product_count}, Product Total: {product_total}")
        if not product_name or not product_color or not product_count or not product_total:
            messages.error(request, 'Пожалуйста, заполните все поля для товара.')
            return redirect('create_order')  # Вернуться на страницу с формой
        order = ShopUser (
            name=name,
            tel=tel,
            email=email,
            product_name=product_name,
            product_color=product_color,
            product_count=product_count,
            product_total=product_total
        )
        order.save()  # Сохраняем заказ в базе данных
        messages.success(request, 'Ваш заказ принят, мы свяжемся с вами в ближайшее время!')
        return redirect('main')
    return render(request, 'produkts.html')


def view_cart(request):
    # del request.session['cart']
    cart = Cart(request)
    total_price = cart.get_total_price()  # Получаем общую сумму


    return render(request, 'cart.html', {
        'cart': cart,
        'total_price': total_price,  # Передаем общую сумму в контекст
    })

def add_to_cart(request, note_id):
    note = get_object_or_404(Note, id=note_id)  # Получаем товар по его ID
    cart = Cart(request)  # Получаем объект корзины

    if request.method == 'POST':
        data = json.loads(request.body)  # Получаем данные из запроса
        quantity = data.get('quantity', 1)  # Получаем количество из данных
        color = data.get('color')  # Получаем цвет из данных
        cart.add(note, quantity, color)  # Добавляем товар в корзину
        return JsonResponse({'message': 'Товар добавлен в корзину!'})

    return JsonResponse({'message': 'Ошибка при добавлении товара.'}, status=400)


def remove_from_cart(request, note_id):
    cart = Cart(request)
    note = get_object_or_404(Note, id=note_id)

    color = request.POST.get('color')
    if color:
        cart.remove(note, color)

    # Перенаправление обратно в корзину
    return redirect('cart_view')  # Убедитесь, что это имя совпадает с именем в urls.py

def update_cart(request, note_id):
    """Обновляет количество товара в корзине."""
    cart = Cart(request)  # Получаем объект корзины
    note = get_object_or_404(Note, id=note_id)  # Получаем товар по его ID

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))  # Получаем новое количество из формы
        color = request.POST.get('color')  # Получаем цвет из формы
        if color:
            cart.add(note, quantity)  # Обновляем количество товара
        return redirect('cart_view')  # Перенаправляем на страницу корзины

    return JsonResponse({'message': 'Ошибка при обновлении товара.'}, status=400)
def cart_count(request):
    cart = Cart(request)
    return JsonResponse({'count': len(cart)})

def create_order_cart(request):
    if request.method == 'POST':
        cart = Cart(request)
        total_price = cart.get_total_price()

        # Создаем новый заказ
        order = Order(
            name=request.POST['name'],
            tel=request.POST['tel'],
            email=request.POST['email'],
            total_price=total_price
        )
        order.save()

        # Сохраняем товары в заказе
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product_id=item['product_id'],  # Убедитесь, что вы используете правильный ключ
                quantity=item['quantity'],
                price=item['price']
            )

        cart.clear()  # Очистка корзины
        return redirect('order_success')
def order_success_view(request):
    return render(request, 'order_success.html')