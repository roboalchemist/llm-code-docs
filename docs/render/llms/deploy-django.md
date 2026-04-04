# Source: https://render.com/docs/deploy-django.md

# Deploy a Django App on Render

This guide walks through deploying a [Django](https://www.djangoproject.com/) Python app on Render. You can [use your existing Django project](#updating-an-existing-django-project) or [create one from scratch](#creating-a-new-django-project).

> If you're new to Django, we recommend first reading the official guide to [Writing your first Django project](https://docs.djangoproject.com/en/5.2/intro/tutorial01/).

## Updating an existing Django project

To prepare an existing Django project for production on Render, we'll make a couple adjustments to its configuration:

- We'll update your project to use a [Render PostgreSQL database](postgresql) instead of a SQLite database.
- We'll configure the [WhiteNoise](https://whitenoise.evans.io/en/stable/django.html) package to serve your project's static files.
- We'll define a build script to run with each deploy.

### Use a Render PostgreSQL database

As part of deploying your project, we'll also deploy a Render PostgreSQL database to serve as its backing datastore. To enable this, let's add a couple of packages to your project:

| Package                                                        | Description                                                                                                                                                                                  |
| -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [psycopg2](https://www.psycopg.org/)                           | This is the most popular Python adapter for communicating with a PostgreSQL database.                                                                                                        |
| [DJ-Database-URL](https://github.com/jacobian/dj-database-url) | This enables you to specify your database details via the `DATABASE_URL` environment variable (you'll obtain your database's URL from the [Render Dashboard](https://dashboard.render.com)). |

1. Run the following commands to install these packages:

   ```bash
   $ pip install psycopg2-binary

   $ pip install dj-database-url

   # Add these dependencies to your requirements.txt file:
   $ pip freeze > requirements.txt
   ```

2. Open `settings.py` in your project's main directory (e.g., `mysite/settings.py`).

   Make the following modifications:

   ```python
   # Import dj-database-url at the beginning of the file.
   import dj_database_url # highlight-line
   ```

   ```python{3-7}
   # Replace the SQLite DATABASES configuration with PostgreSQL:
   DATABASES = {
       'default': dj_database_url.config(
           # Replace this value with your local database's connection string.
           default='postgresql://postgres:postgres@localhost:5432/mysite',
           conn_max_age=600
       )
   }
   ```

### Set up static file serving

Django provides a [dedicated module](https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/) for collecting your project's static files (HTML, CSS, JavaScript, images, and so on) into a single place for serving in production. This module supports moving files from one place to another, relying on the end web server (such as Render's default web server, or a tool like NGINX) to serve them to end users.

In this step, we'll set up [WhiteNoise](https://whitenoise.evans.io) to serve these static assets from Render's web server.

> The following instructions summarize the setup described in the [WhiteNoise documentation](http://whitenoise.evans.io/en/stable/django.html).

1. Add WhiteNoise as a dependency (adding [Brotli](https://en.wikipedia.org/wiki/Brotli) support is optional, but recommended):

   ```bash
   $ pip install 'whitenoise[brotli]'
   $ pip freeze > requirements.txt
   ```

2. Open `settings.py` in your project's main directory (e.g., `mysite/settings.py`).

   Add the following to the `MIDDLEWARE` list, _immediately after_ `SecurityMiddleware`:

   ```python
   MIDDLEWARE = [
       'django.middleware.security.SecurityMiddleware',
       'whitenoise.middleware.WhiteNoiseMiddleware', #highlight-line
       ...
   ]
   ```

3. Still in `settings.py`, find the section where static files are configured.

   Make the following modifications:

   ```python{6,9,11,15}
   # Static files (CSS, JavaScript, Images)
   # https://docs.djangoproject.com/en/5.0/howto/static-files/

   # This setting informs Django of the URI path from which your static files will be served to users
   # Here, they well be accessible at your-domain.onrender.com/static/... or yourcustomdomain.com/static/...
   STATIC_URL = '/static/'

   # This production code might break development mode, so we check whether we're in DEBUG mode
   if not DEBUG:
       # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
       STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

       # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
       # and renames the files with unique names for each version to support long-term caching
       STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
   ```

All set! We're ready to serve static content from our Django project on Render.

### Create a build script

Whenever you deploy a new version of your project, Render runs a *build command* to prepare it for production. Let's create a script for Render to run as this build command.

1. Create a new file called `build.sh` in your project's root directory and paste in the following:

   ```bash
   #!/usr/bin/env bash
   # Exit on error
   set -o errexit

   # Modify this line as needed for your package manager (pip, poetry, etc.)
   pip install -r requirements.txt

   # Convert static asset files
   python manage.py collectstatic --no-input

   # Apply any outstanding database migrations
   python manage.py migrate
   ```

   Make sure the script is executable before adding it to version control:

   ```shell
   chmod a+x build.sh
   ```

   We'll configure Render to run this build script whenever a new deploy is initiated.

2. We'll run your project with [Uvicorn](https://www.uvicorn.org/) and [Gunicorn](https://gunicorn.org/). Add these dependencies to your project:

   ```shell
   pip install gunicorn uvicorn
   pip freeze > requirements.txt
   ```

3. Try running your project locally!

> Replace `mysite` in the command below with your project's name.

   ```shell
   python -m gunicorn mysite.asgi:application -k uvicorn.workers.UvicornWorker
   ```

4. Visit [http://localhost:8000](http://localhost:8000) in your browser to verify that your project is up and running.

Commit all changes and push them to your repository. Your project is ready to deploy to Render!

## Deploying to Render

There are two ways to deploy your Django project on Render, either by [declaring your services within your repository](infrastructure-as-code) using a `render.yaml` file or by manually setting up your services using the dashboard. In this tutorial, we will walk through both options.

### Use `render.yaml` for deploys

1. Create a file named `render.yaml` in the root of your project. This file will define your Django *web service*, along with the [*database*](postgresql) it connects to. Don't forget to commit and push it to your repository.

> The `gunicorn` command in the highlighted line below assumes your Django project is named `mysite`. Update it for your project as needed.

   ```yaml
   databases:
     - name: mysitedb
       plan: free
       databaseName: mysite
       user: mysite

   services:
     - type: web
       plan: free
       name: mysite
       runtime: python
       buildCommand: './build.sh'
       startCommand: 'python -m gunicorn mysite.asgi:application -k uvicorn.workers.UvicornWorker' # highlight-line
       envVars:
         - key: DATABASE_URL
           fromDatabase:
             name: mysitedb
             property: connectionString
         - key: SECRET_KEY
           generateValue: true
         - key: WEB_CONCURRENCY
           value: 4
   ```

2. In the Render Dashboard, go to the [Blueprints page](https://dashboard.render.com/blueprints) and click *New Blueprint Instance*.
3. Select the repository that contains your blueprint and click *Connect*.
4. Give your blueprint project a name and click *Apply*.

That's it! Your project will be live at its `.onrender.com` URL as soon as the build finishes.

### Manual deployment

1. Create a new [PostgreSQL database](postgresql-creating-connecting) on Render. Copy its *internal database URL* for now—you'll need it later.

2. Create a new *web service* on Render, pointing it to your project's GitHub/GitLab/Bitbucket repository (give Render permission to access it if you haven't already).

3. Select `Python 3` for the *Language* and set the following properties (replace `mysite` with your project's name):

   | Property          | Value                                                                         |
   | ----------------- | ----------------------------------------------------------------------------- |
   | *Build Command* | `./build.sh`                                                                  |
   | *Start Command* | `python -m gunicorn mysite.asgi:application -k uvicorn.workers.UvicornWorker` |

4. Add the following environment variables under *Advanced*:

   | Key               | Value                                                            |
   | ----------------- | ---------------------------------------------------------------- |
   | `DATABASE_URL`    | The *internal database URL* for the database you created above |
   | `SECRET_KEY`      | Click *Generate* to get a secure random value                  |
   | `WEB_CONCURRENCY` | `4`                                                              |

That's it! Save your web service to deploy your Django application on Render. It will be live on your `.onrender.com` URL as soon as the build finishes.

### Create a Django admin account

Once your application is live, create a new [Django admin account](https://docs.djangoproject.com/en/3.0/intro/tutorial02/#creating-an-admin-user) by running the following command in the Render Shell:

```shell
python manage.py createsuperuser
```

See [Setting your Python Version](python-version) if you need to customize the version of Python used for your app.

## Creating a new Django project

This section walks through setting up a Django project and adding an application with a simple view.

The finished code for this example is available on [GitHub](https://github.com/render-examples/django), and you can view the project running [here](https://django.onrender.com).

> This tutorial starts with a bare-bones installation and explains all required code modifications. Feel free to adapt it with custom configuration as needed.

### Installation & setup

First, we'll set up our local development environment and create a basic project structure.

We'll call our project `mysite`. You can use a different name, but make sure to modify all commands that use `mysite` below to match the name you choose.

#### 1. Create your directory and virtual environment

Run the following commands in your terminal (see comments for descriptions):

```shell{outputLines:1,4,5,7-8}
# Create a new project directory and cd into it
mkdir mysite
cd mysite

# Create a virtual environment using Python's venv package
python -m venv venv

# Activate the virtual environment to start installing other packages
source venv/bin/activate
```

#### 2. Install Django and create your project

Run the following from your project's root directory to install Django:

```shell{outputLines:1}
# This installs Django 5.0.1 (feel free to modify the version as needed)
pip install django==5.0.1
pip freeze > requirements.txt
```

Then run the following to initialize your `mysite` Django project:

```shell
django-admin startproject mysite .
```

You'll end up with the following directory structure:

```
.
├── manage.py
├── mysite
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── venv (you can ignore everything in here for now)
    ├──
```

You now have a fully functional scaffold for your new Django project! To verify, you can start the development server:

```shell
python manage.py runserver
```

Then visit [http://localhost:8000](http://localhost:8000) in your browser:

<div style="width: 70%; margin: auto;">

[image: Django Successful Installation]

</div>

### Creating a landing page

Next, we'll add an _application_ to our Django project that serves a simple landing page.

> Django _projects_ contain one or more _applications_, which are wired together to form a complete service. Django provides several built-in applications, such as its [admin site](https://docs.djangoproject.com/en/3.0/ref/contrib/admin/).

#### 1. Create a new application

1. Run the following command from your project's root directory:

   ```shell
   python manage.py startapp homepage
   ```

   This creates a directory for a new application named `homepage` with following contents:

   ```
   homepage
   ├── __init__.py
   ├── admin.py
   ├── apps.py
   ├── migrations
   │   └── __init__.py
   ├── models.py
   ├── tests.py
   └── views.py
   ```

2. We need to inform Django about this new `homepage` application. Open `mysite/settings.py` and find the the `INSTALLED_APPS` setting. Add a reference to the `HomepageConfig` class to the _beginning_ of the list:

   ```python
   INSTALLED_APPS = [
       'homepage.apps.HomepageConfig', # highlight-line
       'django.contrib.admin',
       'django.contrib.auth',
       ...
   ]
   ```

   For more information about the `INSTALLED_APPS` setting, see the [Django settings information page](https://docs.djangoproject.com/en/5.0/ref/settings/#installed-apps)

#### 2. Write your first view

Let's create a simple view in our `homepage` application that we'll serve from our service's root path. First we'll define the view, then we'll configure its routing.

1.  Create a new file at `homepage/templates/homepage/index.html`. Paste in the following HTML:

    ```jinja2
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />

        <title>Hello Django on Render!</title>

        <link rel="stylesheet"
              href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css"
              integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk"
              crossorigin="anonymous">
    </head>
    <body>
    <main class="container">
        <div class="row text-center justify-content-center">
            <div class="col">
                <h1 class="display-4">Hello World!</h1>
            </div>
        </div>
    </main>
    </body>
    </html>
    ```

    Nothing fancy

2.  In the file `homepage/views.py`, add the following Python code for the `index` method:

    ```python
    from django.shortcuts import render

    # Create your views here.

    def index(request): # highlight-line
        return render(request, 'homepage/index.html', {}) # highlight-line
    ```

    This method renders the `homepage/index.html` template we just created.

3.  Create a _new_ file named `homepage/urls.py` and paste in the following:

    ```python
    from django.urls import path

    from . import views

    urlpatterns = [
        path('', views.index, name='index'),
    ]
    ```

    This file tells Django that you want to serve the `index` view from your service's root URL.

4.  Configure the Django project to point to the `homepage` application's `urls` module. Open `mysite/urls.py` and update the `from django.urls import path` line to add the `include` module, and then include the `homepage` application's URLs module to our `urlpatterns`, like so:

    ```python{2,6}
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('homepage.urls')),
    ]
    ```

    Your folder structure should now look like this:

    ```text{outputLines:8-10,12}
    render
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── templates
    │   └── render
    │       └── index.html
    ├── tests.py
    ├── urls.py
    └── views.py
    ```

5.  Add a static file to your application. Download this image and save it as `homepage/static/homepage/render-banner.png`:

    [image: Banner for Django app]

6.  Return to your `index.html` template. Load the `static` module and reference the downloaded image in a new `<header></header>` block:

    ```jinja2{1,7-11}
    {% load static %}

    <!doctype html>
    <html lang="en">
    ...
    <body>
    <header class="container mt-4 mb-4">
        <a href="https://render.com">
            <img src="{% static "homepage/render-banner.png" %}" alt="Homepage banner" class="mw-100">
        </a>
    </header>
    ...
    </body>
    </html>
    ```

7.  You can now verify your app is working with the following command:

    ```bash
    python manage.py runserver
    ```

    Reload your browser tab at `localhost:8000` to make sure the banner and text are showing properly.

    <div style="width: 70%; margin: auto;">

    [image: Django Hello World]

    </div>

### Adding basic security

You should ensure that any production-level application is properly secured and configured. The Django documentation provides a useful [deployment checklist](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/), which we'll follow in this step.

1. Open `mysite/settings.py` and find the declaration of the `SECRET_KEY` setting. We don't want to store production secrets in source code, so we'll fetch this value from an environment variable that we'll create later:

   ```python{2}
   # Don't forget to import os at the beginning of the file
   import os
   ```

   ```python{2}
   # SECURITY WARNING: keep the secret key used in production secret!
   SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')
   ```

2. Find the declaration of the `DEBUG` setting. This setting should _never_ be set to `True` in a production environment. You can detect that you're running on Render by checking for the presence of the `RENDER` environment variable in the [application environment](environment-variables):

   ```python{2}
   # SECURITY WARNING: don't run with debug turned on in production!
   DEBUG = 'RENDER' not in os.environ
   ```

3. When `DEBUG` is `False`, Django requires a suitable value for `ALLOWED_HOSTS`. You can get the name of your web service host from the `RENDER_EXTERNAL_HOSTNAME` environment variable, which is automatically set by Render.

   ```python{4-6}
   # https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts
   ALLOWED_HOSTS = []

   RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
   if RENDER_EXTERNAL_HOSTNAME:
       ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
   ```

> If you add a custom domain to your service, don't forget to add it to this list.

### Adding PostgreSQL support

We will add the [DJ-Database-URL](https://github.com/jacobian/dj-database-url) package, which allows us to specify databases in Django using connection strings. Render provides database connection strings in the [Render Dashboard](https://dashboard.render.com), which you will provide to your web service via the `DATABASE_URL` environment variable. We will also need to add [psycopg2](https://www.psycopg.org/) to the project.

1. Run the following command to add the necessary dependencies to your project:

   ```bash
   $ pip install dj-database-url psycopg2-binary
   $ pip freeze > requirements.txt
   ```

2. In `mysite/settings.py`, find the declaration of the `DATABASES` setting and modify it to look like the following:

   ```python{2}
   # Import the dj-database-url package at the beginning of the file
   import dj_database_url
   ```

   ```python{5-9}
   # Database documentation https://docs.djangoproject.com/en/5.0/ref/settings/#databases

   DATABASES = {
       'default': dj_database_url.config(
           # Replace this value with your local database's connection string.
           default='postgresql://postgres:postgres@localhost:5432/mysite',
           conn_max_age=600
       )
   }
   ```

> This connection string assumes that you have PostgreSQL running on localhost, on port 5432, with a database named `mysite` and a user named `postgres` with the password `postgres`.

3. Apply our database migrations. A "migration" is a step-by-step process of creating database tables and fields for our Django project. We will use the `migrate` command to run the migrations:

   ```shell{outputLines:2-22}
   python manage.py migrate
   Operations to perform:
   Apply all migrations: admin, auth, contenttypes, sessions
   Running migrations:
   Applying contenttypes.0001_initial... OK
   Applying auth.0001_initial... OK
   Applying admin.0001_initial... OK
   Applying admin.0002_logentry_remove_auto_add... OK
   Applying admin.0003_logentry_add_action_flag_choices... OK
   Applying contenttypes.0002_remove_content_type_name... OK
   Applying auth.0002_alter_permission_name_max_length... OK
   Applying auth.0003_alter_user_email_max_length... OK
   Applying auth.0004_alter_user_username_opts... OK
   Applying auth.0005_alter_user_last_login_null... OK
   Applying auth.0006_require_contenttypes_0002... OK
   Applying auth.0007_alter_validators_add_error_messages... OK
   Applying auth.0008_alter_user_username_max_length... OK
   Applying auth.0009_alter_user_last_name_max_length... OK
   Applying auth.0010_alter_group_name_max_length... OK
   Applying auth.0011_update_proxy_permissions... OK
   Applying auth.0012_alter_user_first_name_max_length... OK
   Applying sessions.0001_initial... OK
   ```

### Finishing setup

As a final step, jump back to the top of the document and read the section about [Updating an existing Django project](#updating-an-existing-django-project) to make sure your project is production-ready. Then, follow the instructions in [Deploying to Render](#deploying-to-render) to deploy your project.