from flask import (Blueprint, 
                   url_for, 
                   current_app, 
                   abort,
                   render_template,
                   session,
                   redirect,
                   request,
                   flash
                   )

from dataclasses import asdict
import uuid
import datetime
from passlib.hash import pbkdf2_sha256
import functools

from .forms import MovieForm, ExtendedMovieForm, RegisterForm, LoginForm
from .models import Movie, User


pages = Blueprint(
    "pages", __name__, template_folder="templates", static_folder="static"
)

def login_required(route):
    @functools.wraps(route)
    def route_wrapper(*args,**kwargs):
        if session.get("email") is None:
            return redirect(url_for(".login"))
        
        return route(*args,**kwargs)
    
    return route_wrapper



@pages.route("/")
@login_required
def index():
    user_data = current_app.db.user.find_one({"email": session["email"]})
    user = User(**user_data)
    
    movie_data = current_app.db.movies.find({"_id": {"$in": user.movies}})
    movies = [Movie(**movie) for movie in movie_data]
    
    return render_template(
        "index.html",
        title="Movies Watchlist",
        movies_data=movies
    )
    

@pages.route("/register", methods=["GET", "POST"])
def register():
    if session.get("email"):
        return redirect(url_for(".index"))

    form = RegisterForm()
    
    if form.validate_on_submit():
        user = User(
            _id=uuid.uuid4().hex,
            email=form.email.data,
            password=pbkdf2_sha256.hash(form.password.data)
        )
        
        current_app.db.user.insert_one(asdict(user))
        
        flash("User registered successfully", "success")
        
        return redirect(url_for(".login"))
    
    return render_template(
        "register.html",               
        title="Movies Watchlist - Register", 
        form=form
    )
    
@pages.route("/login", methods=["GET", "POST"])
def login():
    if session.get("email"):
            return redirect(url_for(".index"))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        user_data = current_app.db.user.find_one({"email": form.email.data})
        if not user_data:
            flash("Login credentials not correct", category="danger")
            return redirect(url_for(".login"))
        user = User(**user_data)
        
        if user and pbkdf2_sha256.verify(form.password.data, user.password):
            session["user_id"] = user._id
            session["email"] = user.email
            
            return redirect(url_for(".index"))
        
        flash("Login credentials not correct", category="danger")
    
    return render_template(
        "login.html",
        title="Movie Watchlist - Login",
        form=form
    )
    
@pages.route("/logout")
def logout():
    #session.clear() vagy ha a sessionből csak bizonyos elemeket akarunk kitörölni:
    del session["user_id"]
    del session["email"]
    
    return redirect(url_for(".login"))
        
    
@pages.get("/movie/<string:_id>")
def movie(_id: str):
    movie_data = current_app.db.movies.find_one({"_id": _id})
    if not movie_data:
        abort(404)
    movie = Movie(**movie_data)
    return render_template("movie_details.html",movie=movie)
    

@pages.route("/add",methods=["GET","POST"])
@login_required
def add_movie():
    form = MovieForm()
    
    """ugyan azt csinálja mint a if request.method == "POST":
        csak ez egyszerre validálja a formot is"""
    if form.validate_on_submit():
        movie = Movie(
            _id = uuid.uuid4().hex,
            title = form.title.data,
            director = form.director.data,
            year = form.year.data
        )
        
        current_app.db.movies.insert_one(asdict(movie))
        
        current_app.db.user.update_one(
            {"_id": session["user_id"]}, {"$push": {"movies": movie._id}}
        )
        
        
        return redirect(url_for(".movie", _id=movie._id))
    
    return render_template("new_movie.html",
                           title="Movies Watchlist - Add Movie",
                           form=form)


@pages.route("/edit/<string:_id>", methods=["GET","POST"])
@login_required
def edit_movie(_id:str):
    movie_data = current_app.db.movies.find_one({"_id": _id})
    
    if not movie_data:
        abort(404)
        
    movie = Movie(**movie_data)
    form = ExtendedMovieForm(obj=movie)
    if form.validate_on_submit():
        movie.title = form.title.data
        movie.year = form.year.data
        movie.cast = form.cast.data
        movie.series = form.series.data
        movie.tags = form.tags.data
        movie.description = form.description.data
        movie.video_link = form.video_link.data

        current_app.db.movies.update_one({"_id":_id}, {"$set": asdict(movie)})
        return redirect(url_for(".movie",_id=movie._id))
    return render_template("movie_form.html", movie=movie,form=form)


@pages.get("/movie/<string:_id>/rate")
@login_required
def rate_movie(_id):
    rating = int(request.args.get("rating"))
    current_app.db.movies.update_one({"_id":_id}, {"$set": {"rating":rating}})

    return redirect(url_for(".movie", _id=_id))


@pages.get("/movie/<string:_id>/watch")
@login_required
def watch_today(_id):
    current_app.db.movies.update_one({"_id":_id}, {"$set": {"last_watched":datetime.datetime.today()}})
    
    return redirect(url_for(".movie", _id=_id))
    
    
@pages.get("/toggle-theme")
def toggle_theme():
    current_theme = session.get("theme")
    if current_theme == "dark":
        session["theme"] = "light"
    else:
        session["theme"] = "dark"
    """Because all endpoint have to return someting, it will return the same page """
    return redirect(request.args.get("current_page"))