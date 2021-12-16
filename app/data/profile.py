# Profile class will generate a new profile with their own attributes
# This allows for specific profiles to be referenced which will return the same attributes every time it's called
from data.api_functions import *

class Profile :
    def __init__(self):
        self.profileURL = get_profileURL()
        self.kanye = get_kanyequote()
        self.animedata = get_animedata()

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
