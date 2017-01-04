class ShoppingCart(object):
	def __init__(self):
		self.items = []
	def add(self, item, price):
		#if item already exist in car, increment
		for cart_item in self.items:
			if cart_item == item:
				cart_item.q += 1
				return self
		#if item does not exist in cart, add it
		self.items.append(Item(item,price))
		return self
	def item(self, index):
		return self.items[index-1].item
	def price(self, index):
		return self.items[index-1].price
	def total(self, sales_tax):
		sum_price = sum([item.price for item in self.items])
		return sum_price * (1.0 + sales_tax/100.0)
	def __len__(self):
		return len(self.items)

class Item(object):
	def __init__(self, item, price, q=1):
		self.item = item
		self.price = price
		self.q = q

