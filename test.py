from elasticsearch import Elasticsearch

ELASTIC_API = (
    "https://81f06459a705497786d367f6b9a93465."
    "us-central1.gcp.cloud.es.io:443")

API_KEY = (
    "RVR3YWc1TUIwMHFjdS1UYmFCS0Q6R"
    "215NThIcVJSVlNRV2ExUHRRV0hWZw")


ES_INDEX = "my_index_1"

client = Elasticsearch(
    ELASTIC_API,
    api_key = API_KEY,
)


# response = client.indices.create(index="my_index_1")

# response = client.create(index="my_index_1", id = "test_doc", body = {"name": "test"})

response = client.get(index = ES_INDEX, id = "test_doc" )

print(response)