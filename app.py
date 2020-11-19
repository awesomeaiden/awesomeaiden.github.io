from flask import Flask, send_from_directory, render_template
from flask_frozen import Freezer
import os, json, sys

app = Flask(__name__)
freezer = Freezer(app)

images_folder = os.path.join('static/images/')
files_folder = os.path.join('static/files/')

class Project(object):
    def __init__(self, name="name", desc="desc", image="image", link="link"):
        self.name = name
        self.desc = desc
        self.image = image
        self.link = link

    def __repr__(self):
        return "Project: " + self.name

def json2projs(json_file):
    json_dict = json.load(json_file)
    projects = []
    for item in json_dict:
        projects.append(Project(
            name=json_dict[item]['name'],
            desc=json_dict[item]['desc'],
            image=json_dict[item]['image'],
            link=json_dict[item]['link']
        ))
    return projects


@app.route("/")
@app.route("/index.html")
def home():
    projects = None
    with open('projects.json') as json_file:
        projects = json2projs(json_file)
    print(projects)
    return render_template("index.html", images=images_folder, projects=projects)

@app.route("/resume")
@app.route("/resume.pdf")
def resume():
    return send_from_directory(files_folder, "resume.pdf")

@app.route("/contact")
@app.route("/contact.html")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run()
