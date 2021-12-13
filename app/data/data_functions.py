#Users refer to the actual person using website, profiles refer to the randomly generated fake accounts that we make
DB_FILE='database.db'
db = sqlite3.connect(DB_FILE, check_same_thread=False)

#General functions
def create_tables():
    """Creates the tables in the database to store profiles and users"""
    c = db.cursor()
    command = 'CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username TEXT NOT NULL UNIQUE, password TEXT NOT NULL)' #creates users table
    #stores the user id, username, and password
    c.execute(command)
    command = 'CREATE TABLE IF NOT EXISTS profiles (profile_id INTEGER PRIMARY KEY, name TEXT NOT NULL, bio TEXT NOT NULL, pic TEXT NOT NULL)' #creates profiles table
    #stores the profile id, profile name, profile bio, and link to a profile picture
    c.execute(command)
    command = 'CREATE TABLE IF NOT EXISTS friends (user_id INTEGER PRIMARY KEY, profile_id INTEGER friendship INTEGER)' #creates a connecting table
    #Stores a user id and profile id. If a user adds a profile as a friend, a new entry is added to this table with the ids of the user and the profile
    #The friendship value stores how friendly the user and the profile are
    #ok so my very inefficient plan with the friends table is when we need to change something we look at all of a users friended profiles until we find the one with the right id
    c.execute(command)
    db.commit() #save changes

def setFriendship(friendshiplvl, user_id, profile_id):
    #this will allow us to change friendship level
    return None
def befriend(user_id, profile_id):
    c = db.cursor()
    c.execute(f'INSERT INTO friends (user_id, profile_id, friendship) VALUES (?, ?, ?);', (user_id, profile_id, 0)) 
    db.commit()
#User-specific functions: login authentication and account creation
def create_user(username, password):
    """Adds a user with a username and password into the users table of the database"""
    c = db.cursor()
    c.execute(f'INSERT INTO users (username, password) VALUES (?, ?);', (username, password)) 
    db.commit()

def authenticate(username, password):
    """Checks if the username and password match any login info in the users table"""
    c = db.cursor()
    result = list(c.execute(f'SELECT user_id from users where username == ? and password == ?', (username, password)))
    if(len(result) == 0): #length 0 means that password/username combination had no match
        return None
    return result[0][0] #user_id

#Profile-specific functions: returning important values and generating the random profiles
def getProfile(profile_id):
    c = db.cursor()
    result = list(c.execute(f'select profile_id, name, bio, pic from entries where profile_id == ?', (profile_id, )))
    if(len(result) == 0): #if there is no profile with the id 
        return None
    return [{
        "profile_id": profile_id,
        "name": name,
        "bio": bio,
        "pic": pic
    } for (profile_id, name, bio, pic) in result][0]
def create_profile(name, bio, pic):
    c = db.cursor()
    c.execute(f'INSERT INTO profiles (name, bio, pic) VALUES (?, ?, ?);', (name, bio, pic))
    db.commit()
