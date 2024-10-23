from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI
from flaskwebgui import FlaskUI, close_application


app = FastAPI()

# Mounting default static files
app.mount("/public", StaticFiles(directory="public/"))
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("some_page.html", {"request": request})


@app.get("/close")
async def close_server():
    close_application()


def start_fastapi(**kwargs):
    import uvicorn

    uvicorn.run(**kwargs)


if __name__ == "__main__":
    # Default start fastapi

    FlaskUI(
        app=app,
        server="fastapi",
        width=800,
        height=600,
        app_mode=False,
    ).run()

    # Default start fastapi with custom port

    # FlaskUI(
    #     server="fastapi",
    #     app=app,
    #     port=3000,
    #     width=800,
    #     height=600,
    # ).run()

    # Default start fastapi with custom kwargs

    # FlaskUI(
    #     server="fastapi",
    #     server_kwargs={
    #         "app": app,
    #         "port": 3000,
    #     },
    #     width=800,
    #     height=600,
    # ).run()

    # Custom start fastapi

    # def saybye():
    #     print("on_exit bye")

    # FlaskUI(
    #     server=start_fastapi,
    #     server_kwargs={
    #         "app": "main:app",
    #         "port": 3000,
    #     },
    #     width=800,
    #     height=600,
    #     on_shutdown=saybye,
    # ).run()
