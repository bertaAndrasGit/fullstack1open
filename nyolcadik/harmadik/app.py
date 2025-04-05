from flask import Flask,render_template



app = Flask(__name__,static_folder="assets")



@app.route("/",methods=["GET","POST"])
def home():
    return render_template("home.html")



@app.route("/login",methods=["GET","POST"])
def login():
    return render_template("login.html")
    
    
    
@app.route("/signup",methods=["GET","POST"])
def signup():
    return render_template("signup.html")



if __name__ == "__main__":
    app.run