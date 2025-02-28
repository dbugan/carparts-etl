import http.client
import json
import os
import load_dotenv

load_dotenv()

conn = http.client.HTTPSConnection(os.getenv('X_RAPIDAPI_HOST'))    

headers = {
    'x-rapidapi-key': os.getenv(X_RAPIDAPI_KEY),
    'x-rapidapi-host': os.getenv(X_RAPIDAPI_HOST)
}

conn.request("GET", "/category/category-products-groups-variant-3/464/manufacturer-id/184/lang-id/4/country-filter-id/62/type-id/1", headers=headers)

res = conn.getresponse()
data = res.read()

json_data = json.loads(data)

with open('categories.json', 'w') as f:
    json.dump(json_data, f, indent=4)
    
