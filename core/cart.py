from .models import Note

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, note, quantity=1, color=None):
        note_id = str(note.id)
        color = color or str(note.color1)  # Получаем цвет товара, если он не передан

        # Создаем уникальный ключ для товара, включая цвет
        unique_key = f"{note_id}_{color}"

        if unique_key not in self.cart:
            # Если товара нет в корзине, добавляем его
            self.cart[unique_key] = {
                'quantity': 0,
                'price': str(note.price),
                'color': color,  # Сохраняем цвет товара
                'name': str(note.name)  # Сохраняем имя товара
            }

        # Увеличиваем количество для данного уникального ключа
        self.cart[unique_key]['quantity'] += quantity
        self.save()

    def remove(self, note: Note, color: str):
        note_id = str(note.id)
        unique_key = f"{note_id}_{color}"  # Создаем уникальный ключ для удаления
        if unique_key in self.cart:
            del self.cart[unique_key]
            self.save()


    def __iter__(self):
        note_ids = self.cart.keys()
        notes = Note.objects.filter(id__in=[key.split('_')[0] for key in note_ids])  # Получаем только уникальные ID
        for note in notes:
            for key in note_ids:
                if key.startswith(str(note.id)):
                    self.cart[key]['note'] = note
        for item in self.cart.values():
            item['total_price'] = int(item['price']) * item['quantity']  # Убедитесь, что price - это число
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(int(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # Очищаем корзину
        del self.session['cart']
        self.session.modified = True

    def save(self):
        self.session.modified = True

    def count(self):
        return sum(item['quantity'] for item in self.cart.values())
