from flask import session
from flask import request, render_template, Flask, redirect
from os import urandom

app = Flask(__name__)
debug = True
app.secret_key = urandom(24)

#helper method

###NOTE: FOR THE FUNCTIONS user_exists(user), correct_password(user,password), and add_user(user,password):
###THESE FUNCTIONS WERE ADDED HERE TO LET THE CODE COMPILE. THESE METHODS SHOULD COME FROM A SEPERATE DATABASE MANAGEMENT PY FILE
###FOR SAKE OF ORGANIZATION.

def user_exists(user):
    '''returns boolean depending on whether or not the given user exists'''

    #currently only returns True
    return True

    #how to implement:
    #have a database function that checks to see if given user exists within the db and return boolean based on that

def correct_password(user,password):
    '''returns boolean if username and password combination are valid'''

    #currently only returns True
    return True

    #how to implement:
    #have a databsase function that checks to see if the username and password combination is valid and returns a boolean in response
    #True if valid; False if invalid

def add_user(user,password):
    '''adds user given username and password combination'''

    #currently does nothing
    print("user should be added at this point")

    #how to implement:
    #have a database function that... adds the user and password combo to the database

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
        return render_template("home_Page.html", user=session['username'])

    else:
        return render_template('login_Page.html')


@app.route("/register", methods=['GET', 'POST'])
def disp_registerpage():
    '''
    register page
    '''
    if userSignedIn(session):
        return unauthorizedFlow()

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
        return render_template('login_Page.html', extra_Message="Successfully Registered")

    else:
        #Error messages based on incorrect input types
        extra_Message = "An error has been made trying to register you."
        if not password_requirements:
            extra_Message = "Password requirements not met. Check to see that password is at least one character and that password confirmation matches"

        elif username_conflict:
            extra_Message = "Username may already be in use, or does not contain at least one character"

        return render_template('register.html', extra_Message=extra_Message)


@app.route("/logout", methods=['GET', 'POST'])
def logout():
    '''
    logs out the user by setting 'username' key to None
    '''

    session['username'] = None
    return render_template('login_Page.html', extra_Message="Successfully Logged Out")


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
        return render_template('login_Page.html', extra_Message="Login failed, please try again")
