from module.shoppingCart import ShoppingCart
from utilities import IdGenerator
from module.order import Order
from module.library import Library
from module.chat import Chat

class User:
    def __init__(self, name, email, profile_picture="https://www.tech101.in/wp-content/uploads/2018/07/blank-profile-picture.png", level=0):
        self.__name = name
        self.__email = email
        self.__id = IdGenerator.generate_id(email)
        self.__profile_picture = profile_picture
        self.__description = ""
        self.__level = level
        self.__order = Order(self.__id)
        self.__cart = ShoppingCart()
        self.__library = Library()
        self.__chats = Chat(User)
        self.__badge = []

    def __repr__(self):
        return self.__name

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_email(self):
        return self.__email

    def get_profile(self):
        return self.__profile_picture

    def get_level(self):
        return self.__level

    def get_description(self):
        return self.__description

    @property
    def profile_picture(self):
        return self.__profile_picture

    @profile_picture.setter
    def profile_picture(self, picture):
        self.__profile_picture = picture

    @property
    def description(self):
        return self.__description

    @property
    def level(self, level):
        self.__level = level

    def get_cart(self):
        return self.__cart.view_products()

    def view_cart(self):
        return self.__cart.view_products()

    def add_to_cart(self, products):
        self.__cart.add_products(products)
        return self.__cart

    def get_library(self):
        return self.__library

    # def add_chat(self, chat):
    #     self.__chats[chat.get_id()] = chat
    
    def get_chat(self):
        return self.__chats

    def request_item(self, factory):
        factory.check_condition(self)

    def add_badge(self, badge):
        if badge != None:
            self.__badge.append(badge)
