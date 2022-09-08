from flask import Flask
from flask_wtf import CSRFProtect

csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="AKJNAJKAKJSFJMF<JFI"
    )
    csrf.init_app(app)
    from apps.recookpadSite import views
    app.register_blueprint(views.recookpadSite, url_prefix="/")
    return app