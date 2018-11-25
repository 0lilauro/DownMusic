import requests
import json

def SerachInYoutube(youtubeKEY,q):
    url = "https://www.googleapis.com/youtube/v3/search"
    querystring = {
        "part":"snippet",
        "q":q,
        "key": youtubeKEY
    }

    headers = {
        'cache-control': "no-cache",
    }

    response = requests.get(url, headers=headers, params=querystring)

    response = response.json()
    return response