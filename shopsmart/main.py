class Product:
    inventory = []
    product_id = 1
    def __init__(self, product_id, name, category, quantity, price, supplier):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier
        Product.inventory.append(self)
        Product.product_id += 1


    @classmethod
    def add_product(cls, name, category, quantity, price, supplier):
        new_product = cls(cls.product_id, name, category, quantity, price, supplier)
        return "Product added successfully"

    @classmethod
    def update_product(cls, product_id, quantity=None, price=None, supplier=None):
        for product in cls.inventory:
            if product.product_id == product_id:
                if quantity:
                    product.quantity = quantity
                if price:
                    product.price = price
                if supplier:
                    product.supplier = supplier
                return "Product information updated successfully"
        return "Product not found"

    @classmethod
    def delete_product(cls, product_id):
        for product in cls.inventory:
            if product.product_id == product_id:
                cls.inventory.remove(product)
                return "Product deleted successfully"
        return "Product not found"

    @classmethod
    def get_product(cls, product_id):
        for product in cls.inventory:
            if product.product_id == product_id:
                return product
        return None



class Order:
    def __init__(self, order_id, products, customer_info=None):
        self.order_id = order_id
        self.products = products
        self.customer_info = customer_info

    def place_order(self, product_id, quantity, customer_info=None):
        product = Product.get_product(product_id)
        if not product:
            return "Product not found"
        if product.quantity < quantity:
            return "Insufficient quantity"
        product.quantity -= quantity
        self.products.append((product_id, quantity))
        self.customer_info = customer_info
        return f"Order placed successfully. Order ID: {self.order_id}"
