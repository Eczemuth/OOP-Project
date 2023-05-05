import datetime

from web_system import *
from community import *
from fastapi import Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from mocking_data import *
from module.product import Product
from module.publisher import Publisher
from module.productCatalog import ProductCatalog
from fastapi import  FastAPI, Response

app = FastAPI()
TEMPLATE = Jinja2Templates("HTML")

# ==== Init CSS ==== #
# don't forget this -> from fastapi.staticfiles import StaticFiles
css_folder = "Style"  # folder that contain your css file
css_path = "/" + css_folder  # MAJIK

app.mount(css_path, StaticFiles(directory=css_folder), name="Style")

# ==== System Init ==== #
community = Community()
product_catalog = ProductCatalog()

all_post = Board("all")
artwork = Board("artwork")
news = Board("news")
manual = Board("manual")

community.add_board(all_post, artwork, news, manual)
steam = System(product_catalog, community)

# ==== register ==== #
steam.register(user_name="Best", email="best@gmail.com"
               , password1="123Best!", password2="123Best!"
               ,register_as="user")
steam.register(user_name="Boss", email="boss@gmail.com"
               , password1="123Boss!", password2="123Boss!"
               ,register_as="user")
steam.register(user_name="Bass", email="bass@gmail.com"
               , password1="123Bass!", password2="123Bass!"
               ,register_as="user")
steam.register(user_name="Publ", email="publ@gmail.com"
               , password1="123Publ!", password2="123Publ!"
               ,register_as="publisher")

# ==== init product ==== #
for product_info in all_product_info:
    product = Product(product_info)
    steam.add_product(product)

post1 = Post(steam.get_current_user()
             ,"https://steamuserimages-a.akamaihd.net/ugc/2066632296410876700/2AFC974AEFE4A02515EF7245082FEB33A69809FA/?imw=512&&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false"
             ,"Garry Mod")

post2 = Post(steam.get_current_user()
             ,"https://steamuserimages-a.akamaihd.net/ugc/2050870124875593567/D308C2111B90D97E35DB21CA80106A14CA34F12D/?imw=512&&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false"
             ,"Phoenix")

all_post.add_post(post1)
all_post.add_post(post2)

@app.get("/",response_class=HTMLResponse)
async def index(request : Request):
    page_data = {"request" : request}

    recommend_product = steam.get_recommend_product()
    discount_product = steam.get_discount_product()

    page_data["discount_product"] = discount_product
    page_data["recommend_product"] = recommend_product
    page_data["user"] = steam.get_current_user()
    page_data["is_publisher"] = isinstance(steam.get_current_user(), Publisher)

    return TEMPLATE.TemplateResponse("index.html",page_data)

# about publisher
@app.get("/publisher", tags=["Publisher"], response_class=HTMLResponse)
async def publisher(request : Request):
    page_data = {"request":request}
    user = steam.get_current_user()

    page_data["user"] = user
    page_data["is_publisher"] = True
    if user:
        page_data["own_products"] = user.get_all_own_products()

    return TEMPLATE.TemplateResponse("view_own_product.html", page_data)

@app.get("/add_product", tags=["Publisher"], response_class=HTMLResponse)
async def add_product(request : Request):
    page_data = {"request":request}
    user = steam.get_current_user()

    page_data["user"] = user
    page_data["is_publisher"] = True
    page_data["product_info_keys"] = keys
    if user:
        page_data["own_products"] = user.get_all_own_products()

    return TEMPLATE.TemplateResponse("add_product.html", page_data)

@app.get("/add_product_to_catalog", tags=["Publisher"], response_class=HTMLResponse)
async def add_product(request : Request, name, price, os_support, system_req,
                      pre_vid, cover_image, lang_sup, age_rate, discount, description):
    page_data = {"request":request}
    user = steam.get_current_user()

    page_data["user"] = user
    page_data["is_publisher"] = True

    info = {"name":name, "price":int(price), "os_support":os_support, "system_req":system_req,
            "pre_vid":pre_vid, "cover_image":cover_image, "lang_sup":lang_sup,
            "age_rate":age_rate, "discount":float(discount), "description":description,
            "release_date":datetime.datetime.now()}

    product = Product(info)
    print("> ",product)
    steam.add_product(product)
    user.add_product(product)

    return TEMPLATE.TemplateResponse("add_product.html", page_data)

# about product
@app.get("/product/{product_id}", tags=["Product"], response_class=HTMLResponse)
async def view_product(request : Request, product_id):
    page_data = {"request" : request}
    product = steam.get_product(product_id)
    user = steam.get_current_user()
    is_publisher = isinstance(user,Publisher)
    addable = bool(user)
    if addable:
        if product in user.get_cart() or \
           product in user.get_library().get_all_products():
            addable = False

    page_data["product"] = product
    page_data["addable"] = addable
    page_data["user"] = user
    page_data["is_publisher"] = is_publisher

    return TEMPLATE.TemplateResponse("product.html",page_data)

@app.post("/product/{product_id}", tags=["Product"], response_class=HTMLResponse)
async def view_product(request : Request, product_id):
    product = steam.get_product(product_id)
    user = steam.get_current_user()
    is_publisher = isinstance(user,Publisher)
    addable = bool(user)
    if addable:
        if product in user.get_cart() or \
           product in user.get_library().get_all_products():
            addable = False

    page_data = {"request" : request, "product":product, "addable":addable, "user": user, "is_publisher": is_publisher}
    return TEMPLATE.TemplateResponse("product.html",page_data)

@app.get("/search_product/result", tags=["Product"], response_class=HTMLResponse)
async def search_product(request: Request, keyword=""):
    found_products = steam.search_product(search_name=keyword)
    print(found_products, keyword, type(keyword))
    page_data = {"request": request, "found_products": found_products, "kw": keyword}
    return TEMPLATE.TemplateResponse("search_product.html",page_data) # new front-end

@app.get("/cart/{user_id}", tags=["Cart"], response_class=HTMLResponse)
async def cart(request: Request, user_id):
    page_data = {"request": request}
    user = steam.search_profile(search_id=user_id)
    is_publisher = isinstance(user,Publisher)

    page_data["user"] = user
    page_data["is_publisher"] = is_publisher

    return TEMPLATE.TemplateResponse("cart.html", page_data) # new front-end

@app.post("/add_to_cart/{product_id}", tags=["Cart"])
async def add_to_cart(product_id):
    product = steam.get_product(product_id)
    user = steam.get_current_user()
    if user:
        steam.add_to_cart(product, user)
    url = app.url_path_for("view_product",product_id=product_id)
    return RedirectResponse(url=url)

# about profile
@app.get("/profile/{user_id}", tags=["User"], response_class=HTMLResponse)
async def view_profile(request : Request, user_id):
    page_data = {"request": request}
    user = steam.search_profile(search_id = user_id)
    is_publisher = isinstance(user,Publisher)

    page_data["user"] = user
    page_data["is_publisher"] = is_publisher

    return TEMPLATE.TemplateResponse("profile.html",page_data)

@app.get("/search_profile/result", tags=["Profile"], response_class=HTMLResponse)
async def search_profile(request: Request, keyword=""):
    page_data = {"request": request}
    found_user = steam.search_profile(search_name=keyword, search_id="")
    user = steam.get_current_user()
    is_publisher = isinstance(user,Publisher)
    page_data["found_user"] = found_user
    page_data["kw"] = keyword
    page_data["is_publisher"] = is_publisher
    return TEMPLATE.TemplateResponse("search_profile.html",page_data) # new front-end

# login register
@app.get("/login", tags=["System"], response_class=HTMLResponse)
async def login(request: Request, status = None):
    page_data = {"request": request}
    page_data["status"] = status
    return TEMPLATE.TemplateResponse("login.html",page_data) # new front-end

@app.get("/verify_login", tags=["System"], response_class=HTMLResponse)
async def verify_login(request: Request, email, password):
    status, user = steam.login(email=email, password=password)
    if status == LoginStatus.SUCCES:
        redirect_url = request.url_for("index")
        return RedirectResponse(redirect_url)
    else:
        redirect_url = request.url_for("login").include_query_params(status=status)
        return RedirectResponse(redirect_url)

@app.get("/logout", tags=["System"], response_class=HTMLResponse)
async def logout(request: Request):
    steam.logout()
    redirect_url = request.url_for("index")
    return RedirectResponse(redirect_url)

@app.get("/register", tags=["System"], response_class=HTMLResponse)
async def register(request : Request):
    page_data = {"request": request}
    return TEMPLATE.TemplateResponse("register.html",page_data) # new front-end

@app.get("/verify_register", tags=["System"], response_class=HTMLResponse)
async def verify_register(request: Request, register_as, user_name,email,password1,password2):
    status = steam.register(user_name=user_name, email=email, password1=password1, password2=password2,register_as=register_as)

    page_data = {"request": request}
    if status == RegistStatus.SUCCESS:
        # this is the same as index function maybe find some alt
        recommend_product = steam.get_recommend_product()
        discount_product = steam.get_discount_product()

        page_data["discount_product"] = discount_product
        page_data["recommend_product"] = recommend_product
        page_data["user"] = steam.get_current_user()

        return TEMPLATE.TemplateResponse("index.html", page_data)
        # end index function

    else:
        page_data["status"] = status
        return TEMPLATE.TemplateResponse("register.html", page_data) # new front-end

# ==================== Community Route ==================== #
@app.get("/community/{board_name}",tags=["Community"], response_class=HTMLResponse)
async def community(request: Request, board_name= "all"):
    page_data = {"request": request}
    user = steam.get_current_user()
    is_publisher = isinstance(user,Publisher)
    board = steam.get_board(board_name)

    page_data["board"] = board
    page_data["user"] = user
    page_data["is_publisher"] = is_publisher

    return TEMPLATE.TemplateResponse("community.html", page_data)

@app.get("/add_post",tags=["Community"], response_class=HTMLResponse)
async def add_post(request: Request):
    page_data = {"request": request}

    return TEMPLATE.TemplateResponse("add_post.html", page_data)

@app.get("/submit_post",tags=["Community"], response_class=HTMLResponse)
async def submit_post(request: Request, board_name, image, game_name):
    post = Post(steam.get_current_user(), image, game_name)
    board = steam.get_board(board_name)
    board.add_post(post)
    url = app.url_path_for("community",board_name=board_name)
    return RedirectResponse(url=url)

@app.get("/rate_up/{board_name}/{post_id}",tags=["Community"], response_class=HTMLResponse)
async def rate_up(board_name, post_id):
    user = steam.get_current_user()
    board = steam.get_board(board_name)
    post = board.get_post(post_id)
    if post and user:post.rate_up(user)
    url = app.url_path_for("community",board_name=board_name)
    return RedirectResponse(url=url)



