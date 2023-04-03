import hashlib
import re
from User import *
from fuzzywuzzy import process
from enum import Enum


class LoginStatus(Enum):
    EMAILNOTFOUND = False
    PASSNOTCORRECT = False
    NOPROBLEM = True

class UserStatus(Enum):
    GUEST = 0
    LOGEDIN = 1
    PUBLISHER = 2

class RegistStatus(Enum):
    EMAILALREADYEXIST = False
    PASSNOTMATCH = False
    PASSNOTSECURE = False
    PASSAVAILABLE = True

class IdGenerator:
    @staticmethod
    def generate_id(username):
        user_id = hashlib.md5(username.encode()).hexdigest()
        return user_id

class System:
    def __init__(self):
        self.__boards = []
        self.__product_catalog = {}
        self.__user_account = {}  # email:password
        self.__user_by_id = {}
        self.__user_by_name = {}
        self.__current_user_status = UserStatus.GUEST

    def add_product(self,product):
        self.__product_catalog[product.get_name()] = product

    def add_user(self,user):
        self.__user_by_name[user.get_name()] = user
        self.__user_by_id[user.get_id()] = user

    def verify_payment(self):
        return True

    def register(self,**kwargs):
        # kwargs have to have these fixed argument
        email = kwargs["email"]
        pass1 = kwargs["password1"]
        pass2 = kwargs["password2"]
        user_name = kwargs["user_name"]

        if email in self.__user_account:
            print("Email already exist")
            return RegistStatus.EMAILALREADYEXIST

        pass_status = self.password_available(pass1,pass2)
        if pass_status == RegistStatus.PASSNOTMATCH:
            print("Password not match")
            return RegistStatus.PASSNOTMATCH
        elif pass_status == RegistStatus.PASSNOTSECURE:
            print("Password not secure must contain 1 lowercase, 1 uppercase, 1 number, 1 special character")
            return RegistStatus.PASSNOTSECURE

        self.__user_account[email] = pass1

        # this will add user to self.user
        user = User(user_name,pass1)
        self.add_user(user)
        self.__current_user_status = UserStatus.LOGEDIN
        print("Register success")
        return True

    def login(self,email,password):
        if email not in self.__user_account:
            print("Email not found")
            return LoginStatus.EMAILNOTFOUND
        elif password != self.__user_account[email]:
            print("Password incorrect")
            return LoginStatus.PASSNOTCORRECT

        print("Login succes")
        self.__current_user_status = UserStatus.LOGEDIN
        return LoginStatus.NOPROBLEM

    def password_available(self,pass1,pass2):
        # use regex to check password
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
        if pass1 != pass2:
            return RegistStatus.PASSNOTMATCH
        elif not re.match(reg, pass1):
            return RegistStatus.PASSNOTSECURE
        return RegistStatus.PASSAVAILABLE

    def search_profile(self,**kwargs):
        # get id and name that user want to search
        search_id = kwargs["search_id"]
        search_name = kwargs["search_name"]

        if search_id:  # if there is id to search
            try:
                return [self.__user_by_id[search_id]]
            except KeyError:
                return []
        elif search_name:  # if there is name to search
            # the extract return tuple -> (str,similarity)
            found_user_name = process.extract(search_name, self.__user_by_name.keys())
            # keep the user that have similarity 55 percent or more
            found_user = [self.__user_by_name[user[0]] for user in found_user_name if user[1] >= 55]
            # if there occur some user
            if found_user:
                return found_user
        # if there are no id or name to search
        return []

    def search_product(self,search_name=""):
        if search_name != "":
            found_product_name = process.extract(search_name, self.__product_catalog.keys())
            found_product = [self.__product_catalog[product[0]] for product in found_product_name if product[1] > 55]

            if found_product:
                return found_product
        return []

    def view_profile(self,user_id):
        return self.__user_by_id[user_id].get_info()

    def view_product(self,prood_id):
        return self.__product_catalog[prood_id].get_info()

    def change_info(self,new_info):
        self.__product_catalog[new_info["name"]].change_info(new_info)