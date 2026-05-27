import requests

api = "https://api.inaturalist.org/v2/observations"

params = {
    "taxon_id": 47208,
    "quality_grade": "research",
    "per_page": 10,
    "fields": "photos.url"
}

response = requests.get(api, params=params)

data = response.json()

amount = 1
for obs in data["results"]:
    print(f"Entry {amount}:")
    for photo in obs["photos"]:
        photo = photo["url"].replace("square", "large")
        print(photo)
    amount += 1