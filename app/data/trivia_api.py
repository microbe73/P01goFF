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
    '''takes parameter arg, an int, which gets concatenated to the url request
    returns trivia api dicitonary, where amount=10 and category=args'''

    url = "https://opentdb.com/api.php?amount=10&type=boolean&category="+str(arg)

    return parseURL(url)
def getTrivHuman(arg):
    '''takes parameter arg, a string, which accesses getTrivDict using dictionary
    indexing to proper numberal representation of the category'''

    categories = {
        "everything":0,
        "general":9,
        "film":11,
        "music":12,
        "tv":14,
        "games":15,
        "science":17,
        "tech":18,
        "math":19,
        "myths":20,
        "sports":21,
        "geography":22,
        "history":23,
        "politics":24,
        "animals":27,
        "vehicles":28,
        "anime":31
    }
    information = getTrivDict(categories[arg])
    try:
        if information['response_code'] == 0:
            return information['results']
        else:
            return False
    except:
        return False

if __name__ == "__main__":
    x = getTrivHuman("everything")

    for list in x:
        print(list)
