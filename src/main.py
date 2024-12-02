from fastapi import FastAPI
from api import about_author, get_cve


app = FastAPI()
app.include_router(about_author.router)
app.include_router(get_cve.router)