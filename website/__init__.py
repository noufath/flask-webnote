from flask import Flask
from .views import views
from .auth import auth


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'lm^-)t38ph@gbgbv$rk$moh-26t@rk&5q=2pl5v&sydvju94o^'

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app






