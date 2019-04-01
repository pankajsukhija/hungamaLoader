from requests import get

# content_id hard-code for testing only. Arg parser can be used.
content_id = 22464657  # THIS WILL DOWNLOAD `VERSACE ON THE FLOOR` by Bruno Mars. You can download any other song. 
user_id =  133574320 # Can be obtained using MITM.
agent = "MiuiMusic/6.0.1 (Linux; U; Android 6.0.1; Redmi 3S Build/MMB29M" # Must be MiuiMusic
key = "184932e55a27f1c8047b35d0774afe6d" # Can be obtained using MITM.

infoHeaders = {"User-agent": agent,
"PRODUCT": "MIMUSIC",
"API-KEY": key,
"Host": "capi.hungama.com",
"Connection": "Keep-Alive",
"Accept-Encoding": "gzip"
}

downloadHeaders = {"User-agent": agent,
"Host": "akdls3re.hungama.com",
"Connection": "Keep-Alive",
"Accept-Encoding": "gzip"
}

albumArtHeaders = {"User-agent": agent,
"PRODUCT": "MIMUSIC",
"API-KEY": key,
"Host": "capi.hungama.com",
"Connection": "Keep-Alive",
"Accept-Encoding": "gzip"
}

def reqSongInfo(content_id, user_id):
    # Parse song title and album art link.
    url = "http://49.44.117.129/webservice/thirdparty/content/music/song_details?content_id=" + str(content_id) + "&user_id=" + str(user_id)
    request = get(url, headers = albumArtHeaders)
    albumArtLink = request.json()["response"]["images"]["image_500x500"][0]
    songTitle = request.json()["response"]["title"]
    return [albumArtLink, songTitle]

def downloadMP3(content_id, user_id):
    url = "http://35.190.13.63/webservice/thirdparty/streaming/audio?content_id=" + str(content_id) + "&user_id=" + str(user_id)
    request =get(url, headers = infoHeaders)
    mp3Link = (request.json()["response"]["url"])
    reqMP3 = get(mp3Link, headers = downloadHeaders)
    if reqMP3.headers["Content-Type"] == "audio/mpeg": # Confirms if content is mpeg.
        fileTitle = reqSongInfo(content_id, user_id)[1] # Not using album art for now.
        mp3File = open( fileTitle + ".mp3", "wb") # Writes the content to an mp3 file in binary mode.
        mp3File.write(reqMP3.content)
        mp3File.close()
        print()
    else:
        print("Invalid data recieved\n.")
        exit()


if __name__ == "__main__":
    downloadMP3(content_id, user_id)