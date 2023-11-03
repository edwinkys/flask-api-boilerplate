from flask_cors import CORS

# Initialize extensions.
cors = CORS()


def register_extension(app):
    cors.init_app(app)
