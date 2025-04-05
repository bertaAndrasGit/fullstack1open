import datetime
import os
from dotenv import load_dotenv
from flask import Flask,render_template,request
from pymongo import MongoClient

load_dotenv()

def create_app():
    app = Flask(__name__)
    #TODO: hide login details before git push (DONE (ADDED GITIGNORE AND .ENV))
    #a flask termináljában futtasd
    try:
        #hogy ne közvetlenöl bele legyen égetve a castlakozási URI ezért egy környezeti változót hozhatunk létre rá (.env ben)
        client = MongoClient(os.getenv("MONGODB_URI"))
        app.db = client.microblog
    except Exception as e:
        print(f"Error: {e}")
    

    @app.route("/", methods=["GET","POST"])
    def home():
        #print(list(app.db.entries.find({})))
        #a request importot nem lehet fuc on kívül használni
        # mivel nem tudunk a requestre válaszolni amit a böngésző "csinált"
        if request.method == "POST":
            # a "content" a textarea-nak a neve ami a formban van.
            # ha más lenne a neve vagy nem létezne,
            # akkor None értéket kapnánk vissza.
            entry_content = request.form.get("content")
            formatted_date = datetime.datetime.today().strftime("%y-%m-%d")
            app.db.entries.insert_one({"content": entry_content, "date": formatted_date})
            
            
        entries_with_dates = [
            (
                entry["content"],
                entry["date"],
                datetime.datetime.strptime(entry["date"],"%y-%m-%d").strftime("%b %d")
            ) for entry in app.db.entries.find({})
        ]
        
        
        return render_template("home.html",entries=entries_with_dates)

    if __name__ == "__main__":
        app.run
        
    return app