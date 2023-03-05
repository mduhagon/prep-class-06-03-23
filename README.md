# Python Anywhere Setup

## Get your account ready

1. If you have not done it so far, register for a Beginner Free plan in https://www.pythonanywhere.com/

2. The plan has limitations, so if you already had an account and some website running, you cannot have two.

## Create a web app

3. You will upload your code as a web app. It is possible to start a Web app with a Flask mininmal app.py:


    3.1 Go to Web > Ad a new web app
    3.2 In the free plan you cannot choose your domain name, one is given, accept
    3.3 Select Flask as Python Web Framework
    3.4 Python version: 3.10
    3.5 Set a path for your initial app file, like: ``/home/mduhagon/class-06-03-23/app.py``
    3.6 Check your empty web app now, you should see a 'Hello from Flask!' message when you access the home page. Check the code that was created in app.py, Python Anywhere requires you to tweak a few things, i.e you do not call app.run() from your code. You also get a configuration file called something like ``/var/www/username_pythonanywhere_com_wsgi.py``, there is important configuration there for starting your app the right way:

    ```
    # This file contains the WSGI configuration required to serve up your
    # web application at http://<your-username>.pythonanywhere.com/
    # It works by setting the variable 'application' to a WSGI handler of some
    # description.
    #
    # The below has been auto-generated for your Flask project

    import sys

    # add your project directory to the sys.path
    project_home = '/home/mduhagon/class-06-03-23'
    if project_home not in sys.path:
        sys.path = [project_home] + sys.path

    # import flask app but need to call it "application" for WSGI to work
    from app import app as application  # noqa
    ```

    Starting app.py:

    ```
    # A very simple Flask Hello World app for you to get started with...

    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello from Flask!'
    ```


## Make your web app use the code from your git repo

4. You will need a Bash console to execute git commands, and clone / pull your repo
    4.1 Go to Consoles > Start a new console > Bash
    4.2 cd into your web app root folder and clone the repo (if it is not public you will have to setup credentials)
    ```
    cd class-06-03-23
    rm app.py
    git init
    git remote add origin https://github.com/mduhagon/prep-class-06-03-23.git
    git remote -v
    git pull origin main
    ```