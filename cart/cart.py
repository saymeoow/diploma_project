from decimal import Decimal
from django.conf import settings
from onlinestore.models import Sneakers


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        sneakers_ids = self.cart.keys()
        sneakers = Sneakers.objects.filter(id__in=sneakers_ids)

        cart = self.cart.copy()
        for sneakers in sneakers:
            cart[str(sneakers.id)]['sneakers'] = sneakers

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, sneakers, quantity=1, update_quantity=False, sizes=1):
        sneakers_id = str(sneakers.id)
        if sneakers_id not in self.cart:
            self.cart[sneakers_id] = {'quantity': 0,
                                      'sizes': 0,
                                      'price': str(sneakers.price)}
        if update_quantity:
            self.cart[sneakers_id]['quantity'] = quantity
            self.cart[sneakers_id]['sizes'] = sizes
        else:
            self.cart[sneakers_id]['quantity'] += quantity
            self.cart[sneakers_id]['sizes'] = sizes

        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, sneakers):
        sneakers_id = str(sneakers.id)
        if sneakers_id in self.cart:
            del self.cart[sneakers_id]
            self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity']
                   for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
