from fastapi import FastAPI, Request, HTTPException, Response
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from webSystem import *
from MockingData import *

css_folder = "Style"
css_path = "/" + css_folder
app = FastAPI()

app.mount(css_path, StaticFiles(directory=css_folder), name=css_folder)

TEMPLATE = Jinja2Templates("HTML")


@app.get("/library/{User}", response_class=HTMLResponse)
async def library(User, request: Request):
    data = {"request": request}
    user = steen_system.search_profile(
        search_name=None, search_id=IdGenerator.generate_id(User))[0]
    data['library'] = user.get_library().get_products()
    return TEMPLATE.TemplateResponse("library.html", data)

steen_system = System()
steen_system.register(user_name="Bob", email="dark97975@gmail.com",
                      password1="123Paul!", password2="123Paul!")
steen_system.register(user_name="pop", email="dark97976@gmail.com",
                      password1="123Paul!", password2="123Paul!")
steen_system.register(user_name="Big", email="dark979757@gmail.com",
                      password1="123Paul!", password2="123Paul!")
steen_system.add_product(dota_2)
steen_system.add_product(let_build_a_zoo)
steen_system.add_product(tribes_of_midgard)
# steen_system.get_user_by_id(IdGenerator.generate_id("Bob")).get_library().add_product(dota_2)
# steen_system.get_user_by_id(IdGenerator.generate_id("Bob")).get_library().add_product(let_build_a_zoo)
# steen_system.get_user_by_id(IdGenerator.generate_id("Bob")).get_library().add_product(tribes_of_midgard)


@app.get("/catalog", tags=["Catalog"])
async def get_catalog():
    print(steen_system.get_products_name())
    return steen_system.get_products_name()


@app.put("/library/{user}/add", tags=["Library"])
async def add_product_to_library(product, user):
    item = steen_system.search_product(product)[0]
    library = steen_system.get_user_by_id(
        IdGenerator.generate_id(user)).get_library()
    if item.get_name() not in [i.get_name() for i in library.get_products()]:
        library.add_product(item.get_info())
    return {f"{product}": f"added to {user}'s library"}


@app.get("/chat", tags=["Chat"], response_class=HTMLResponse)
async def chat(request: Request):
    data = {"request": request}
    return TEMPLATE.TemplateResponse("chat.html", data)


@app.get("/chat/{target}", tags=["Chat"])
async def view_chat(User, Target):
    user = steen_system.search_profile(
        search_name=None, search_id=IdGenerator.generate_id(User))[0]
    target = steen_system.search_profile(
        search_name=None, search_id=IdGenerator.generate_id(Target))[0]
    return user.get_chat().view_message(target)


@app.put("/chat/{target}", tags=["Chat"])
async def chat_with(User, Target, message: str):
    user = steen_system.search_profile(
        search_name=None, search_id=IdGenerator.generate_id(User))[0]
    target = steen_system.search_profile(
        search_name=None, search_id=IdGenerator.generate_id(Target))[0]
    user.get_chat().send_message(message, target)
    print(user.get_chat().get_message_box())
    print(target.get_chat().get_message_box())
    return {"message": "sent"}


@app.get("/{User}/all-chat", tags=["Chat"])
async def all_chat(User):
    user = steen_system.search_profile(
        search_name=None, search_id=IdGenerator.generate_id(User))[0]
    print(user.get_chat().get_message_box())
    return {"value": user.get_chat().get_message_box()}


@app.post("/", tags=["Cart"])
async def add_product_to_cart(User, Product):
    user = steen_system.search_profile(
        search_name=None, search_id=IdGenerator.generate_id(User))[0]
    product = steen_system.search_product(Product)[0]
    if product in user.get_cart().get_products():
        return {"status": "product already added"}

    user.get_cart().add_product(product)
    return {"status": f"{[product.get_name()]} added to cart"}


@app.get("/", tags=["Cart"])
async def view_cart(User):
    user = steen_system.search_profile(
        search_name=None, search_id=IdGenerator.generate_id(User))[0]
    return {"cart": user.get_cart().view_in_cart()}
