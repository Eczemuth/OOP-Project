from Order import *
from shoppingCart import *
from Library import *
from utilities import IdGenerator
from Group import *

class User:
    def __init__(self, name, email, profile_picture="https://cdn.akamai.steamstatic.com/steamcommunity/public/images/items/650330/658d7a42b02f59a94b0ea2a97ee46b4323b66c78.gif"
                 , description=None, level=0):
        self.__name = name
        self.__email = email
        self.__id = IdGenerator.generate_id(email)
        self.__profile_picture = profile_picture
        self.__description = description
        self.__level = level
        self.__order = Order(self.__id)
        self.__cart = ShoppingCart()
        self.__library = Library()
        self.__groups = []

    def __repr__(self):
        return self.__name

    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id

    def get_cart(self):
        return self.__cart.view_cart()

    def view_cart(self):
        return self.__cart.view_products()
    
    def add_to_cart(self, product):
        self.__cart.add_product(product)

    def get_library(self):
        return self.__library

    def create_group(self):
        new_group = Group()

    def get_profile_pic(self):
        return self.__profile_picture

    @property
    def profile_picture(self):
        return self.__profile_picture

    @profile_picture.setter
    def picture_profile(self, picture):
        self.__profile_picture = picture

    @property
    def description(self):
        return self.__description

    def add_product(self, product):
        self.__cart.add_product(product)
        return self.__cart

    # def add_chat(self, chat):
    #     self.__chats[chat.get_id()] = chat

    def get_chat(self):
        return self.__chats

    def request_item(self, factory):
        factory.check_condition(self)

    def add_badge(self, badge):
        if badge != None:
            self.__badge.append(badge)
