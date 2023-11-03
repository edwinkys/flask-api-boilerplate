# Flask REST API Template

This repository contains the template to kickstart the development of REST API project using Flask.

Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.

# Getting started

Note: Using a virtual environment is recommended.

To get started, use this repository as a template and install the dependencies using the following commands:

```bash
pip install -r requirements.txt
```

Before running the app, make sure to have the environment variable from the `.env.sample` file set up in the `.env` file.

To run the API project on your local machine, use the following command:

```bash
flask run # or python application.py
```

This will start the API on localhost:5000. Please note that this command is only for development purposes. For production, use a WSGI server such as Gunicorn.

If you send a GET request to the root endpoint, you should get the following response:

```json
{ "status": "functional" }
```
