from flask import Flask
from os import environ, makedirs
from pathlib import Path


def create_app(config_overrides=None):
    app = Flask(__name__, instance_relative_config=True)

    instance_dir = Path(app.instance_path)
    makedirs(instance_dir, exist_ok=True)

    app.config["SQLALCHEMY_DATABASE_URI"] = environ.get(
        "SQLALCHEMY_DATABASE_URI",
        f"sqlite:///{instance_dir / 'db.sqlite'}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if config_overrides:
        app.config.update(config_overrides)

    from todo.models import db
    from todo.models.todo import Todo

    db.init_app(app)

    with app.app_context():
        db.create_all()
        db.session.commit()

    from todo.views.routes import api
    app.register_blueprint(api)

    return app