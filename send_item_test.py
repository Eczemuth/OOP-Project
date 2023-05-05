class Factory:
  def __init__(self, user, product):
    self.__product = product
    self.__user = user

  def create_item(self, name, picture, got_date, description, status):
    item = {'name ': name, 'picture': picture, 'got_date':got_date, 'description': description, 'status' : status}
    return item

  def send_item(self, name, picture, got_date, description, status):
    item = self.create_item(name, picture, got_date, description, status)
    self.__user.add_item(item)

  

class User:
    def __init__(self):
       self.items = []
    
    def add_item(self, item):
       self.items.append(item)
  

# Create an instance of user
user = User()

# Create an instance of factory
factory = Factory(user, 'product')

print(user.items)
factory.send_item('paul', '02205150', '1/1/2023', 'someItemHere', 'status')
print(user.items)