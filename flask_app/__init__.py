from flask import Flask
import config

def create_app(config=None):
    app = Flask(__name__)
    
    if app.config["ENV"] == 'production':
        app.config.from_object('config.ProductionConfig')
    else:
        app.config.from_object('config.DevelopmentConfig')

    if config is not None:
        app.config.update(config)

    from flask_app.views import (main_routes, user_routes)
    app.register_blueprint(main_routes.bp)
    app.register_blueprint(user_routes.bp, url_prefix='/api')
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)