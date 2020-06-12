from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "This is my website <h1>HELLO</h1>"

if __name__ == "__main__":
    app.run()
