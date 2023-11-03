# Flask REST API Template

This repository contains the template to kickstart the development of REST API project using Flask.

Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.

# Getting started

Note: Using a virtual environment is recommended.

To get started, use this repository as a template and install the dependencies using the following commands:

```bash
pip install -r requirements.txt
```

To run the API, use the following command:

Before running the command, make sure to have the environment variable from the `.env.sample` file set up in the `.env` file.

```bash
flask run # or python application.py
```

This will start the API on localhost:5000.

You can use your favorite API client to test the API.

Try to send a `GET` request to the `/` endpoint, the default healthcheck endpoint. This should return `200` if set up properly.
