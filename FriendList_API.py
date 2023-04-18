from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI , Request
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# css_folder = "Style"  # folder that contain your css file
# css_path = "/" + css_folder  # MAJIK
# app.mount(css_path, StaticFiles(directory=css_folder), name=css_folder)

TEMPLATE = Jinja2Templates("html")

@app.get("/FriendList", response_class=HTMLResponse)
async def friendList(request: Request):
    data_for_page = {"request" : request}
    return TEMPLATE.TemplateResponse("FriendList.html",data_for_page)
