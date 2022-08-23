import requests


response = requests.get("https://deploy.heumtax.com/deployment/")
print(response.json())
