from flask import Flask,render_template

app = Flask(__name__)


def is_square(value):
    return (value ** 0.5).is_integer()

app.jinja_env.tests["is_square"] = is_square

@app.route("/",methods=["GET","POST"])
def todo():
    return render_template("fizzbuzz.html")