class ShoppingCart:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def get_products(self):
        return self.__products

    def view_in_cart(self):
        name_list = []
        for item in self.__products:
            name_list.append(item.get_name())
        return name_list

    def purchase_myself(self, product, price):
        pass

    def purchase_myfriend(self, product, user_id, price):
        pass

    def remove_all_product(self, product):
        self.__products = []

    def remove_product(self, product):
        self.__products.remove(product)

    def add_to_wishlist(self, product):
        pass
