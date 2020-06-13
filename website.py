from flask import Flask, redirect, url_for, render_template
import os

app = Flask(__name__)

files_folder = os.path.join('static')

@app.route("/")
@app.route("/index")
def home():
    background_filename = os.path.join(files_folder, "BlurredPurdueBackground.jpg")
    return render_template("index.html", background=background_filename)

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run()
