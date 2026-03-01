# Source: https://fly.io/docs/django/getting-started/

Title: Getting Started

URL Source: https://fly.io/docs/django/getting-started/

Published Time: Thu, 26 Feb 2026 22:12:40 GMT

Markdown Content:
Getting Started · Fly Docs
===============

[Skip to content](https://fly.io/docs/django/getting-started/#main-content-start)

[](https://fly.io/)[](https://fly.io/docs/)

[**Need a Logo?** View Our Brand Assets](https://fly.io/docs/about/brand/)

Open main menu[](https://fly.io/)[](https://fly.io/docs/)

[Pricing](https://fly.io/pricing/)[Support](https://fly.io/docs/about/support/)

[Sign In](https://fly.io/app/sign-in/)[Sign Up](https://fly.io/app/sign-up/)

[Docs Index](https://fly.io/docs/)[](https://fly.io/docs/django/)[Getting Started](https://fly.io/docs/django/getting-started/)Toggle Getting Started section
*   [Existing Django Apps](https://fly.io/docs/django/getting-started/existing/)

[Advanced guides](https://fly.io/docs/django/advanced-guides/)Toggle Advanced guides section
*   [Staging environments with GitHub actions](https://fly.io/docs/django/advanced-guides/staging-environments-with-github-actions/)

--- title: Getting Started layout: framework_docs order: 1 redirect_from: /docs/getting-started/django/ subnav_glob: docs/django/getting-started/*.html.* objective: Build and deploy a very basic Django app to Fly.io. This guide is the fastest way to try using Fly.io, so if you're short on time start here. related_pages: - /docs/django/getting-started/existing - /docs/flyctl/ - /docs/reference/configuration/ - /docs/postgres/ --- <div><img src="/static/images/django-intro.webp" srcset="/static/images/django-intro@2x.webp 2x" alt="Green book titled Django on a shelf with other books and a plant"></div> In this guide we recreate and deploy [this Django application](https://github.com/fly-apps/hello-django) to demonstrate how quickly Django apps can be deployed to Fly.io! ## Initial Local Setup Make sure that [Python](https://www.python.org/) is already installed on your computer along with a way to create virtual environments. This allows you to run your project locally, and test that it works, before deploying it to Fly.io. > We recommend the latest [supported versions](https://devguide.python.org/versions/#supported-versions) of Python. Create a folder for your project. Here we'll call it `hello-django`. Enter the folder with `cd`: ```cmd mkdir hello-django && cd hello-django ``` ### Virtual Environment For this guide, we use [venv](https://docs.python.org/3/library/venv.html#module-venv) but any of the other popular choices such as [Poetry](https://python-poetry.org/), [Pipenv](https://github.com/pypa/pipenv), or [pyenv](https://github.com/pyenv/pyenv) work too. ```shell # Unix/macOS $ python3 -m venv .venv $ source .venv/bin/activate (.venv) $ ``` ```powershell # Windows (PowerShell) > python -m venv .venv > .venv\Scripts\Activate.ps1 (.venv) ...> ``` <section class="callout">From this point on, the commands won't be displayed with `(.venv)` but we assume you have your Python virtual environment activated.</section> ### Install Django With your virtual environment **activated**, install the [latest](https://www.djangoproject.com/download/#supported-versions) version of Django using [pip](https://pip.pypa.io/en/stable/): ```cmd python -m pip install Django ``` ### Create a Django Project Inside the `hello-django` folder, create a Django project named `hello_django`: ```cmd django-admin startproject hello_django . ``` > Don't forget the `.` at the end. It's crucial because it tells the script to create the Django project directory structure in the current directory, our folder `hello-django`. Note that by convention, we name Django projects using `snake_case`: words written in lowercase with spaces replaced by underscore (`_`). Hyphens (`-`) are not valid identifiers and you might get this error message: ```terminal 'hello-django' is not a valid project name. Please make sure the name is a valid identifier. ``` By this point, our project structure should look like this: ```terminal hello-django/ |-- .venv |-- hello_django/ | |-- __init__.py | |-- asgi.py | |-- settings.py | |-- urls.py | |-- wsgi.py |-- manage.py ``` ### Create and Map a URL to a View Now let's configure a basic view that returns the text, `Hello, Fly!` by updating the [`hello_django/urls.py`](https://github.com/fly-apps/hello-django/blob/main/hello_django/urls.py) file: ```python # hello_django/urls.py from django.contrib import admin from django.http import HttpResponse from django.urls import path # ↓ New basic view returning "Hello, Fly!" ↓ def hello(request): return HttpResponse("Hello, Fly!") urlpatterns = [ path("admin/", admin.site.urls), path("", hello, name="hello"), # ← Added! ] ``` ### Run migrations As part of Django's core functionality, some existing apps are included by default to provide you with out-of-the-box features. Some of those apps require their own database tables. To initialize the local database and set up those tables, run the `migrate` command: ```cmd python manage.py migrate ``` ### Start the Web Server Now `runserver` to start up Django's local web server: ```cmd python manage.py runserver ``` If you open `http://127.0.0.1:8000/` in your web browser it now displays the text `Hello, Fly!`. ## Django Deployment Checklist By default, Django is configured for local development. The [How to Deploy Django](https://docs.djangoproject.com/en/stable/howto/deployment/) and [Django Deployment Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/) guide list the various steps required for a secure deployment. > You can also find a complete guide [Deploying Django to Production](https://fly.io/django-beats/deploying-django-to-production/) in our [Django Beats Blog](https://fly.io/django-beats/). However, for demonstration purposes, we can take some shortcuts. First, in the [`hello_django/settings.py`](https://github.com/fly-apps/hello-django/blob/main/hello_django/settings.py) file update the `ALLOWED_HOSTS` configuration to accept a host on which it's deployed. Use the [`FLY_APP_NAME`](https://fly.io/docs/machines/runtime-environment/#fly_app_name) environment variable for that: ```python # hello_django/settings.py import os APP_NAME = os.environ.get("FLY_APP_NAME") ALLOWED_HOSTS = [f"{APP_NAME}.fly.dev"] # ← Updated! ``` Second, install [Gunicorn](https://gunicorn.org/) as our [production server](https://docs.djangoproject.com/en/dev/ref/django-admin/#runserver): ```cmd python -m pip install gunicorn ``` Third, create a [`requirements.txt`](https://github.com/fly-apps/hello-django/blob/main/requirements.txt) file listing all the packages in the current Python virtual environment: ```cmd pip freeze > requirements.txt ``` That's it! We're ready to deploy on Fly.io. ## flyctl Fly.io has its own command-line utility for managing apps, [flyctl](/docs/flyctl/). If not already installed, follow the instructions on the [installation guide](/docs/flyctl/install/) and [log in to Fly.io](/docs/getting-started/sign-up-sign-in/). ## Configure and Deploy your Fly App To configure and launch the app, run the `fly launch` command and follow the wizard. You can set a name for the app and choose your primary region. You can also choose to launch and attach a Postgres database and/or a Redis database though we are not using either in this example. ```cmd fly launch ``` ```output Scanning source code Detected a Django app Creating app in /flyio/hello-django We're about to launch your Django app on Fly.io. Here's what you're getting: Organization: Joe Doe (fly launch defaults to the personal org) Name: hello-django (derived from your directory name) Region: Amsterdam, Netherlands (this is the fastest region for you) App Machines: shared-cpu-1x, 1GB RAM (most apps need about 1GB of RAM) Postgres: <none> (not requested) Redis: <none> (not requested) ? Do you want to tweak these settings before proceeding? Yes Opening https://fly.io/cli/launch/mo1ootho9ualooghoch3iih6cha2shah ... Waiting for launch data... Done Created app 'hello-django' in organization 'personal' Admin URL: https://fly.io/apps/hello-django Hostname: hello-django.fly.dev Set secrets on hello-django: SECRET_KEY Wrote config file fly.toml [INFO] Python 3.10.12 was detected. 'python:3.10-slim-bullseye' image will be set in the Dockerfile. Validating /flyio/hello-django/fly.toml Platform: machines ✓ Configuration is valid Your app is ready! Deploy with `flyctl deploy` ``` This creates two new files in the project that are automatically configured: a [`Dockerfile`](https://github.com/fly-apps/hello-django/blob/main/Dockerfile) and [`fly.toml`](https://github.com/fly-apps/hello-django/blob/main/fly.toml) file to configure applications for deployment. To deploy the application use the following command: ```cmd fly deploy ``` This will take a few seconds as it uploads your application, verifies the app configuration, builds the image, and then monitors to ensure it starts successfully. Once complete visit your app with the following command: ```cmd fly apps open ``` YAY! You are up and running! Wasn't that easy? ## Recap We started with an empty directory and in a matter of minutes had a running Django application deployed to the web. A few things to note: * Your application is running on a Virtual Machine that was created based on the `Dockerfile` image. * The `fly.toml` file controls your app configuration and can be modified as needed. * `fly dashboard` can be used to monitor and adjust your application. Pretty much anything you can do from the browser window you can also do from the command line using [`fly` commands](/docs/flyctl/). Try `fly help` to see what you can do. Now that you have seen how to deploy a simple Django application, it is time to move on to [Existing Django Apps](/docs/django/getting-started/existing/) that feature static files and a Postgres database. 

[Docs](https://fly.io/docs/)[Django on Fly.io](https://fly.io/docs/django)Getting Started
Getting Started
===============

![Image 1: Green book titled Django on a shelf with other books and a plant](https://fly.io/static/images/django-intro.webp)

In this guide we recreate and deploy [this Django application](https://github.com/fly-apps/hello-django) to demonstrate how quickly Django apps can be deployed to Fly.io!

[](https://fly.io/docs/django/getting-started/#initial-local-setup)Initial Local Setup
--------------------------------------------------------------------------------------

Make sure that [Python](https://www.python.org/) is already installed on your computer along with a way to create virtual environments.

This allows you to run your project locally, and test that it works, before deploying it to Fly.io.

> We recommend the latest [supported versions](https://devguide.python.org/versions/#supported-versions) of Python.

Create a folder for your project. Here we’ll call it `hello-django`. Enter the folder with `cd`:

 Wrap text  Copy to clipboard 

```
mkdir hello-django && cd hello-django
```

### [](https://fly.io/docs/django/getting-started/#virtual-environment)Virtual Environment

For this guide, we use [venv](https://docs.python.org/3/library/venv.html#module-venv) but any of the other popular choices such as [Poetry](https://python-poetry.org/), [Pipenv](https://github.com/pypa/pipenv), or [pyenv](https://github.com/pyenv/pyenv) work too.

 Wrap text  Copy to clipboard 

```
# Unix/macOS
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $
```

 Wrap text  Copy to clipboard 

```
# Windows (PowerShell)
> python -m venv .venv
> .venv\Scripts\Activate.ps1
(.venv) ...>
```

From this point on, the commands won’t be displayed with `(.venv)` but we assume you have your Python virtual environment activated.

### [](https://fly.io/docs/django/getting-started/#install-django)Install Django

With your virtual environment **activated**, install the [latest](https://www.djangoproject.com/download/#supported-versions) version of Django using [pip](https://pip.pypa.io/en/stable/):

 Wrap text  Copy to clipboard 

```
python -m pip install Django
```

### [](https://fly.io/docs/django/getting-started/#create-a-django-project)Create a Django Project

Inside the `hello-django` folder, create a Django project named `hello_django`:

 Wrap text  Copy to clipboard 

```
django-admin startproject hello_django .
```

> Don’t forget the `.` at the end. It’s crucial because it tells the script to create the Django project directory structure in the current directory, our folder `hello-django`.

Note that by convention, we name Django projects using `snake_case`: words written in lowercase with spaces replaced by underscore (`_`). Hyphens (`-`) are not valid identifiers and you might get this error message:

 Wrap text  Copy to clipboard 

```
'hello-django' is not a valid project name. Please make sure the name is a valid identifier.
```

By this point, our project structure should look like this:

 Wrap text  Copy to clipboard 

```
hello-django/
|-- .venv
|-- hello_django/
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|-- manage.py
```

### [](https://fly.io/docs/django/getting-started/#create-and-map-a-url-to-a-view)Create and Map a URL to a View

Now let’s configure a basic view that returns the text, `Hello, Fly!` by updating the [`hello_django/urls.py`](https://github.com/fly-apps/hello-django/blob/main/hello_django/urls.py) file:

 Wrap text  Copy to clipboard 

```
# hello_django/urls.py
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

# ↓ New basic view returning "Hello, Fly!" ↓
def hello(request):
    return HttpResponse("Hello, Fly!")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", hello, name="hello"),  # ← Added!
]
```

### [](https://fly.io/docs/django/getting-started/#run-migrations)Run migrations

As part of Django’s core functionality, some existing apps are included by default to provide you with out-of-the-box features. Some of those apps require their own database tables.

To initialize the local database and set up those tables, run the `migrate` command:

 Wrap text  Copy to clipboard 

```
python manage.py migrate
```

### [](https://fly.io/docs/django/getting-started/#start-the-web-server)Start the Web Server

Now `runserver` to start up Django’s local web server:

 Wrap text  Copy to clipboard 

```
python manage.py runserver
```

If you open `http://127.0.0.1:8000/` in your web browser it now displays the text `Hello, Fly!`.

[](https://fly.io/docs/django/getting-started/#django-deployment-checklist)Django Deployment Checklist
------------------------------------------------------------------------------------------------------

By default, Django is configured for local development. The [How to Deploy Django](https://docs.djangoproject.com/en/stable/howto/deployment/) and [Django Deployment Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/) guide list the various steps required for a secure deployment.

> You can also find a complete guide [Deploying Django to Production](https://fly.io/django-beats/deploying-django-to-production/) in our [Django Beats Blog](https://fly.io/django-beats/).

However, for demonstration purposes, we can take some shortcuts.

First, in the [`hello_django/settings.py`](https://github.com/fly-apps/hello-django/blob/main/hello_django/settings.py) file update the `ALLOWED_HOSTS` configuration to accept a host on which it’s deployed. Use the [`FLY_APP_NAME`](https://fly.io/docs/machines/runtime-environment/#fly_app_name) environment variable for that:

 Wrap text  Copy to clipboard 

```
# hello_django/settings.py
import os

APP_NAME = os.environ.get("FLY_APP_NAME")
ALLOWED_HOSTS = [f"{APP_NAME}.fly.dev"]  # ← Updated!
```

Second, install [Gunicorn](https://gunicorn.org/) as our [production server](https://docs.djangoproject.com/en/dev/ref/django-admin/#runserver):

 Wrap text  Copy to clipboard 

```
python -m pip install gunicorn
```

Third, create a [`requirements.txt`](https://github.com/fly-apps/hello-django/blob/main/requirements.txt) file listing all the packages in the current Python virtual environment:

 Wrap text  Copy to clipboard 

```
pip freeze > requirements.txt
```

That’s it! We’re ready to deploy on Fly.io.

[](https://fly.io/docs/django/getting-started/#flyctl)flyctl
------------------------------------------------------------

Fly.io has its own command-line utility for managing apps, [flyctl](https://fly.io/docs/flyctl/). If not already installed, follow the instructions on the [installation guide](https://fly.io/docs/flyctl/install/) and [log in to Fly.io](https://fly.io/docs/getting-started/sign-up-sign-in/).

[](https://fly.io/docs/django/getting-started/#configure-and-deploy-your-fly-app)Configure and Deploy your Fly App
------------------------------------------------------------------------------------------------------------------

To configure and launch the app, run the `fly launch` command and follow the wizard. You can set a name for the app and choose your primary region. You can also choose to launch and attach a Postgres database and/or a Redis database though we are not using either in this example.

 Wrap text  Copy to clipboard 

```
fly launch
```

 Wrap text  Copy to clipboard 

```
Scanning source code
Detected a Django app
Creating app in /flyio/hello-django
We're about to launch your Django app on Fly.io. Here's what you're getting:

Organization: Joe Doe                (fly launch defaults to the personal org)
Name:         hello-django           (derived from your directory name)
Region:       Amsterdam, Netherlands (this is the fastest region for you)
App Machines: shared-cpu-1x, 1GB RAM (most apps need about 1GB of RAM)
Postgres:     <none>                 (not requested)
Redis:        <none>                 (not requested)

? Do you want to tweak these settings before proceeding? Yes
Opening https://fly.io/cli/launch/mo1ootho9ualooghoch3iih6cha2shah ...

Waiting for launch data... Done
Created app 'hello-django' in organization 'personal'
Admin URL: https://fly.io/apps/hello-django
Hostname: hello-django.fly.dev
Set secrets on hello-django: SECRET_KEY
Wrote config file fly.toml

[INFO] Python 3.10.12 was detected. 'python:3.10-slim-bullseye' image will be set in the Dockerfile.

Validating /flyio/hello-django/fly.toml
Platform: machines
✓ Configuration is valid
Your app is ready! Deploy with `flyctl deploy`
```

This creates two new files in the project that are automatically configured: a [`Dockerfile`](https://github.com/fly-apps/hello-django/blob/main/Dockerfile) and [`fly.toml`](https://github.com/fly-apps/hello-django/blob/main/fly.toml) file to configure applications for deployment.

To deploy the application use the following command:

 Wrap text  Copy to clipboard 

```
fly deploy
```

This will take a few seconds as it uploads your application, verifies the app configuration, builds the image, and then monitors to ensure it starts successfully. Once complete visit your app with the following command:

 Wrap text  Copy to clipboard 

```
fly apps open
```

YAY! You are up and running! Wasn’t that easy?

[](https://fly.io/docs/django/getting-started/#recap)Recap
----------------------------------------------------------

We started with an empty directory and in a matter of minutes had a running Django application deployed to the web. A few things to note:

*   Your application is running on a Virtual Machine that was created based on the `Dockerfile` image. 
*   The `fly.toml` file controls your app configuration and can be modified as needed. 
*   `fly dashboard` can be used to monitor and adjust your application. Pretty much anything you can do from the browser window you can also do from the command line using [`fly` commands](https://fly.io/docs/flyctl/). Try `fly help` to see what you can do. 

Now that you have seen how to deploy a simple Django application, it is time to move on to [Existing Django Apps](https://fly.io/docs/django/getting-started/existing/) that feature static files and a Postgres database.

Additional resources
--------------------

*   [Existing Django Apps](https://fly.io/docs/django/getting-started/existing/)
*   [flyctl - The Fly.io CLI](https://fly.io/docs/flyctl/)
*   [App configuration (fly.toml)](https://fly.io/docs/reference/configuration/)
*   [Fly Postgres (Unmanaged)](https://fly.io/docs/postgres/)

Copy page as markdown or[Open in ChatGPT](https://chatgpt.com/?hints=search&q=Read+https%3A%2F%2Fraw.githubusercontent.com%2Fsuperfly%2Fdocs%2Fmain%2Fdjango%2Fgetting-started%2Findex.html.md)

[Report an issue](https://github.com/superfly/docs/issues/new?body=I+found+an+issue+with+this+document.%0A%0ATitle%3A+Getting+Started%0ALocation%3A+https%3A%2F%2Ffly.io%2Fdocs%2Fdjango%2Fgetting-started%2F%0ASource%3A+https%3A%2F%2Fgithub.com%2Fsuperfly%2Fdocs%2Fblob%2Fmain%2Fdjango%2Fgetting-started%2Findex.html.md%0A%0A%23%23%23+Describe+the+issue%0A%0A%3C%21--+Describe+the+issue+and+include+the+section+you%27re+referring+to%2C+if+applicable.+Provide+lots+of+detail+about+the+issue+that+you+found.++--%3E%0A%0A%23%23%23+Additional+info%0A%0A%3C%21--+Add+any+other+context+about+the+issue+here.+If+applicable%2C+add+screenshots+to+help+explain+the+issue.+--%3E%0A&title=Issue+with+the+%22Getting+Started%22+doc) or [edit this page on GitHub](https://github.com/superfly/docs/edit/main/django/getting-started/index.html.md)

[On this page](https://fly.io/docs/django/getting-started/#)
*   [Initial Local Setup](https://fly.io/docs/django/getting-started/#initial-local-setup)
    *   [Virtual Environment](https://fly.io/docs/django/getting-started/#virtual-environment)
    *   [Install Django](https://fly.io/docs/django/getting-started/#install-django)
    *   [Create a Django Project](https://fly.io/docs/django/getting-started/#create-a-django-project)
    *   [Create and Map a URL to a View](https://fly.io/docs/django/getting-started/#create-and-map-a-url-to-a-view)
    *   [Run migrations](https://fly.io/docs/django/getting-started/#run-migrations)
    *   [Start the Web Server](https://fly.io/docs/django/getting-started/#start-the-web-server)

*   [Django Deployment Checklist](https://fly.io/docs/django/getting-started/#django-deployment-checklist)
*   [flyctl](https://fly.io/docs/django/getting-started/#flyctl)
*   [Configure and Deploy your Fly App](https://fly.io/docs/django/getting-started/#configure-and-deploy-your-fly-app)
*   [Recap](https://fly.io/docs/django/getting-started/#recap)

Copy page as markdown[Open in ChatGPT](https://chatgpt.com/?hints=search&q=Read+https%3A%2F%2Fraw.githubusercontent.com%2Fsuperfly%2Fdocs%2Fmain%2Fdjango%2Fgetting-started%2Findex.html.md)
