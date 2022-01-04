# Profile class will generate a new profile with their own attributes
# This allows for specific profiles to be referenced which will return the same attributes every time it's called
from data.api_functions import *
from data.genius_api import *

class Profile :
    def __init__(self):
        self.profileURL = get_profileURL()
        self.kanye = get_kanyequote()
        self.animedata = get_animedata()
        self.songinfo = get_songinfo()

    def get_profileURL(self):
        return self.profileURL

    def get_fullname(self):
        return get_fullname(self.profileURL)

    def get_kanyequote(self):
        return self.kanye

    def get_animequote(self):
        quote = self.animedata.get('quote')
        return quote

    def get_animechar(self):
        character = self.animedata.get('character')
        return character

    def get_anime(self):
        anime = self.animedata.get('anime')
        return anime

    def get_picture(self):
        return get_picture(self.profileURL)

    def get_age(self):
        return get_age(self.profileURL)

    def get_song(self):
        song_name = self.songinfo.get("full_title")
        #song_name = info.get("title") #no artist name
        return song_name

    def get_songimg(self):
        song_img = self.songinfo.get("song_art_image_thumbnail_url")
        return song_img

    def get_songURL(self):
        song_url = self.songinfo.get("url")
        return song_url

    def get_interests(self, count):
        interests = get_categories(count)
        return interests
    def get_friendship(self):
        return self.friendship