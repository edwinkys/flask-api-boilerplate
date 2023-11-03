from flask import Flask, jsonify
from extensions import register_extension


def create_app(settings_override=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object("config.settings")
    app.config.from_pyfile("settings.py", silent=True)

    if settings_override:
        app.config.update(settings_override)

    # Register blueprints.

    # Register extensions.
    register_extension(app)

    return app


# This is required by Elastic Beanstalk.
app = application = create_app()


@app.route("/", methods=["GET"])
def healthcheck():
    return jsonify({"status": "functional"}), 200


# run the app.
if __name__ == "__main__":
    app.run()
