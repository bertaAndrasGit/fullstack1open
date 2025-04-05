from flask import Blueprint,abort,render_template,request,redirect,url_for,current_app


pages = Blueprint("portfolio",__name__,template_folder="emplates",static_folder="static")

projects = [
    {"name":"Habit tracking app with Python and MongoDB",
     "thumb":"img/habit-tracking.png",
     "hero":"img/habit-tracking-hero.png",
     "categories":["python","web"],
     "slug":"habit-tracking",
     "prod":"https://udemy.com",
     },
    {"name":"Microblog for my stuff",
     "thumb":"img/personal-finance.png",
     "hero":"img/microblog-hero.png",
     "categories":["python","web"],
     "slug":"microblog",
     },
    {"name":"Movie watchlist for the movies that i like",
     "thumb":"img/rest-api-docs.png",
     "hero":"img/movie-watchlist-hero.png",
     "categories":["python","web"],
     "slug":"movie-watchlist",
     },
]

slug_to_project = {project["slug"]: project for project in projects }
"""
kb így fog kinézni:

{habit-tracking: {"name":"Habit tracking app with Python and MongoDB",
                  "thumb":"img/habit-tracking.png",
                  "hero":"img/habit-tracking-hero.png",
                  "categories":["python","web"],
                  "slug":"habit-tracking",
                  "prod":"https://udemy.com",
                  }
}...
"""

@pages.route("/")
def home():
    return render_template("home.html",projects=projects)


@pages.route("/about")
def about():
    return render_template("about.html")


@pages.route("/contact")
def contact():
    return render_template("contact.html")

@pages.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html",
                           project=slug_to_project[slug])

@pages.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404