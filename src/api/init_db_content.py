import os
import requests
from fastapi import APIRouter
from dotenv import load_dotenv

router = APIRouter(tags = ["Init Endpoints"])

@router.get("/init-db-content")
def text_init_db_content():
    load_dotenv()
    url = "https://api.cvesearch.com/search?q=CVE-2019-0708"
    headers = { "X-Api-Key": os.getenv("CVE_API_TOKEN") }

    response = requests.request("GET", os.getenv("CVE_API_URL"), headers = headers)


    return response
