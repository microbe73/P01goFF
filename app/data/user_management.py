from data.data_functions import * 
def user_exists(user):
    '''returns boolean depending on whether or not the given user exists'''

    #currently only returns True
    return user in get_usernames()

    #how to implement:
    #utilize db functions and paste into here

def correct_password(user, password):
    '''returns boolean if username and password combination are valid'''

    #currently only returns True
    return authenticate(user,password)

    #how to implement:
    #have a databsase function that checks to see if the username and password combination is valid and returns a boolean in response
    #True if valid; False if invalid

def add_user(user, password):
    '''adds user given username and password combination'''

    #currently does nothing
    create_user(user,password)

    #how to implement:
    #have a database function that... adds the user and password combo to the database
