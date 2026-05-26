import requests

api = "https://api.inaturalist.org/v2/observations"

params = {
    "taxon_name": "Coleoptera",
    "quality_grade": "research",
    "per_page": 5,
    "fields": "photos.url"
}

response = requests.get(api, params=params)

data = response.json()

for obs in data["results"]:
    photo = obs["photos"][0]["url"]
    photo = photo.replace("square", "small")
    print(photo)

