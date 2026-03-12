from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# route.
@app.route("/")
# defining the pages
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()