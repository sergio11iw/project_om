from django.conf import settings
from .models import Note

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, note: Note, quantity=1):
        note_id = str(note.id)
        if note_id not in self.cart:
            self.cart[note_id] = {'quantity': 0, 'price': str(note.price)}  # Сохраняем цену как строку
        self.cart[note_id]['quantity'] += quantity
        self.save()

    def remove(self, note: Note):
        note_id = str(note.id)
        if note_id in self.cart:
            del self.cart[note_id]
            self.save()

    def __iter__(self):
        note_ids = self.cart.keys()
        notes = Note.objects.filter(id__in=note_ids)
        for note in notes:
            self.cart[str(note.id)]['note'] = note
        for item in self.cart.values():
            item['total_price'] = int(item['price']) * item['quantity']  # Убедитесь, что price - это число
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(int(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session['cart']
        self.save()

    def save(self):
        self.session.modified = True

    def count(self):
        return sum(item['quantity'] for item in self.cart.values())