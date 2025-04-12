import requests
import json

limit = 3
api_url = 'https://api.api-ninjas.com/v1/facts'.format(limit)
response = requests.get(api_url, headers={'X-Api-Key': 'your_api_key_here'})
if response.status_code == requests.codes.ok:
    string_result = response.text
    list1 = json.loads(string_result); 
    print(list1[0]["fact"])
else:
    print("Error:", response.status_code, response.text)