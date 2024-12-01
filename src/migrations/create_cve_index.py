import os
from dotenv import load_dotenv
from elasticsearch import Elasticsearch

def create_cve_index():
    es_url = os.getenv("ES_URL")
    es_token = os.getenv("ES_TOKEN")
    
    if not (es_url and es_token):
        print("No provided Elasticsearch URL and Token!")

    client = Elasticsearch(es_url, api_key = es_token)
    response = client.indices.create(index = "cve")

    if response.meta.status == 200:
        print("Success")
    else:
        print("Creation Failed")

if __name__ == "__main__":
    load_dotenv()
    create_cve_index()