from flask import Flask, render_template

app = Flask(__name__)

class GalileanMoons:
    def __init__(self, first, second, third, fourth, fifth):
      self.first = first
      self.second = second
      self.third = third
      self.fourth = fourth
      self.fifth = fifth      

@app.route("/")
def hello_world():
    return render_template("first_page.html")


@app.route("/second/")
def hello_world_fancy():
    orange_amount = 10
    apple_amount = 20
    name = "Alice"
    
    kwargs = {
        "orange_amount": orange_amount,
        "apple_amount": apple_amount,
        "name": name,
    }
    
    return render_template(
        "second_page.html", **kwargs)


@app.route("/data-structures/")
def render_data_structures():
    
    moons = GalileanMoons("IO","Europa","Ganymede","Callisto","Unknown")
    
    movies = ["Up!","Shrek","Finding Nemo"]
    
    car = {
        "brand": "Tesla",
        "model": "Roadster",
        "year": "2020",
    }
    
    return render_template(
        "data_structures.html",movies=movies, car=car, moons=moons)


@app.route("/conditionals/")
def render_conditionals():
    company = "Microsoft"
    
    return render_template("conditionals.html", company=company)


@app.route("/forloop/")
def render_forloop():
    planets = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune",
    ]
    
    return render_template("forloop.html",planets=planets)


@app.route("/forloop-and-conditionals/")
def render_forloopandconditionals():
    user_os = {
        "Bob Smith": "Windows",
        "Anne Pun": "MacOS",
        "Adam Lee": "Linux",
    }
    
    return render_template("forloopandconditionals.html",user_os=user_os)
















if __name__ == '__main__':
  app.run