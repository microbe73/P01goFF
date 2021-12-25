from urllib.request import Request, urlopen, HTTPError, URLError
import json, urllib, requests, random, os.path, pdb

url = "https://api.genius.com"
path = os.path.dirname(__file__) + '/../keys/key_api0.txt'
with open(path, "r", encoding="utf-8") as key:
    auth_token = key.read().strip() #receives an auth token from key_api0.txt file

headers = {
    "User-Agent": "CompuServe Classic/1.22",
    "Accept": "application/json",
    "Authorization": "Bearer " + auth_token
}

def get_song():
    id = random.randint(100000,999999) #all genius songs can be accessed by their 6 digit ids
    URL = url + "/songs/" + str(id)
    #print("request URL: " + URL)
    req = Request(URL, headers=headers)
    try:
        page = urlopen(req)
    except HTTPError as e:
        print("error status: " + str(e.code))
        return get_song() #if the song/url does not exist, try again
    except URLError as e:
        print("error: " + e.reason)
    else:
        dict = json.loads(page.read())
        info = dict.get("response").get("song")
        song_name = info.get("full_title")
        song_url = info.get("url")
        #print("song url: " + song_url)
        return (song_name)

if __name__ == "__main__":
    print("song name: " + (get_song()))
