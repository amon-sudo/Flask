from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# route.
@app.route("/<name>")
# defining the pages
def home(name):
    return render_template("index.html" )

@app.route("/login", method= ["POST", "GET"])

def login():
    return render_template("login.html")


@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}<h1>"
    


if __name__ == "__main__":
    app.run(debug=True)