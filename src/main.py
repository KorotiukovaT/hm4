from fastapi import FastAPI
from api import init_db_content

app = FastAPI()
app.include_router(init_db_content.router)
