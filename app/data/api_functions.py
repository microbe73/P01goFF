#A library of helper functions for extracting data from APIs

from urllib.request import Request, urlopen
import json, urllib, random

def parseURL(url):
    ''' parseURL() will open, read, and turn the given url into a dictionary '''
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'}) #establishes a useragent so we don't look like a bot
    try:
        page = urlopen(req)
        dict = json.loads(page.read())
        return dict
    except:
        return False

# functions related to the animequote api
def get_animedata():
    ''' get_animedata() will generate a random piece of data with an anime quote, the anime it came from, and the character who said it '''
    url = "https://animechan.vercel.app/api/random"
    data = parseURL(url) #will contain anime, character, and quote
    # print(quote + "- " + character + " from " + anime)
    return data

# functions related to the kanye.rest api
def get_kanyequote():
    ''' get_kanyequote() will generate a random kanye quote '''
    url = "https://api.kanye.rest/"
    data = parseURL(url)
    quote = data.get('quote')
    # print(quote + " - Kanye")
    return quote

#functions related to the Random User Generator API
def get_profileURL():
    ''' get_profileurl() will generate a random profile url with a seed '''
    url = "https://randomuser.me/api/?inc=gender,name,dob,picture"
    data = parseURL(url)
    info = data.get('info')
    seed = info.get('seed') #seeds allow you to access specific profiles (like an id)
    seedURL = "https://randomuser.me/api/?seed=" + str(seed) #creates a url you can use when referencing a specific profile
    # print(seedURL)
    return seedURL

def get_fullname(seed):
    ''' get_fullname() will generate a full name string based on a profile(seed) '''
    data = parseURL(seed)
    info = data.get('results')[0]
    name = info.get('name')
    firstname = name.get('first')
    lastname = name.get('last')
    fullname = firstname + " " + lastname
    # print(name)
    # print(firstname)
    # print(lastname)
    # print(fullname)
    return fullname

def get_picture(seed):
    ''' get_picture() will generate a picture (link) based on a profile '''
    data = parseURL(seed)
    info = data.get('results')[0]
    pic = info.get('picture').get('medium')
    return pic

def get_age(seed):
    ''' get_picture() will generate a age based on a profile '''
    data = parseURL(seed)
    info = data.get('results')[0]
    age = info.get('dob').get('age')
    return age

def get_categories(count):
    categories = [
        "general",
        "film",
        "music",
        "tv",
        "games",
        "science",
        "tech",
        "math",
        "myths",
        "sports",
        "geography",
        "history",
        "politics",
        "animals",
        "vehicles",
        "anime"
    ]
    final = random.sample(categories, count)
    print(final)
    return final
