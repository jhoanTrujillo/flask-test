import os
import json
from flask import Flask, render_template

app = Flask(__name__)

# Helper mixing to add routes and render them using the function below them
@app.route("/")
def index():

  # Renders the page template called in the string
  return render_template("index.html")


@app.route("/about/<member_name>")
def about_member(member_name):
   member = {}
   with open("data/company.json", "r") as json_data:
     data = json.load(json_data)
     for obj in data:
        if obj["url"] == member_name:
           member = obj

   return "<h1>" + member["name"] + "</h1>"

@app.route("/about")
def about():
   # Empty array to hold array of objects in company.json file
   data = []

   # We open the company.json file as "r" (read only) with the name json_data
   with open("data/company.json", "r") as json_data:
     
     # using json module we load the json_data variable in the data array
     data = json.load(json_data)
   # We can pass data after the about tag using comas
   return render_template("about.html", page_title="About", company=data)


@app.route("/careers")
def careers():
   return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "8000")),
        # Debug should be change to False when on production
        debug=True
    )
    app.config['TEMPLATES_AUTO_RELOAD'] = True

