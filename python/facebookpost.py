import requests

url = "https://scraper-api.decodo.com/v2/scrape"

payload = {
    "target": "universal",
    "parse": False,
    "headless": "html",
    "url": "https://www.facebook.com/zuck/posts/pfbid0HeY54v4LMcv2EMxDz5RvnWaR6swsGFWikzUbrsEFtvxu9n4GCx7zA2YTM69XdiYnl"
}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Basic AUTH"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
