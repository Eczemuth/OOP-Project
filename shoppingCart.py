from utilities import IdGenerator

class ShoppingCart:
    def __init__(self):
        self.__cart_id = IdGenerator.generate_id(id(self))
        self.__products = []
        
    def purchase_myself(self,product,price):
        pass

    def purchase_myfriend(self,product,user_id,price):
        pass
    
    def remove_all_product(self):
        self.__products = []

    def remove_product(self,to_remove_product):
        prod_dup = []
        for product in self.__products:
            if product not in to_remove_product:
                prod_dup.append(product)

        self.__products = prod_dup

    def add_to_wishlist(self,product):
        pass

    def add_product(self, product):
        self.__products.append(product)

    def view_cart(self):
        return self.__products
