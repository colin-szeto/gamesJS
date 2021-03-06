from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/animation")
def animation():
    return render_template("animation.html")

@app.route("/line")
def line():
    return render_template("drawLine.html")

@app.route("/multiAnimation")
def animationMulti():
    return render_template("animationMulti.html")

@app.route("/ledDraw")
def ledDraw():
    return render_template("ledDraw.html")


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, host='127.0.0.1', port='5000')