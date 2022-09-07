from flask import Flask

def create_app():
    app = Flask(__name__)
    from apps.recookpadSite import views
    app.register_blueprint(views.recookpadSite, url_prefix="/")
    return app