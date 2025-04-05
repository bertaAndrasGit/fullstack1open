import functools
import os
import secrets
from flask import Flask,session,render_template,request,abort,flash,redirect,url_for
from passlib.hash import pbkdf2_sha256
app = Flask(__name__)


"""generated with secrets.token_urlsafe() """
"""if the secret_key not changes, the old cookies will still be valid"""
app.secret_key = "[generatesecretkeyhere]"

users = {}

def login_required(route):
    @functools.wraps(route)
    def route_wrapper(*args,**kwargs):
        if not session.get("email"):
            return redirect(url_for("login"))
        return route(*args,**kwargs)
    return route_wrapper


@app.get("/")
@login_required
def home():
    #session.clear() #<- deletes previous cookies
    return render_template("home.html", email=session.get("email"))


@app.get("/protected")
@login_required
def protected():
    return render_template("protected.html")


@app.route("/login",methods=["GET", "POST"])
def login():
    email = ""
    
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        #if the incoming pwd is = with the hashed one in the users dict
        if pbkdf2_sha256.verify(password, users.get(email)):
            #log in ˇˇˇ
            session["email"] = email
            flash("Incorrect e-mail or password.")
            return redirect(url_for("protected"))
            
    return render_template("login.html", email=email)


@app.route("/signup", methods=["GET","POST"])
def signup():
    #if the form is submitted
    #get = if the browser is accessing a page
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        users[email] = pbkdf2_sha256.hash(password)
        print(users)
        #if i want to make the user instantly logged in after sign up, use:
        
        #session["email"] = email
        #flash("Successfully signed up","info")
        #return redirect(url_for("home"))
        
        #this sends a cookie to the browser with the email in it and 
        #when the browser is accessing the flask server, it is going to send the email to the server.
        #so when we accessing tne /protected endpoint, the session.get("email") will not be empty and i can access the protected page.
        
        flash("Successfully signed up","info")
        return redirect(url_for("login"))
    
    return render_template("signup.html")

