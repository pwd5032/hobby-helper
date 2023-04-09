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
    * [5: Set up your ](#5-set-up-your-postgresql-database)
    * [6: Create your Django views](#6-create-your-django-views)
    * [7: Define your Django URL patterns](#7-define-your-django-url-patterns)
    * [8: Set up your React app](#8-set-up-your-react-app)
    * [9: Create your React components](#9-create-your-react-components)
    * [10: Connect your React app to your Django backend](#10-connect-your-react-app-to-your-django-backend)
    * [11: Test your app](#11-test-your-app)
    * [12: Deploy your app](#12-deploy-your-app)
* [Next Step Questions](#next-step-questions)
* [Proposed Next Steps](#proposed-next-steps)
* [List of Tech Used](#list-of-tech-used)


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

8. [Set up your React app](#8-set-up-your-react-app) - Create a new React app and set up the necessary dependencies and configuration files.

9. [Create your React components](#9-create-your-react-components) - Define the React components that will display your app's user interface and interact with your Django backend.

10. [Connect your React app to your Django backend](#10-connect-your-react-app-to-your-django-backend) - Use AJAX or a similar method to connect your React app to your Django views and retrieve data from your PostgreSQL database.

11. [Test your app](#11-test-your-app) - Test your app locally to ensure that it is functioning as intended and that all features are working correctly.

12. [Deploy your app](#12-deploy-your-app) - Set up a production server, deploy your app, and configure continuous integration and continuous deployment (CI/CD) to automate the deployment process.

13. [Next Steps](#next-step-questions) - What are the next steps I should take to improve my app?

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
    - Highly suggest you read [VS Code w/ React Tutorial](https://code.visualstudio.com/docs/nodejs/reactjs-tutorial)
    - Open a command prompt or terminal window and enter the command `npm install -g create-react-app` to install the create-react-app package globally.
    - **TODO** Create a new React app by entering the command `npx create-react-app my-app` where "my-app" is the name you choose for your app.
    - Wait for the installation to complete.

After following these steps, you should have a fully functional development environment with Python, Django, PostgreSQL, and React installed using Pipenv.

------------------------------------------------------------
## 3: Create a new Django project
[Back to Table of Contents](#table-of-contents)

1. Open a command prompt or terminal window.

2. Navigate to the directory where you want to create your Django project.

3. Enter the following command to create a new Django project:

```
django-admin startproject myproject .
```

Replace "myproject" with the name you want to give your project. PWD - I'm going with `hobby_helper`

Note the . at the end of the command. This tells Django to create the project files in the current directory rather than in a new subdirectory.

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

5. To create a new app within your project, run the following command:
```
python manage.py startapp myapp
```
Replace myapp with the name of your app.  I will use `espresso_tracker`

This will create a new directory called myapp within your Django project directory, along with some initial files and directories that are used to define the app.

6. To include your app in your project, you will need to add it to your project's list of installed apps. Open your project's `settings.py` file and add the name of your app to the `INSTALLED_APPS` list:
```
INSTALLED_APPS = [    ...    'myapp',]
```

7. You can now proceed to the next steps to create your Django models, views, and templates.

After following these steps, you should have a new Django project with the basic structure and files necessary to start building your web app.

### To Test Your App Locally

1. Open your terminal or command prompt.

2. Navigate to your Django project directory.

3. Run the following command to start the development server:
```
python manage.py runserver
```

4. If the server started successfully, you should see some output in your terminal that looks like this:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

5. Open a web browser and navigate to `http://localhost:8000/` or `http://127.0.0.1:8000/`. You should see the default Django welcome page, which indicates that your server is up and running.

6. To test your app specifically, you will need to navigate to the appropriate URL for your views. For example, if you have a view that displays a list of items at `/items/`, you would navigate to `http://localhost:8000/items/` or `http://127.0.0.1:8000/items/` to test it.

7. As you make changes to your code, you can refresh your web browser to see the updated results. If you encounter any errors or issues, Django will display them in your terminal output or in the browser window, depending on the type of error.


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

Example models.py file:
```
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    num_pages = models.IntegerField()
    is_available = models.BooleanField(default=True)
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
This will create a new database called myproject that you can use for your Django project. Use name `hobby_helper`

Note - this didn't work for me.  Turns out this only works for unix/linux.  I had to login to psql from cmd as the super user:
```
psql -U postgres #or whatever the superuser name is
```
then I ran the psql command:
```
CREATE DATABASE hobby_helper;
```

3. Create a new database user for your Django project. You can do this using the createuser command-line tool that comes with PostgreSQL. For example:
```
CREATE ROLE <username> WITH LOGIN PASSWORD '<password>';
```

This will create a new user called etluser in this case that you can use to connect to your database.
```
psql -U postgres -d hobby_helper
```
Before you can give permissions to a schema, you first need to instantiate the schema by building a table in it. (working theory)
```
CREATE SCHEMA espresso;
```

Now give this user permissions to... everything?  Don't fully understand this and probably need to look into minimal permissions at some point.

Need to grant permissions on public schema for django migrations

```
GRANT ALL PRIVILEGES ON SCHEMA public TO etluser;

GRANT ALL PRIVILEGES ON DATABASE hobby_helper TO etluser;
GRANT ALL PRIVILEGES ON SCHEMA espresso TO etluser;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA espresso TO etluser;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA espresso TO etluser;
```
Check for success:
```
SELECT has_database_privilege('etluser', 'hobby_helper', 'CONNECT');

SELECT has_table_privilege('etluser', table_name, 'SELECT, INSERT, UPDATE, DELETE')
FROM information_schema.tables
WHERE table_schema = 'public';
```

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
python manage.py makemigrations
python manage.py migrate

```
To summarize, makemigrations creates new database migrations based on changes to your Django models, while migrate applies those database migrations to your database, modifying the database schema to reflect the changes to your models.

This will create the necessary tables in your PostgreSQL database based on the models you have defined in your Django app.

That's it! Your Django project should now be set up to use your PostgreSQL database. You can now use the Django ORM to interact with your database and create, read, update, and delete records as needed.

------------------------------------------------------------
## 6: Create your Django views
[Back to Table of Contents](#table-of-contents)

In this step, we'll create Django views that handle requests from your web app and render the appropriate responses. For this espresso tracking app, we'll need views to handle the following:
1. List all brews
2. Add a new brew
3. Update an existing brew
4. Delete a brew
5. List all beans
6. Add a new bean
7. Update an existing bean
8. Delete a bean

### 1: Import necessary modules
Inside the `espresso_tracker` folder, you'll find a file named views.py. Open it and start by importing the necessary modules:

```
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Brew, Bean
import json
```

### 2: Create the views
Next, create the views for the different actions you want to handle:
```
# List all brews
def brews(request):
    if request.method == 'GET':
        brew_list = list(Brew.objects.values())
        return JsonResponse(brew_list, safe=False)

# Add a new brew
@csrf_exempt
def add_brew(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        brew = Brew.objects.create(**data)
        return JsonResponse({'id': brew.id})

# Update an existing brew
@csrf_exempt
def update_brew(request, brew_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        brew = get_object_or_404(Brew, id=brew_id)
        for key, value in data.items():
            setattr(brew, key, value)
        brew.save()
        return JsonResponse({'id': brew.id})

# Delete a brew
@csrf_exempt
def delete_brew(request, brew_id):
    if request.method == 'DELETE':
        brew = get_object_or_404(Brew, id=brew_id)
        brew.delete()
        return JsonResponse({'id': brew_id})

# List all beans
def beans(request):
    if request.method == 'GET':
        bean_list = list(Bean.objects.values())
        return JsonResponse(bean_list, safe=False)

# Add a new bean
@csrf_exempt
def add_bean(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        bean = Bean.objects.create(**data)
        return JsonResponse({'id': bean.id})

# Update an existing bean
@csrf_exempt
def update_bean(request, bean_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        bean = get_object_or_404(Bean, id=bean_id)
        for key, value in data.items():
            setattr(bean, key, value)
        bean.save()
        return JsonResponse({'id': bean.id})

# Delete a bean
@csrf_exempt
def delete_bean(request, bean_id):
    if request.method == 'DELETE':
        bean = get_object_or_404(Bean, id=bean_id)
        bean.delete()
        return JsonResponse({'id': bean_id})

```

------------------------------------------------------------
## 7: Define your Django URL patterns
[Back to Table of Contents](#table-of-contents)

### 1: Create URL patterns
Now, we need to wire up these views to the respective URL patterns in the urls.py file inside the `espresso_tracker` folder. If you don't have a `urls.py` file, create one and add the following code:
```
from django.urls import path
from . import views

urlpatterns = [
    path('brews/', views.brews, name='brews'),
    path('brews/add/', views.add_brew, name='add_brew'),
    path('brews/update/<int:brew_id>/', views.update_brew, name='update_brew'),
    path('brews/delete/<int:brew_id>/', views.delete_brew, name='delete_brew'),
    path('beans/', views.beans, name='beans'),
    path('beans/add/', views.add_bean, name='add_bean'),
    path('beans/update/<int:bean_id>/', views.update_bean, name='update_bean'),
    path('beans/delete/<int:bean_id>/', views.delete_bean, name='delete_bean'),
]
```

### 2: Include URL patterns in the project
Finally, include these URL patterns in your project's main `urls.py` file:
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('espresso_tracker.urls')),
]
```
Now you have created the views for handling the brew and bean actions in your Django app. In the next steps, you'll create React components to interact with these views and display the data to the user.

------------------------------------------------------------
## 8: Set up your React app
[Back to Table of Contents](#table-of-contents)

### 1: Install Node.js and npm
First, make sure you have Node.js and npm (Node package manager) installed on your machine. You can download the installer for your operating system from the [official Node.js website.](https://nodejs.org/en/download/)

### 2: Create a new React app
Once Node.js and npm are installed, open your terminal or command prompt, navigate to your Django project directory, and run the following command to create a new React app using [Create React App:](https://github.com/facebook/create-react-app)
```
npx create-react-app frontend
```
This command creates a new folder named `frontend` inside your Django project directory, which will contain your React app.

### 3: Change to the `frontend` directory
Navigate to the `frontend` directory by running the following command in your terminal or command prompt:
```
cd frontend
```

### 4: Install necessary dependencies
To interact with your Django backend, you'll need the `axios` library to make API requests. Install it by running the following command:
```
npm install axios
```

### 5: Start the React development server
You can now start the React development server by running the following command:
```
npm start
```
This command will start the React development server, and your React app will be accessible at `http://localhost:3000/`. The development server will automatically reload your app whenever you make changes to your React components.

That's it! You've now set up your React app. In the next step, you'll create React components to interact with your Django backend and display the data to the user.

------------------------------------------------------------
## 9: Create your React components
[Back to Table of Contents](#table-of-contents)

------------------------------------------------------------
## 10: Connect your React app to your Django backend
[Back to Table of Contents](#table-of-contents)

------------------------------------------------------------
## 11: Test your app
[Back to Table of Contents](#table-of-contents)

------------------------------------------------------------
## 12: Deploy your app
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

# Proposed Next Steps
[Back to Table of Contents](#table-of-contents)

1. Add a user model to the Django app
2. Add a login page to the React app
3. Add a signup page to the React app
4. Add a logout button to the React app
5. Add a profile page to the React app
6. Add a dashboard page to the React app


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