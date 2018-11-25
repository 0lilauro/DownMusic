# pip install bs4 base64 youtube_dl eyeD3

import requests
import bs4
import base64
import json 
import os
import shutil
import spotfunctions as spotify
import matcher
import searcher
import youtuber
import creator

directory = "music"
#shutil.rmtree(directory)
#os.mkdir(directory)

# PUT YOUR SPOTIFY CREDENTIALS HERE
client_id='0000000000000000000000000000000000000'
client_secret='0000000000000000000000000000000000'

#PUT YOUR GOOGLE CREDENTIALS HERE
youtube_KEY = "000000000000000000000000000000000000000"

#PUT YOUR PLAYLIST URL HERE
playlist_url = "https://open.spotify.com/user/22ql3mdjbu7eovdrj5ctdv66a/playlist/2hcPm88zj3Ayi3AgmkXr08?si=H2sZw4HBTqKxzFnaQRHxgA"

auth = str(base64.b64encode((client_id+":"+client_secret).encode()))[2:-1]
playlist_id = playlist_url[playlist_url.find("playlist/")+len("playlist/"):playlist_url.find("?si=")]

print(playlist_id)

params = {"grant_type":"client_credentials"}
header = {"Authorization": "Basic "+auth}
result = requests.post("https://accounts.spotify.com/api/token",data=params,headers=header);

access = result.json()
data=[];

auth = access['token_type']+" "+access['access_token']
url ="https://api.spotify.com/v1/playlists/"+playlist_id+"/tracks"

total = spotify.GetSizeDataSpotify(auth,access,url,0)
print(total)
if total > 100:
    i = 0
    while i <= total:
        spotify.GetDataSpotify(auth,access,url,i,data)
        i+=100
else:
    spotify.GetDataSpotify(auth,access,url,0,data)

spotify.WriteErrorJson()
spotify.WriteFile(data)
total = 0
max_total = len(data)
for line in data:
    creator.PrepareAlbumFolder(directory,line)
    musicsNames = matcher.MakeNames(line["name"],line["artist"],line["album_name"])
    response = ""
    r = -1
    for query in musicsNames:
        try :
            res = searcher.SerachInYoutube(youtube_KEY,query)
            rp = matcher.IsMusicSearched(line,res)
            if not(rp is False):
                response =  res
                r = rp
                break
        except:
            pass
    if r != -1:
        try:
            if response["items"][r]["id"]["videoId"]:      
                youtube_url = response["items"][r]["id"]["videoId"]
                directory_album = directory+"/"+line["album_name"]+"/"
                youtuber.SearchAndSaveMusic(youtube_url,directory_album,line,data.index(line))
                total+=1
                print("{}/{}".format(total,max_total))
            else:
                print("err1")
                jsonFile = open("./files/erros.json", "r")
                datae = json.load(jsonFile)
                jsonFile.close()
                datae.append({'music_id': data.index(line)})
                with open("./files/erros.json", "w") as jsonFile:
                    json.dump(datae, jsonFile)

                
        except:
            print("erro3 ao baixa: {}".format( data.index(line)))
            jsonFile = open("./files/erros.json", "r")
            datae = json.load(jsonFile)
            jsonFile.close()
            datae.append({'music_id': data.index(line)})
            with open("./files/erros.json", "w") as jsonFile:
                json.dump(datae, jsonFile)

print("\n...CORRGINDO ERROS ...\n")
jsonFile = open("./files/erros.json", "r")
erros = json.load(jsonFile)
Nmax_total = len(erros)
if Nmax_total > 0:
    for er in erros:
        nb = er["music_id"]
        line = data[nb]
        musicsNames = matcher.MakeNames(line["name"],line["artist"],line["album_name"])
        response = ""
        r = -1

        for query in reversed(musicsNames):
            try :
                res = searcher.SerachInYoutube(youtube_KEY,query)
                rp = matcher.IsMusicSearched(line,res)
                if not(rp is False):
                    response =  res
                    r = rp
                    break
            except:
                pass
        if r != -1:
            try:
                if response["items"][r]["id"]["videoId"]:      
                    youtube_url = response["items"][r]["id"]["videoId"]
                    directory_album = directory+"/"+line["album_name"]+"/"
                    youtuber.SearchAndSaveMusic(youtube_url,directory_album,line,data.index(line))
                    total+=1
                    print("{}/{}".format(total,max_total))
                else:
                    print("err1")
                    jsonFile = open("./files/erros.json", "r")
                    datae = json.load(jsonFile)
                    jsonFile.close()
                    datae.append({'music_id': data.index(line)})
                    with open("./files/erros.json", "w") as jsonFile:
                        json.dump(datae, jsonFile)

                    
            except:
                print("erro3 ao baixa: {}".format( data.index(line)))
                jsonFile = open("./files/erros.json", "r")
                datae = json.load(jsonFile)
                jsonFile.close()
                datae.append({'music_id': data.index(line)})
                with open("./files/erros.json", "w") as jsonFile:
                    json.dump(datae, jsonFile)
        
        jsonFile = open("./files/erros.json", "r")
        datae = json.load(jsonFile)
        jsonFile.close()
        del(datae[datae.index(er)])
        with open("./files/erros.json", "w") as jsonFile:
            json.dump(datae, jsonFile)
        

print('Tudo OKaEY')
