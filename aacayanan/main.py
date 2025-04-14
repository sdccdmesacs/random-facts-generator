import requests

url = "https://catfact.ninja/fact"

try:
    response = requests.get(url)
    cat_fact = response.json()["fact"]
    print(cat_fact)
except Exception as e:
    print(f"Error {response.status_code}. {response.json()["message"]}.")