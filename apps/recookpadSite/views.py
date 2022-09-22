from flask import Blueprint, render_template
from apps.recookpadSite.forms import TestForm
from apps.recookpadSite.models import Test
from apps.app import db

#--------------------------#
#作業中
#福永 = なし
#井上 = なし

#メモ
#git pull origin main
#git push origin main
#--------------------------#

recookpadSite = Blueprint(
    "recookpadSite",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="static/recookpadSite"
)
auth = Blueprint(
    "auth",
    __name__,
    template_folder="templates",
    static_folder="static"
)

@recookpadSite.route('/')
def index():
    return render_template("index.html")



@recookpadSite.route('/register')
def register():
    return render_template("register.html")



@recookpadSite.route('/login')
def login():
    return render_template("auth/login.html")



@recookpadSite.route('/create')
def create():
    return render_template("create.html")



@recookpadSite.route('/show')
def show():
    return render_template("show.html")



@recookpadSite.route('/mypage')
def mypage():
    return render_template("mypage.html")















@recookpadSite.route('/test', methods=["POST","GET"])
def test():
    testForm = TestForm()
    message = ''

    if testForm.is_submitted():
        message = testForm.test.data or ''
        if message != '':
            test = Test(text=message)
            db.session.add(test)
            db.session.commit()



    print(message)
    data = {
        "form": testForm,
        "text": message
    }
    return render_template("test.html",data=data)