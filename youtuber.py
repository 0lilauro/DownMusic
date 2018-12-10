
from __future__ import unicode_literals
import youtube_dl
import eyed3
import json 
import os

def SearchAndSaveMusic(url,directory_album,data,idx):
    url_s = []
    url_s.append(url)
    art = ""
    for artist in data["artist"]:
        if len(data["artist"])-1 is data["artist"].index(artist):
            art+= artist["name"]
        else: 
            art += artist["name"] +" - "
    music_name = "{} - {}".format(data["name"],art)

    ydl_opts = {
        'outtmpl': directory_album+'{}.%(ext)s'.format(music_name),
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    try:
        music_path = "{}{}.mp3".format(directory_album,music_name)
        
        if not os.path.exists(music_path):
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(url_s)
            
        
            if os.path.exists(music_path):
                img = directory_album+"album.jpeg"

                song = eyed3.load(music_path)
                song.tag.artist = u"{}".format(art)
                song.tag.album = u"{}".format(data["album_name"])
                song.tag.title = u"{}".format(data["name"])

                if os.path.exists(img):
                    imagedata = open(img,"rb").read()
                    song.tag.images.set(3,imagedata,"image/jpeg",u"{}".format(data["name"]+" "+data["album_name"]))
                song.tag.save()
    except:
        with open("./files/error.json","w") as final:
            print("erro2 ao baixa: {}".format(idx))
            jsonFile = open("./files/error.json", "r")
            datae = json.load(jsonFile)
            jsonFile.close()
            datae.append({'music_id':idx})
            with open("./files/error.json", "w") as jsonFile:
                json.dump(datae, jsonFile)