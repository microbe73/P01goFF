from urllib.request import Request, urlopen
import json
import urllib

def parseURL(url):
    ''' parseURL() will open, read, and turn the given url into a dictionary '''
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'}
                  )  # establishes a useragent so we don't look like a bot

    page = urlopen(req)
    dict = json.loads(page.read())
    return dict

#args must be an integer
def getTrivDict(arg):
    '''takes parameter arg, which gets concatenated to the url request
    returns trivia api dicitonary, where amount=10 and category=args'''
    
    url = "https://opentdb.com/api.php?amount=10&type=boolean&category="+str(arg)

    return parseURL(url)

print(getTrivDict(9))