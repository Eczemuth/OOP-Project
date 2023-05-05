from datetime import datetime
from fastapi import FastAPI

from webSystem import System
from User import User
from Product import Product
app = FastAPI()

steen_system = System()

steen_system.register(user_name="Paul",email="dark97975@gmail.com",password1="12345Paul!",password2="12345Paul!")

steen_system.add_product({
            "name": "Mario",
            "price": 219,
            "os_support": "WINDOW-MACOS-LINUX",
            "system_req": "2.4GHz-NVIDIA1050",
            "tags": "KUECHIARAI",
            "cover_image": None,
            "lang_sup": "Thai-Bangladesh-English-Japanese",
            "ban_country": None,
            "exc_country": "Thailand",
            "age_rate": "20+",
            "discount": 0,
            "description": "This is not suit you",
            "release_date": datetime.now()
            })
steen_system.add_product({
            "name": "Dog",
            "price": 399,
            "os_support": "WINDOW-MACOS",
            "system_req": "3.2GHz-NVIDIA3050",
            "tags": "KUECHIARAI",
            "cover_image": None,
            "lang_sup": "English-Japanese",
            "ban_country": None,
            "exc_country": None,
            "age_rate": "5+",
            "discount": 0,
            "description": "Play this till the end of da day",
            "release_date": datetime.now()
            })


@app.get("/send_item")
async def request_item(product_name:str,user_id):
    product_instance = steen_system.search_product(search_name=product_name)[0]
    user_instance = steen_system.search_profile(search_name=user_id,search_id=None)[0]
    factory = Factory(product_instance, user_instance)
    status = factory.verify_condition()
    return status

class Item:
  def __init__(self, name, picture, description, amount, got_date):
    self.name = name
    self.picture = picture
    self.description = description
    self.amount = amount
    if got_date is None:
      self.got_date = datetime.now()
    else:
      self.got_date = got_date
    

item1 = Item("Slime Bunny", 'https://steamuserimages-a.akamaihd.net/ugc/170415821560894203/7FAC8319EA6E62FE667D9C86385E1695939986EF/', "cute slimy", 1,)
item2 = Item("Platinyan", 'https://steamuserimages-a.akamaihd.net/ugc/170415189367767268/B111AFFA6F311AC28DE69EE1A3B2BE6ED807D2FF/', "not platinum...", 5,)
item3 = Item("Kitten", 'https://steamuserimages-a.akamaihd.net/ugc/170415189369495447/6931908A7FEF2C14A5C4BC5DE4C9B96DC344FA4B/', "cute slimy", 1,)
item4 = Item("Singularity Sheep", 'https://steamuserimages-a.akamaihd.net/ugc/83722891606505516/E141B8530C583D134B96E675B6D8CB8FECF37FC7/', "les go galaxy", 3,)
item5 = Item("RIP", 'https://steamuserimages-a.akamaihd.net/ugc/170415189368228132/CF8BA7AE6AB983F74493F74488C2F3636539D1D9/', "You has died peacefully", 10,)
item6 = Item("Da King", 'https://steamuserimages-a.akamaihd.net/ugc/83721528723411114/4C3AE9EAD5F24AF3A48DAA3A7110EFFAD8B11872/', "Golden Crown", 1,)
item7 = Item("Sugar Rush!", 'https://steamuserimages-a.akamaihd.net/ugc/170415189368247427/45096CC689596C69818168804BE921E267C04247/', "Sweet", 60,)
item8 = Item("Golden Apple", 'https://steamuserimages-a.akamaihd.net/ugc/83722391142833651/BB950C023CC5535D1E4BF00C0F882B602DE1BA95/', "Effect: Regeneration", 1,)
item9 = Item("Holy Nuts!", 'https://steamuserimages-a.akamaihd.net/ugc/825693460684574511/97FEF8CBF732834FF9D761B69A2481550CB1C1C8/', "Shiny Nuts!", 3,)
item10 = Item("Crystal", 'https://steamuserimages-a.akamaihd.net/ugc/170415672419600768/EEF2D0600569B6CF21A23DBC7F1119DF40FD663D/', "Beautiful crystal", 7,)

class Badge:
  def __init__(self, name='', picture='', description='', status='', got_date=None):
    self.name = name
    self.picture = picture
    self.description = description
    self.status = status
    if got_date is None:
      self.got_date = datetime.now()
    else:
      self.got_date = got_date

class Factory:
  def __init__(self, product, user):
    self.product = product
    self.user = user
    self.item_creator = ItemCreator()
    self.badge_creator = BadgeCreator()


  def verify_condition(self, user):
    if self.user.get_level() > 99:
      self.send_item(item1)
      return "item sent"
    
    elif self.user.get_level() > 98:
      self.send_badge(item2)
      return "badge sent"
    
    elif self.user.get_level() > 97:
      self.send_badge(item3)
      return "badge sent"
    
    elif self.user.get_level() > 96:
      self.send_badge(item4)
      return "badge sent"
    
    elif self.user.get_level() > 95:
      self.send_badge(item5)
      return "badge sent"
    
    elif self.user.get_level() > 94:
      self.send_badge(item6)
      return "badge sent"
    
    elif self.user.get_level() > 93:
      self.send_badge(item7)
      return "badge sent"
    
    elif self.user.get_level() > 92:
      self.send_badge(item8)
      return "badge sent"
    
    elif self.user.get_level() > 91:
      self.send_badge(item9)
      return "badge sent"
    
    elif self.user.get_level() > 90:
      self.send_badge(item10)
      return "badge sent"


    return "nothing were sent"

  def send_item(self,item,user):
      user.add_item(item)

  def send_badge(self,item,user):
      user.add_badge(item)

class ItemCreator:
  def create_item(self, name, picture, description, status, amount, got_date=None):
    item = Item(name, picture, description, status, amount, got_date)
    return item

class BadgeCreator:
  def create_badge(self, name, picture, description, status, got_date=None):
    badge = Badge(name, picture, description, status, got_date)
    return badge