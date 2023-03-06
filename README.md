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
    3.6 Check your empty web app now, you should see a 'Hello from Flask!' message when you access the home page. Check the code that was created in app.py, Python Anywhere requires you to tweak a few things, i.e you do not call app.run() directly from your code (within an if based on __name__ is ok). You also get a configuration file called something like ``/var/www/username_pythonanywhere_com_wsgi.py``, there is important configuration there for starting your app the right way:

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

    This guide explains more in depth how to deal with Flask in Python Anywhere:
    https://help.pythonanywhere.com/pages/Flask


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

    Optionally:
    ```
    git branch --set-upstream-to=origin/main master
    ```


## Setting up the map demo

Setup a virtual env (https://help.pythonanywhere.com/pages/RebuildingVirtualenvs/):

```
mkvirtualenv --python=python3.10 webapp-virtualenv
workon webapp-virtualenv
pip install -r requirements.txt
```
Also you need to set the virtual env path on the config page of the web app


## Setting ENV variables in Python anywhere

https://help.pythonanywhere.com/pages/environment-variables-for-web-apps/

```
workon webapp-virtualenv
pip install python-dotenv
```

Save the secrets in an ```.env file (and keep this always out of git!!!!!):

```
echo "export GOOGLE_MAPS_API_KEY=somethingelse" >> .env
```

Update the wsgi file:
```
# This file contains the WSGI configuration required to serve up your
# web application at http://<your-username>.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# The below has been auto-generated for your Flask project

import sys
import os
from dotenv import load_dotenv

# add your project directory to the sys.path
project_home = '/home/mduhagon/class-06-03-23'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

load_dotenv(os.path.join(project_home, '.env'))

# import flask app but need to call it "application" for WSGI to work
from app import app as application  # noqa
```

## What to use as a database from Python anywhere?


Unfortunately Python anywhere free version does not include Postgres or PostGIS (the geospatial functions)
An alternative is to use MongoDB Atlas, a NoSQL store that does provide geospatial capabilities,
but, also unfortunate! flask libs for Mongo don't seem to support geospatial data, so... it is 
possible still to use Mongo, but we won't use any geospatial features, yust store regular data there.

For this, you need to use the following library instead of SQLAlchemy:

https://pypi.org/project/flask-mongoengine/

And setup a DB / Cluster in Mongo DB Atlas site:
https://www.mongodb.com/atlas/database

The Mongo DB access details will need to be set as environment variables 
(so they are not part of your code, which is publicly visible in git):

```
export DATABASE_USER=username
export DATABASE_PASS=password
export DATABASE_HOST=mongodb+srv://clustername.xxxxx.mongodb.net/clustername
```

Initialize MySQL:
- Provide a password. Save it somewhere local for use from the code later.

You cannot connect to the DB in PythonAnywhere from the outside with a free account:
(https://help.pythonanywhere.com/pages/AccessingMySQLFromOutsidePythonAnywhere/)

So, to use MySQl locally, you need to install the DB engine:
https://dev.mysql.com/downloads/mysql/
You will be asked to set a root account password, set it and sotre it somewhere local for use from the code later. 


sudo apt-get install libmysqlclient-dev