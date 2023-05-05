
class Product:
    def __init__(self, info):
            self.__info = {
            "name": info["name"],
            "price": info["price"],
            "os_support": info["os_support"],
            "system_req": info["system_req"],
            "tags": info["tags"],
            "cover_image": info["cover_image"],
            "lang_sup": info["lang_sup"],
            "ban_country": info["ban_country"],
            "exc_country": info["exc_country"],
            "age_rate": info["age_rate"],
            "discount": info["discount"],
            "description": info["description"],
            "release_date": info["release_date"]
            }

    def __repr__(self):
        return self.__info["name"]

    def get_info(self):
        return self.__info

    def get_name(self):
        return self.__info['name']

    def get_price(self):
        return self.__info['price']
    
    def get_id(self):
        return self.__info['id']
    
    def change_info(self,new_info):
        for key in new_info:
            if new_info[key] != None:
                self.__info[key] = new_info[key]