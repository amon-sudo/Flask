from flask import Flask, render_template, Blueprint


second = Blueprint("second", __name__, static_folder="static", template_folder="templates")

@second.route("/home")
@second.route("/")
def home():
    return render_template("home.html")


@second.route("/test")
def test():
    return "<h1>welcome tom ymy home page my nigga</h1>"