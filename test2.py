from datetime import datetime

class User:
  def __init__(self, name):
    self.name = name
    self.items = []

  def add_item(self, item):
    self.items.append(item)

class Item:
  def __init__(self, name='', picture='', description='', status='', amount=0, got_date=None):
    self.name = name
    self.picture = picture
    self.description = description
    self.status = status
    self.amount = amount
    if got_date is None:
      self.got_date = datetime.now()
    else:
      self.got_date = got_date

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

class ItemCreator:
  def create_item(self, name, picture, description, status, amount, got_date=None):
    item = Item(name, picture, description, status, amount, got_date)
    return item

class BadgeCreator:
  def create_badge(self, name, picture, description, status, got_date=None):
    badge = Badge(name, picture, description, status, got_date)
    return badge

class Factory:
  def __init__(self, product, user):
    self.product = product
    self.user = user

  def send_item(self, name, picture, description, status, amount, got_date=None):
    item_creator = ItemCreator()
    item = item_creator.create_item(name, picture, description, status, amount, got_date)
    self.user.add_item(item)


# create a user object
user = User("Paul")

# create a factory object
factory = Factory("ItongItem", user)

print(user.items)
# create an item using ItemCreator and send it to the user
factory.send_item("aa", "bb", "cc", "dd", 10)
print([item.name for item in user.items])