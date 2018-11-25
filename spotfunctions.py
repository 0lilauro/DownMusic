import requests
import bs4
import os
import base64
import json 

def GetSizeDataSpotify(auth,access,url,offset):
    newheader = {'Authorization':auth}
    newparams = {'offset':offset}
    r = requests.get(url, params=newparams,headers=newheader)
    response = r.json()
    return response['total']

def NormalizeAlbum(Album):
    normalized = Album.replace(".","")    
    normalized = normalized.replace("'","")       
    
    return normalized
def GetDataSpotify(auth,access,url,offset,data):
    newheader = {'Authorization':auth}
    newparams = {'offset':offset}
    r = requests.get(url, params=newparams,headers=newheader)
    print(r)
    response = r.json()
    for item in response['items']:
        artists = []
        img = "";
        for artist in item['track']['album']['artists']:
            art_line = {'name':artist['name']}
            artists.append(art_line)
        if len(item['track']['album']['images']) > 0:
            img = item['track']['album']['images'][0]['url']
        else:
            img = None
        line={
            'name':item['track']['name'],
            'album_name': NormalizeAlbum(item['track']['album']['name']),
            'album_img': img,
            'album_date': item['track']['album']['release_date'],
            'artist': artists
        }
        data.append(line)    

def WriteFile(data):
    with open("./files/data.json","w") as final:
        json.dump(data,final, sort_keys = True, indent = 4, ensure_ascii = False)

def WriteErrorJson():
    if os.path.exists("files/error.json"):
        os.remove("files/error.json")
    var = []
    with open("./files/error.json","w") as final:
        json.dump(var,final, sort_keys = True, indent = 4, ensure_ascii = False)