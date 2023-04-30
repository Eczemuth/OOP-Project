import datetime

class Order:
    def __init__(self, product_list, date=None):
        self.__id = id
        self.__products = product_list
        self.__create_date = datetime.date.today()
        self.__paid_date = date

    def choose_method(system):
        return system.verify_payment()
    
    def update_paid(self):
        self.__paid_date = datetime.date.today()
        
    def update_products(self, product):
        self.__products.append(product)
        
    def get_products(self):
        return self.__products
    
    def get_id(self):
        return self.__id
    
    def get_create_date(self):
        return self.__create_date
    
    def get_paid_date(self):
        return self.__paid_date
        
    
