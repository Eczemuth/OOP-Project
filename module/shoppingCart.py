class ShoppingCart:
    def __init__(self):
        self.__cart_id = ""
        self.__products = []
        
    def purchase_myself(self,product,price):
        pass

    def purchase_myfriend(self,product,user_id,price):
        pass

    def remove_all_product(self,product):
        pass

    def remove_product(self,product):
        pass

    def add_to_wishlist(self,product):
        pass

    def add_products(self, products):
        if products not in self.__products:
            self.__products.append(products)

    def view_products(self):
        return self.__products