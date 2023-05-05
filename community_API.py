from fastapi import FastAPI,Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app3 = FastAPI()
TEMPLATE = Jinja2Templates("HTML_page")

# css_folder = "Style"  # folder that contain your css file
# css_path = "/" + css_folder  # MAJIK

# app.mount(css_path, StaticFiles(directory=css_folder), name=css_folder)

@app3.get("/community", response_class=HTMLResponse)
async def view_community(request: Request):

     post_list = ['terraria', 'monster hunter', 'GTA V', 'Sekiro']
     data_for_page = {"request" : request, "post" : post_list}

     return TEMPLATE.TemplateResponse("community.html",data_for_page)