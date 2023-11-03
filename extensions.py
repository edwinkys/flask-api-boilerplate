# For every Flask extension we have,
# we initialize it and add the init_app
# method to register_extension.

from flask_cors import CORS

# Initialize extensions.
cors = CORS()


def register_extension(app):
    cors.init_app(app)
