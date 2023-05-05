from order import Order
from shoppingCart import ShoppingCart
from library import Library
from chat import Chat
from UserItem import Factory
from Product import Product
from Utilities import IdGenerator


import datetime


class User:
    def __init__(self, name,email , profile_picture=None, description=None, level=0):
        self.__name = name
        self.__id = IdGenerator.generate_id(name)
        self.__profile_picture = profile_picture
        self.__description = description
        self.__level = level
        self.__order = Order(self.__id)
        self.__cart = ShoppingCart(self.__id)
        self.__library = Library()
        self.__chats = {}
        self.__badge = []
        self.__item = []
        self.__wish_list = []

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    @property
    def profile_picture(self):
        return self.__profile_picture

    @profile_picture.setter
    def picture_profile(self, picture):
        self.__profile_picture = picture

    @property
    def description(self):
        return self.__description

    @property
    def level(self, level):
        self.__level = level

    def get_cart(self):
        return self.__cart

    def view_cart(self):
        return self.__cart.view_products()

    def add_products(self, product):
        self.__cart.add_products(product)
        return self.__cart

    def get_library(self):
        return self.__library

    def add_chat(self, chat):
        self.__chats[chat.get_id()] = chat

    def request_item(self, factory):
        factory.check_condition(self)

    def add_badge(self, badge):
        if badge != None:
            self.__badge.append(badge)
    
    def add_item(self, item):
        if item != None:
            self.__badge.append(item)
    
    def get_wish_list(self):
        return self.__wish_list
    
    def add_wish_list(self, product):
        self.__wish_list.append(product)