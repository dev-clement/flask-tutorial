import os

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='48e1f3b0c4024756807d5e19607812b3',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )
    if test_config is None:
        # Load the instance config if that exists
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test_config if it is passed in
        app.config.from_mapping(test_config)
    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    # A simple HTML page saying HelloWorld
    @app.route('/home')
    def hello():
        return "Hello World !"
    from . import db
    db.init_app(app=app)
    from . import auth, blog
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    return app
