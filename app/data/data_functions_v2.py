from sqlite3 import connect
from data.table import Table

data = connect("data.db", isolation_level=None, check_same_thread=False)
#"username", "password"
users = Table(data, "users", "username")

#"name", "pfp", "age", "bio", "song", "quote", "gender"
profiles = Table(data, "profiles", "name")

#management for users table
def get_usernames():
    "retuns a list of usernames"
    return users.get_main_values()


def user_exists(username):
    "returns true if user exists"
    return users.value_exists(username)


def correct_password(username, password):
    "returns true if username matches password"
    real_password = users.get_value(username, "password")
    return password == real_password


def add_user(username, password):
    "adds a user with username and passsowrd"
    users.add_values([username, password])
    edited_stories = Table(data, username, "title")
    edited_stories.create(["title"])

#management for profiles table

def get_profiles():
    "returns a list of profiles"
    return profiles.get_main_values()

def profile_exists(name):
    "returns true if profile with name exists"
    return profiles.value_exists(name)

def add_profile(name, user, pfp, age, songURL, songName, quote, like1, like2, like3, dislike1, dislike2, dislike3, friendship): #user refers to the account to which the profile is friended
    "adds a profile 'name' with desired parameters; throws error if conflicts with existing profile"
    if(not profile_exists(name)):
        profiles.add_values([name, user, pfp, age, songURL, songName, quote, like1, like2, like3, dislike1, dislike2, dislike3, friendship])
        return True
    return False

def get_profile_value(name, field):
    "gets desired field of the profile with name; throws error if profile with name does not exist"
    if(not profile_exists(name)):
        raise KeyError("the given profile cannot be found")
    else:
        return profiles.get_value(name,field)

def set_profile_value(name, field, value):
    "Updates a value in the profile table"
    if(not profile_exists(name)):
        raise KeyError("The given profile cannot be found")
    else:
        profiles.set_value(name, field, value)
def get_profiles_of_user(username):
    profs = get_profiles()
    profs_of_user = []
    for i in profs:
        if(get_profile_value(i, "user") == username):
            profs_of_user.append(i)
    return profs_of_user
def reset_data():
    "resets the database to empty user and profile tables"
    open("data.db", "w").close()
    users.create(["username", "password"])
    profiles.create(["name", "user", "pfp", "age", "songURL", "songName", "quote", "like1", "like2", "like3", "dislike1", "dislike2", "dislike3", "friendship"])



###THE BELOW CODE IS FROM WHEN theonionsone WORKED ON THE STORY IMPROV PROJECT
# def get_stories():
#     return stories.get_main_values()


# def get_edited_stories(username):
#     "returns a list of titles of stories edited by user"
#     edited_stories = Table(data, username, "title")
#     return edited_stories.get_main_values()


# def get_unedited_stories(username):
#     "returns a list of titles of stories not edited by user"
#     stories = set(get_stories())
#     edited_stories = set(get_edited_stories(username))
#     return stories - edited_stories


# def story_exists(title):
#     "returns true if story exists"
#     return stories.value_exists(title)


# def add_story(title):
#     "adds a story with title"
#     stories.add_values([title, "", ""])


# def get_old_part(title):
#     return stories.get_value(title, "old_part")


# def get_new_part(title):
#     "returns the newest addition to story"
#     return stories.get_value(title, "new_part")


# def attach(old_part, new_part):
#     if old_part == "":
#         return new_part
#     return old_part + "\n\n" + new_part


# def get_full_story(title):
#     "returns the full text of story"
#     old_part = get_old_part(title)
#     new_part = get_new_part(title)
#     return attach(old_part, new_part)


# def add_new_part(title, new_part, username):
#     "adds new part to story being edited by user"
#     full_story = get_full_story(title)
#     stories.set_value(title, "old_part", full_story)
#     stories.set_value(title, "new_part", new_part)
#     edited_stories = Table(data, username, "title")
#     edited_stories.add_values([title])
