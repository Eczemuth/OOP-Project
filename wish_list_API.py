# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
#
# css_folder = "Style"  # folder that contain your css file
# css_path = "/" + css_folder  # MAJIK
#
# app.mount(css_path, StaticFiles(directory=css_folder), name=css_folder)

# @app.get("/cart", responses_class=HTMLResponse)
# async def view_cart(request: Request):
#
#     data_for_page = {"request" : request}
#
#     return TEMPLATE.TemplateResponse("cart.html",data_for_page)
from webSystem import System
from fastapi import FastAPI,Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from User import User

app2 = FastAPI()
TEMPLATE = Jinja2Templates("HTML_page")

# css_folder = "Style"  # folder that contain your css file
# css_path = "/" + css_folder  # MAJIK

# app.mount(css_path, StaticFiles(directory=css_folder), name=css_folder)

steen_system = System()
steen_system.register(user_name="Best",email="dark97975@gmail.com",password1="123Paul!",password2="123Paul!")

print()

@app2.get("/wish_list/{UserID}", response_class=HTMLResponse)
async def search_wish(request: Request, UserID):
     user = steen_system.search_profile(search_id=UserID,search_name=None)[0]
     user_wish_list = user.get_wish_list()
     data_for_page = {"request" : request, "user_wish_list" : user_wish_list}
     
     return TEMPLATE.TemplateResponse("wish_list.html",data_for_page)