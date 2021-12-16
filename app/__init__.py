from flask import session
from flask import request, render_template, Flask, redirect
from os import urandom
from data.user_management import *
from data.profile import Profile

app = Flask(__name__)
debug = True
app.secret_key = urandom(24)

#helper method

###NOTE: FOR THE FUNCTIONS user_exists(user), correct_password(user,password), and add_user(user,password):
###THESE FUNCTIONS WERE ADDED HERE TO LET THE CODE COMPILE. THESE METHODS SHOULD COME FROM A SEPERATE DATABASE MANAGEMENT PY FILE
###FOR SAKE OF ORGANIZATION.

def unauthorizedFlow():
    '''
    returns static html for when user accesses site they should not
    '''

    #simply redirects to desired site
    return redirect("/static/unauthorized.html", code=302)

#helper method


def userSignedIn(session):
    '''
    returns the status of user login
    '''
    return 'username' in session.keys() and session['username']


@app.route("/", methods=['GET', 'POST'])
def welcome():
    '''
    Welcome Page
    '''

    if userSignedIn(session):
        return render_template("home_page.html", user=session['username'])

    else:
        #fill in with watever we want later
        return render_template('index.html')


@app.route("/login", methods = ['GET','POST'])
def login():
    '''login page'''
    if userSignedIn(session):
        return unauthorizedFlow()

    if 'username' in request.form.keys() and request.form.get('username') != "":
        username = request.form.get('username')
        password = request.form.get('password')
        #authflow variable
        loginAuthorized = user_exists(
            username) and correct_password(username, password)

        if loginAuthorized:
            session['username'] = username
            return redirect("/", code=302)
        else:
            return render_template('login.html', error="Login failed, please try again")

    return render_template("login.html")


@app.route("/register", methods=['GET', 'POST'])
def disp_registerpage():
    '''
    register page
    '''
    if userSignedIn(session):
        return redirect("/unauthorized.html", code=302)

    if 'username' in request.form.keys() and request.form.get('username') != "":
        #store form information
        username = request.form.get('username')
        password = request.form.get('password')
        con_password = request.form.get('c_password')

        #checks password requirements against password confirmation and password existence; False means it fails requirements
        password_requirements = password == con_password and bool(password)

        #checks db for existing user and user existence; False means it passes requirements
        username_conflict = user_exists(username) or (not bool(username))

        if password_requirements and (not username_conflict):
            add_user(username, password)
            return redirect("/login")

        else:
            #Error messages based on incorrect input types
            extra_Message = "An error has been made trying to register you."
            if not password_requirements:
                extra_Message = "Password requirements not met. Check to see that password is at least one character and that password confirmation matches"
                print(username)
                print(password)
                print(con_password)

            elif username_conflict:
                extra_Message = "Username may already be in use, or does not contain at least one character"

            return render_template('register.html', error=extra_Message)

    return render_template('register.html')

#Checks the register to make sure everything is good
#Password and confirm password should be the same


@app.route("/check_register", methods=['GET', 'POST'])
def check_register():
    '''
    function for post-form request; register process given POST form arguments
    '''

    if userSignedIn(session):
        return redirect("/unauthorized.html", code=302)

    #store form information
    username = request.form.get('username')
    password = request.form.get('password')
    con_password = request.form.get('confirm_password')

    #checks password requirements against password confirmation and password existence; False means it fails requirements
    password_requirements = password == con_password and bool(password)

    #checks db for existing user and user existence; False means it passes requirements
    username_conflict = user_exists(username) or (not bool(username))

    if password_requirements and (not username_conflict):
        add_user(username, password)
        return render_template('login_page.html', error="Successfully Registered")

    else:
        #Error messages based on incorrect input types
        extra_Message = "An error has been made trying to register you."
        if not password_requirements:
            extra_Message = "Password requirements not met. Check to see that password is at least one character and that password confirmation matches"

        elif username_conflict:
            extra_Message = "Username may already be in use, or does not contain at least one character"

        return render_template('register.html', error=extra_Message)


@app.route("/logout", methods=['GET', 'POST'])
def logout():
    '''
    logs out the user by setting 'username' key to None
    '''

    session['username'] = None
    return render_template('login_page.html', error="Successfully Logged Out")


@app.route("/auth_ed", methods=['POST'])
def authenticate():
    '''
    authorization page; redirects and logs in if credentials work, loads login template if not
    '''
    #retrieve from FORM instead of ARGS because we are retrieving from POST method
    username = request.form.get('username')
    password = request.form.get('password')

    #authflow variable
    loginAuthorized = user_exists(
        username) and correct_password(username, password)

    if loginAuthorized:
        session['username'] = username
        return redirect("/", code=302)
    else:
        return render_template('login_page.html', error="Login failed, please try again")

@app.route("/dashboard", methods=['GET', 'POST'])
# TESTER CODE. FINAL PRODUCT MAY VARY DUE TO PRODUCT ENHANCEMENT.
def dashboard():
    p1 = Profile()
    print("seed: " + p1.get_profileURL())
    print("full name: " + p1.get_fullname())
    print("picture: " + p1.get_picture())
    print("age: " + str(p1.get_age()))
    print("kanye quote: " + p1.get_kanyequote())
    print("anime quote: " + p1.get_animequote())
    print("char for quote: " + p1.get_animechar())
    print("anime for quote: " + p1.get_anime())
    return render_template('index.html') #switch out

def main():
    """
    false if this file imported as module
    debugging enabled
    """
    try:
        app.debug = True
        app.run()
    except:
        return render_template('ErrorResponse.html')

@app.route("/template_test", methods = ['GET','POST'])
def profile():
    character = {
        "name" : "Fish",
        "age":-10,
        "pfp": "https://cdn.britannica.com/83/89183-050-D00C8FDC/Scup-porgy.jpg",
        "song":{"genre":"rock", "name":"livin on a prayer"},
        "likes":["food","games","chips"],
        "dislikes":["nofood","nogames","nochips"]
    }

    return render_template("profile.html",name=character["name"],
    age=character["age"],pfp=character["pfp"],song_name=character["song"]["name"],
    song_genre = character["song"]["genre"],likes=character["likes"],dislikes=character["dislikes"])

if __name__ == "__main__":
    main()
