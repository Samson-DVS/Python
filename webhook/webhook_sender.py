import requests
import json
url = "http://127.0.0.1:5000/webhook"
data = {
   "hash_id" : 105850112915039,
   "user_id" : "samson",
}
r = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})