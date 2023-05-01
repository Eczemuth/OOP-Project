# import datetime


class Order:
    def __init__(self, product_list=None, date=None):
        # self.__id = id
        self.__products = product_list
        # self.__create_date = datetime.date.today()
        self.__paid_date = date
        self.__shipping_detail = {}
        self.__total_cost = 0

    def receive_shipping_detail(self, method, card_number, expiration_month, expiration_year, first_name, last_name,
                                billing_address1, billing_address2, country, city, postal_code, phone_number):
        self.__shipping_detail["method"] = method
        self.__shipping_detail["card_number"] = card_number
        self.__shipping_detail["expiration_month"] = expiration_month
        self.__shipping_detail["expiration_year"] = expiration_year
        self.__shipping_detail["first_name"] = first_name
        self.__shipping_detail["last_name"] = last_name
        self.__shipping_detail["billing_address1"] = billing_address1
        self.__shipping_detail["billing_address2"] = billing_address2
        self.__shipping_detail["country"] = country
        self.__shipping_detail["city"] = city
        self.__shipping_detail["postal_code"] = postal_code
        self.__shipping_detail["phone_number"] = phone_number

    def update_paid(self):
        self.__paid_date = datetime.date.today()

    def add_in_products(self, product):
        self.__products.append(product)

    def delete_in_products(self, product):
        self.__products.remove(product)

    def get_products(self):
        return self.__products

    def get_id(self):
        return self.__id

    def get_create_date(self):
        return self.__create_date

    def get_paid_date(self):
        return self.__paid_date

    def get_shipping_detail(self, key):
        return self.__shipping_detail[key] 
    
    def get_total_cost(self):
        return self.__total_cost
    
    def calculate_total_cost(self):
        temp_cost = 0
        for product in self.__products:
            temp_cost += product.get_price()
        self.__total_cost = temp_cost