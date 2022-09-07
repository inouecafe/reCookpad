from flask import Blueprint, render_template

recookpadSite = Blueprint(
    "recookpadSite",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="static/recookpadSite"
)

@recookpadSite.route('/')
def index():
    return render_template("index.html")