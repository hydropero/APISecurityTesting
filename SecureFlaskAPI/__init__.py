from flask import Flask, Blueprint

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjsdsisgdigr erohegrgiergi'

    from .views import views
    from .auth import auth
    app.register_blueprint(auth, url_prefix='/auth/')
    app.register_blueprint(views, url_prefix='/')
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
#
    return app