import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps

app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///BloodAssit.db")


# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response




def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


STATES=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
BLOODTYPES=["A+","A-","B+","B-","AB+","AB-","O+","O-","A1+","A1-","A2+","A2-","A1B+","A1B-","A2B+","A2B-"]

@app.route("/")
@login_required
def index():
    return render_template("homepage.html")



@app.route("/register",methods=["GET","POST"])
@login_required
def register():
    if request.method=="POST":
        #ensure name was submitted
        if not request.form.get("Name"):
            return render_template("error.html",code=1)
        #ensure age was submitted
        if not request.form.get("Age"):
            return render_template("error.html",code=2)

        #ensure age is between 18 and 60
        if  int(request.form.get("Age"))<18 or int(request.form.get("Age"))>60:
            return render_template("error.html",code=3)
        #ensure city was submitted
        if not request.form.get("City"):
            return render_template("error.html",code=4)
        #ensure phoneno was submitted
        if not request.form.get("Phoneno"):
            return render_template("error.html",code=5)

        #ensure that the user has not already registered
        rows=db.execute("SELECT * FROM registered WHERE Id=?",session["user_id"])
        if(len(rows)!=0):
            return render_template("error.html",code=6)





        #register the user
        db.execute("INSERT INTO registered(Id,Name,Age,City,State,Bloodtype,Phoneno)VALUES(?,?,?,?,?,?,?)", session["user_id"],request.form.get("Name"),request.form.get("Age"),request.form.get("City"),request.form.get("State"),request.form.get("Bloodtype"),request.form.get("Phoneno"))
        return render_template("registered.html")
    else:
        return render_template("register.html",states=STATES,bloodtypes=BLOODTYPES)

@app.route("/locate")
@login_required
def locate():
    INFO=db.execute("SELECT * FROM registered")
    return render_template("locate.html",info=INFO,states=STATES,bloodtypes=BLOODTYPES)

@app.route("/myths")
@login_required
def myths():
    return render_template("myths.html")


@app.route("/contact")
@login_required
def contact():
    return render_template("contact.html")

@app.route("/condition")
@login_required
def condition():
    return render_template("condition.html")


@app.route("/search")
@login_required
def search():

    IN=db.execute("SELECT * FROM registered WHERE State = ? AND Bloodtype=?",request.args.get("searchstate"),request.args.get("searchblood"))

    return render_template("search.html",information=IN)




@app.route("/info")
@login_required
def info():
    return render_template("info.html")





@app.route("/signup",methods=["GET","POST"])
def signup():
    if request.method=="POST":

        #ensure username was provided
        if not request.form.get("username"):
            return render_template("errorlogsign.html",code=1)
        #ensure password was submitted
        elif not request.form.get("password"):
            return render_template("errorlogsign.html",code=2)

        #ensure that the username and password doesn't already exists
        rows=db.execute("SELECT * FROM signup WHERE username = ?",request.form.get("username"))
        if len(rows)!=0:
            return render_template("errorlogsign.html",code=4)

        #signup the user
        db.execute("INSERT INTO signup(Username,hash)VALUES(?,?)",request.form.get("username"),generate_password_hash(request.form.get("password")))

        #log the user in
        rows=db.execute("SELECT * FROM signup WHERE username=?",request.form.get("username"))
        session["user_id"]=rows[0]["Id"]

         # Redirect user to home page
        return redirect("/")
    else:
      return render_template("signup.html")

@app.route("/login", methods=["GET","POST"])
def login():

    # Forget any user_id
    session.clear()

    if request.method=="POST":

        #ensure username was provided
        if not request.form.get("username"):
            return render_template("errorlogsign.html",code=1)
        #ensure password was submitted
        elif not request.form.get("password"):
            return render_template("errorlogsign.html",code=2)

         # Query database for username
        rows = db.execute("SELECT * FROM signup WHERE Username = ?", request.form.get("username"))


        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return render_template("errorlogsign.html",code=3)


        # Remember which user has logged in
        session["user_id"] = rows[0]["Id"]

         # Redirect user to home page
        return redirect("/")
    else:
      return render_template("login.html")




@app.route("/logout")
@login_required
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/deregister")
@login_required
def deregister():
    rows=db.execute("SELECT * FROM registered WHERE Id=?",session["user_id"])
    if(len(rows)==0):
        return render_template("error.html",code=8)



    db.execute("DELETE FROM registered WHERE Id=?",session["user_id"])
    return render_template("error.html",code=7)








