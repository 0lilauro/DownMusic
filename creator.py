import requests
import os


def DirExists(directory,album):
    path = directory+"/"
    dirName = path+album    
    r = os.path.exists(dirName)
    return r


def PrepareAlbumFolder(directory,line):
    url = line['album_img']
    album = line['album_name']
    path = directory+"/"
    dirName = path+album

    if not DirExists(directory,album):
        os.makedirs(dirName)
        if url is not None:
            result = requests.get(url, allow_redirects=True)
            ext = (result.headers.get('content-type'))
            ext = (ext[ext.find("/")+1:]).lower()
            if ext in ('jpeg','jpg','png','ico'):
                filename= dirName +"/album.{}".format(ext)
                with open(filename, 'wb') as file:
                    file.write(result.content)
            else:
                print("Invalid IMG")
        else:
            print("Invalid IMG")


