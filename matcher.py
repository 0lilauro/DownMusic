

def MakeNames(music,all_artist,album):
    artist = ""
    for art in all_artist:
        if len(all_artist)-1 is all_artist.index(art):
            artist+= art["name"]
        else: 
            artist += art["name"] +" - "
            
    names = []
    names.append("{} {} {}".format(music,album,artist))
    names.append("{} {} Audio Oficial".format(music,album))
    names.append("{} {} Audio".format(music,album))
    names.append("{} {} music audio".format(music,album))
    names.append("{} {} lyrics".format(music,album))
    names.append("{} {} mp3".format(music,album))
    names.append("{} {} video official".format(music,album))
    names.append("{} {} video".format(music,album))
    names.append("{} {} video clip".format(music,album))
    names.append("{} {} {} mp3".format(music,album,artist))
    names.append("{} {} {} Audio Oficial".format(music,album,artist))
    names.append("{} {} {} Oficial".format(music,album,artist))
    names.append("{} {} {} lyrics".format(music,album,artist))
    names.append("{} {} {} music".format(music,album,artist))
    names.append("{} {} {} video oficial".format(music,album,artist))
    names.append("{} {} {} video".format(music,album,artist))
    names.append("{} {} {} video clip".format(music,album,artist))
    names.append("{} {} lyrics".format(music,artist))
    names.append("{} {} Audio Oficial".format(music,artist))
    names.append("{} {} lyrics".format(music,artist))
    names.append("{} {} Audio".format(music,artist))
    names.append("{} {} video".format(music,artist))
    names.append("{} {} video oficial".format(music,artist))
    names.append("{} {} video clip".format(music,artist))
    names.append("{} {} music audio".format(music,artist))
    names.append("{} Audio Oficial".format(music))
    names.append("{} lyrics".format(music))
    names.append("{} Audio".format(music))
    names.append("{} music audio".format(music))
    names.append("{} video".format(music))
    names.append("{} video oficial".format(music))
    names.append("{} video clip".format(music))
    return names

def IsMusicSearched(music,response):
    if len(response["items"]) > 0:
        name = music["name"].lower()
        album = music["album_name"].lower()
        artist = ""
        for art in music["artist"]:
            if len(music["artist"])-1 is music["artist"].index(art):
                artist+= art["name"]
            else: 
                artist += art["name"] +" - "
        artist = artist.lower()
        collection = []
        for music in response["items"]:
           
            ytb_title = music["snippet"]["title"].lower()
            ytb_description = music["snippet"]["description"].lower()
            counter = 0
            searched = ["mp3","audio","music","letra","lyrics","musica","official"]
            nimb1 = 10//len(searched)
            searched2 = [name+" audio", name+" lyrics", name+" musica", name+" music", name+" official",name+" "+artist, name+" "+album,name+" "+artist+ " Audio", name+" "+album + " Music"]
            nimb2 = 70//len(searched)
            for s1 in searched:
                if s1 in ytb_description or s1 in ytb_title:
                    counter+=nimb1

            for s2 in searched2:
                if s2 in ytb_description or s2 in ytb_description:
                    counter+= nimb2
            break_name = name.split()
            break_album = album.split()
            break_artist = artist.split(" - ")

            for word in break_name :
                numb = 15//(len(break_name))
                if word in ytb_title:
                    counter+= numb
                if word in ytb_description:
                    counter+= numb

            for word in break_album :
                numb = 15//(len(break_album))
                if word in ytb_title:
                    counter+= numb
                if word in ytb_description:
                    counter+= numb
            
            for word in break_artist :
                numb = 15//(len(break_artist))
                if word in ytb_title:
                    counter+= numb
                if word in ytb_description:
                    counter+= numb
                
            collection.append(counter)
            if counter >= 80: 
                idx = response["items"].index(music)
                return idx
        
        maximum = max(collection)
        if maximum <= 40:
           return False
        else:
            index = collection.index(maximum)
            return index


    else:
        return False