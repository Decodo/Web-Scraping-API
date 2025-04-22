import requests

url = "https://scraper-api.decodo.com/v2/scrape"

payload = {
    "target": "universal",
    "parse": False,
    "url": "https://www.facebook.com/groups/1394454774138066"
}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Basic AUTH"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
