from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# route.
@app.route("/<name>")
# defining the pages
def home(name):
    return render_template("index.html", content ="Amon" )


if __name__ == "__main__":
    app.run(debug=True)