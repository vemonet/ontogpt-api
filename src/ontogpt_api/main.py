from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from oaklib.utilities.apikey_manager import set_apikey_value
from src.ontogpt_api.config import settings
from src.ontogpt_api.opengpt import app as opengpt_router

set_apikey_value("openai", settings.OPENAI_APIKEY)
set_apikey_value("bioportal", settings.BIOPORTAL_APIKEY)

app = FastAPI(
    title="OntoGPT API",
    description="""API to extract informations from text using OntoGPT.

[Source code](https://github.com/vemonet/ontogpt-api)
""",
    license_info={"name": "MIT license", "url": "https://opensource.org/licenses/MIT"},
    contact={
        "name": "Vincent Emonet",
        "email": "vincent.emonet@gmail.com",
        "url": "https://github.com/vemonet/ontogpt-api",
    },
)
app.include_router(opengpt_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", include_in_schema=False)
def redirect_root_to_docs():
    """Redirect the route / to /docs"""
    return RedirectResponse(url="/docs")
