# hobby-helper Project
Web app to help with microgreens, espresso, and more

## Currently on [Step 3](#3-create-a-new-django-project)
___

Table of Contents
=================
* [Project Overview](#project-overview)
* [Environment Prep](#env-prep)
* [ChatGPT Prompt Suggestions](#chat-gpt-plus-prompts)
* [App Steps](#app-steps)
    * [1: Plan and design your app](#1-plan-and-design-your-app)
    * [2: Set up your development environment](#2-set-up-your-development-environment)
    * [3: Create a new Django project](#3-create-a-new-django-project)
    * [4: Define your Django models](#4-define-your-django-models)
    * [5: ](#5-set-up-your-postgresql-database)
    * [6: ](#6-create-your-django-views)
    * [7: ](#7-define-your-django-url-patterns)
* [Next Steps](#next-step-questions)
* [Tech Used](#list-of-tech-used)


# Project Overview

## Espresso Tracker

## Microgreen/Sprout Tracker

## Plant Tracker

## Workout Tracker (??)

## Cooking (??)

## Mountain Bike Maintenance Tracker (??)

----------------------------------------------------
# Env prep
1. Ensure there is a .venv folder in the base directory
2. In the terminal, call pipenv shell to activate the virtual environment
3. 

# Chat GPT plus prompts
[Back to Table of Contents](#table-of-contents)
* You are an expert web app developer and designer specializing in django.  I want to build a web app with django, postgresql, and react.  This app will help users to track the quality of their home-made espresso by factors such as grind size, brew time, and yield.  I want to develop locally and eventually deploy to a web host with cicd.  What are the steps I need to take from start to finish? I'll refer to these steps as "app steps"
* can you rewrite these steps as markdown code for me to copy

```
Help me with this step:
<Plan and design your app - Define the scope of your app, create wireframes, design the user interface, and determine the features and functionality that you want to include in your app.>

Please output as markdown code so I can easily copy it.  
```

------------------------------------------------------------
# App Steps
[Back to Table of Contents](#table-of-contents)

1. [Plan and design your app](#1-plan-and-design-your-app) - Define the scope of your app, create wireframes, design the user interface, and determine the features and functionality that you want to include in your app.

2. [Set up your development environment](#2-set-up-your-development-environment) - Install Python, Django, PostgreSQL, and React. You may also want to use a virtual environment to keep your development environment isolated from your system.

3. [Create a new Django project](#3-create-a-new-django-project) - Use the Django command line interface to create a new project, which will create the basic structure and files for your web app.

4. [Define your Django models](#4-define-your-django-models) - Create the Django models that will represent the data you want to track in your app, such as espresso recipes and brewing data.

5. [Set up your PostgreSQL database](#5-set-up-your-postgresql-database) - Install and configure PostgreSQL, create a new database, and configure your Django project to connect to it.

6. [Create your Django views](#6-create-your-django-views) - Define the views that will handle requests from your web app and render the appropriate responses.

7. [Define your Django URL patterns](#7-define-your-django-url-patterns) - Create URL patterns that will map to your views, allowing your app to respond to requests at specific URLs.

8. [Set up your React app]() - Create a new React app and set up the necessary dependencies and configuration files.

9. [Create your React components]() - Define the React components that will display your app's user interface and interact with your Django backend.

10. [Connect your React app to your Django backend]() - Use AJAX or a similar method to connect your React app to your Django views and retrieve data from your PostgreSQL database.

11. [Test your app]() - Test your app locally to ensure that it is functioning as intended and that all features are working correctly.

12. [Deploy your app]() - Set up a production server, deploy your app, and configure continuous integration and continuous deployment (CI/CD) to automate the deployment process.

------------------------------------------------------------
## 1: Plan and design your app
[Back to Table of Contents](#table-of-contents)

1. Define the scope of your app:
    
    - Determine the purpose of your app and what problems it will solve.
    - Identify your target audience and their needs.
    - Write a brief description of your app's main features and functionality.

2. Create wireframes:

    - Sketch out the basic layout and structure of your app using pen and paper or a digital tool.
    - Consider the user experience and how users will interact with your app.
    - Refine your wireframes based on feedback and testing.

3. Design the user interface:

    - Choose a color scheme and typography that fits your brand and target audience.
    - Create mockups of your app's screens and design the interface elements.
    - Refine your designs based on feedback and testing.

4. Determine the features and functionality:

    - Make a list of all the features and functionality you want to include in your app.
    - Prioritize these features based on their importance and impact on the user experience.
    - Consider any potential technical challenges or limitations that may affect your ability to implement certain features.

5. Create a detailed project plan:

    - Break down your app development into smaller, manageable tasks.
    - Determine the estimated time and resources required for each task.
    - Set deadlines and milestones to keep your project on track.

By following these steps, you can effectively plan and design your app, ensuring that it meets the needs of your target audience and provides a great user experience.

------------------------------------------------------------
## 2: Set up your development environment
[Back to Table of Contents](#table-of-contents)

1. Install Python: 

    - Download the latest version of Python from the official website at https://www.python.org/downloads/.
    - Run the installer and follow the prompts to complete the installation.
    - Verify that Python is installed correctly by opening a command prompt or terminal window and entering the command `python --version`.

2. Install PostgreSQL:

    - Download and install the latest version of PostgreSQL from the official website at https://www.postgresql.org/download/.
    - Follow the prompts to complete the installation, making sure to remember the username and password you set for the database.
    - Verify that PostgreSQL is installed correctly by opening a command prompt or terminal window and entering the command `psql --version`.

3. Install Pipenv: 

    - Open a command prompt or terminal window and enter the command `pip install pipenv`.
    - Wait for the installation to complete.

4. Set up a virtual environment:

    - Navigate to the directory where you want to create your project.
    - Create a new directory called `.venv` to store the virtual env
    - Enter the command `pipenv shell` to create a new virtual environment and activate it.
    - All subsequent commands will be run within this virtual environment.
    - if you have a pipfile already, run `pipenv install` to install all python modules specified in the pipfile.

5. Install Django and other dependencies (not needed if you have pip file): 

    - Enter the command `pipenv install django djangorestframework django-cors-headers psycopg2-binary`.
    - This command will install Django and other necessary dependencies within the virtual environment.

6. Install Node.js and React: 

    - Install Node.js from the official website at https://nodejs.org/en/download/.
    - Open a command prompt or terminal window and enter the command `npm install -g create-react-app` to install the create-react-app package globally.
    - **TODO** Create a new React app by entering the command `npx create-react-app my-app` where "my-app" is the name you choose for your app.
    - Wait for the installation to complete.

After following these steps, you should have a fully functional development environment with Python, Django, PostgreSQL, and React installed using Pipenv.

**CURRENT**
------------------------------------------------------------
## 3: Create a new Django project
[Back to Table of Contents](#table-of-contents)

1. Open a command prompt or terminal window.

2. Navigate to the directory where you want to create your Django project.

3. Enter the following command to create a new Django project:

```
django-admin startproject myproject
```

Replace "myproject" with the name you want to give your project. PWD - I'm going with "hobby_helper"

4. This will create a new directory called "myproject" (or whatever name you chose) with the following files and directories:

```
myproject/
├── manage.py
└── myproject/
├── init.py
├── settings.py
├── urls.py
└── wsgi.py
```

- The `manage.py` file is used to manage various aspects of your Django project, such as running the development server or applying database migrations.
- The `myproject/` directory contains the main settings and configuration files for your project.
- The `__init__.py` file is required to treat the directory as a Python package.
- The `settings.py` file contains all the settings for your Django project, such as the database configuration, installed apps, middleware, and more.
- The `urls.py` file contains the URL routing configuration for your project.
- The `wsgi.py` file is used for deploying your project to a WSGI (Web Server Gateway Interface) server, such as Apache or Nginx.

5. You can now proceed to the next steps to create your Django models, views, and templates.

After following these steps, you should have a new Django project with the basic structure and files necessary to start building your web app.

------------------------------------------------------------
## 4: Define your Django models
[Back to Table of Contents](#table-of-contents)

Models represent a database table and its associated fields, and they provide an object-oriented way to interact with the database. Each model typically corresponds to a single database table, and the fields of the model define the columns of the table.

Django models also provide a powerful ORM (Object-Relational Mapping) that allows you to interact with the database using Python objects rather than SQL. This means that you can use Python code to create, read, update, and delete records in the database, rather than writing raw SQL queries.

To define your Django models, follow these steps:

1. Create a new file called `models.py` in your Django app directory.

2. Import the `django.db` module at the top of your file:
```
from django.db import models
```

3. Define your models using Django's built-in `Model` class:
```
class Recipe(models.Model):
    name = models.CharField(max_length=255)
    grind_size = models.CharField(max_length=255)
    brew_time = models.DurationField()
    yield = models.DecimalField(max_digits=5, decimal_places=2)
```
This example defines a `Recipe` model with four fields: `name`, `grind_size`, `brew_time`, and `yield`.

4. Use Django's built-in field types to define the types and constraints of your fields. Common field types include:
- `CharField` for text fields
- `IntegerField` for integer fields
- `FloatField` for floating point fields
- `BooleanField` for boolean fields
- `DateTimeField` for date and time fields
- `DurationField` for time duration fields
- `DecimalField` for decimal fields

5. Use Django's built-in model relationships to define relationships between your models. Common relationship types include:
- `ForeignKey` for one-to-many relationships
- `OneToOneField` for one-to-one relationships
- `ManyToManyField` for many-to-many relationships

6. Run migrations to create and update your database schema:
```
python manage.py makemigrations
python manage.py migrate

```

------------------------------------------------------------
## 5: Set up your PostgreSQL database
[Back to Table of Contents](#table-of-contents)

To set up your PostgreSQL database for your Django project, follow these steps:

1. Install PostgreSQL on your machine. You can download PostgreSQL from the official website (https://www.postgresql.org/download/) or use a package manager for your operating system.

2. Create a new database for your Django project. You can do this using the createdb command-line tool that comes with PostgreSQL. For example:
```
createdb myproject
```
This will create a new database called myproject that you can use for your Django project.

3. Create a new database user for your Django project. You can do this using the createuser command-line tool that comes with PostgreSQL. For example:
```
createuser myuser --interactive
```

This will create a new user called myuser that you can use to connect to your database.

4. Set the DATABASES setting in your Django project's settings.py file to connect to your PostgreSQL database. For example:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myproject',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
This configuration tells Django to use the PostgreSQL database engine, and to connect to the myproject database using the myuser user and mypassword password. The HOST and PORT settings can be used to specify the location and port number of your PostgreSQL server, if necessary.

5. Run database migrations to create the necessary tables and schema for your Django app. You can do this using the following command:
```
python manage.py migrate

```
This will create the necessary tables in your PostgreSQL database based on the models you have defined in your Django app.

That's it! Your Django project should now be set up to use your PostgreSQL database. You can now use the Django ORM to interact with your database and create, read, update, and delete records as needed.

------------------------------------------------------------
## 6: Create your Django views
[Back to Table of Contents](#table-of-contents)

------------------------------------------------------------
## 7: Define your Django URL patterns
[Back to Table of Contents](#table-of-contents)

------------------------------------------------------------
## 8: 
[Back to Table of Contents](#table-of-contents)

------------------------------------------------------------
## 9: 
[Back to Table of Contents](#table-of-contents)

------------------------------------------------------------
## 10: 
[Back to Table of Contents](#table-of-contents)

------------------------------------------------------------
## 11: 
[Back to Table of Contents](#table-of-contents)

------------------------------------------------------------
## 12: 
[Back to Table of Contents](#table-of-contents)

------------------------------------------------------------
# Next Step Questions
[Back to Table of Contents](#table-of-contents)

* How do I secure my app?
* How do I invite users (friends and family) to use my app?
* How do I keep user data separate?
* How do I enable multiple users to share the same account/data?
* How do I backup data in the database?
* How do I make a real-time admin dashboard?

------------------------------------------------------------
# List of Tech Used 
[Back to Table of Contents](#table-of-contents)

* Python w/ Django
* PostgreSQL
* HTML/CSS
* React
* AJAX
* Git + Github
* Github Actions
* Cloud?