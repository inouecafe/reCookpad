from flask import Blueprint, render_template

#--------------------------#
#作業中
#福永 = なし
#井上 = なし
#--------------------------#

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



@recookpadSite.route('/register')
def register():
    return render_template("register.html")



@recookpadSite.route('/login')
def login():
    return render_template("login.html")



@recookpadSite.route('/create')
def create():
    return render_template("create.html")



@recookpadSite.route('/show')
def show():
    return render_template("show.html")



@recookpadSite.route('/mypage')
def mypage():
    return render_template("mypage.html")