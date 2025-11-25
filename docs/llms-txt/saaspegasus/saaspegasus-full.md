# Saaspegasus Documentation

Source: https://docs.saaspegasus.com/llms-full.txt

---

<SYSTEM>This is the full developer documentation for SaaS Pegasus</SYSTEM>

# SaaS Pegasus Documentation

> Everything you need to know about setting up and configuring Pegasus for your project.

### Quicklinks

[Section titled “Quicklinks”](#quicklinks)

[Getting Started ](/getting-started/)

[Configuration ](/configuration/)

[Teams ](/teams/)

[Subscriptions ](/subscriptions/)

[Deployment ](/deployment/overview/)

[Get Help From AI ](/ai/development/)

# Getting Started

> Complete setup guide for Pegasus projects with Docker or native Python, including database configuration and post-installation steps.

Here’s everything you need to start your first Pegasus project.

## Watch the video

[Section titled “Watch the video”](#watch-the-video)

Visual learner? The above video should get you going. Else read on below for the play-by-play.

## Create and download your project codebase

[Section titled “Create and download your project codebase”](#create-and-download-your-project-codebase)

If you haven’t already, you’ll need to [purchase a Pegasus License on saaspegasus.com](http://www.saaspegasus.com/licenses/).

Then, [create a new project on saaspegasus.com](https://www.saaspegasus.com/projects/), following the prompts and filling in whatever configuration options you want to use for your new project. Make sure that the “license” field at the bottom is set.

Once you’re done, [connect your project to Github](/github) or download your project’s source code as a zip file.

**Note: it’s recommended to use the Github integration which will make future upgrades and changes to your project easier to manage.**

## Set up source control

[Section titled “Set up source control”](#set-up-source-control)

It is highly recommended to use git for source control. [Install git](https://git-scm.com/downloads) and then follow the instructions below:

### If using the Github integration

[Section titled “If using the Github integration”](#if-using-the-github-integration)

If you created your project on Github, you can use `git clone` to get the code. Get your git URL from the Github page and then run the following command, swapping in your user account and project id:

```bash
git clone https://github.com/user/project-id.git
```

### If using the Zip file download

[Section titled “If using the Zip file download”](#if-using-the-zip-file-download)

If you chose to use a zip file instead, unzip it to a folder where you want to do your development and then manually initialize your repository:

```bash
git init
git add .Building
git commit -am "initial project creation"
```

It is also recommended to create a `pegasus` branch at this time for future upgrades.

```bash
git branch pegasus
```

You can read [more about upgrading here](/upgrading).

## Install prerequisites

[Section titled “Install prerequisites”](#install-prerequisites)

The following prerequisites are needed to run the app in the recommended configuration:

* [Docker](/docker#install-prerequisites)
* [uv](/python/setup/#using-uv)
* [Node and npm](/front-end/overview/#prerequisites-to-building-the-front-end)

On Windows, you will also need to install `make`, which you can do by [following these instructions](https://stackoverflow.com/a/57042516/8207).

Other configurations

* If you use Docker “full mode” you do not need to install uv or Node/npm.
* If you do not want to use Docker for Postgres and Redis, you will need to install them separately.
* To run Python without `uv` you’ll need to follow the instructions for your own environment on [this page](/python/setup#using-native--system-python-with-virtual-environments-and-pip-tools).

## Quick start

[Section titled “Quick start”](#quick-start)

Once you’ve installed the prerequisites, you can get up and running with the following commands:

```bash
make init
make dev  # This is not required if running Docker in "full mode"
```

Open a browser and visit <http://localhost:8000> and you should see your application!

Then skip ahead to the [post-install steps](/getting-started/#post-installation-steps).

## Manual setup

[Section titled “Manual setup”](#manual-setup)

The `make` quick start commands cover a lot for you. If you’d rather do everything manually, continue to the sections below.

### Enter the project directory

[Section titled “Enter the project directory”](#enter-the-project-directory)

```bash
cd {{ project_name }}
```

You should see your project files, including a `manage.py` file.

### Set up your Python environment

[Section titled “Set up your Python environment”](#set-up-your-python-environment)

There are several ways of setting up your Python environment.

See [this page](/python/setup) for information on choosing an option and setting up your environment.

### Install package requirements

[Section titled “Install package requirements”](#install-package-requirements)

With `uv`:

```bash
# with uv
uv sync
# or if using pip tools
pip install -r dev-requirements.txt
```

Note: if you have issues installing `psycopg2`, try installing the dependencies outlined in [this thread](https://stackoverflow.com/questions/22938679/error-trying-to-install-postgres-for-python-psycopg2) (specifically `python3-dev` and `libpq-dev`).

On Macs you may also need to follow the instructions from [this thread](https://stackoverflow.com/a/58722268/8207). And specifically, run:

```bash
brew reinstall openssl
export LIBRARY_PATH=$LIBRARY_PATH:/usr/local/opt/openssl/lib/
```

### Create your .env file

[Section titled “Create your .env file”](#create-your-env-file)

If you installed with Github, you’ll have to create your `.env` file for your environment variables and secrets. You can do this from the example, by running:

```bash
cp .env.example .env
```

### Set up database

[Section titled “Set up database”](#set-up-database)

If you installed with Postgres, edit the `DATABASE_URL` value in `.env` with the appropriate username and password for connecting to your DB.

You will also need to create a database for your project if you haven’t already. Assuming that your postgres admin user is named `postgres`:

```bash
createdb -U postgres -h localhost -p 5432 {{ project_name }}
```

Followed by the password for the postgres user.

Or, using identity authentication:

```bash
sudo -u postgres createdb {{ project_name }}
```

### Create database migrations

[Section titled “Create database migrations”](#create-database-migrations)

```bash
# with uv
uv run manage.py makemigrations
# or with normal venv
python ./manage.py makemigrations
```

### Run database migrations

[Section titled “Run database migrations”](#run-database-migrations)

```bash
# with uv
uv run manage.py migrate
# or with normal venv
python ./manage.py migrate
```

### Run server

[Section titled “Run server”](#run-server)

```bash
# with uv
uv run manage.py runserver
# or with normal venv
python ./manage.py runserver
```

### Build/run front end

[Section titled “Build/run front end”](#buildrun-front-end)

```bash
npm install
npm run dev
```

For more details, see the [front end docs](/front-end/overview).

### Load your app

[Section titled “Load your app”](#load-your-app)

Open a browser and visit <http://localhost:8000> and you should see your application!

Continue to the post-installation steps below.

## Post-installation steps

[Section titled “Post-installation steps”](#post-installation-steps)

Once up and running, you’ll want to review these common next-steps.

### Create a User

[Section titled “Create a User”](#create-a-user)

To create your first user account, just go through the sign up flow in your web browser.

From there you should be able to access all built-in functionality and examples.

### Enable admin access

[Section titled “Enable admin access”](#enable-admin-access)

Use [the `promote_user_to_superuser` management command](/cookbooks/#use-the-django-admin-ui) to enable access to the Django Admin site.

### Confirm your site URL

[Section titled “Confirm your site URL”](#confirm-your-site-url)

For Stripe callbacks, email links, and JavaScript API clients to work, you must make sure that you have [configured absolute URLs correctly](/configuration/#absolute-urls).

### Set up your Stripe subscriptions

[Section titled “Set up your Stripe subscriptions”](#set-up-your-stripe-subscriptions)

If you’ve installed with subscriptions, you’ll want to set things up next.

Head to the [subscriptions documentation](/subscriptions) and follow the steps there!

### Set up background tasks

[Section titled “Set up background tasks”](#set-up-background-tasks)

For the progress bar example to work---and to run background tasks of your own---you’ll need a Celery environment running.

Head to [celery](/celery) and follow the steps there!

## Using the Makefile

[Section titled “Using the Makefile”](#using-the-makefile)

Pegasus ships with a self-documenting `Makefile` that will run common commands for you, including starting your containers, performing database operations, and building your front end.

You can run `make` to list helper functions, and you can view the source of the `Makefile` file in case you need to add to it or run any once-off commands. Commands are also documented in your project’s AI rules files.

You can add custom commands to the `Makefile` by editing `custom.mk`.

## Customize your application

[Section titled “Customize your application”](#customize-your-application)

At this point, Pegasus has installed scaffolding for all of the user management, authentication, and (optionally) team views and Stripe subscriptions, and given you a beautiful base UI template and clear code structure to work from.

Now that you’re up and running it’s time for the fun part: building your new application!

This can obviously be done however you like. Some examples of things you might want to do next include:

* Customize your landing page and set up a pricing page
* Start modifying the list of navigation tabs and logged-in user experience
* Create a new django app and begin building out your data models in `models.py`. It’s recommended to use the [Pegasus CLI](https://github.com/saaspegasus/pegasus-cli/) for this.

For some initial pointers on where to to make Pegasus your own, head on over to the [Customizations Page](/customizations).

For the nitty-gritty details on setting up things like email, error logging, sign up flow, analytics, and more go to [Settings and Configuration](/configuration).

# Working with Python Packages (uv)

> Fast Python package management with uv using pyproject.toml and uv.lock files for adding, removing, and upgrading dependencies efficiently.

Recent versions of Pegasus use [uv](https://docs.astral.sh/uv/) to manage Python packages. It provides all the functionality of `pip-tools` while being much faster and offering more flexibility and features.

### Requirements Files

[Section titled “Requirements Files”](#requirements-files)

`uv` uses two files to manage requirements. The first is a `pyproject.toml` file, which contains the base list of packages. The `pyproject.toml` file also supports dependency groups, which are used for development and production requirements. `pyproject.toml` replaces the previous `requirements.in`, `dev-requirements.in`, and `prod-requirements.in` files.

The second file is the `uv.lock` file. This file contains the pinned versions of dependencies that are used by the project’s environment. This file is automatically generated from the `pyproject.toml` file and *should not be edited by hand*. `uv.lock` replaces the previous `requirements.txt`, `dev-requirements.txt`, and `prod-requirements.txt` files.

#### Adding or removing a package

[Section titled “Adding or removing a package”](#adding-or-removing-a-package)

To add or remove packages you can run the following commandss:

```bash
# native version
uv add <package_name>
uv remove <package_name>


# docker version
make uv add <package_name>
make uv remove <package_name>
```

If you’re using natively this is all you have to do! The command will update your `pyproject.toml` file, your `uv.lock` file, and sync your virtual environment.

On Docker, you will have to also rebuild the container. You can do that with:

```bash
make build
make restart
```

The `make requirements` command can also be used to sync your `uv.lock` file and rebuild / restart your containers.

#### Upgrading a package

[Section titled “Upgrading a package”](#upgrading-a-package)

You can upgrade a package with:

```bash
# native version - update the lockfile
uv lock --upgrade-package <package_name>
# native version - update the lockfile and sync the virtual environment
uv sync --upgrade-package <package_name>


# docker version
make uv "lock --upgrade-package wagtail"
```

You can upgrade *all* packages with:

```bash
# native version - update the lockfile
uv lock --upgrade
# native version - update the lockfile and sync the virtual environment
uv sync --upgrade


# docker version
make uv "lock --upgrade"
```

Like with adding packages, if you’re using Docker, you’ll have to rebuild and restart Docker containers for the updated environment to work:

```bash
make build
make restart
```

# Pegasus's Code Structure

> Understand Pegasus project organization with apps, static files, templates, and code formatting using pre-commit hooks and ruff.

## Overall structure

[Section titled “Overall structure”](#overall-structure)

This is the overall structure of a new Pegasus project:

* {{project\_name}}/

  * {{project\_name}}/

    * …

  * apps

    * subscriptions/

      * …

    * teams/

      * …

    * users/

      * …

    * utils/

      * …

    * web/

      * …

  * pegasus

    * apps/

      * …

  * assets

    * javascript/

      * …

    * styles/

      * …

  * requirements/

    * …

  * static

    * css/

      * …

    * images/

      * …

    * js/

      * …

  * templates/

    * …

The first three directories are Python modules while the remaining ones are not.

## Your `{{project_name}}` module

[Section titled “Your {{project\_name}} module”](#your-project_name-module)

This is your Django project root directory. It’s where your settings, root urlconf and `wsgi.py` file will live.

## Your `apps` module

[Section titled “Your apps module”](#your-apps-module)

This is where your project’s apps will live. It is pre-populated with Pegasus’s default apps for you to further customize to your needs.

The module starts with several apps, depending on your configuration. Here are some of the main ones:

* `content` is where the [Wagtail CMS models](/wagtail) are configured.
* `subscriptions` is for functionality related to [Stripe subscriptions](/subscriptions).
* `users` is where your user models and views are defined.
* `teams` is where [team models and views](/teams) are defined.
* `utils` is a set of functionality shared across the project.
* `web` contains utilities and components related to the generic views, layouts and templates.

## The `pegasus` module

[Section titled “The pegasus module”](#the-pegasus-module)

This is where the Pegasus examples live.

In general, it is not expected that you’ll need to modify much in this module, though feel free to do so!

## The `requirements` folder

[Section titled “The requirements folder”](#the-requirements-folder)

This is where you define your project’s Python requirements.

Requirements are managed using `pip-tools`. For more information on using it see [their documentation](https://github.com/jazzband/pip-tools).

## The `assets` folder

[Section titled “The assets folder”](#the-assets-folder)

This is where the source files for your site’s JavaScript and CSS live. These files are what you should edit to change your JS and CSS.

See [front-end](/front-end/overview) for more information on how to compile these files.

## The `static` folder

[Section titled “The static folder”](#the-static-folder)

This folder contains your project’s static files, including the compiled output files from the `assets` folder as well as images.

## The `templates` folder

[Section titled “The templates folder”](#the-templates-folder)

This folder contains your project’s Django templates. There is one sub-folder for each application that has templates. The majority of the project’s base template layouts are in the `templates/web` folder.

## Code formatting

[Section titled “Code formatting”](#code-formatting)

For projects that have enabled the `Autoformat code` option, the code will have been formatted using [ruff](https://github.com/astral-sh/ruff)—a drop-in replacement for [black](https://black.readthedocs.io/en/stable/) and [isort](https://pycqa.github.io/isort/) that runs much faster than those tools.

The project will also include [pre-commit](https://pre-commit.com/) as a dependency in the requirements file as well as the `.pre-commit-config.yaml` file in the root directory. pre-commit is a tool for managing pre-commit hooks - which can be used to ensure your code matches the correct format when it’s committed.

After installing the project dependencies you can install the pre-commit hooks:

```bash
$ pre-commit install --install-hooks
pre-commit installed at .git/hooks/pre-commit
```

The default configuration that ships with Pegasus will run `ruff` and `ruff-format` prior to every Git commit. If there are fixes that are needed you will be notified in the shell output.

### pre-commit Usage

[Section titled “pre-commit Usage”](#pre-commit-usage)

**Manually running hooks**

```bash
# run all hooks against currently staged files
pre-commit run
# run all the hooks against all the files. This is a useful invocation if you are using pre-commit in CI.
pre-commit run --all-files
```

**Temporarily disable hooks**

See <https://pre-commit.com/#temporarily-disabling-hooks>

For more information on using and configuring pre-commit check out the [pre-commit docs](https://pre-commit.com/#quick-start)

### Tool configurations

[Section titled “Tool configurations”](#tool-configurations)

The configuration for the tools can be found in the [`pyproject.toml`](https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#what-on-earth-is-a-pyproject-toml-file) file, using the same syntax as `black`.

For the most part the default black/ruff formats have been preserved, with a few updates, for example, increasing the line length to 120.

You can find more information about these values in the [ruff README](https://github.com/astral-sh/ruff?tab=readme-ov-file#configuration).

### Upgrading

[Section titled “Upgrading”](#upgrading)

See [this cookbook](/cookbooks/#migrating-to-auto-formatted-code) for guidance on how to enable code formatting on an existing Pegasus project.

# Settings and Configuration

> Configure Django settings, environment variables, email providers, social authentication, Stripe payments, and production deployments.

This section describes some of the settings and configuration details you can change inside Pegasus.

## Settings and environment files

[Section titled “Settings and environment files”](#settings-and-environment-files)

Pegasus uses environment variables and `django-environ` to manage settings. You *can* modify values directly in `settings.py`, but the recommended way to modify any setting that varies across environments is to use a `.env` file.

Out-of-the-box, Pegasus will include multiple `.env` files for your settings:

**`.env` is for development in either a native or a Docker-based environnment.** It will be picked up by default if you run `./manage.py runserver` or `docker compose start`. If you need to swap between these environments you might need to modify a few variables in this file---in particular the database and redis URLs.

The `.env` is typically not checked into source control (since it may include secrets like API keys), so is included in the `.gitignore`.

**`.env.example` is an example file.** It is not used for anything, but can be checked into source control so that developers can use it as a starting point for their `.env` file.

Projects downloaded as zip files will include a `.env` file, but projects created or pulled from Github will typically only include a `.env.example` file, so you will need to copy this file locally to run your development server.

*Note: Pegasus versions prior to 2024.3 also included a `.env.docker` file. This has been merged with the `.env` file.*

### Settings environment precedence

[Section titled “Settings environment precedence”](#settings-environment-precedence)

Most settings are configured in the form:

```python
SOME_VALUE = env('SOME_VALUE', default='')
```

As mentioned above, *it is recommended to set these values in your environment / `.env` file*, which will always work as expected.

The environment takes precedence over the default if it’s set---even if it is set to an empty value. This can lead to confusing behavior.

For example, if in your `.env` file you have this line:

```dotenv
SOME_VALUE=''
```

And in your `settings.py` you provide a default:

```python
SOME_VALUE = env('SOME_VALUE', default='my value')
```

The default will be ignored, and `SOME_VALUE` will be an empty string.

To fix this, either *remove the value entirely from your `.env` file*, or *explicitly set the value in your `settings.py`* (instead of using the `default` argument). E.g.

```python
SOME_VALUE = 'my value'
```

## Project Metadata

[Section titled “Project Metadata”](#project-metadata)

When you first setup Pegasus it populated the `PROJECT_METADATA` setting in `settings.py` with various things like page titles and social sharing information.

These settings can later be changed as you like by editing the setting directly:

```python
PROJECT_METADATA = {
    'NAME': 'Your Project Name',
    'URL': 'http://www.example.com',
    'DESCRIPTION': 'My Amazing SaaS Application',
    'IMAGE': 'https://upload.wikimedia.org/wikipedia/commons/2/20/PEO-pegasus_black.svg',
    'KEYWORDS': 'SaaS, django',
    'CONTACT_EMAIL': 'you@example.com',
}
```

See the [project metadata documentation](/page-metadata) for more information about how this is used.

## Absolute URLs

[Section titled “Absolute URLs”](#absolute-urls)

In most of Django/Pegasus, URLs are *relative*, represented as paths like `/account/login/` and so forth. But in some cases you need a complete URL, including the *protocol* (http vs https) and *server* (e.g. [www.example.com](http://www.example.com)). These are necessary whenever you use a link in an email, with an external site (e.g. Stripe API callbacks and social authentication), and in some places when APIs are accessed from your front end.

### Setting your site’s protocol

[Section titled “Setting your site’s protocol”](#setting-your-sites-protocol)

The *protocol* is configured by the `USE_HTTPS_IN_ABSOLUTE_URLS` variable in `settings.py`. You should set this to `True` when using https and `False` when not (typically only in development).

### Setting your server URL

[Section titled “Setting your server URL”](#setting-your-server-url)

When you first install Pegasus it will use the `URL` value from `PROJECT_METADATA` above to create a Django `Site` object in your database. The domain name of this `Site` will be used for your server address.

If you need to change the URL after installation, you can go to the site admin at `admin/sites/site/` and modify the values accordingly, leaving off any http/https prefix.

In development, you’ll typically want a domain name of `localhost:8000`, and in production this should be the domain where your users access your app. Note that this URL must match *exactly* what is in the browser address bar. So, for example, if you load your development site from `127.0.0.1:8000` instead of `localhost:8000` then that is what you should put in.

**Example Development Configuration**

![Development Site Settings](/_astro/site-admin-dev.D-ocuSIA_16FrW3.webp)

**Example Production Configuration**

![Site Settings](/_astro/site-admin.B37AAtIM_Z25ivwv.webp)

## Sending Email

[Section titled “Sending Email”](#sending-email)

Pegasus is setup to use [django-anymail](https://github.com/anymail/django-anymail) to send email via Amazon SES, Mailgun, Postmark, and a variety of other email providers.

To use one of these email backends, change the email backend in `settings.py` to:

```python
EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
```

And populate the `ANYMAIL` setting with the required information. For example, to use [Mailgun](https://www.mailgun.com/) you’d populate the following values:

```python
ANYMAIL = {
    "MAILGUN_API_KEY": "key-****",
    "MAILGUN_SENDER_DOMAIN": 'mg.{{project_name}}.com',  # should match what's in mailgun
}
```

If you are in the EU you may also need to add the following entry:

```python
    'MAILGUN_API_URL': 'https://api.eu.mailgun.net/v3',
```

The [anymail documentation](https://anymail.readthedocs.io/en/stable/) has much more information on these options.

The following django settings should also be set:

```python
SERVER_EMAIL = 'noreply@{{project_name}}.com'
DEFAULT_FROM_EMAIL = 'you@{{project_name}.com'
ADMINS = [('Your Name', 'you@{{project_name}}.com'),]
```

See [Sending email](https://docs.djangoproject.com/en/stable/topics/email/) in the django docs for more information.

## User Sign Up

[Section titled “User Sign Up”](#user-sign-up)

The sign up workflow is managed by [django-allauth](https://allauth.org/) with a sensible set of defaults and templates.

### Social logins

[Section titled “Social logins”](#social-logins)

Pegasus optionally ships with “Login with Google/Twitter/Github” options.

You’ll separately need to follow the steps listed on the [provider-specific pages here](https://docs.allauth.org/en/latest/socialaccount/providers/index.html) to configure things on the other side. These steps can sometimes be a bit involved and vary by platform. But will generally entail two steps:

1. Creating a new application / client on the service you want to use.
2. Adding the credentials to your environment (`.env`) file.

See the Google guide below for an example you can follow.

If you want to add a social login that’s not supported out of the box (e.g. Facebook/Meta or Apple), you can follow the existing patterns and configure things based on the allauth docs.

If you need help setting this up feel free to get in touch! Additionally, see the resources below.

#### Google OAuth Specific instructions

[Section titled “Google OAuth Specific instructions”](#google-oauth-specific-instructions)

1. Register the application with google by following just the “App registration” section [here](https://docs.allauth.org/en/latest/socialaccount/providers/google.html). Note that the trailing slash for the “Authorized redirect URLs” is required. For example, assuming you are developing locally, it should be set to exactly `http://localhost:8000/accounts/google/login/callback/`.

2. Set the resulting client id and secret key in the `.env` file in the root of your project.

   ```dotenv
   GOOGLE_CLIENT_ID="actual client id from the google console"
   GOOGLE_SECRET_ID="actual secret id from the google console"
   ```

#### Other Social Setup Guides

[Section titled “Other Social Setup Guides”](#other-social-setup-guides)

The Pegasus community has recommended the following guides to set things up with specific providers:

* [Github](https://python.plainenglish.io/django-allauth-a-guide-to-enabling-social-logins-with-github-f820239fb73f)

### Requiring email confirmation

[Section titled “Requiring email confirmation”](#requiring-email-confirmation)

Pegasus does not require users to confirm their email addresses prior to logging in. However, this can be easily changed by changing the following value in `settings.py`

```python
ACCOUNT_EMAIL_VERIFICATION = 'optional'  # change to "mandatory" to require users to confirm email before signing in.
```

*Note: The email verification step will be skipped if using a social login.*

### Enabling sign in by email code

[Section titled “Enabling sign in by email code”](#enabling-sign-in-by-email-code)

Sign in by email code is controlled by the `ACCOUNT_LOGIN_BY_CODE_ENABLED` setting. You can enable / disable it in `settings.py`.

```python
ACCOUNT_LOGIN_BY_CODE_ENABLED=True
```

### Two-factor authentication

[Section titled “Two-factor authentication”](#two-factor-authentication)

Two-Factor authentication (2FA) is configured using the [allauth’s mfa](https://docs.allauth.org/en/latest/mfa/index.html) support.

When using Two-Factor Auth with Pegasus, a new section is added to the user profile for enabling & configuring the OTP (one-time password) devices for the user.

If a user has a Two-Factor device configured then they will be prompted for a token after logging in.

### Customizing emails

[Section titled “Customizing emails”](#customizing-emails)

Pegasus ships with simple, responsive email templates for password reset and email address confirmation. These templates can be further customized by editing the files in the `templates/account/email` directory.

See [the allauth email documentation](https://docs.allauth.org/en/latest/common/email.html) for more information about customizing account emails.

### Disabling public sign ups

[Section titled “Disabling public sign ups”](#disabling-public-sign-ups)

If you’d like to prevent everyone from signing up for your app, set the following in your `settings.py`, replacing the existing value:

```python
ACCOUNT_ADAPTER = 'apps.users.adapter.NoNewUsersAccountAdapter'
```

This will prevent all users from creating new accounts, though existing users can continue to login and use the app.

### Further configuration

[Section titled “Further configuration”](#further-configuration)

Allauth is highly configurable. It’s recommended that you look into the various [configuration settings available within allauth](https://docs.allauth.org/en/latest/account/configuration.html) for any advanced customization.

## Stripe

[Section titled “Stripe”](#stripe)

If you’re using [Stripe](https://www.stripe.com/) to collect payments you’ll need to fill in the following in `settings.py` (or populate them in the appropriate environment variables):

```python
STRIPE_LIVE_PUBLIC_KEY = os.environ.get("STRIPE_LIVE_PUBLIC_KEY", "<your publishable key>")
STRIPE_LIVE_SECRET_KEY = os.environ.get("STRIPE_LIVE_SECRET_KEY", "<your secret key>")
STRIPE_TEST_PUBLIC_KEY = os.environ.get("STRIPE_TEST_PUBLIC_KEY", "<your publishable key>")
STRIPE_TEST_SECRET_KEY = os.environ.get("STRIPE_TEST_SECRET_KEY", "<your secret key>")
STRIPE_LIVE_MODE = False  # Change to True in production
```

## Google Analytics

[Section titled “Google Analytics”](#google-analytics)

To enable Google Analytics, add your analytics tracking ID to your `.env` file or `settings.py` file:

```python
GOOGLE_ANALYTICS_ID = 'UA-XXXXXXX-1'
```

Pegasus uses a “global site tag” with gtag.js by default, which is a simpler version of Google Analytics that can be rolled out with zero additional configuration. If you use Google Tag Manager, you can make changes in `templates/web/components/google_analytics.html` to match the snippet provided by Google.

See [this article](https://support.google.com/tagmanager/answer/7582054) for more on the differences between gtag.js and Google Tag Manager.

## Sentry

[Section titled “Sentry”](#sentry)

[Sentry](https://sentry.io/) is the gold standard for tracking errors in Django applications and Pegasus can connect to it with a few lines of configuration.

If you build with Sentry enabled, all you need to do is populate the `SENTRY_DSN` setting - either directly in your `settings.py` or via an environment variable.

After setting it up on production, you can test your Sentry integration by visiting `https://<yourdomain>/simulate_error`. This should trigger an exception which will be logged by Sentry.

## OpenAI and LLMs

[Section titled “OpenAI and LLMs”](#openai-and-llms)

For help configuring LLMs and AIs, see the [AI docs](/ai/development/).

## Celery

[Section titled “Celery”](#celery)

See the [celery docs](/celery) for set up and configuration of Celery.

## Turnstile

[Section titled “Turnstile”](#turnstile)

To enable support for [Cloudflare Turnstile](https://www.cloudflare.com/products/turnstile/), set `TURNSTILE_KEY` and `TURNSTILE_SECRET` in your settings or environment variables.

This should automatically enable turnstile on your sign up pages.

It is recommended to create two different Turnstile accounts on Cloudflare for development and production. In development you can specify “localhost” as your domain like this:

![Turnstile Dev](/_astro/turnstile.1SEbnPxr_Z8Udm.webp)

In production, you should replace that with your site’s production domain.

## Mailing List

[Section titled “Mailing List”](#mailing-list)

Pegasus includes support for subscribing users to a marketing email list upon signup. Currently, three platforms are supported:

1. [Mailchimp](https://mailchimp.com/)
2. [Kit (formerly ConvertKit)](https://kit.com/)
3. [Email Octopus](https://emailoctopus.com/?urli=Cd7hX)

Make sure you choose the platform you would like to use when building your Pegasus project.

Then follow the instructions below for the platform you’ve chosen. After completing these steps, new sign-ups will automatically be added to your configured marketing list. Note that it is your responsibility to notify your users / get their consent as per your local privacy regulations.

### Mailchimp

[Section titled “Mailchimp”](#mailchimp)

To enable the Mailchimp integration, first create a mailing list, then fill in the following to values in your environment/settings.

```python
MAILCHIMP_API_KEY = '<Api Key>'
MAILCHIMP_LIST_ID = '<List ID>'
```

### Kit (formerly ConvertKit)

[Section titled “Kit (formerly ConvertKit)”](#kit-formerly-convertkit)

To enable the Kit integration, create your Kit account and go to Settings —> Developer, and create a new V4 API key.

Then add the API key value to your `.env` file or your environment/settings.

```python
KIT_API_KEY = "<Api Key>"
```

That’s it! New user sign-ups will automatically be added as Kit subscribers.

### Email Octopus

[Section titled “Email Octopus”](#email-octopus)

To enable the Email Octopus integration, first create a mailing list, then fill in the following values in your environment/settings.

```python
EMAIL_OCTOPUS_API_KEY = "<Api Key>"
EMAIL_OCTOPUS_LIST_ID = "<List ID>"
```

Note: If you use [this link](https://emailoctopus.com/?urli=Cd7hX) to sign up for email octopus, you’ll get $15 off your first payment, and help support Pegasus.

## Logging

[Section titled “Logging”](#logging)

Pegasus ships with a default Django log configuration which outputs logs to the console as follows:

* Django log messages at level INFO and above
* Pegasus log messages at level INFO and above

The Pegasus loggers are all namespaced with the project name e.g. `{{project_name}}.subscriptions`.

### Changing log levels

[Section titled “Changing log levels”](#changing-log-levels)

There are two environment variables which can be used to control the log levels of either Django messages or Pegasus message:

* `DJANGO_LOG_LEVEL`
* `{{project_name.upper()}}_LOG_LEVEL`

Alternatively the entire log configuration can be overridden using the `LOGGING` setting as described in the [Django docs](https://docs.djangoproject.com/en/stable/topics/logging/).

## Storing media files

[Section titled “Storing media files”](#storing-media-files)

SaaS Pegasus ships with optional configuration for storing dynamic media files in S3 e.g. user profile pictures. If you do not have this enabled the [default Django configuration](https://docs.djangoproject.com/en/stable/topics/files/) will be used which requires you to have persistent storage available for your site such as a Docker volume.

### Setting up S3 media storage

[Section titled “Setting up S3 media storage”](#setting-up-s3-media-storage)

*For a video walkthrough of this content (using kamal deployment), see below:*

This section assumes you have set up your SaaS Pegasus project with the **S3 media file storage** enabled.

In order to use S3 for media storage you will need to create an S3 bucket and provide authentication credentials for writing data to the bucket.

Once you have done the S3 setup (see below), you can update your `.env` file as follows:

```dotenv
USE_S3_MEDIA=True
AWS_ACCESS_KEY_ID=<IAM user's access key>
AWS_SECRET_ACCESS_KEY=<IAM user's secret key>
```

With this configuration your media files will be accessible at `https://{{ project_name }}-media.s3.amazonaws.com/media/`.

[This guide](https://testdriven.io/blog/storing-django-static-and-media-files-on-amazon-s3/) is an excellent resource with step-by-step instructions for the S3 setup.

#### Additional settings

[Section titled “Additional settings”](#additional-settings)

AWS\_STORAGE\_BUCKET\_NAME : Name of the S3 bucket to use. Defaults to `{{project_name}}-media`.

### Alternative storage backends

[Section titled “Alternative storage backends”](#alternative-storage-backends)

Should you wish to use a different storage backed e.g. [Digital Ocean Spaces](https://www.digitalocean.com/products/spaces) you can follow the setup described in the [django-storages](https://django-storages.readthedocs.io/en/latest/index.html) documentation.

There is also a [Pegasus community guide](/community/digital-ocean-spaces) that walks through this in more detail.

## Django Debug Toolbar

[Section titled “Django Debug Toolbar”](#django-debug-toolbar)

Pegasus ships with [Django Debug Toolbar](https://github.com/jazzband/django-debug-toolbar#readme) as an optional package. This section describes how the feature is configured in Pegasus.

The `django-debug-toolbar` package is placed in the `dev-requirements.txt` file which means it will only be available in dev environments. Should you wish to use it in a production environment you will need to add it to your `prod-requirements.in` file and [re-build](/python/setup) your `prod-requirements.txt` file.

By default, the toolbar is enabled in development environments via the `ENABLE_DEBUG_TOOLBAR` setting in your `.env` file(s). You can change this setting in any environment to turn it on/off.

```dotenv
ENABLE_DEBUG_TOOLBAR=True
```

# APIs

> Django REST Framework APIs with auto-generated OpenAPI schemas, TypeScript clients, and authentication support for building modern web applications.

Pegasus comes with a rich ecosystem of APIs that can used by your app’s front end as well as exposed to third-party developers.

## APIs in Pegasus

[Section titled “APIs in Pegasus”](#apis-in-pegasus)

APIs in Pegasus consist of three pieces:

1. **API endpoints**, created with [Django Rest Framework (DRF)](https://www.django-rest-framework.org/). These are the Django views that serve your APIs.
2. **API schemas**, created with [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/). These are automatically created by your APIs, and can be used for API documentation and client generation. They follow the [OpenAPI 3](https://spec.openapis.org/oas/v3.1.0) specification.
3. **API clients**, created by [OpenAPI Generator](https://openapi-generator.tech/). These can be used by developers to interact with your APIs. Pegasus ships with a TypeScript (JavaScript) client that is used in your app’s front end by the parts of the app that interact with the backend APIs (e.g. JavaScript charts, and the React/Vue demos).

This might sound like a lot of moving parts, but, critically, *all the logic lives in the API endpoints themselves*. The schemas are auto-generated by the endpoints, and the clients are auto-generated by the schemas. So you only have to maintain your APIs in a single place, and everything else is kept in sync with tooling.

Using the schemas and clients is optional. You can always interact with a Pegasus API by making the appropriate HTTP requests directly. However, using a client can greatly simplify the code you write and improve the development experience. Front end code in Pegasus that interacts with APIs uses it by default.

Additionally, getting API docs “for free” from the schemas can be a big win if you plan to make your project’s API third-party-developer-facing.

## API Documentation

[Section titled “API Documentation”](#api-documentation)

By default, your Pegasus app ships with two built-in sets of API documentation available at the `/api/schema/swagger-ui/` endpoint (<http://localhost:8000/api/schema/swagger-ui> in development) and `/api/schema/redoc/` endpoint (<http://localhost:8000/api/schema/redoc/> in development).

The API docs will look something like this:

**Swagger API docs:**

![Swagger API Docs](/_astro/swagger-api-docs.CyMzYekt_ZX2A8c.webp)

**Redoc API docs:**

![Redoc API Docs](/_astro/redoc-api-docs.9KICU7qX_Z1EUqMg.webp)

## API Clients

[Section titled “API Clients”](#api-clients)

As part of the [front end](/front-end/overview), Pegasus ships with an API client that can be used to interact with your project’s APIs. **This client is automatically generated from your APIs and should not be modified by hand.**

You can find the source code of the API client(s) in the `api-client` folder in your project’s root directory.

*Note: In releases prior to 2024.3 the API client was in the `assets/javascript/api-client` directory.*

### Using the API client

[Section titled “Using the API client”](#using-the-api-client)

There are several example usages of the API client in the Pegasus codebase. The steps, as seen in the employee app demo, are as follows:

**Initialize the API client**

```javascript
import {Cookies} from "./app";
import {Configuration, PegasusApi} from "./api-client";


const apiConfig = new Configuration({
  basePath: 'https://yourserver.com/',  // or pass this in via {{server_url}} template variable
  headers: {
    'X-CSRFToken': Cookies.get('csrftoken'),
  }
})
const client = new PegasusApi(apiConfig);
```

**Call an API**

```javascript
client.employeesList().then((result) => {
  // do something with the API result here
  console.log('your employees are ', result.results);
});
```

### Client method names

[Section titled “Client method names”](#client-method-names)

The easiest way to find out the methods available in the API client is by looking at the source code in `api-client/apis/<AppName>Api.ts`.

Method names are determined by the `operationId` value for the API in the auto-generated `schema.yaml` file. These identifiers are auto-generated, but can be overridden using DRF Spectacular’s `extend_schema_view` and `extend_schema` helper functions.

This can be done for an entire `ViewSet` as follows:

```python
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets


@extend_schema_view(
    create=extend_schema(operation_id='employees_create'),
    list=extend_schema(operation_id='employees_list'),
    retrieve=extend_schema(operation_id='employees_retrieve'),
    update=extend_schema(operation_id='employees_update'),
    partial_update=extend_schema(operation_id='employees_partial_update'),
    destroy=extend_schema(operation_id='employees_destroy'),
)
class EmployeeViewSet(viewsets.ModelViewSet):
    # rest of viewset code here
```

The IDs in the Python code will be converted to camelCase in the JavaScript client.

### Generating the OpenAPI3 schema.yml file

[Section titled “Generating the OpenAPI3 schema.yml file”](#generating-the-openapi3-schemayml-file)

In a new Pegasus installation, the OpenAPI3 `schema.yml` will be available at the `/api/schema/` endpoint (<http://localhost:8000/api/schema/> in dev).

If you plan to use the `schema.yml` file in production, it is more efficient to create it once and serve it as a static file. This can be done by running:

```bash
./manage.py spectacular --file static/api-schema.yml
```

Then you can reference the file by using `{% static /api-schema.yml %}` in a Django template.

### Generating the API client

[Section titled “Generating the API client”](#generating-the-api-client)

Anytime you change your APIs you should create a new API client to keep things in sync. This can be done using the [OpenAPI Generator](https://openapi-generator.tech/) project. The [typescript-fetch](https://openapi-generator.tech/docs/generators/typescript-fetch) client is the one used by Pegasus.

#### Running natively (requires Java)

[Section titled “Running natively (requires Java)”](#running-natively-requires-java)

To generate your API client natively, first install the `openapi-generator-cli` (this library also requires `java`):

```bash
npm install @openapitools/openapi-generator-cli -g
```

Then run it as follows:

```bash
openapi-generator-cli generate -i http://localhost:8000/api/schema/ -g typescript-fetch -o ./api-client/
```

The above assumes your Django server is running at <http://localhost:8000>, but you can replace that value with any URL or file system reference to your `schema.yml` file.

#### Running in docker

[Section titled “Running in docker”](#running-in-docker)

You can also generate your API client with docker to avoid having to install Java by running:

```bash
make build-api-client
```

while your server is running. You should see the files in `api-client` get updated.

#### Rebuilding your front end

[Section titled “Rebuilding your front end”](#rebuilding-your-front-end)

After re-creating the API client, you’ll have to rebuild your front end:

```bash
npm run dev
```

Note that introducing breaking changes to your APIs can also break your API client! If you’re unsure if you introduced breaking changes it is worth testing any functionality that depends on the API client.

## Authentication APIs

[Section titled “Authentication APIs”](#authentication-apis)

*Added in version 2024.3. Changed in 2025.4.1*

If you enable the “Use Authentication APIs” checkbox in your project, Pegasus will generate a set of API endpoints for registering and logging in users. These endpoints can be used to integrate your backend with single page applications (SPAs) and mobile apps.

Under the hood, Pegasus uses [allauth headless](https://docs.allauth.org/en/dev/headless/openapi-specification/) for these endpoints.

This feature uses Django’s session-based authentication by default---which works great for single page apps---though it is possible to add in JWT or another token-based authentication scheme to better support mobile applications.

A complete end-to-end example that uses the API authentication feature in a React SPA can be found in the experimental [standalone front end](/experimental/react-front-end). This example includes React/API-based sign up, login, password reset, two-factor authentication, email confirmation and more.

## API Keys

[Section titled “API Keys”](#api-keys)

Pegasus supports the use of API Keys to access APIs, built on top of the [Django REST Framework API Key](https://florimondmanca.github.io/djangorestframework-api-key/) project.

Pegasus includes the ability to create API keys, associate them with your User objects, and access APIs using the key.

### Creating and managing API keys

[Section titled “Creating and managing API keys”](#creating-and-managing-api-keys)

A simple UI for creating, viewing, and revoking API keys is available to end users from the Profile page.

More advanced/customized management of API keys---including the ability to associate names and expiry dates with keys---is available through the Django admin interface.

Note that when an API key is created it will be displayed *once* and will not be available after that.

For more details on working with API keys see [the library documentation](https://florimondmanca.github.io/djangorestframework-api-key/guide/#creating-and-managing-api-keys).

### API keys and Users

[Section titled “API keys and Users”](#api-keys-and-users)

Pegasus associates API keys with your Django `User` objects. This is a good, practical way to get started with API key scoping. All access granted by the key will the same as the associated `CustomUser` object, which allow you to easily create APIs that work with logged-in users *or* API keys.

The `apps.api.models.UserAPIKey` class is used to associate an API key with a `CustomUser`. You can then enable API keys for any user-specific views, by following the instructions for `APIView`s and `ViewSet`s below.

More complex API key permissions---for example, associating a key with a single API or a single team---can be created by following [these instructions](https://florimondmanca.github.io/djangorestframework-api-key/guide/#api-key-models).

To enable API-key support for an `APIView`, or `ViewSet`, use the `IsAuthenticatedOrHasUserAPIKey` permission class in place of `IsAuthenticated`. This will allow either authenticated users or UserAPIKey users to access the APIs. In either case, the associated user object will be available as `request.user`.

You can see an example `APIView` in the `EmployeeDataAPIView` class that ships with the Pegasus examples, and an example `ViewSet` in the `EmployeeViewSet` code.

### Testing API keys

[Section titled “Testing API keys”](#testing-api-keys)

The easiest way to test API key functionality is to use a tool like [curl](https://curl.se/).

The following command can be used to test a user-based API key with a default Pegasus installation:

```bash
curl http://localhost:8000/pegasus/employees/api/employees/ -H "Authorization: Api-Key <your-api-key>"
```

You should replace `<your-api-key>` with the API key displayed when it is created.

## Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

### API client requests are failing

[Section titled “API client requests are failing”](#api-client-requests-are-failing)

When API client requests fail you will get error messages in parts of the application that use the API clients, including the Teams UI (if you are using React), and the React/Vue employee examples.

The most common reason that API client requests fail is a mismatch between the absolute URL configured in the server and the servers *actual* URL. This mismatch be fixed by modifying the Django Site object and settings to match the URL you’re loading the site from, as described in the documentation on [absolute URLs](/configuration/#absolute-urls).

In *development* the most common issues are:

1. Your Django Site is not set up for development. Ensure the site’s domain name is `localhost:8000` in your Django admin, [as described here](/configuration/#absolute-urls).
2. You are loading from a mismatched domain. Be sure you are loading your browser at <http://localhost:8000> and not <http://127.0.0.1:8000>. Or alternatively, if you want to use the 127.0.0.1 address, update the Django site accordingly to use that.

# Async and Websocket Support

> Enable asynchronous Django views and real-time websockets using Daphne, Uvicorn, and Django Channels for modern web applications.

As of version 2023.10, Pegasus provides support [asynchronous support](https://docs.djangoproject.com/en/stable/topics/async/), as well as support for websockets via the [channels library](https://channels.readthedocs.io/).

## Enabling Async Support

[Section titled “Enabling Async Support”](#enabling-async-support)

You can enable Async support by checking the “Use Async / Websockets” option in your project settings. Enabling Async will:

1. Change your default development server to [Daphne](https://docs.djangoproject.com/en/stable/howto/deployment/asgi/daphne/).
2. Change your default production server to [Uvicorn](https://www.uvicorn.org/) (via gunciorn).
3. Add and configure `channels` in your project for websocket support.

In addition to the above configuration changes, enabling async will also use it for LLM chats if available. Finally, there is an optional group chat application you can separately add (details below).

## The Async / Websocket Demo Application

[Section titled “The Async / Websocket Demo Application”](#the-async--websocket-demo-application)

Pegasus includes an optional demo application to demonstrate the asynchronous and socket capabilities. The demo application is an extension of the demo application that you build while completing the [channels tutorial](https://channels.readthedocs.io/en/latest/tutorial/index.html). You can see a demo below.

The demo application uses the [HTMX websockets extension](https://htmx.org/extensions/ws/) to simplify the implementation. If you prefer not to use HTMX at all, you can change your websocket connection logic to use vanilla JavaScript instead, as shown in the [channels tutorial here](https://channels.readthedocs.io/en/latest/tutorial/part_2.html#add-the-room-view).

A React-based websocket demo is on the roadmap.

## Websocket urls

[Section titled “Websocket urls”](#websocket-urls)

Websocket URLs are defined separately from your app’s main `urls.py` file. In Pegasus, the convention is to put your websocket urls in `channels_urls.py` in your project folder (the same one containing `urls.py`).

Because websocket urls are separate from your main app, and because they follow a different protocol, they must be referenced as absolute URLs in your front end (including prepending “ws\://” or “wss\://” depending on whether you’re using HTTPS).

Pegasus ships with two helper functions you can use to assist with working with URLs, so long as you follow Pegasus conventions. The `websocket_reverse` function will reverse a relative websocket URL, and the `websocket_absolute_url` function will turn a relative URL into an absolute websocket URL based on your Site address and the `USE_HTTPS_IN_ABSOLUTE_URLS` setting.

You can combine these functions like so to pass the URL of a websocket endpoint to a template:

```python
room_ws_url = websocket_absolute_url(websocket_reverse("ws_group_chat", args=[room_id]))
```

You can then use the websocket URL in a template/JavaScript like this:

```js
const chatSocket = new WebSocket({{ room_ws_url}});
chatSocket.onmessage = function(e) {
  // handle message
};
```

## Asynchronous web servers

[Section titled “Asynchronous web servers”](#asynchronous-web-servers)

There are several ASGI servers supported by Django. By default, Pegasus uses the Daphne web server in development and the Uvicorn web server in production, for reasons described below. That said, you can customize your app to use whichever server you prefer.

### Daphne

[Section titled “Daphne”](#daphne)

In development, Pegasus uses the [Daphne](https://pypi.org/project/daphne/) web server for its tight integration with Django’s `runserver` command, as [outlined in the Django docs](https://docs.djangoproject.com/en/stable/howto/deployment/asgi/daphne/).

Daphne is installed via `dev-requirements` and will be added to your `INSTALLED_APPS` whenever `settings.DEBUG` is `True`.

### Uvicorn

[Section titled “Uvicorn”](#uvicorn)

In production, Pegasus uses the [Uvicorn](https://www.uvicorn.org/) web server. Uvicorn has a seamless integration with `gunicorn`, making transitioning to it very easy.

Uvicorn is installed via `prod-requirements`, and if you build with async features enabled, your `gunicorn` command will be updated to use it.

## Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

**The chat app loads but nothing happens when I send a message.**

The most likely reason this would happen is if your site URLs are not set up properly, which would cause the websocket endpoints to not hit the right address.

See the documentation on [absolute URLs](/configuration/#absolute-urls) to fix this, and in particular make sure your Django site object has the right domain. In development this should be set to `localhost:8000`.

**I’m getting an error: No module named ‘daphne’**

If you are getting this error *in production* it is likely because your `DEBUG` environment variable is not set.

Due to the order in which settings are imported, you *must* define `DEBUG=False` in your *environment*, `.env` file, or main `settings.py` file. This is in addition to (or instead of) setting `DEBUG=False` in your `settings_production.py` file.

If you are getting this error *in development*, be sure that Daphne is installed. You should have the a `channels[daphne]` entry in your `dev-requirements.in` file, and you should [build and install your requirements](/python/setup) as needed.

To do this in a non-Docker environment, run:

```plaintext
pip-compile requirements/dev-requirements.in
pip install -r requirements/dev-requirements.txt
```

**I’m having another issue deploying to production.**

Since this is a new feature there may be some speed-bumps getting it into production on all platforms. While every deployment platform is expected to work, it is not possible to test every app/configuration. So, if you have any issues please reach out over email (<support@saaspegasus.com>) or on Slack and I will do my best to help!

# Celery

> Set up Celery distributed task queues with Redis for background tasks, scheduled jobs, and async processing in Pegasus applications.

[Celery](https://docs.celeryq.dev/) is a distributed task queue used to run background tasks.

It is required by several Pegasus features, including:

1. The “background task” example.
2. Per-unit subscriptions (celery runs the background task to sync unit amounts with Stripe).
3. AI Chat (it is used in all builds to set chat names, and, if async is not enabled, for the chats themselves).

If you aren’t using any of the above features, you can disable celery by unchecking the “use celery” option---added in version 2025.1---in your project settings. **If you *are* using any of the above features, this option will not do anything.**

## Quick Start

[Section titled “Quick Start”](#quick-start)

**If you’re using [Docker in development](/docker) then Celery should automatically be configured and running. The instructions in this section are for running Celery outside of Docker.**

The easiest way to get going in development is to [download and install Redis](https://redis.io/download) (if you don’t already have it) and then run:

*With uv:*

```bash
uv run celery -A {{ project_name }} worker -l info --pool=solo
```

*With standard Python:*

```bash
celery -A {{ project_name }} worker -l info --pool=solo
```

Note that the ‘solo’ pool is recommended for development but not for production. When running in production, you should use a more robust pool implementation such as `prefork` (for CPU bound tasks) or `gevent` (for I/O bound tasks).

### Celery and Gevent

[Section titled “Celery and Gevent”](#celery-and-gevent)

In production Celery is configured to run with the `gevent` pool, which drastically improves performance of Celery when running tasks that are I/O bound (which tends to be most tasks that make API or database calls).

However, `gevent` does have some limitations, including that it does not work well `asyncio`. This means that if you are calling lots of async code in your Celery tasks, you should consider a different pool.

To change the pool used by Celery you can modify (or remove) the `--pool` command when you call it. Note that `--pool=solo` or `--pool=gevent` is recommended for running Celery on Windows, since Celery 4.x [no longer officially supports Windows](https://docs.celeryq.dev/en/4.0/whatsnew-4.0.html#removed-features).

For more information see the [Celery documentation](https://docs.celeryq.dev/en/stable/userguide/concurrency/gevent.html).

## Setup and Configuration

[Section titled “Setup and Configuration”](#setup-and-configuration)

The above setup uses [Redis](https://redis.io/) as a message broker and result backend. If you want to use a different message broker, for example [RabbitMQ](https://www.rabbitmq.com/), you will need to modify the `CELERY_BROKER_URL` and `CELERY_RESULT_BACKEND` values in `settings.py`.

More details can be found in the [Celery documentation](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/index.html).

## Monitoring with Flower

[Section titled “Monitoring with Flower”](#monitoring-with-flower)

[Flower](https://flower.readthedocs.io/en/latest/) is an open-source web application for monitoring and managing Celery clusters. It provides real-time information about the status of Celery workers and tasks.

If you’d like to use Flower in development, add the following to the `services` section of your `docker-compose.yml`:

```yaml
  flower:
    image: mher/flower
    environment:
      - CELERY_BROKER_URL=redis://redis:6379
    command: celery flower
    ports:
      - 5555:5555
    depends_on:
      - redis
```

In production, you will likely want to run Flower behind a private VPN, or [set up authentication](https://flower.readthedocs.io/en/latest/auth.html) on your Flower instance, and use a [reverse proxy](https://flower.readthedocs.io/en/latest/reverse-proxy.html) to expose it.

## Scheduled Tasks with Celery Beat

[Section titled “Scheduled Tasks with Celery Beat”](#scheduled-tasks-with-celery-beat)

[Celery Beat](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html) is a scheduler that triggers tasks at regular intervals, which can be used to run periodic tasks like daily reports, or sending scheduled notifications.

### Configuration

[Section titled “Configuration”](#configuration)

By default, Celery Beat will store the schedule in file on the filesystem. When running in a production environment and especially in a containerized environment, you should use persistent storage to store the schedule. Pegasus is pre-configured to store the schedule in the Pegasus database using [`django-celery-beat`.](https://django-celery-beat.readthedocs.io/en/latest/).

You can place the schedule task definitions in the `SCHEDULED_TASKS` setting in your `settings.py` file and then run the `bootstrap_celery_tasks` management command to create the tasks in the database.

```python
from celery.schedules import crontab


SCHEDULED_TASKS = {
    'example-task-every-morning': {
        'task': '{{ project_name }}.tasks.example_task',
        'schedule': crontab(hour=7, minute=0),  # Run every day at 7:00 AM
    },
    'another-example-every-hour': {
        'task': '{{ project_name }}.tasks.another_example',
        'schedule': 3600.0,  # Run every hour (in seconds)
        'args': (16, 16),  # Arguments to pass to the task
    },
}
```

```bash
python manage.py bootstrap_celery_tasks --remove-stale
```

This will create or update the tasks in the database and remove any stale tasks that are no longer defined in `SCHEDULED_TASKS`.

If you want to bootstrap the tasks automatically during you application deploy process you can do so by running the bootstrap command alongside the Django migration command.

### Running Celery Beat

[Section titled “Running Celery Beat”](#running-celery-beat)

To run Celery Beat in development:

*With Docker:*

If you are using the local dockerized setup with docker compose, then Celery Beat will already be running as part of the `celery` service.

*With uv:*

```bash
# Alongside the Celery worker, you can run Celery Beat
uv run celery -A {{ project_name }} worker -l info --beat


# AS a dedicated process
uv run celery -A {{ project_name }} beat -l info
```

Note that if you run Celery Beat as a standalone process, you will need to ensure that the Celery worker is running separately. This is because Celery Beat is responsible for scheduling tasks while the worker executes them.

#### Production Setup

[Section titled “Production Setup”](#production-setup)

In production, you can run Celery Beat as a separate process. You must ensure that there is only ever one Celery Beat process running at a time to avoid multiple instances of the same task being scheduled.

It’s also important to note that you can not run Celery Beat in the same process as a worker that is using the `gevent` pool.

For more information, see the [Celery Beat documentation](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html).

# Cookbooks

> Step-by-step guides for Django admin setup, migrating from pip-tools to uv, enabling code formatting, and common development tasks.

Step-by-step guides to some different things you might want to do with Pegasus.

## Use the Django Admin UI

[Section titled “Use the Django Admin UI”](#use-the-django-admin-ui)

Pegasus ships with a simple script to promote any user to a superuser who can access the Django admin.

After going through the sign up flow, to convert your newly-created user into an admin, run the following command, being sure to replace the email address with the one you used to sign up:

**Docker:**

```bash
docker compose exec web python ./manage.py promote_user_to_superuser yourname@example.com
```

**Native:**

```bash
python ./manage.py promote_user_to_superuser yourname@example.com
```

Now you should be able to access the django admin at <http://localhost:8000/admin>

## Migrating from pip-tools to uv

[Section titled “Migrating from pip-tools to uv”](#migrating-from-pip-tools-to-uv)

To migrate your project from pip-tools to uv follow these steps.

### Install uv

[Section titled “Install uv”](#install-uv)

If you haven’t already, [install uv](https://docs.astral.sh/uv/getting-started/installation/):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Update your project code

[Section titled “Update your project code”](#update-your-project-code)

It’s recommended to do this in two steps:

1. [Upgrade your project](/upgrading) to the latest Pegasus version, keeping your package manager as “pip-tools”. Merge all conflicts and ensure your project is working properly on this version.
2. Then, change the package manager from pip-tools to uv in your project settings and do another upgrade/pull request.

At this point you will likely have conflicts in your requirements files, but hopefully nowhere else. See the next sections for resolving these.

### Prepare to resolve conflicts

[Section titled “Prepare to resolve conflicts”](#prepare-to-resolve-conflicts)

First, follow the github instructions to merge your project on your local machine, by checking out the pegasus upgrade branch and merging the main branch into it. You will have to update the command below with the exact branch name of the pull request created by Pegasus:

```bash
git fetch origin
git checkout pegasus-<version>-<timestamp>
git merge main
```

At this point you’ll have a partially merged branch with conflicts.

### Migrate your requirements.in files

[Section titled “Migrate your requirements.in files”](#migrate-your-requirementsin-files)

The uv build of Pegasus no longer uses requirements files, so any changes you’ve made to these will need to be migrated to `pyproject.toml` and `uv.lock`.

You can use the [reqs-sync](https://github.com/saaspegasus/reqs-sync/) package to help with this. Follow the steps below for any file with conflicts.

To migrate your main *requirements.in* file:

```bash
uv tool run reqs-sync reqs-to-toml requirements/requirements.in
```

To migrate your development *dev-requirements.in* file:

```bash
uv tool run reqs-sync reqs-to-toml requirements/dev-requirements.in --group=dev
```

To migrate your production *prod-requirements.in* file:

```bash
uv tool run reqs-sync reqs-to-toml requirements/prod-requirements.in --group=prod
```

These commands should copy all project requirements from your `requirements.in` file(s) to your `pyproject.toml` file (into the appropriate group, if necessary).

### Update your uv.lock file

[Section titled “Update your uv.lock file”](#update-your-uvlock-file)

Next you should rebuild your `uv.lock` file from the updated `pyproject.toml` file:

```bash
uv lock
```

You should then check the versions that were added to the `uv.lock` file and update any as needed based on the versions your requirements.txt files.

### Test the migration

[Section titled “Test the migration”](#test-the-migration)

Run your project (`uv run python manage.py runserver`) and verify everything works as expected.

### Remove your requirements files

[Section titled “Remove your requirements files”](#remove-your-requirements-files)

Finally, run:

```bash
git rm requirements/*`
```

To remove all your requirements files.

Congratulations, you’ve migrated to uv! Resolve any other conflicts, push and merge your code, and you’re done!

## Migrating to auto-formatted code

[Section titled “Migrating to auto-formatted code”](#migrating-to-auto-formatted-code)

As of February, 2023 all Pegasus projects have the option to auto-format your Python code.

To migrate a project from non-formatted to formatted code, you can go through the following steps:

1. First, do a full Pegasus upgrade to the version you want to update to, as described [here](/upgrading). **Do *not* check the “autoformat” checkbox yet.**

2. Next, run the formatting tools on your project’s `main` branch:

   1. Install ruff: `pip install ruff`
   2. Run ruff linting `ruff check --extend-exclude migrations --line-length 120 . --fix`
   3. Run ruff formatting: `ruff format --line-length 120 .`

3. Commit the result:

   1. `git add .`
   2. `git commit -m "apply formatting changes"`

4. Finally, check the “autoformat” box on your Pegasus project, and do *another* upgrade according to the same process.

## Migrating an existing project to Pegasus

[Section titled “Migrating an existing project to Pegasus”](#migrating-an-existing-project-to-pegasus)

There is not a one-size-fits-all answer to how to migrate an existing app to Pegasus, as it can depend on the size, complexity, age, and architecture of the project you’re migrating from.

That said, the strategy that has worked best for most people on small-to-medium-sized projects is to basically **start a new project on Pegasus and merge your existing functionality into it**.

Here is a rough guideline for how you can do that:

1. Create a new Pegasus project with the exact settings you want your app to have. If your existing app uses certain technologies (e.g. css frameworks, deployment, etc.) it’s probably easiest to pick all the same ones, if possible, unless you know you want to change those at the same time.
2. Bring across the custom logic of your legacy project, while largely preserving the previous project’s structure. So, for example, if your project was split into multiple Django apps, just copy those across. If it was a monolith, just leave it that way, and so on.
3. Reconcile any conflicting data models. E.g. you will only want a single user model. Ideally you would use Pegasus’s built-in `CustomUser` model and update your foreign keys accordingly, although this can make data migrations more complicated.
4. Try and get the urls/views etc. working for your previous app’s functionality. Don’t worry about UI, but just try to get the routes and business logic working and routing to the right tmeplates.
5. Migrate those templates to use the Pegasus base templates, etc. (if possible). You can kind of do this page by page, making each one look good as you go. Alternatively, keep your own base template if it is different enough from Pegasus’s or if you want to keep your existing app scaffolding. The latter option will require updating Pegasus’s built-in functionality to work with your own templates, and will make future upgrades/merges more complicated.
6. Figure out a data migration (assuming you already have production data). This can often be the trickiest part, especially if you’re swapping the user model or othe foregn keys. It can often be easiest to write scripts to copy the data across from one instance to the other, but in some cases you might prefer to keep your previous migration history in place and run migrations on the live database. The larger the project is, the more likely it is you’ll want to keep the database and existing models and just use migrations to do the minimal set of Pegasus changes.

The main downsides of the above approach are that you lose your git history on the previous project, data migrations can be tricky, and if you have a complex UI then it might take some effort to port across. The main upside is that once you get through the pain, all future Pegasus updates will likely be much smoother.

## Delete Pegasus Examples

[Section titled “Delete Pegasus Examples”](#delete-pegasus-examples)

You can remove the Pegasus examples by unchecking the “Include Examples” checkbox on your project page and re-downloading (/or [upgrading](/upgrading)) your codebase.

For earlier versions you can use [these instructions](https://github.com/saaspegasus/pegasus-docs/blob/1becc2cb8f86738eeba85c9faddb15f69b8ad7bc/cookbooks.md#delete-pegasus-examples).

# Customizations

> Customize landing pages, navigation, styles, and JavaScript in your Pegasus application with popular CSS frameworks.

This page outlines the basics of customizing Pegasus to meet your application’s needs.

## Personalize your landing page

[Section titled “Personalize your landing page”](#personalize-your-landing-page)

Pegasus ships with a simple landing page that varies based on your selected CSS framework. Most projects will want to highly customize the landing page from what comes out of the box. Unless you are planning on building a marketing site on a different platform, this is likely one of the first things you’ll do.

To modify the default landing page, you can edit the `./templates/web/landing_page.html` file (and any included sub-templates) and make the customizations you want.

Another good option is to use a paid or open-source alternative for your marketing content. Some recommended places to get marketing templates include:

* **Tailwind**: [Tailwind UI](https://tailwindui.com/), [Flowbite](https://flowbite.com/).
* **Bootstrap**: [Official themes](https://themes.getbootstrap.com/), [other free recommendations](https://dev.to/bootstrap/bootstrap-5-templates-91p).
* **Bootstrap (Material)**: [Material Kit Pro](https://www.creative-tim.com/product/material-kit-pro)

## Update the logged-in experience

[Section titled “Update the logged-in experience”](#update-the-logged-in-experience)

After you’ve tweaked your landing page, you’ll likely want to dive into the nuts and bolts that make up your app.

To modify the logged-in default page, edit the `./templates/web/app_home.html` file to your liking.

### Changing the navigation

[Section titled “Changing the navigation”](#changing-the-navigation)

There are two levels of navigation that ship with Pegasus, the top nav and the sidebar nav. You’ll likely want to modify both.

To change the top nav edit the `./templates/web/components/top_nav.html` file.

To change the sidebar nav edit the `./templates/web/components/app_nav.html` file.

## Styles

[Section titled “Styles”](#styles)

All of Pegasus’s CSS frameworks are designed to be customized to your needs. You can set specific colors or override the themes entirely.

How styles are customized depends on the CSS framework. For more information, see the individual page for your framework in [the CSS docs](/css/overview)

## Javascript

[Section titled “Javascript”](#javascript)

The project uses a Vite build pipeline to compile the JavaScript files.

For more details on how it works see the [front-end documentation](/front-end/overview).

# Using Docker in Development

> Set up Django development environment with Docker Compose including PostgreSQL, Redis, Celery, and debugging configuration.

Pegasus recommends using [Docker](https://www.docker.com/) during development. Although Docker is not strictly required, many parts of the documentation and helper tools do assume you are using it.

In production, Docker can also be used to deploy your application to containerized platforms. See [the deployment page](/deployment/overview) for more details on Docker in production.

## Choosing a Docker Setup

[Section titled “Choosing a Docker Setup”](#choosing-a-docker-setup)

When configuring your Pegasus project to use Docker, you can select from two different options: **services-only**, and **full-Docker development**.

In **services-only mode**, Docker is only used to run the external services: PostgreSQL and Redis. The Django server, Celery and any other processes are run directly on the local machine. In this mode, you don’t need to install PostreSQL and Redis on your local machine, which simplifies the setup and maintenance. You also have direct access to the other dev processes which simplifies debugging and inspection. The main downside of services-only mode is that it requires installing `uv` and `npm`.

In **full-Docker** mode, Docker is used to run the services, as above, but also runs Django, npm, and Celery. No processes are run directly on your local machine. This mode makes it easier to get up and running---since all you need to install is Docker---but it can make development more complicated, since all the processes are running inside Docker.

As a rough guideline: **If you are comfortable installing and running Python and Node.js on your machine, use services-only mode. Otherwise, use full-Docker mode.**

## Install prerequisites

[Section titled “Install prerequisites”](#install-prerequisites)

You need to install [Docker](https://www.docker.com/get-started) prior to setting up your environment.

Mac users have reported better performance on Docker using [OrbStack](https://orbstack.dev/), which is a Docker Desktop alternative optimized for performance.

## Starting the application

[Section titled “Starting the application”](#starting-the-application)

To start the Docker services, run:

```bash
make start
```

This will start the Database services (PostgreSQL and Redis) and in full-mode, start all the processes needed to run your application, including Django, the front end build, and Celery.

make and Windows

Windows users may need to install a 3rd-party package to run `make` commands. The easiest way to do that is via [these instructions](https://stackoverflow.com/a/57042516/8207).

The first time you run the app you should run:

```bash
make init
```

Which will also create and run database migrations and bootstrap your application.

## Architecture and how it works

[Section titled “Architecture and how it works”](#architecture-and-how-it-works)

This section provides technical details about the Docker setup and how it works.

The Docker configuration is primarily in `docker-compose.yml`, where you can inspect the configured containers.

### Services only mode

[Section titled “Services only mode”](#services-only-mode)

In this mode, the `docker-compose.yml` file will only include container definitions for PostgreSQL and Redis. The containers listed below will run with their default ports exposed. Use `docker ps` to check.

| Container Name | Purpose                              | Port |
| -------------- | ------------------------------------ | ---- |
| `db`           | Runs Postgres (primary Database)     | 5432 |
| `redis`        | Runs Redis (Cache and Celery Broker) | 6379 |

### Full Docker dev mode

[Section titled “Full Docker dev mode”](#full-docker-dev-mode)

In this mode, the `docker-compose.yml` file will also include containers for Django, node, and Celery.

Depending on your project settings, there are several containers that might be running. These are outlined in the table below:

| Container Name | Purpose                                  | Included                                                                |
| -------------- | ---------------------------------------- | ----------------------------------------------------------------------- |
| `db`           | Runs Postgres (primary Database)         | Always                                                                  |
| `redis`        | Runs Redis (Cache and Celery Broker)     | Always                                                                  |
| `web`          | Runs Django                              | Always                                                                  |
| `vite`         | Runs Vite (for CSS/JavaScript assets)    | If [building with Vite](/front-end/vite)                                |
| `webpack`      | Runs Webpack (for CSS/JavaScript assets) | If [building with Webpack](/front-end/webpack)                          |
| `celery`       | Runs Celery (for background tasks)       | If [Celery is enabled](/celery)                                         |
| `frontend`     | Runs the React Front End                 | If [the standalone front end is enabled](/experimental/react-front-end) |

Like above, the DB containers will expose their default ports.

You can inspect the `Dockerfile`s being used in `docker-compose.yml`. Python containers use the `Dockerfile.dev` file.

### Settings

[Section titled “Settings”](#settings)

The docker environment sets environment variables using the included `.env` file.

The `.env` file is automatically ignored by git, so you can put any additional secrets there. It generally should not be checked into source control. You can instead add variables to `.env.example` to show what should be included.

## Working with full docker mode

[Section titled “Working with full docker mode”](#working-with-full-docker-mode)

The following instructions are specific to “full” docker mode, where Docker is also running your application.

### Python environments

[Section titled “Python environments”](#python-environments)

The Python environment is run in the containers, which means you do not need to have your own local environment if you are always using Docker for development. Python requirements are automatically installed when the container builds.

However, keep in mind that if you go this route, you will need to run all commands inside the containers as per the instructions below.

### Running once-off management commands

[Section titled “Running once-off management commands”](#running-once-off-management-commands)

Running commands on the server can be done using `docker compose`, by following the pattern used in the `Makefile`.

For example, to bootstrap Stripe subscriptions, run:

```bash
docker compose exec web python manage.py bootstrap_subscriptions
```

Or to promote a user to superuser, run:

```bash
docker compose exec web python manage.py promote_user_to_superuser me@example.com
```

You can also use the `make manage` command, passing in `ARGS` like so:

```bash
make manage ARGS='promote_user_to_superuser me@example.com'
```

You can add any commonly used commands you want to `custom.mk` for convenience.

### Updating Python packages

[Section titled “Updating Python packages”](#updating-python-packages)

If you add or modify anything in your `requirements.in` (and `requirements.txt`) files, you will have to rebuild your containers.

The easiest way to add new packages is to add them to `requirements.in` and then run:

```bash
make requirements
```

Which will rebuild your `requirements.txt` file, rebuild your Docker containers, and then restart your app with the latest dependencies.

### Debugging

[Section titled “Debugging”](#debugging)

You can use debug tools like `pdb` or `ipdb` by enabling service ports.

This can be done by running your web container with the following:

```bash
docker compose run --service-ports web
```

If you want to set up debugging with PyCharm, it’s recommended to follow [this guide on the topic](https://testdriven.io/blog/django-debugging-pycharm/).

## Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

### ”No such file or directory” errors

[Section titled “”No such file or directory” errors”](#no-such-file-or-directory-errors)

Some environments---especially on Windows---can have trouble finding the files on your local machine. This will often show up as an error like this when starting your app:

```plaintext
python: can't open file '/code/manage.py': [Errno 2] No such file or directory
```

These issues are usually related to your *disk setup*. For example, mounting your code on a remote filesystem or external drive to your machine. To fix, try running the code on the same drive where Docker Desktop is installed, or on your machine’s default “C:” drive.

You can also get around this issue by running your application natively, instead of with Docker.

## Other Resources

[Section titled “Other Resources”](#other-resources)

* [Dockerizing Django with Postgres, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/) provides an overview of the setup, and has additional information about using Docker in production
* [Environment variables in Compose](https://docs.docker.com/compose/environment-variables/) is a good resource on the different ways to work with environment variables in Docker

# Feature Flags

> Implement feature flags with Django Waffle to control feature rollouts, A/B testing, and user-specific or team-based feature access.

[Waffle](https://waffle.readthedocs.io/en/stable/) is the top library for managing feature flags in Django. Pegasus includes configuration for using Waffle with or without teams.

If you are using [Teams](/teams) then the Waffle flags can be turned on based on the user or the team. If you are not using Teams then flags only apply to users.

## Usage

[Section titled “Usage”](#usage)

Waffle can be used to turn on and off features. For example:

```python
import waffle


def my_view(request):
    if waffle.flag_is_active(request, 'flag_name'):
        """Behavior if flag is active."""
    else:
        """Behavior if flag is inactive."""
```

The flags themselves are managed via the Django Admin site where each flag can be activated for specific users or teams, or based on certain conditions such as *superuser* status. Flags can also be managed via the command line.

For full details on configuring flags see the [Flag Attributes](https://waffle.readthedocs.io/en/stable/types/flag.html#flag-attributes) of the Waffle docs.

Flags may be used in views, templates, JavaScript and more. For full details see the [Waffle docs](https://waffle.readthedocs.io/en/stable/usage/index.html)

## Usage with *Teams*

[Section titled “Usage with Teams”](#usage-with-teams)

If you are using [Teams](/teams), Pegasus ships with a [custom flag model](https://waffle.readthedocs.io/en/stable/types/flag.html#custom-flag-models) which allows you to activate flags on a per-team basis in addition to the other default options.

## Example usage

[Section titled “Example usage”](#example-usage)

To see flags in actions look at the “Flags” example in the Pegasus Example Gallery.

The flag in the example is configured in [test mode](https://waffle.readthedocs.io/en/stable/testing/user.html) which allows us to activate the flag with a URL parameter.

# Forms

> Render Django forms with CSS framework integration, dynamic Alpine.js functionality, and custom template tags for better UX.

Pegasus ships with some extensions to Django forms to integrate with different CSS frameworks and add some extensions.

## The `form_tags` module

[Section titled “The form\_tags module”](#the-form_tags-module)

You can use default Django form rendering for forms, but if you want all the built-in style support, you should instead use the utilities in the `form_tags` module.

To use it, first include `form_tags` in any Django template file:

```jinja
{% load form_tags %}
```

Then, you can render a form using the `render_form_fields` template tag. Here is a basic example:

```jinja
<form method="post">
  {% csrf_token %}
  {{ form.non_field_errors }}
  {% render_form_fields form %}
  <div class="mt-2">
    <button class="pg-button-primary" type="submit">{% translate "Submit Form" %}</button>
  </div>
</form>
```

You can also render individual fields using `render_field`:

```jinja
<form method="POST" action="{% url 'account_change_password' %}" class="password_change">
  {% csrf_token %}
  {{ form.non_field_errors }}
  {% render_field form.username %}
  {% render_field form.password %}
  <div class="mt-2">
    <input class="pg-button-primary" type="submit" value="{% translate 'Login' %}">
  </div>
</form>
```

## Dynamic forms with Alpine.js

[Section titled “Dynamic forms with Alpine.js”](#dynamic-forms-with-alpinejs)

*Added in version 2023.6*

The form rendering helpers also support adding attributes, which can be useful to add Alpine.js to make a form more dynamic.

For example, you can bind a form value to an alpine model by passing it in `attrs` like this:

```python
class ExampleFormAlpine(forms.Form):
    YES_NO_OTHER = (
        ("yes", gettext("Yes")),
        ("no", gettext("No")),
        ("other", gettext("Other")),
    )
    like_django = forms.ChoiceField(
        label=gettext("Do you like Django?"),
        choices=YES_NO_OTHER,
        widget=forms.Select(attrs={"x-model": "likeDjango"}),  # this line will bind the value to an alpine model
    )
```

Then in the HTML template you have to add an alpine model to the form:

```jinja
<form method="post" x-data="{ likeDjango: '{{ form.like_django.data|default:"yes" }}', styleValue: '{{ form.styled_options.data|default:"regular" }}' }">
  <!--  other fields here  -->
  {% render_field form.like_django %} <!--  this will bind to `likeDjango` above  -->
```

The `render_field` tags support two special syntaxes to make using alpine easier:

1. Any attribute starting with `x` will be automatically converted to `x-`.
2. Double underscores (`__`) will be replaced with colons (`:`).

The following example alpine form and template (which also ship with Pegasus, available at <http://localhost:8000/pegasus/forms/alpine/>) demonstrate this usage, including hiding/showing a field based on the value of another field, rendering field values in labels, and changing the style of a field based on its value.

Django form class:

```python
class ExampleFormAlpine(forms.Form):
    YES_NO_OTHER = (
        ("yes", gettext("Yes")),
        ("no", gettext("No")),
        ("other", gettext("Other")),
    )
    STYLES = (
        ("regular", gettext("Normal")),
        ("success", gettext("Success")),
        ("danger", gettext("Danger")),
    )
    like_django = forms.ChoiceField(
        label=gettext("Do you like Django?"),
        help_text=gettext("Try choosing 'other' to see unhiding a form field based on a value."),
        choices=YES_NO_OTHER,
        widget=forms.Select(attrs={"x-model": "likeDjango"}),
    )
    like_django_other = forms.CharField(label=gettext("Please specify more details about your answer."))
    styled_options = forms.ChoiceField(
        label=gettext("Styled Options"),
        help_text=gettext("Try picking an option to see how you can style a component based on its value."),
        choices=STYLES,
        widget=forms.Select(attrs={"x-model": "styleValue"}),
    )
```

Django template:

```jinja
<form method="post" x-data="{ likeDjango: '{{ form.like_django.data|default:"yes" }}', styleValue: '{{ form.styled_options.data|default:"regular" }}' }">
  {% csrf_token %}
  {% render_field form.like_django %}
  {% render_field form.like_django_other xshow="likeDjango === 'other'" xcloak='True' %}
  {% render_field form.styled_options xbind__class="'pg-bg-' + styleValue" %}
  <p class="mt-4">You can also use alpine to display selected values.
    <em>
      Like Django: <strong x-text="likeDjango"></strong>,
      Style: <strong x-text="styleValue"></strong>
    </em>
  </p>
  <input type="submit" value="Save Data" class="pg-button-secondary mt-2">
</form>
```

# GitHub Integration

> Integrate projects with GitHub using OAuth or personal access tokens for automated updates, pull requests, and version control.

As of February, 2024 you can connect your Pegasus projects directly to GitHub instead of downloading them as a zip file. This makes for a more streamlined workflow---especially when changing or upgrading your project.

## Watch the video

[Section titled “Watch the video”](#watch-the-video)

The following video shows how to create and update a project using the Github integration.

## Connecting your account

[Section titled “Connecting your account”](#connecting-your-account)

There are two ways to connect your Github account. The Oauth-based “Connect Github” option is easier and more reliable, while personal access token option allows you to control exactly what repositories Pegasus can access.

### Using “Connect Github” (Oauth)

[Section titled “Using “Connect Github” (Oauth)”](#using-connect-github-oauth)

The easiest way to connect your account is by using the “Connect Github” button on the project download page. You will be prompted to accept permissions, and your account will be connected in a few seconds.

Note: While you will be prompted to grant access to “all private repository data,” Pegasus does not view or modify data in any repositories unless you connect them.

### Using Personal Access Tokens

[Section titled “Using Personal Access Tokens”](#using-personal-access-tokens)

If you prefer not to grant Pegasus access to your entire Github account, you can use [Personal Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) to limit the scope of what Pegasus has access to.

#### With Classic Tokens

[Section titled “With Classic Tokens”](#with-classic-tokens)

To use Pegasus with a classic token, visit the [Personal access tokens](https://github.com/settings/tokens) page on Github, then select “Generate new token (classic)” from the dropdown, or [visit this page](https://github.com/settings/tokens/new).

Choose a note and expiration date for your token and grant the following scopes:

* user:email (Access user email addresses (read-only))
* repo (Full control of private repositories)
* workflow (Update GitHub Action workflows)

Then click “Generate token”. You will be taken to a page where your token is displayed. Copy this value and paste it into the “personal access token” field from your project download page on Pegasus. Note that you won’t be able to view the token again!

#### With Fine-Grained Access Tokens

[Section titled “With Fine-Grained Access Tokens”](#with-fine-grained-access-tokens)

If you want the most control over your permissions, you should use a fine-grained access token, which allow you to control access to specific repositories.

Note that if you use fine-grained tokens **you must create the repository for your project before creating the token**. Pegasus cannot create the project for you with these tokens.

After creating the repository, [create a new fine-grained-token from this page](https://github.com/settings/personal-access-tokens/new). Set a token name and expiration date, and then use “Only select repositories” to choose the repositories you want to grant access to (the one you just created).

Under “Permissions” —> “Account Permissions” you must grant *read* access to:

* Email addresses

Then under “Permissions” —> “Repository Permissions” you must grant **read and write** access to:

* Contents
* Pull Requests
* Workflows

Then click “Generate token”. You will be taken to a page where your token is displayed. Copy this value and paste it into the “personal access token” field from your project download page on Pegasus. Note that you won’t be able to view the token again!

## Connecting an existing project to Github

[Section titled “Connecting an existing project to Github”](#connecting-an-existing-project-to-github)

Projects that were created before February 2024, or that didn’t use the Github integration can still be connected to Github via a one-time process. After completing this, you will be able to upgrade and change your Pegasus project using automatic pull requests.

First, you’ll have to connect your Github account using one of the methods described above.

Next, you will need to find the commit id of the last Pegasus update you have made. If you have never updated your codebase, this will be the first commit in the repository, which you can find by running `git log --reverse`.

If you have updated your codebase using one of the other methods below, this will be the last commit on the `pegasus` branch of your repository, which you can find by running `git checkout pegasus` followed by `git log`.

Once you have the commit id ready, add your existing Github repository to your Pegasus project from the downloads page. After completing this step you will be prompted with a page that looks like this:

![Set Commit](/_astro/set-commit.Bh21vQoQ_mJB17.webp)

Enter the commit ID there, and you should now be able to update your project with pull requests.

## Working with repositories owned by an organization

[Section titled “Working with repositories owned by an organization”](#working-with-repositories-owned-by-an-organization)

Github organizations do not allow API-based repository access by default, so to connect a repository owned by an organization you will also have to grant programmatic access.

Github provides detailed guidance on how to do this. For “Connect Github,” follow the [oauth instructions](https://docs.github.com/en/organizations/managing-oauth-access-to-your-organizations-data), and for personal access tokens, follow the [personal access token instructions](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/setting-a-personal-access-token-policy-for-your-organization).

## Pushing Pegasus code to a subdirectory in your repository

[Section titled “Pushing Pegasus code to a subdirectory in your repository”](#pushing-pegasus-code-to-a-subdirectory-in-your-repository)

By default, your entire git repository is dedicated to Pegasus, with all of Pegasus’s files included at the root of the repository. Some projects---especially those with a separate front end---may want to instead include Pegasus code in a subdirectory of the repository (e.g. “backend”), so that other projects (e.g. “frontend”) can be included in the same repository.

It is possible to configure your Github integration this way. To do so, when adding the repository, click “Show Advanced Options,” then specify the subdirectory you want to use for your Pegasus code in the “Subdirectory” field.

If you would like to update an existing project to use a subdirectory, you’ll have unlink and re-add your repository, then [reconnect it](#connecting-an-existing-project-to-github).

## Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

**I keep getting “Error pushing to GitHub. Please check your token scopes.” when pushing my project.**

While Pegasus does its best to catch errors that come from Github and show them to you, sometimes it will return this generic error.

One common reason a valid token is unable to push code is related to email privacy settings. Specifically the “Blocking command line pushes that expose your personal email address” setting---which currently must be *disabled* in order to use the Github integration.

To check and disable this setting:

1. Go to your [Github email settings](https://github.com/settings/emails)
2. Scroll down to where it says “Keep my email addresses private”.
3. If that option is checked, ensure that the “Block command line pushes that expose my email” option below it is *not* checked.
4. If that option is *not* checked, then it is a different problem. You are welcome to reach out directly for support

# Using Github Actions

> Automate Django testing and front-end builds with GitHub Actions CI/CD workflows for continuous integration.

[GitHub Actions](https://github.com/features/actions) allows you to automate your software workflows. Pegasus apps optionally ship with Github actions support for a few things to build off.

If you’ve built with Github actions support, they should successfully run the first time you push your code to Github.

Actions are configured in the `.github` directory in your project. The following actions ship with Pegasus:

## Running Django Tests

[Section titled “Running Django Tests”](#running-django-tests)

The Django tests are configured in `.github/tests.yml`.

By default, it will:

* Run on every push to the `main` branch and every pull request.
* Run on Python version 3.12 (other Python versions can be added by modifying the `python-version` list)
* Use the latest version of Postgres
* Run `./manage.py test`

All of these can be changed by modifying the relevant sections of the `.github/tests.yml` file.

## Building the Front End

[Section titled “Building the Front End”](#building-the-front-end)

The front end build is configured in `.github/build_frontend.yml`.

By default, it will:

* Run on every push to the `main` branch and every pull request.
* Run on Node version 22 (other Node versions can be added by modifying the `node-version` list).
* Run `npm run build`, ensuring your front end builds properly.
* Run `npm run type-check`, ensuring all type checks pass.

Any compilation errors in your JavaScript should show up as build failures.

# Internationalization

> Add multi-language support and timezone handling to Django applications with translation files, locale management, and user preferences.

Pegasus supports internationalization via built-in support for timezones and language translations. To enable timezone and multi-language support, you must select the “use internationalization” option in your project settings.

## Translation Demo

[Section titled “Translation Demo”](#translation-demo)

This two-minute demo highlights how translations work in Pegasus apps.

## Localization

[Section titled “Localization”](#localization)

Pegasus ships with full support for localizing user-facing text.

Currently, not all the user-facing text is properly tagged for localization but this will be incrementally addressed in future releases.

For full documentation on localization see the [Django docs](https://docs.djangoproject.com/en/stable/topics/i18n/).

## Big picture

[Section titled “Big picture”](#big-picture)

Big picture there are two steps to translation:

1. **Define the text you want to translate (in Python, HTML, or JavaScript)**. This step happens in your project’s code.
2. **Add a translation for that text to other languages**. This step happens in your project’s translation files, which can be found in the `locale/<lang_code>/LC_MESSAGES/` folders (there will be one for each language).

## Managing enabled languages

[Section titled “Managing enabled languages”](#managing-enabled-languages)

There are two steps to updating the list of languages that will be available on your site. The first step is to define it in `settings.LANGUAGES`. Out of the box this will be English and French:

```python
from django.utils.translation import gettext_lazy


LANGUAGES = [
    ('en', gettext_lazy('English')),
    ('fr', gettext_lazy('French')),
    # add other languages here
]
```

The second step is to create the translations folder for the language. This can be done by running:

```bash
python ./manage.py makemessages -l [new lang code] --ignore node_modules --ignore venv
```

Or in Docker:

```bash
docker compose exec web python manage.py makemessages -l [new lang code] --ignore node_modules --ignore venv
```

## Marking text in your app for translation

[Section titled “Marking text in your app for translation”](#marking-text-in-your-app-for-translation)

All text you want to be translatable must be tagged in your application. This can be done as follows:

**In Python:**

```python
from django.utils.translation import gettext


def my_view(request):
    output = gettext("Welcome to my site.")
    return HttpResponse(output)
```

See the [Django docs](https://docs.djangoproject.com/en/stable/topics/i18n/translation/#internationalization-in-python-code) for more.

**In Django templates:**

```jinja
{% load i18n %}
<title>{% translate "This is the title." %}</title>
```

See the [Django docs](https://docs.djangoproject.com/en/stable/topics/i18n/translation/#internationalization-in-template-code) for more.

**In JavaScript:**

```javascript
document.write(gettext('this is to be translated'));
```

See the [Django docs](https://docs.djangoproject.com/en/stable/topics/i18n/translation/#internationalization-in-javascript-code) for more.

**In Wagtail:**

See the [Wagtail docs](/wagtail/#internationalization).

## Creating / updating translation files

[Section titled “Creating / updating translation files”](#creating--updating-translation-files)

After you’ve marked text for translation, you’ll need to update your language files. This can be done by running:

```bash
python ./manage.py makemessages --all --ignore node_modules --ignore venv
python ./manage.py makemessages -d djangojs --all --ignore node_modules --ignore venv
```

Or in Docker:

```bash
make translations
```

Note: if you get any errors you may need to [install gettext](https://stackoverflow.com/q/35101850/8207).

## Adding actual translations for other languages

[Section titled “Adding actual translations for other languages”](#adding-actual-translations-for-other-languages)

To add a translation for another language you need to edit that languages messages (.po) file.

For example, to edit a French translation, you would update `locale/fr/LC_MESSAGES/django.po`. Then search for the text you want to translate, and add the French translation:

```plaintext
msgid "My Team"
msgstr "Mon Équipe"
```

The above lines will replace “My Team” with “Mon Équipe” whenever the French language is configured.

After editing any message (.po) file, you will have to compile the messages for the updates to show up in your app. This can be done by:

```bash
python ./manage.py compilemessages
```

Or in Docker:

```bash
make translations
```

## Technical notes

[Section titled “Technical notes”](#technical-notes)

Pegasus is configured to use cookies to track the current locale. This allows localization to work for both authenticated and unauthenticated users.

More information on this approach is available the Django docs: [How Django discovers language preference](https://docs.djangoproject.com/en/stable/topics/i18n/translation/#how-django-discovers-language-preference)

## Timezones

[Section titled “Timezones”](#timezones)

Pegasus includes support for user’s setting their own time zones via their profile (version 2023.7 and later). When a user sets a timezone, it will be automatically activated by the `UserTimezoneMiddleware` so that by default all dates and times will appear in their local time.

For more information on working with timezones in Django, see [Django’s timezone documentation](https://docs.djangoproject.com/en/stable/topics/i18n/timezones/).

# Project/Page Metadata and SEO

> Configure SEO metadata, page titles, social sharing tags, and XML sitemaps for better search engine optimization and discoverability.

Pegasus comes with some built in tools and best-practices for setting page-level metadata (e.g. title, image URL, etc.).

## The `PROJECT_METADATA` setting

[Section titled “The PROJECT\_METADATA setting”](#the-project_metadata-setting)

Your Pegasus project will ship with a `settings.py` variable called `PROJECT_METADATA` with the following values:

```python
PROJECT_METADATA = {
    'NAME': '<your app name>',
    'URL': '<your app domain>',
    'DESCRIPTION': '<your app description>',
    'IMAGE': 'https://upload.wikimedia.org/wikipedia/commons/2/20/PEO-pegasus_black.svg',
    'KEYWORDS': 'SaaS, django',
    'CONTACT_EMAIL': '<your email>',
}
```

This information will be available in every view under the variable name `project_meta`. Out of the box, the values are used in a number of places, though can be overridden/modified at the view level.

## Page Titles

[Section titled “Page Titles”](#page-titles)

The default title for your pages will be your project name and description from `PROJECT_METADATA`.

If you want to add a custom page title, you can pass a `page_title` context variable to the template.

For example:

```python
def my_new_view(request):
    return render('a/template.html', {'page_title': 'My New Page'})
```

Pegasus will then set your title to be `My New Page | <project name>`.

If you’d like to change the way the title is formatted (e.g. remove the project name), you can change that behavior in `web.templatetags.meta_tags.get_title`.

In Pegasus versions after 2022.4 you can also override the title directly in a template by overriding the `page_title` block.

For example:

```jinja
{% block page_title %}This title will be used instead of the Pegasus versions{% endblock %}
```

## Sitemaps

[Section titled “Sitemaps”](#sitemaps)

As of version 2022.6, Pegasus will automatically generate a basic [sitemap](https://developers.google.com/search/docs/advanced/sitemaps/overview) for your site at `sitemap.xml`. Out of the box, the sitemap will only contain your application’s homepage, but can be readily extended by adding URLs in `apps/web/sitemaps.py`.

If you have [enabled Wagtail](/wagtail), your sitemap will also include any content managed by Wagtail. Make sure you [properly set the hostname in your Wagtail site](https://docs.wagtail.org/en/stable/reference/contrib/sitemaps.html#setting-the-hostname).

# E-Commerce / Payments

> Build digital storefronts with Stripe integration for one-time and recurring payments, product management, and purchase tracking.

Pegasus (version 2023.9.1 and up) includes an out-of-the-box E-Commerce/Payments demo. In a few clicks you can have a fully functional digital storefront in your application, allowing you to collect and track one-time or recurring payments with Stripe.

## Watch a video

[Section titled “Watch a video”](#watch-a-video)

To see how this feature works, you can watch the following video:

## Getting Started

[Section titled “Getting Started”](#getting-started)

### Set up Stripe Products

[Section titled “Set up Stripe Products”](#set-up-stripe-products)

First add your products in the Stripe dashboard. Be sure to add readable product names, descriptions, and images, as these will be used for the in-app store. Additionally, make sure each product includes at least one Price.

### Set up your development environment

[Section titled “Set up your development environment”](#set-up-your-development-environment)

Setting up your development is similar to the [process for subscriptions](/subscriptions), but has fewer steps.

1. If you haven’t already, update the `STRIPE_*` variables in `settings.py` or in your os environment variables to match the keys from Stripe. See [this page](https://stripe.com/docs/keys) to find your API keys.
2. Run `python manage.py bootstrap_ecommerce` to sync your Stripe products and prices to your local database.

Once you’ve done this, login and click on the e-commerce tab in the navigation, and you should see your store.

## Data models

[Section titled “Data models”](#data-models)

### `ProductConfiguration`

[Section titled “ProductConfiguration”](#productconfiguration)

What shows up in your store is controlled by the `ProductConfiguration` data model. You can manage these objects from the Django admin (available at <http://localhost:8000/admin/ecommerce/productconfiguration/> locally). For example, to remove a product from the store you can uncheck “is active”.

The `ProductConfiguration` model is also a good place to add additional information to your products. For example, you can add additional display data there, or add a `FileField` if you want purchases to grant access to a digital download.

### `Purchase`

[Section titled “Purchase”](#purchase)

The `Purchase` model is used to record user purchases. A `Purchase` is associated with a `User` and a `ProductConfiguration` and also has details of the Stripe checkout session, date of purchase, and product/price used at the time of purchase.

## Feature gating

[Section titled “Feature gating”](#feature-gating)

The `@product_required` decorator can be used to restrict access to a view based on whether or not the logged-in user has purchased a particular product. This decorator expects a `product_slug` field in the URL / view with the slug of the `ProductConfiguration` object to be checked. If the user owns the product, they will be granted access to the view.

Additionally, if the user gets access, two additional field will be populated on the `request` object:

* `request.product_config` will have the `ProductConfiguration` object.
* `request.product_purchase` will have the `Purchase` object.

If the user does *not* have access to the product, the decorator will redirect them back to the store homepage.

## Webhooks

[Section titled “Webhooks”](#webhooks)

Like subscriptions, it’s recommended to use webhooks to ensure you receive all updates from Stripe. For the e-commerce store, the only required webhook is `checkout.session.completed`.

Follow [the subscriptions documentation](/subscriptions/#webhooks) to set up webhooks in development and production.

# Version History and Release Notes

> Complete changelog and version history for SaaS Pegasus Django boilerplate with detailed feature updates and migration guides.

Releases of [SaaS Pegasus: The Django SaaS Boilerplate](https://www.saaspegasus.com/) are documented here.

## Version 2025.11.1

[Section titled “Version 2025.11.1”](#version-2025111)

This is a minor hotfix release fixing two issues:

* Fixed a crash in the teams example app, due to an incorrect reference to `model.for_team()` (instead of the correct `model.for_team`). Thanks Eugen for reporting!
* Fixed an issue where Heroku Redis URLs accidentally removed `?ssl_cert_reqs=none` if you used the Docker-based build. Thanks Steven for reporting!

*November 17, 2025*

## Version 2025.11

[Section titled “Version 2025.11”](#version-202511)

Here’s what’s in the November release.

### New Team scoping features

[Section titled “New Team scoping features”](#new-team-scoping-features)

These updates provide more consistent ways to filter your models based on the current team and help avoid writing bugs related to forgetting to apply a team filter to your DB queries.

If you’re happy with the current teams setup you can largely ignore these changes—they mainly add new, optional functionality on top of the existing system.

If you would like to introduce more strict Team filtering and checking in your app, review the changes below and updated sections of the documentation.

Details:

* Added a new [context variable](/teams/#team-context-variable) to keep track of the current team.
* Updated the `TeamsMiddleware` to automatically set/unset the variable for the user’s current team.
* Added a new `TeamScopedManager` class to automatically filter a queryset based on the current team (from the context variable).
* Updated `BaseTeamModel` to add `for_team = TeamScopedManager()`, which can be used to automatically filter a team moodel based on the current team.
* `TeamsMiddleware` will no longer set `request.team` to the user’s default team if it is not in the URL. Previously it would return the most recently visited team or the first team that the user is a member of. If you need that behavior, you can now use `request.default_team`.
* Added several tests for the above functionality.

See [the updated teams documentation](/teams) for more information about working with these tools, including how to use them to [always enforce that a team is set](/teams/#strict-team-access).

### Other changes

[Section titled “Other changes”](#other-changes)

**Added**

* **Added [AGENTS.md](https://agents.md/) as an additional output format for AI rules files.**
* **You can now clone/copy projects in SaaS Pegasus**—starting a new project with an existing project’s configuration instead of the defaults each time. (Thanks Patrick for the suggestion!)

**Changed**

* **Upgraded all Python packages.**

* **Upgraded all JavaScript packages.**

* Updated `.vite` declaration in the `.gitignore` to make it more obvious how to check in vite’s built static files if you want to do that. Thanks Lile for suggesting!

* Updated AI API key environment variables to be the defaults used by Pydantic AI so they can be set in a single place. You should now set `OPENAI_API_KEY` instead of `AI_CHAT_OPENAI_API_KEY` and `ANTHROPIC_API_KEY` instead of `AI_CHAT_ANTHROPIC_API_KEY`.

* Updated links to the Django docs to always point to the latest stable release.

* Updated Kit (formerly ConvertKit) mailing list integration to V4 of the API. Thanks Ben H for suggesting!

  * Changed `CONVERTKIT_API_KEY` setting / environment variable name to `KIT_API_KEY`.
  * Also updated [the docs](/configuration/#kit-formerly-convertkit).

* Updated `django_browser_reload` to only setup the app/middleware if `DEBUG=True`. This removes a warning in production. (Thanks Zac for the suggestion!)

* Made minor updates to AI rules files.

**Fixed**

* The employee agent demo now uses a proper `Enum` for departments, preventing invalid options from being used.
* Fixed an issue with using `TransactionTestCase` in certain build configurations due to an issue with `django-waffle`. This was done by updating a migration to remove the unexpected tables, as outlined in [this comment](https://github.com/django-waffle/django-waffle/issues/317#issuecomment-488398832). Thanks Ben N for reporting!
  * The migration was also renamed - see upgrade section for details.
* Fixed some places where types were set incorrectly or didn’t pass type-checking.
* Fixed a bug where `django_browser_reload` was always enabled, even if you had turned it off.

### Upgrading

[Section titled “Upgrading”](#upgrading)

* If you had any code dependent on `request.team` being set even if there was no team in the URL, you should update that code to use `request.default_team`.
* If you were using the (Convert)Kit integration, you should update based on the [latest documentation](/configuration/#kit-formerly-convertkit).
* The migration `/apps/web/migrations/0002_patch_djstripe_column.py` was renamed to `/apps/web/migrations/0002_patch_third_party_tables.py`.
  * In most cases, this should apply correctly, but if you have any issues with it, you can re-create the migration by running `./manage.py makemigrations web --empty` and then copying the contents of the file across (except for the generated `("web", "000x_xxxx"),` dependency line). Alternatively, if you don’t use `TransactionTestCase`, you can just reject the migration file changes.

*Nov 10, 2025*

## Version 2025.10

[Section titled “Version 2025.10”](#version-202510)

This release improves the developer experience of working with Pegasus. It has a number of changes that make things simpler, smoother, and more consistent. These changes also make it easier for AI agents to work in Pegasus codebases.

Key changes:

* All projects will default to Postgres, Vite, and Tailwind moving forwards. Other options will be slowly phased out.
* All projects will ship with Docker containers for Postgres and Redis (you can ignore these if you want to run them separately)
* The `Makefile` now ships with every project and includes commands for running everything you need in development. These commands are also available in AI rules files for AI agents.
* `make init` will work on all projects, and is all you need to get running (after installing prerequisites)
* Added some dev quality-of-life tools.

Details below.

### Services-only Docker setup

[Section titled “Services-only Docker setup”](#services-only-docker-setup)

This release adds default “services-only” Docker setup for projects that weren’t using Docker already. In this mode, Postgres and Redis run via Docker, but Python and Node/npm run natively. *This is now the recommended way to develop Pegasus applications.* You can read more in the updated [Docker docs](/docker).

### Expanded `make` support

[Section titled “Expanded make support”](#expanded-make-support)

The `Makefile` will now be included on all Pegasus builds. This can be used to run the app, tests, migrations, front end, and more without having to remember the exact commands, and can be easily customized.

You can run `make` without any arguments to see the available options.

### Added a `dev.sh` script to run Django and Vite/Webpack in a single command

[Section titled “Added a dev.sh script to run Django and Vite/Webpack in a single command”](#added-a-devsh-script-to-run-django-and-vitewebpack-in-a-single-command)

For projects not already using Docker, a `dev.sh` script was added that runs both Django and Webpack/Vite in a single command, handling process management for you. Running `make dev` will use script, though you can also run it manually via `./scripts/dev.sh`.

This allows you to easily stop and start these two coupled processes together without having to fiddle with multiple terminals or tools like `tmux`.

### Expanded README and Agents files

[Section titled “Expanded README and Agents files”](#expanded-readme-and-agents-files)

The project’s README and the various Agent files (cursor rules, CLAUDE.md, etc.) have been overhauled and expanded to use the `make` commands. This provides a simpler on-ramp both for developers and agents to run the app and the various supporting commands.

### Streamlined development tooling

[Section titled “Streamlined development tooling”](#streamlined-development-tooling)

Two new packages were added to improve the developer experience:

* [django-watchfiles](https://github.com/adamchainz/django-watchfiles) improves the Django dev server’s autoreloading behavior in several ways, making it both faster and use less system resources. [Learn more here](https://adamj.eu/tech/2025/09/22/introducing-django-watchfiles/).
* [django-browser-reload](https://github.com/adamchainz/django-browser-reload) adds automatic page reloading to your browser whenever code changes.

Both of these options are development features, and should have no impact on applications in production. Browser reload is enabled on all projects by default, while watchfiles is off by defualt because of [this “file watch limit reached” issue on some filesystems](https://github.com/adamchainz/django-watchfiles/issues/135). Both options can be enabled/disabled under advanced development settings.

Thanks to [Adam Johnson](https://adamj.eu/) for the great tools!

### Deprecating configuration options

[Section titled “Deprecating configuration options”](#deprecating-configuration-options)

The following options have been deprecated and will be dropped in a future release.

* **Bulma and Bootstrap CSS Frameworks have been deprecated.** Tailwind will be the primary CSS framework moving forwards.
* **Webpack has been deprecated.** Existing projects should [migrate to Vite](https://docs.saaspegasus.com/front-end/migrating/).
* **SQLite has been deprecated.** While it will likely still work, it will no longer be QA’d, and various pieces of infrastructure and documentation will assume development is done on Postgres. Postgres can be easily run locally using the Docker services option referenced above.

Removing these options will provide a more consistent set of best-practices, that work well for nearly every project and will improve the stability and velocity of Pegasus updates.

If you have any questions or concerns about migrating, don’t hesitate to get in touch.

### Other changes

[Section titled “Other changes”](#other-changes-1)

* Overhauled the “[Gettting started](/getting-started/)” and “[Docker](/docker/)” sections of the docs to reflect the latest changes.
* In addition to the major changes mentioned above, made some minor changes and corrections to the README and AI Rules files.
* Postgres and Redis docker containers now expose their service ports on the host container.
* The development Postgres Docker container is now pinned to version 17.
* Added a url route to test the `429` (too many requests) error page. Thanks Brennon for suggesting!
* Updated the default Anthropic LLM model to the newly-released Claude Sonnet 4.5.

*Oct 10, 2025*

## Version 2025.9.2

[Section titled “Version 2025.9.2”](#version-202592)

This release fixes some small bugs when deploying `uv` projects to Heroku with the Python buildpack:

* Don’t include `runtime.txt` for Heroku deployments that use uv
* Include production dependencies in main `dependencies` section of `pyproject.toml` for Heroku Python builds.

Thanks Norman for reporting these!

*Sep 25, 2025*

## Version 2025.9.1

[Section titled “Version 2025.9.1”](#version-202591)

This is a minor maintenance/bugfix release that upgrades packages, improves the employee agent demo, and addresses some minor bugfixes.

Details:

* **Upgraded nearly every Python package to the latest version, except a few that had compatibility issues.**

  * Pinned dj-stripe to < 2.10, which is not yet supported.
  * Pinned litellm to < 1.77.2 to prevent [this installation issue](https://github.com/BerriAI/litellm/issues/14762)

* **Add better UI status indicator if chat websocket connection fails or is interrupted.**

* Add `created_at` / `updated_at` fields to the Employee agent tools.

* The `delete_employee` agent tool now takes an ID instead of an `EmployeeData`.

* Fixed issues in the agent tools that delete and update employees to better handle retries and error conditions (for example, when trying to operate on an employee that doesn’t exist).

* Don’t include `websocket_url` templatetag if building without async support.

* Fixed broken documentation links in the app that were using the old docs url formats. (Thanks Sam for reporting!)

* Fixed a bug in `fly.toml` that had extra newlines in the worker and beat commands. (Thanks Sam for reporting!)

* The `fly.toml` file now includes a `vm` section for celerybeat if enabled. (Thanks Sam for reporting!)

* Fixed a bug in `fly.toml` that included a worker process even if celery was disabled.

*Sep 23, 2025*

## Version 2025.9

[Section titled “Version 2025.9”](#version-20259)

### Agents support

[Section titled “Agents support”](#agents-support)

The big update in this release is a set of example workflows you can use as a foundation for building agentic chatbots, built with Pydantic AI. These include:

* Injecting the logged-in user’s information into the chatbot context.
* A tool use example that demonstrates a chatbot accessing live weather information for anywhere in the world.
* An agentic editing example, that allows you to use natural language to create, update, list, and delete data in the employee application.
* An MCP-based agent that allows superusers to ask questions about the applicaton database.

You can learn more about these features and how they work in the following video, as well as the [LLM documentation](/ai/llms/):

### Changes related to agent support

[Section titled “Changes related to agent support”](#changes-related-to-agent-support)

* **Added Pydantic AI agent applications:**

  * Weather and location lookup agent, with tools to do geo-lookups and access current weather information. You can [demo this here](https://www.saaspegasus.com/chat/chat/agent/new/)
  * Chatbot to interact with employee application data models, with tools to work with employee data. This has been added as a new example, if AI chat is enabled. You can [demo this here](https://www.saaspegasus.com/pegasus/employees/objects/agent/)
  * Chatbot to interact with system database, with MCP tool to access postgres data. This has been added to the project dashboard page and is only available for superusers.
  * Tool to send emails.
  * Pydantic AI is now a dependency if you enable AI chat.

* **Added a `chat_type` field to `Chat` models to differentiate between normal and agent chats.**

* **Added an `agent_type` field to `Chat` models to differentiate between different agents.**

* Resuming chats will use the appropriate chat/agent type.

* Refactored how chat sessions are managed to a set of `ChatSession` helper classes that help decouple chat session behavior from the websocket / consumer class.

* Refactored `ChatConsumer` websocket handler to a base class, and extended the base class to support different chat types (normal and agent)
  * Added new consumer classes for various agent types for the built-in examples.

### Other changes

[Section titled “Other changes”](#other-changes-2)

* **Removed the “OpenAI” chat configuration option. All AI chat functionality now uses the `litellm` module, which supports OpenAI, as well as Anthropic, Google, and other models.**
* Changed `AI_CHAT_DEFAULT_LLM_MODEL` environment variable to `DEFAULT_LLM_MODEL`
* Updated the default LLM model to be `gpt-5-nano`.
* Added translations markup to a few places in the chat app.
* Added a default log config for the “pegasus” namespace.
* Updated the ai chat app logger to use “pegasus.ai” namespace.
* Added a `ChatMessageInline` admin class so that chat messages show up in their associated `Chat` admin pages.
* Updated the Postgres MCP server (dev tool) to use [mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy), since the original Postgres MCP server is now deprecated.
* Removed the `UserSignupStatsSerializer` and the unused `UserSignupStatsView` API view.
* Added a `websocket_url` templatetag that can be used in Django templates to reverse websocket URLs similar to how the built-in `{% url %}` tag works.
* Extracted employee table component to a template so it can be used in multiple places.
* Simplified Stripe product serialization when used in subscription metadata.
* Upgraded Django to the latest version (5.2.6).

*September 10, 2025*

## Version 2025.8.1

[Section titled “Version 2025.8.1”](#version-202581)

This release is focused on improving the AI chat experience, with an eye towards laying the groundwork for some future use cases that are in the works. The main new feature related to this work is an integrated AI chat widget that can be easily embedded on any page of your app.

**Screenshots:**

![Chat Widget](/_astro/chat-windows.C3qXCZEi_Z1UcdWK.webp)

Complete details are below.

### Added

[Section titled “Added”](#added)

* **Added a way to add an AI chat to any page in your app.** See [the new documentation for using this feature](/ai/llms/#the-chat-widget) or [try it on saaspegasus.com](https://www.saaspegasus.com/chat/) (requires login). This change also included some refactors and changes that allow re-using parts of the AI code:

  * JavaScript websocket events are now initialized in an external JavaScript file (`assets/javascript/chat/ws_initialize.ts`)
  * Message thread component was moved to a separate template to be re-usable by the main chat page and component.

### Changed

[Section titled “Changed”](#changed)

* **The htmx websocket extension is now installed locally instead of loaded from unpkg.com.**
* The default system prompt is now overridden in AI chats, enabling you to easily change it in a single place.
* Chat names are now set synchronously if the initial message is short.
* Updated websocket URL names from `"ws_openai_..."` to `"ws_ai_..."` since there is no requirement to use OpenAI.
* Improved the default chat UI styles on Tailwind builds to be more comatible with DaisyUI themes.
* Updated the default claude model used to `claude-sonnet-4-20250514`
* Added default `AI_CHAT_ANTHROPIC_API_KEY` to example `.env` files.
* Made minor formatting changes to `user_dashboard.html`.
* The user-facing error message when creating an account with an existing email no longer reveals that the account is already signed up (this improves privacy/security). Thanks Brennon for the contribution!
* Update: Updated `.pre-commit-config.yaml` to run the latest version of `ruff` and explicitly use the `ruff-check` hook.
  * Also pinned `ruff` dependency to the same minimum version.

### Fixed

[Section titled “Fixed”](#fixed)

* Updated the Digital Ocean deployment to use a managed database instead of a development database. Development databases are no longer well-supported in app platform.

  * Also updated the [Digital Ocean deployment docs](/deployment/digital-ocean) to reflect the latest changes.
  * Thanks Jan for the suggestion!

* For the production `REDIS_URL`, only add `ssl_cert_reqs=none` for Heroku builds, and set it to required on Digital Ocean, which has valid certificates. Thanks Jan for the suggestion!

* Fixed an issue with the honeypot field that caused a large horizontal scroll on the signup page on some CSS Frameworks.

  * Also improved spacing on the signup forms.
  * Thanks Finbar for the contribution!

* Use Wagtail’s built-in page titles and meta descriptions is the SEO fields for blog posts, if they have been set. Thanks Richard for the suggestion!

* Moved `@tailwindcss/typography` from `devDependencies` to `dependencies` in `package.json`

### Deprecated

[Section titled “Deprecated”](#deprecated)

* Using `pip-tools` as a package manager is deprecated and new projects will automatically default to using `uv`. Existing projects using `pip-tools` are encouraged to [migrate to `uv`](/cookbooks/#migrating-from-pip-tools-to-uv), and support for `pip-tools` will be dropped in an upcoming release. If this is a problem for you, get in touch!

*Aug 26, 2025*

## Version 2025.8

[Section titled “Version 2025.8”](#version-20258)

This is a maintenance release which improves Docker-based development, upgrades dependencies and addresses a number of minor issues reported by the community.

Thanks to everyone who contributed ideas and code to this release!

### Changed

[Section titled “Changed”](#changed-1)

* **Changed how CSS files are built and imported in vite builds. This fixes the flash of unstyled content when running Vite in development.**

  * Removed the redundant `site-<framework>.js` files and instead added the imported CSS files directly as entry points to `vite.config.ts`.
  * Updated `base.html` to use `vite_asset_url` instead of `vite_asset` for CSS files.

* **Updated development Docker setup to always use a separate container for Node / NPM.** This removes all node/npm logic from `Dockerfile.dev` and uses either `Dockerfile.vite` or `Dockerfile.webpack` for the front end.
  * Also updated the `Makefile` to reference this new container where necessary.

* **Upgraded all Python packages to their latest versions.**

* **Upgraded all JavaScript packages to their latest versions.**

* Changed `sentry-sdk` to `sentry-sdk[django]` and pinned the version. Thanks Ralph for suggesting!

* Changed how email confirmation works when updating an email address to be more aligned with allauth best practices, and stop using a method that was removed in the latest allauth.

* Changed the typescript module resolution strategy to “bundler”, which aligns better with how Vite resolves modules in the project.

* Added `.claude/settings.local.json` to `.gitignore`.

* Updated the behavior of the subscription page for team non-admins so that it shows a useful message telling them they aren’t allowed to manage subscriptions for their team, instead of returning a generic 404. Thanks Haydn for the suggestion!

* `./manage.py bootstrap_subscriptions` will now use Stripe’s “marketing features” property of Products to generate the relevant configuration in Pegasus. Thanks Zac for suggesting!

* `./manage.py bootstrap_subscriptions` will now only use products that have recurring pricing set when generating the Pegasus configuration.

* The `build-api-client` make target will now delete unused files and set correct file permissions on the generated code. Thanks Finbar for the contribution!

### Fixed

[Section titled “Fixed”](#fixed-1)

* **Improved the Python environment setup in `Dockerfile.dev` to be much more performant. This should make Docker container rebuilds after adding/changing Python dependencies much faster.**

  * Python environments and packages are now created and installed as the django user to avoid expensive chown calls. Thanks Jacob and Mark for the suggestion!
  * Uv now uses Docker’s cache system consistently so that dependencies are cached by Docker across builds.

* Added a `require_POST` decorator to `create_api_key` view so it doesn’t work with GET requests. Thanks Brennon for reporting!

* Fixed a bug where subscriptions tests failed due to a missing `dateutil` dependency under certain build configurations. Thanks Jacob for reporting!

* Fixed styling of allauth’s “email change” template, which is used if you set `ACCOUNT_CHANGE_EMAIL = True`. Thanks Finbar for the report and fix!

* Fixed a bug where `./manage.py bootstrap_subscriptions` and `./manage.py bootstrap_ecommerce` sometimes had to be run twice to sync all products and prices to a new installation. Thanks Zac for reporting!

* Updated stripe API imports to remove warnings about deprecated `stripe.api_resources` packages. Thanks Cristian for reporting!

*August 1, 2025*

## Version 2025.6.2

[Section titled “Version 2025.6.2”](#version-202562)

This hotfix release addresses two minor issues in the 2025.6 release:

* Remove breaking reference to `.babelrc` in `Dockerfile.web` on Vite builds. This was causing deployments to fail on some Docker-based platforms.
* Always add `gevent` dependency to production requirements if using celery. This fixes an issue running celery in production on certain deployment platforms.

Thanks Justin and Eugene for the bug reports!

*June 25, 2025*

## Version 2025.6.1

[Section titled “Version 2025.6.1”](#version-202561)

This is a hotfix release which addresses two minor issues:

* Fix `make npm-install` and `make npm-uninstall` commands when using vite as a bundler. Thanks Matt for reporting!
* Fix broken dark mode behavior on Tailwind when attempting to disable it. Thanks Wik for the report and fix!

*June 23, 2025*

## Version 2025.6

[Section titled “Version 2025.6”](#version-20256)

This release hardens the production Celery set up, expands AI-development tooling, improves production support for the standalone React front end, and extends the ecommerce application.

Read on for details!

### Celery improvements

[Section titled “Celery improvements”](#celery-improvements)

* Celery periodic tasks can now be configured via `settings.SCHEDULED_TASKS` and synchronized with a new management command (`./manage.py bootstrap_celery_tasks`). The previous migration files that created celery periodic tasks have been removed.
* The Celery gunicorn worker pool changed from the default of ‘prefork’ to ‘gevent’ in production, and the concurrency was increased. This should be a more scalable setup for most projects, though may need to be changed for projects that are heavily CPU-bound.
* Because of the above change, a separate worker for Celery Beat has been added to all production deploy environments (because beat can’t be run with the gevent pool).
* Updated the [Celery documentation](/celery) to reflect these changes.

### AI-Coding improvements

[Section titled “AI-Coding improvements”](#ai-coding-improvements)

* **Added an optional Claude Code Github workflow**. When enabled, you can mention @claude on a Github pull request or issue to trigger a Claude Code update. Learn more [in the docs here](/ai/development/#the-github-workflow-file).
* **Added optional support for JetBrains / PyCharm Junie AI rules files.** [Docs](/ai/development/#working-with-junie)
* Edited and expanded the AI rules files based on various user feedback (thanks to many who have contributed to this).

### Standalone front end improvements

[Section titled “Standalone front end improvements”](#standalone-front-end-improvements)

These updates affect the [standalone React front end](/experimental/react-front-end).

* Updated the front end CSS to build the files directly in the front end (and import relevant files from the Django app in `index.css`), rather than including the built Django CSS files directly.
  * Some required Tailwind CSS files in the `assets` directory will be included if you use the standalone front end even if you build for a different framework.
* Added tailwindcss, the typography plugin, and daisyui as explicit dependencies (and plugins) to the front end to enable the above change.
* Upgraded all JavaScript dependencies in the front end.
* Removed unnecessary default styles from `index.css`.
* Updated front end to use aliases for the “assets” directory. Also updated `tsconfig.json` to handle this.
* Updated `vite.config.ts` to fix various build issues if the parent `node_modules` isn’t available.
* Fixed the default values of `FRONTEND_ADDRESS` and related values in `settings.py` and `.env` files to point to “<http://localhost:5174>” (instead of port 5173).
* Added `CSRF_COOKIE_DOMAIN`, `CORS_ALLOWED_ORIGINS`, and `SESSION_COOKIE_DOMAIN` to `settings.py` using environment variables. These must be customized when deploying the standalone front end.
* Updated Kamal’s `deploy.yml` to include default values for the above settings.
* **Added initial documentation on [deploying the standalone front end to production](/experimental/react-front-end/#deployment).**

### Other updates

[Section titled “Other updates”](#other-updates)

* **Added a digital download example to the ecommerce application.** You can now associate a file with ecommerce products and only people who have purchased the product will be able to access it.
  * Also added tests for this workflow.

* Added a private storage backend, for storing private files on S3-compatible storage backends (used by the above).

* Upgraded most Python dependencies to their latest versions.

* Fix `target-version` in `pyproject.toml` to match the currently recommended Python 3.12. Thanks Finbar for reporting!

* Fixed a bug where group chat avatars were incorrectly styled on Tailwind builds. Added a new `pg-avatar` CSS class to handle this.

* Made some updates Digital Ocean deployments:

  * Switched Redis to Valkey, and upgraded it to version 8.
  * Upgraded Postgres to version 17.
  * Updated the [Digital Ocean deployment docs](/deployment/digital-ocean) to reflect the latest changes.

* Fixed email verification emails when `ACCOUNT_EMAIL_VERIFICATION_BY_CODE_ENABLED = True`. Thanks Justin for reporting and helping with the fix!

* Removed default font-weight styling from `email_template_base.html`.

* Api keys associated with inactive users will no longer pass API permission checks. Thanks Brennan for the suggestion!

* Removed unused `.babelrc` file if not building with Webpack.

* Automatically confirm user emails when they create accounts through the invitation acceptance workflow, since they can only get the invitation URL from the email link.

### Upgrading

[Section titled “Upgrading”](#upgrading-1)

If your project has existing migration files that create celery tasks (e.g. `/apps/subscriptions/migrations/0001_celery_tasks.py`), you should leave them in your repository to prevent issues running future migrations. The tasks themselves are unaffected, since they live in the database.

*June 10, 2025*

## Version 2025.5.1

[Section titled “Version 2025.5.1”](#version-202551)

This is a minor bugfix release on top of 2025.5.

* Removed bad reference to Modals in `site.js`. Thanks Jacob for reporting!
* Fixed Python Celery setup in `build_celery.sh` when using `uv` (Render deployments only). Thanks Jacob for reporting!
* Fixed issue with the shadcn dashboard caused by a missing `{% vite_react_refresh %}` tag. Thanks Shoaib for reporting!

*May 16, 2025*

## Version 2025.5

[Section titled “Version 2025.5”](#version-20255)

This release has a few big updates:

### Use Vite instead of Webpack for building the front end

[Section titled “Use Vite instead of Webpack for building the front end”](#use-vite-instead-of-webpack-for-building-the-front-end)

This release adds the option to use [Vite](https://vite.dev/) as a bundler instead of Webpack. Vite is a modern build tool that adds a few key benefits over the Webpack build system:

1. It is much faster than Webpack.
2. Hot Module Replacement (HMR)—a development feature that lets code changes in your front end files automatically update without a full-page reload.
3. Code splitting—a production feature that breaks your front end files into individual bundles that encapsulate code dependencies. This leads to less redundant JavaScript and faster page loads.

You can watch the video below for a walkthrough of these benefits and how they work in the new setup.

You can also see the overhauled [front end documentation](/front-end/overview) and [Vite-specific guidance](/front-end/vite) for more details.

### Gitlab CI support

[Section titled “Gitlab CI support”](#gitlab-ci-support)

You can now run CI on Gitlab in addition to Github. Gitlab’s CI will run your tests, linting, and build / type-check your front end files.

Thanks to Paolo and Simon for contributing to this feature!

### Retiring the Bootstrap Material Theme

[Section titled “Retiring the Bootstrap Material Theme”](#retiring-the-bootstrap-material-theme)

**The material theme for Bootstrap has been deprecated.** This means that the theme will be in maintenance-only mode, and support will eventually be dropped (probably in 6-12 months). Existing projects can continue using the theme, but new projects should not, and new Pegasus features will eventually not be developed and tested on the theme.

Dropping support for this theme was a difficult decision. The main reason it was made is that several Pegasus customers have complained about the lack of documentation and support for this theme from its maintainer, Creative Tim. Additionally, their process around updating the theme has involved releasing large, poorly-documented updates which have been difficult to incorporate back into Pegasus.

If you would like help migrating off this theme, you can reach out via standard support channels.

### Complete changelog

[Section titled “Complete changelog”](#complete-changelog)

**Changes related to Vite support**

* **Added Vite as an option for your front end build system. See [the front end](/front-end/overview) and [vite-specific docs](/front-end/vite) for details.**

* **`window.SiteJS` is now populated explicitly in JavaScript files (in addition to webpack’s library support, which does not work with Vite builds).**

  * Affected files include: `app.js` (`window.SiteJS.app`), `pegasus.js` (`window.SiteJS.pegasus`)
  * Imports in those files were also renamed to avoid namespace confilcts.

* Updated all JavaScript files using JSX to have a `.jsx` extension.

* Removed legacy Vue2 code and imports from the Vue example.

* Removed unused imports shadcn components.

* Removed leading tilde (”\~” character) from CSS imports in various places.

* Changed CSS imports in JavaScript files from `require` to `import`.

* Fixed a few small React warnings/issues in the AI chat app.

* Removed no longer needed `vue-template-compiler` dependency.

* **Updated the standalone front end to run on port 5174 to not conflict with the default vite port.**

**Other Changes**

* **Added “Gitlab” as an option for CI.** (Thanks Paolo and Simon!)
* **Deprecated the Material Bootstrap theme.**
* **Upgraded all Python packages to the latest versions, including Django 5.2.**
* **Upgraded all npm packages to the latest versions.**
* **Updated all `blocktranslate` tags to use the `trimmed` option for easier translation.**
* Added explicit width and height to some svgs to slightly improve styling when CSS is not present.
* Made minor updates to AI rules files.
* Use the new `ACCOUNT_SIGNUP_FIELDS` setting to configure sign up fields and removed usages of deprecated allauth fields.
* **Removed `project_settings` from the `project_meta` context processor.** This was previously only used to pass the now-deprecated `ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE` setting to sign up templates. The sign up templates now render the second password field based on the form value.

### Upgrading

[Section titled “Upgrading”](#upgrading-2)

For help switching from Webpack to Vite, see [the Webpack to Vite migration guide](/front-end/migrating).

*May 15, 2025*

## Version 2025.4.4

[Section titled “Version 2025.4.4”](#version-202544)

This is another minor release:

* Stop dynamically setting user/group ID in the `Makefile` and just default to `1000`. The dynamic ID assignment was continuing to cause issues on certain MacOS environments.
* Add `make build-api-client` target even when not using Docker.
* Added additional guidance on Pegasus’s Django model conventions to the Python AI rules.

*May 5, 2025*

## Version 2025.4.3

[Section titled “Version 2025.4.3”](#version-202543)

This is another bugfix release:

* Make the user/group creation more resilient in development Docker containers, which fixes a permissions issue on MacOS in certain environments. Thanks Chris for reporting!
* Add `architecture.md` to cursor rules directory.

*May 1, 2025*

## Version 2025.4.2

[Section titled “Version 2025.4.2”](#version-202542)

This is a bugfix release that addresses a few problems in the most recent build:

* Moved the new `CustomHeadlessAdapter` to `users/adapters.py` to fix an issue with it not being available if you built without teams enabled. Thanks Alex for reporting!
* Remove source maps for JavaScript bundles in production. This results in substantially smaller production bundle sizes. Thanks Jan for reporting!
* Automatically do a best effort to set the user/group ID used by the development docker container in the `Makefile`. Thanks Jacob for suggesting!

For the source map fix, you can change the “devtool” setting in `webpack.config.js` to this:

```javascript
  devtool: process.env.NODE_ENV === 'production' ? false : "eval-cheap-source-map",
```

*Apr 29, 2025*

## Version 2025.4.1

[Section titled “Version 2025.4.1”](#version-202541)

This is a big release with a few major updates.

### Team invitation workflow changes

[Section titled “Team invitation workflow changes”](#team-invitation-workflow-changes)

The workflow around new users joining teams and accepting invitations has been streamlined based on user feedback. For a summary of the changes you can watch [this walkthrough](https://youtu.be/qxr_WdQEL2g) or read below.

Key user-facing changes:

* **When a user signs up with a pending invitation they will be redirected to view it before creating their first team.**
* **Accepting an invitation requires having a verified email address for the email it was sent to.**
* Users can view pending invitations for any of their email addresses from the team selector dropdown.
* Inviting an email address of someone who’s already in a team will show an error message that they are already part of the team.

In addition, the following fixes and code updates were made:

* Added an API and serializer for accessing the logged-in user’s invitations, used by the React view.
* React: renamed `getInviteUrl` helper JS function to `getResendInviteUrl`.

*Thanks to EJ, Geoff, Valics, Simon, Arno, and possibly others who contributed ideas and feedback on the design of these changes.*

### API authentication and Standalone front end updates

[Section titled “API authentication and Standalone front end updates”](#api-authentication-and-standalone-front-end-updates)

The [Standalone React Front end](/experimental/react-front-end) underwent a major overhaul. Importantly, it now uses [allauth headless](https://docs.allauth.org/en/dev/headless/index.html) instead of a custom `dj-rest-auth` and custom authentication APIs.

On top of this, support for many new authentication workflows was added to the standalone front end, including email confirmation, password reset, and social authentication. The standalone front end—which is still in experimental mode—is now close-to-parity with the Django authentication system.

Details:

* **Enabled and configured [allauth headless](https://docs.allauth.org/en/dev/headless/index.html)** (if authentication APIs are enabled or using the standalone front end).

* **Removed `dj-rest-auth` and `djangorestframework-simplejwt` and associated setup code. Auth now uses allauth headless and sessions by default.**

* **Removed the `apps/authentication` app and associated api client code.**

* **Updated the standalone front end to use an authentication system against allauth headless and added support for email confirmation, social authentication and password reset.** These changes borrow heavily from the [allauth example](https://github.com/pennersr/django-allauth/tree/main/examples/react-spa) project, and involve a large number of code-level changes which are not fully outlined here, though some of the larger ones are listed below:

  * Added a `CustomHeadlessAdapter` class to add the user’s profile picture to the API.
  * Removed translation markup from JavaScript code that is shared with the standalone front end. Translations are not supported, currently.
  * Upgraded eslint-related libraries.
  * Updated `.eslintrc.cjs` to `eslint.config.mjs` and tweaked the configuration settings.
  * Show more/better validation errors on login, signup, etc.
  * Changed `ProtectedRoute` to `AuthenticatedRoute`.
  * Added templates and components for various new authentication workflows (email confirmation, password reset, etc.).
  * Added an `ACCOUNT_USER_DISPLAY` setting.

* Updated [the standalone front end docs](/experimental/react-front-end) to reflect the latest setup.

### Djstripe upgrade and webhook updates

[Section titled “Djstripe upgrade and webhook updates”](#djstripe-upgrade-and-webhook-updates)

This release upgrades `dj-stripe` to version 2.9 and migrates to dj-stripe’s database-backed webhooks. This lets you set up multiple webhook endpoints/secrets, if desired. See the upgrade section below for details on updating.

Details:

* **Upgraded dj-stripe to version 2.9**
* **Webhook endpoints now need to be configured in the database instead of having a single global endpoint.** See [the updated subscription webhooks documentation](/subscriptions/#webhooks) for more details.
* Updated webhook handling for subscriptions and ecommerce purchases to be compatible with the above model.
* Added a `bootstrap_dev_webhooks` management command to help set up `djstripe` webhooks for development.
* Added `apps.utils` to `settings.INSTALLED_APPS` so that management commands inside it are picked up.
* Removed the no-longer used `DJSTRIPE_WEBHOOK_SECRET` setting and environment variable.
* Upgraded `stripe` to version `11.6` (there is [a bug with djstripe and the latest `12.0` release](https://github.com/dj-stripe/dj-stripe/issues/2153))
* Updated the [subscription docs](/subscriptions/#webhooks) to reflect the latest changes for setting up webhooks in dev and production.

### Ruff linting updates

[Section titled “Ruff linting updates”](#ruff-linting-updates)

The ruff linting rules were expanded and code has been modified to pass the revised ruleset. This leads to cleaner, more consistent code across the project and should make future Pegasus merges/upgrades smoother.

Details:

* **Updated the default ruff rules to enable all of the [E (error) Rules](https://docs.astral.sh/ruff/rules/#error-e), as well as the [UP (pyupgrade) Rules](https://docs.astral.sh/ruff/rules/#pyupgrade-up), [B (flake8-bugbear) Rules](https://docs.astral.sh/ruff/rules/#flake8-bugbear-b), and [SIM (flake8-simplify) rules](https://docs.astral.sh/ruff/rules/#flake8-simplify-sim), in addition to the already-enabled [F (Pyflakes) Rules](https://docs.astral.sh/ruff/rules/#pyflakes-f), and [I (isort) Rules](https://docs.astral.sh/ruff/rules/#isort-i).**

* These lead to some minor code changes, including:

  * Use `contextlib.suppress` in a few places instead of the previous exception handling
  * Use `raise ... from` in several places for more explicit exception handling.
  * Combined some nested if statements into single lines.
  * Use `super()` instead of `super(C, self)`
  * Use f-strings instead of percent style format strings when possible.
  * Use `Type | OtherType` instead of `Union[Type, OtherType]` in type hints
  * Use core types for `list`, `dict` etc. instead of the type classes.
  * Define classes without the object base class.
  * Increased strictness around line lengths.

* Changed rule definition from `extend-select` to `select` based on [ruff’s recommendations](https://docs.astral.sh/ruff/linter/#rule-selection).

### Other updates

[Section titled “Other updates”](#other-updates-1)

* **Change: Upgraded npm to the latest version (11.3) in Docker containers and docs.**
* **Change: Added a honeypot field to the sign up form to help reduce bot/spam sign ups.** (Thanks Chris and Stian for suggesting!)
* Change: Added an ”@” alias for the `assets/javascript` folder and started using it in imports.
* Change: Updated development Docker setup to run as the logged-in user (under a `django` user account) instead of root. This should help with file ownership permissions being assigned to root after running the project with Docker. Thanks Finbar and Jacob for the suggestion and help with this!
* Change: Removed the “app-card” styling from the loading widget to make it more versatile.
* Change: Tweaked whitespace in a few templates to be more consistent across the project.
* Change: Use `blocktranslate trimmed` instead of `blocktranslate` in some Django templates.
* Change: Updated the output of `bootstrap_subscriptions` to communicate that only subscription products should be added to `ACTIVE_PRODUCTS`.
* **Fix: Changed reference of `stripe.Invoice.upcoming` to `stripe.Invoice.create_preview` since Stripe [deprecated the upcoming invoice API](https://docs.stripe.com/changelog/basil/2025-03-31/invoice-preview-api-deprecations).**
  * This fixes an issue with loading the “manage subscription” page when using the latest Stripe API version.
* Fix: Added `DEBUG=false` to `heroku.yml` setup section, which helps enforce that debug is disabled when running `collectstatic`. This helps avoid “No module named ‘daphne’” errors in async deployments. Thanks Abhishek for reporting!
* Fix: The `dark_mode_selector.html` component is no longer included if you have disabled dark mode.
* Fix: Improved chat height styling on mobile screens to avoid extra scrolling.
* Fix: Updated the migration that creates the default Site object to also update the table sequence ID. Thanks Julian and Geoff for the suggestion and help with this!
* Fix: Fixed a test case in `test_member_management` that wasn’t getting properly exercised.
* Fix: Deleted the unused `_create_api_keys_if_necessary` function in `bootstrap_subscriptions.py`
* Fix: Fixed the hover text color of the `.pg-button-danger` CSS class styles on tailwind builds.

### Upgrading

[Section titled “Upgrading”](#upgrading-3)

There are several changes in this release that may require additional steps during the upgrade process. To help with this, I recorded a video walkthrough of myself upgrading one of my own projects, which you can watch below:

#### Authentication APIs

[Section titled “Authentication APIs”](#authentication-apis)

If you were using Pegasus’s [standalone React front end](/experimental/react-front-end) then your setup should work out of the box after upgrading.

If you were using the `dj-rest-auth` app and previous authentication APIs in a different way, then you will need to either:

1. Update the client code to work with allauth headless. This can be done by referring to the example front end and [allauth documentation](https://docs.allauth.org/en/dev/headless/index.html).
2. Restore the previous implementation of the authentication APIs. This can be achieved by *rejecting* the proposed changes to remove the `apps.authentication` app and library dependencies/setup during the upgrade process.

#### Djstripe and Webhooks

[Section titled “Djstripe and Webhooks”](#djstripe-and-webhooks)

There are a few issues you might run into with the dj-stripe upgrade.

**Database Migrations**

If you get an `InconsistentMigrationHistory` running `manage.py migrate` on your database, look for any diffs in your existing migration files that change the `djstripe` dependency from `0012_2_8` to `0014_2_9a`, and then revert these changes back to `0012_2_8`.

**Webhooks**

The most recent dj-stripe has disabled the global webhook support in favor of database-backed webhooks. These are more versatile, secure, and easier to set up, but require a migration from the previous set up.

To migrate your webhooks, follow the instructions to set up a new webhook endpoint from the [subscriptions docs](/subscriptions/#webhooks-in-production) and then delete your previous webhook endpoint. There is a complete walkthrough of this process in the video above. **If you fail to do this your webhooks will stop working in production.**

#### Formatting and linting

[Section titled “Formatting and linting”](#formatting-and-linting)

All Pegasus code should be updated to pass the new ruff linting configuration, but the configuration changes might cause build failures on code that has been added/modified. Many fixes can be automated by running:

```bash
(uv run) ruff check --fix --unsafe-fixes
```

On the upgraded codebase and reviewing the changes made.

However, some errors will likely require manual fixing, which can be done by reading the output and making the suggested change (or even giving the task to an LLM). You can see how I did this process with Claude code in the above video. Alternatively, you can modify the `[tool.ruff.lint]` section of `pyproject.toml` to remove any categories of fixes you don’t want to turn on for your project.

*April 24, 2025*

## Version 2025.4

[Section titled “Version 2025.4”](#version-20254)

The main feature of this release is improved support for AI tools and coding assistants. This release adds a suite of rules files that can be used with Cursor, Claude Code, or other AI-enabled IDEs. It also adds an MCP configuration for interfacing with your development database and controlling a web browser. These options are configurable via new project settings.

Watch a demo below, or check out the new [AI tool docs](/ai/development).

### Added

[Section titled “Added”](#added-1)

* **Optional rules files and MCP configuration for Cursor or Claude.**
  * These files will continue to be modified and iterated on as more developers use them and provide feedback.settings

### Changed

[Section titled “Changed”](#changed-2)

* Improved default file input styles.
* Add front end install / build to `make init`. (Thanks Jacob for reporting!)
* Bumped `vite` used by the standalone front end to the latest version.
* Upgraded several Python packages to their latest versions.
* Removed unused `postcss.config.js` file from the front end. (Thanks Jacob for reporting!)

### Fixed

[Section titled “Fixed”](#fixed-2)

* **Fixed a potential XSS vulnerability issue with `markdown_tags` not properly escaping vulnerable tags.** This issue existed if you were using the AI chat UI, or built other functionality on top of that library. All markdown is now sanitized with `nh3`. (Thanks Mitja for reporting!)
  * Also added tests for this functionality.

### Translation Creator updates

[Section titled “Translation Creator updates”](#translation-creator-updates)

A number of new features were added to [Translation Creator](https://www.saaspegasus.com/store/product/translation-creator/) this month. Big thanks to community member Valics who contributed the first draft of most of these updates.

* **Upgraded to the latest Pegasus, including Tailwind 4 and DaisyUI 5.**
* **Translations will now retain comments.**
* **Added pagination, sort, and filtering to the translations view.**
* Added the ability to delete projects and clear translations.
* Updated the DB constraint to use a hash of the input text instead of the text itself, which improves performance and fixes a bug with long translations.
* Added / updated test cases.

*April 4, 2025*

## Version 2025.3

[Section titled “Version 2025.3”](#version-20253)

This release upgrades TailwindCSS to version 4 (and DaisyUI to Version 5). It also has several minor updates and fixes.

### Tailwind 4 Update

[Section titled “Tailwind 4 Update”](#tailwind-4-update)

Pegasus now runs on Tailwind V4! This comes with [a huge number of improvements](https://tailwindcss.com/blog/tailwindcss-v4), including much faster build times, simplified tooling, automatic content detection, and more.

Tailwind and DaisyUI were upgraded using the associated guides ([Tailwind](https://tailwindcss.com/docs/upgrade-guide), [DaisyUI](https://daisyui.com/docs/upgrade/)). There is also an [upgrade guide for Pegasus apps](/css/tailwind/#upgrading-from-tailwind-3-to-4).

Here’s a detailed breakdown of the changes:

* **Upgraded to Tailwind 4 and DaisyUI 5.**

* **Changed how tailwind is imported and customized in `site-tailwind.css` to match the V4 guidance.**

* **Removed `content` section of `tailwind.config.js`. Tailwind 4 automatically finds all content for the project.**

* **Updated `postcss.config.js` to match the Tailwind 4 recommendation (using `@tailwindcss/postcss`).**

* **Converted tailwind-specific CSS to V4 syntax, using `npx @tailwindcss/upgrade`. *These changes were automated.***

  * Removed `@layer` declarations
  * Converted some helper classes to use `@utility`
  * Changed some double quotes to single quotes and cleaned up whitespace in css files.
  * Updated various classes in templates/JavaScript files according to the migration guide, e.g. `outline-none` —> `outline-hidden`, `flex-grow` —> `grow`, `max-w-screen-xl` —> `max-w-(--breakpoint-xl)` etc.

* DaisyUI updates:

  * **DaisyUI is now initialized as a plugin in `site-tailwind.css` instead of `tailwind.config.js`.**
  * **Themes are also now handled in this section. The docs have been updated to reflect this.**
  * Updated Pegasus CSS color variables to use the DaisyUI 5 versions.
  * Cleaned up Tailwind form rendering tags, removed unnecessary markup, and upgraded markup to be compatible DaisyUI 5, e.g. removing `-bordered` classes.
  * Checkboxes will now appear on the left instead of the right of labels.
  * Updated active tabs to use the latest DaisyUI markup (`menu-active` instead of `active`).

* Shadcn updates:

  * **Moved shadcn components from `assets/javascript/components/ui` to `assets/javascript/shadcn/components/ui`.**
  * **New shadcn components can now be added via the CLI and will end up in the right place with no additional steps.**
  * Updated `tsconfig.json` and `webpack.config.js` to be consistent with new shadcn setup.
  * Regenerated shadcn components from the latest version of the library.
  * Changed shadcn themeing to use `@theme` declaration.
  * Removed all shadcn customizations from `tailwind.config.js` as they are superceded by the theme system.
  * Upgraded various shadcn dependencies to their latest versions.

* Flowbite updates:

  * **Upgraded Flowbite to version 3.1.**
  * **Flowbite is now initialized as a plugin in `site-tailwind.css`.**
  * Explicitly import flowbite styles when building with flowbite enabled. This fixes out-of-the-box styling of some plugins. (Thanks Eeshan for reporting and fixing!)

* Extracted dark mode selector to its own component and upgraded it to work with DaisyUI 5.

* Other fixes / changes

  * Cleaned up various bits of CSS to use nested selectors.
  * Improved the contrast of the `pg-text-muted` class on dark mode.
  * Cleaned up commented out code in CSS files.

* Removed unused “app” CSS class styles.

* Standalone front end updates:
  * **Removed tailwind entirely from the standalone front end CSS.** The standalone front end currently gets its css from the same built file as the Django app.

* Updated the [Tailwind Documentation](/css/tailwind) to reflect the V4 changes.

### Other Updates

[Section titled “Other Updates”](#other-updates-2)

* Fixed an issue running `./manage.py` commands in production docker containers when using `uv`. Thanks Richard, Bryan, and Ken for reporting!
* Fixed active tab highlighting on Flowbite demo.
* Removed `--no-emit-package setuptools` from the `make pip-compile` command. Some configurations require setuptools and this was causing issues on some pip-tools builds. Thanks Jim for reporting and fixing!
* Changed ruff `exclude` to `extend-exclude` in `pyproject.toml` to keep ruff’s defaults. Thanks Justin for the suggestion!
* Added help text to a few `make` targets that were missing it. Thanks Steve for the suggestion!
* Removed unused `pg-is-loading` CSS class.
* Fix syntax of commented out `EMAIL_BACKEND` variable in `deploy.yml`.
* Removed language codes from the language selector dropdown.

### Upgrading

[Section titled “Upgrading”](#upgrading-4)

See the [Tailwind upgrade guide](/css/tailwind/#upgrading-from-tailwind-3-to-4) for details on upgrading existing Tailwind projects.

*Mar 26, 2025*

## Version 2025.2.2

[Section titled “Version 2025.2.2”](#version-202522)

This is a hotfix release that fixes a bug in the styling of the avatar in the navbar on Bootstrap using certain browsers. Thanks Luc for reporting!

* Restored `navbar.css` on bootstrap builds and moved it out of the bulma-specific folder.
* Updated imports in `base.css` accordingly.

*Mar 13 2025*

## Version 2025.2.1

[Section titled “Version 2025.2.1”](#version-202521)

This is a hotfix release that fixes a missing newline between `REDIS_URL` and `GOOGLE_ANALYTICS_ID` in `.env` / `secrets` files. Thanks Peter for the bug report!

*Mar 7 2025*

## Version 2025.2

[Section titled “Version 2025.2”](#version-20252)

This is a maintenance release with a number of upgrades and fixes.

### Added

[Section titled “Added”](#added-2)

* **You can now configure the Github integration to push your Pegasus code to a subdirectory of the repository.** [More details in the updated Github docs here](/github/#pushing-pegasus-code-to-a-subdirectory-in-your-repository). Thanks to Simon for helping with this, and Aaron, Bernard, Danil, and Arno for suggesting it!
* Added a `429.html` error template.

### Changed

[Section titled “Changed”](#changed-3)

* **Migrated the majority of shared style files from sass to css, and removed sass from Tailwind builds.** This makes the setup more consistent with a typical Tailwind project.

  * Removed “sass” and “sass-loader” packages from Tailwind builds.
  * Updated `webpack.config.js` on bootstrap and bulma builds to also now handle `.css` files.
  * Related, ported the `navbar.sass` file to css, moved it to the `bulma` folder, and removed it from non-Bulma builds.

* **Set [Django’s cache framework](https://docs.djangoproject.com/en/latest/topics/cache/) to use Redis in production by default.**

  * The Redis cache will be enabled when `settings.DEBUG` is `False`.
  * Also explicitly list `redis` as a first-class requirement, which fixes a bug where tests could fail if you disabled celery.

* Added `.venv` and `venv` to the `.gitignore` file. (Thanks Peter for suggesting!)

* Use the project id in the default `AWS_STORAGE_BUCKET_NAME` in deploy.yml. (Kamal deployments, thanks Peter for suggesting!)

* Updated the version of `ruff` used by pre-commit to the one that’s installed in the project, and upgraded ruff to the latest (0.9.7). (Thanks Peter for reporting!)

* Added a timeout and error handling to turnstile requests, to prevent hanging if Cloudflare was for some reason down. (Thanks Peter for suggesting!)

* Removed `ENABLE_DEBUG_TOOLBAR=True` from production environment/secrets files.

* Consistently use double quotes instead of single quotes in environment and deployment files. (Thanks Peter for suggesting!)

* Removed duplicate and unused variable declarations across Kamal’s `deploy.yml` and `secrets` files. Public variables are now listed in `deploy.yml` and private ones are listed in `secrets`. (Thanks Peter for suggesting!)

### Fixed

[Section titled “Fixed”](#fixed-3)

* **Improved edge-case handling the Stripe checkout integration.**

  * Users should now see helpful error messages instead of getting 500 errors or ending up in an invalid state if they hit certain invalid URLs.
  * This also fixes a vulnerability where an attacker could potentially simulate e-commerce purchases through manual inspection and manipulation of requests.

* Fixed a bug where `setuptools` was accidentally not present in production requirements files when using pip-tools. This caused production deployments to fail in certain cases. (Thanks Eeshan and Jim for reporting!)

* Fixed an issue deploying to Heroku with Docker when using uv by removing Docker caching, which Heroku does not support. (thanks Toul for reporting!)

* Fixed the active tab highlighting styles in the examples navigation on Bulma builds.

* Removed unnecessary `<div>` elements from `top_nav.html` on Bootstrap builds.

* Don’t include Docker translation instructions in README if not using Docker. (Thanks Peter for reporting!)

* Updated the Pegasus CLI to [version 0.8](https://github.com/saaspegasus/pegasus-cli/releases/tag/v0.8), which fixes a bad html closing tag in the generated templates. (Thanks Julian for the bugfix!)

* Removed celery sections from `deploy.yml` in kamal builds if celery isn’t enabled.

### Removed

[Section titled “Removed”](#removed)

* Removed `django_otp` dependency and configuration, which was only there to facilitate the transition to `allauth.mfa`. See the release notes for [Version 2024.5](#version-20245) for more information on this change.
  * Also removed the associated `migrate_allauth_2fa` management command.
* Removed the default user-facing messages on login/logout. You can add them back or customize them by editing the files in `/templates/account/messages/`.

### Documentation

[Section titled “Documentation”](#documentation)

* Added [a community guide on using Digital Ocean Spaces](/community/digital-ocean-spaces) (alongside Amazon SES). Thanks Neil and Finbar for the contribution!

### Upgrading

[Section titled “Upgrading”](#upgrading-5)

Tailwind projects that have added their own `.sass` files will need to either restore sass support or port these files to `.css` (llms are good at this!). You can “restore” sass support by rejecting the proposed changes in `package.json` and `webpack.config.js` during upgrade.

If you have removed Redis from your project you will need to update the default cache config in `settings.py`.

*Feb 28, 2025*

## Version 2025.1.1

[Section titled “Version 2025.1.1”](#version-202511-1)

This is a hotfix release that fixes an issue with installing Node 22 in the development Docker container. Thanks Oscar and Emiliano for reporting!

If you’d rather manually apply the patch, you can just apply the following patch to your `Dockerfile.dev` file:

```diff
RUN --mount=target=/var/lib/apt/lists,type=cache,sharing=locked \
    --mount=target=/var/cache/apt,type=cache,sharing=locked \
    rm -f /etc/apt/apt.conf.d/docker-clean && \
    echo "deb https://deb.nodesource.com/node_22.x bookworm main" > /etc/apt/sources.list.d/nodesource.list && \
    wget -qO- https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - && \
    curl -fsSL https://deb.nodesource.com/setup_22.x | bash - && \
    apt-get update && \
    apt-get install -yqq nodejs \
```

*Jan 28, 2025*

## Version 2025.1

[Section titled “Version 2025.1”](#version-20251)

This release includes mostly backend infrastructure changes to some Pegasus features to pave the way for a (future) plugin ecosystem. This should make it easier to maintain Pegasus apps as well as possible (in the future) for other people to develop apps that can seamlessly integrate into Pegasus.

### New “async” build flag

[Section titled “New “async” build flag”](#new-async-build-flag)

Previously when you enabled async / websockets, you also got the group chat example application. Now you can enable async features without this additional example app, and turn it on separately with a new configuration option.

This lets you use async but not have to manually delete the example application.

### Added a flag to remove Celery (if possible)

[Section titled “Added a flag to remove Celery (if possible)”](#added-a-flag-to-remove-celery-if-possible)

Added a configuration option that will remove celery and all dependencies + configuration ***if no other parts of your application need it***. Celery will also be removed from production deployment configurations.

Celery is still required (and will be automatically enabled) if you are using any of:

1. The Pegasus examples
2. Subscriptions with per-unit billing enabled
3. Any AI chat features

If you’re not using these features and want to disable Celery you can do that from your project settings page.

### Organizational changes to apps for more consistency

[Section titled “Organizational changes to apps for more consistency”](#organizational-changes-to-apps-for-more-consistency)

The following changes don’t have any new features or functionality, but change small things about how the code is organized for affected apps (AI chat, AI images, and async group chat). It is hoped that these changes will make maintenance, upgrades, and future extensions to Pegasus easier.

Changes affecting the AI Chat, AI Images, and Group Chat apps:

* Moved app declarations for these apps to the end of `PROJECT_APPS` in `settings.py`
* Moved url declarations for these apps to the end of `urls.py`.
* Moved settings and environment variables for these apps to be located together.
* Settings for these apps are now prefixed with `AI_CHAT_` or `AI_IMAGES_`, respectively.
  * **This also means that shared settings like `OPENAI_API_KEY` are now declared multiple times and need to be updated in multiple places.** See the “upgrading” section below on how to get around this duplication.
* Moved chat JavaScript setup to the end of `module.exports` in `webpack.config.js`.
* Depending on your configuration, the order of navigation tabs in the UI may change.
* Made minor tweaks to how channels urls are set up.
* Image logos used by the AI chat and images apps were moved to `/static../../assets/images/ai_../../assets/images/` and `/static../../assets/images/ai_../../assets/images/`, respectively.
* The declaration for these apps has moved to a new “plugins” section of `pegasus-config.yml`.

### Other Changes

[Section titled “Other Changes”](#other-changes-3)

Other changes included in this release are below.

**Changed**

* **Upgraded default Python to Python 3.12.**

  * Bumped the Python version to 3.12 in CI, and dev/production Docker containers.
  * Also added [a `.python-version` file](https://docs.astral.sh/uv/concepts/python-versions/#python-version-files) for uv builds (set to 3.12)

* **Upgraded default Node to 22.**
  * Bumped the Node version to 22 in CI, and dev/production Docker containers.

* **Upgraded nearly all Python packages to their latest versions.**
  * Added a pin to `dj-stripe<2.9` because 2.9 is not yet supported.

* **Upgraded nearly all JavaScript packages to their latest versions.**
  * Tailwind v4 was not upgraded as it was just released and is not yet supported.

* **Ruff and pre-commit will now sort imports by default.** (See upgrade notes below)
  * **This also updates import sorting in a number of files.**

* **Pre-commit now runs ruff with `--fix` enabled, which will automatically apply (but not stage) fixable errors.**

* Dependencies are now sorted in `pyproject.toml` (uv builds) and `requirements.in` (pip-tools builds)

* Added email address to admin search for team memberships and invitations. Thanks EJ for the suggestion!

* Made the “timezone” field editable in the user admin. Thanks Peter for the suggestion!

* Changed active tab variable for ai image app from “ai\_images” to “ai-images” to match convention of other apps.

* Added a link from the user profile to manage email addresses if the user has more than one email registered. (Thanks Simon for the suggestion!)

* Make it so that `./manage.py` commands default to `uv run` if you build with uv enabled.

* The `chat_tags` template tag library was moved to the `web` app and renamed to `markdown_tags`, making it easier to use outside the chat application.

**Fixed**

* **Fixed an issue that caused Render deployments to fail when using uv.** (Thanks Jacob for reporting and helping fix!)
* Add `psycopg2-binary` to production requirements if using sqlite, since it still required for production deployments. (Thanks Randall for reporting!)
* Updated invitations to always store email addresses in lowercase to be consistent with account emails. Also fixed comparisons between invitations and sign up emails to be case-insensitive. (Thanks EJ for reporting and the fix!)
* Renamed `tailwind.config.js` to `tailwind.config.cjs` which prevents build failures on Node 22.

**Removed**

* Removed no-longer-used `payments.js` and `stripe.sass` files.
* Stopped including `pip-tools` in `dev-requirements` when using `uv`, as it is no longer needed.

### Upgrading

[Section titled “Upgrading”](#upgrading-6)

**Python / Node updates**

You may need to manually modify your dev/production environment to upgrade to Python 3.12 and Node 22. If you’re using Docker, this should happen automatically by following the [upgrade process](/upgrading).

Pegasus apps should still run on Python 3.11 / Node 20, but will no longer be extensively tested on those versions moving forwards.

**Settings Changes**

Some settings around AI API keys have been renamed and will need to be updated in your `settings.py` and `.env` files. If you are using AI chat and AI images with OpenAI, the easiest way to use a shared API key is to add the following to your `.env` / environment variables:

```plaintext
OPENAI_API_KEY="sk-***"
```

And then modify your settings variables to read from that value:

```python
# add an OPENAI_API_KEY setting, in case it was referenced elsewhere in your code
OPENAI_API_KEY = env("OPENAI_API_KEY", default="")
# modify the image/chat settings to use the same openai key instead of reading from new environment variables
AI_IMAGES_OPENAI_API_KEY = OPENAI_API_KEY
AI_CHAT_OPENAI_API_KEY = OPENAI_API_KEY
```

**Import Sorting Changes**

If you have auto-formatting enabled you will likely get CI errors after upgrading due to the stricter import sorting.

You can fix these by running a manual ruff check locally and then committing the result:

```plaintext
ruff check --fix
# or with uv
uv run ruff check --fix
```

*Jan 27, 2025*

## Version 2024.12.1

[Section titled “Version 2024.12.1”](#version-2024121)

This is a minor hotfix release for 2024.12

* **Fixed a bug where the delete workflow was broken for apps created by the Pegasus CLI on non-Tailwind builds.** This happened becasue the “css\_framework” cli option was accidentally missing from `pegasus-config.yml`. Thanks Robert for reporting!
* Updated the README instructions for setting up pre-commit hooks when using uv.

*Jan 13, 2025*

## Version 2024.12

[Section titled “Version 2024.12”](#version-202412)

content/ This release adds first-class support for using uv as a complete replacement for development and production workflows (see below), and has a handful of fixes/changes.

### UV support!

[Section titled “UV support!”](#uv-support)

This release adds full support for [uv](https://docs.astral.sh/uv/) as a replacement package manager for your project. You can use uv by selecting the new “uv” as your “Python package manager” on your project settings page.

When you select uv the following changes will be made:

* All requirements.in / requirements.txt files are removed.
* Your project requirements will now be listed in your `pyproject.toml` file.
  * Development and production dependencies will be listed under separate dependency-groups.
* Your pinned project requirements will be listed in a new `uv.lock` file.
* Docker containers (in development and production) will use `uv` to set up and manage the Python environment.
* A `make uv` target will be added to Docker builds to run `uv` commands in your container.

The main benefits of using uv are:

* Speed. It is just way, way faster to anything related to package management.
* Easier to setup and install Python.
* Lock files (pinned versions) are consistent across any platform.
* More tooling.
* Speed. (It’s so fast we put it twice.)

There will be a longer write up about uv released very soon, but in the meantime you can review the updated [python documentation](/python/setup) and new [uv documentation](/python/uv).

The rest of the docs have been updated to accommodate uv, though it’s possible there are some places that were missed. If you spot any issues in the docs, get in touch!

### Other fixes

[Section titled “Other fixes”](#other-fixes)

* **Upgraded the pegasus cli to fix an issue where the generated list views were not properly scoped to the appropriate team / user.** If you used the CLI to generate any apps it’s highly recommended that you check that you are not exposing objects that should not be viewable.

### Other updates

[Section titled “Other updates”](#other-updates-3)

* **Changed the default set up of social logins to use settings-based configuration instead of `SocialApps` in the database.** See the upgrade notes if you are using social logins to prevent issues. Thanks Alex for the suggestion and for helping with the updated documentation!
* Updated the default flowbite setup to disable the forms plugin. This was causing styling conflicts with the default DaisyUI styles on certain form elements, including checkboxes.
* Re-formatted the default form input template for readability.

### Upgrading

[Section titled “Upgrading”](#upgrading-7)

To migrate an existing project to `uv` see [this guide](/cookbooks/#migrating-from-pip-tools-to-uv).

If your application was already using social logins defined in the database, the new settings-based declaration will conflict and cause errors on social login. To fix this you can either delete the `APPS` section of the relevant service in `settings.SOCIALACCOUNT_PROVIDERS`, or you can move the credentials into your project environment (e.g. `.env`) and delete relevant the `SocialApp` from the Django admin.

*November 29, 2024*

## Version 2024.11.3

[Section titled “Version 2024.11.3”](#version-2024113)

This is a minor maintenance release with a few changes in preparation for adding `uv` support (coming soon!).

### Changed

[Section titled “Changed”](#changed-4)

* Pinned the version of `uv` used in CI and Dockerfiles.
* Added `venv` and `.venv` directories to the `.dockerignore` file and `make translations` target.
* The `make requirements` command now restarts containers in the background, making it easier to combine with other make targets.
* Added a catch-all to the `Makefile` to prevent error messages when running `make npm-install <package_name>` and similar commands.
* Updated README commands to consistently use `python manage.py` instead of just `./manage.py`.
* Made some minor formatting changes to `pyproject.toml`.
* Fixed the link to the multi-stage dockerfile docs in `Dockerfile.web`
* Upgraded a number of Python packages.
* Updated the `default_stages` of the `.pre-commit-config.yaml` file to the latest expected format (`pre-commit`).

*Nov 21, 2024*

## Version 2024.11.2

[Section titled “Version 2024.11.2”](#version-2024112)

This release adds the ability to disable dark mode on Tailwind, upgrades front end libraries, bumps the API client version, and has a handful of other small changes and fixes.

## Added

[Section titled “Added”](#added-3)

* **Added a new build option to disable dark mode for Tailwind builds.** (Thanks Arno for suggesting!)
* Added basic user-facing error messages to the standalone front end sign up and login workflows.

## Changed

[Section titled “Changed”](#changed-5)

* **Upgraded all JavaScript dependencies.**
* **Updated the API client to use the latest version 7.9.0, and updated the standalone front end to work with the latest changes.**
* Updated template-partials installation to be manually loaded, to allow for easier integration with other templating systems like django-cotton.
* Moved active tab highlighting to the base view in the example object demo.
* Made a few very minor edits to comments and whitespace in a few places.

## Fixed

[Section titled “Fixed”](#fixed-4)

* Fixed a bug where your migrations and tests would fail if your project name was > 50 characters (thanks Bernard for reporting!).
* Fixed a bug in the group chat demo where submitting an empty room name would take you to a 404 page.
* The `docker_startup.sh` file is no longer included if you are not using a docker-based deploy platform.
* Updated the `config/README` file which had outdated information that predated the migration to Kamal 2. (Thanks Arno for reporting!)
* Improved comments in the kamal `secrets` file and `.env` files. (Thanks Arno for suggesting!)

## Removed

[Section titled “Removed”](#removed-1)

* The `.env` file is no longer included in zip downloads. This file was already removed from Github builds so this just makes the two consistent. Projects should create `.env` file from the `.env.example` file.
* Removed the `migrate_customers_to_teams` management command. This was added for an upgrade two years ago, and is assumed to be no longer needed.

*Nov 14 2024*

## Version 2024.11.1

[Section titled “Version 2024.11.1”](#version-2024111)

This is a minor hotfix release.

### Fixed

[Section titled “Fixed”](#fixed-5)

* Fixed an issue where the team selector was accidentally transparent in Tailwind builds.
* Removed shadcn template that was accidentally included even if shadcn was disabled.

### Updated

[Section titled “Updated”](#updated)

* Removed extra whitespace from `form_tags.py`. (Thanks Brennon for reporting!)
* Updated `make help` to allow for commands defined in `custom.mk` with digits to also show up. (Thanks Arno for suggesting!)

*Nov 4 2024*

## Version 2024.11

[Section titled “Version 2024.11”](#version-202411)

This is a feature release with an emphasis on improving the Tailwind CSS experience with Pegasus.

Watch the video below for a demo, or read on for the highlights.

### Dark mode improvements

[Section titled “Dark mode improvements”](#dark-mode-improvements)

A dark mode selector was added to the navigation, allowing users to easily toggle between light, dark, and “system default” mode. The user’s selection is preserved server-side in the session object, which also helps to prevent flickering across page loads.

### Better Theme Support

[Section titled “Better Theme Support”](#better-theme-support)

It’s now easier than ever to change your project’s theme. Each project now supports a default light and dark theme which will be used throughout the site. The default themes need only be changed in `tailwind.config.js`, and `settings.py` and everything else is taken care of.

See the updated [tailwind theme documentation](/css/tailwind/#changing-your-themes) for more details.

### New shadcn integration and demo dashboard

[Section titled “New shadcn integration and demo dashboard”](#new-shadcn-integration-and-demo-dashboard)

A new build setting allows you to build your project with [shadcn/ui](https://ui.shadcn.com/) installed. Shadcn is a great and versatile component library for React and Tailwind, but it is difficult to integrate it into a Django project without building a separate front end. Now Pegasus takes care of that integration for you, and provides a reference dashboard implementation of how to work with the library.

The reference dashboard is a hybrid single-page React app served by Django. It uses the same colors as the DaisyUI theme, and will update when you change your theme, and has many interactive components. However, it is not connected to any backend data—it is just a UI example.

Read more in the [shadcn docs here](/css/tailwind/#shadcn).

### New flowbite integration and demo component page

[Section titled “New flowbite integration and demo component page”](#new-flowbite-integration-and-demo-component-page)

Another new build setting allows you to build your project with [flowbite](https://flowbite.com/) installed. Flowbite is another great component library for Tailwind and does *not* use React—making it a great fit for htmx projects. If you enable this setting, flowbite will automatically be installed and you can drop flowbite components into any Django template. The reference page has an example of a few of these components.

Read more in the [flowbite docs here](/css/tailwind/#flowbite).

### Other updates

[Section titled “Other updates”](#other-updates-4)

* **Upgraded all Python packages to their latest versions.**

* **[uv](https://docs.astral.sh/uv/) is now used to install Python packages in Docker files and Github actions.**

  * Also updated `make pip-compile` target to use `uv`.
  * This resulted in minor changes to all `requirements.txt` files.

* **Team invitation pages now prompt a user to log in instead of sign up if the email is associated with a known account.** (Thanks Daniel for suggesting!)

* Your configured Github username, if available, will be used in a few places instead of a default value. (Thanks Richard for suggesting!)

* Added `bg-base-100` to the `<body>` tag of the base template and removed it from other components where it was now redundant. This improves theming support when themes heavily modify the base color. (Tailwind builds only)

* Added equals signs to `ENV` declarations in production Docker files, for consistency. (Thanks Denis for suggesting!)

* Slightly improved the styling of the e-commerce app.

* Overhauled the [Tailwind CSS documentation](/css/tailwind).

**Updates to the CLI ([release notes](https://github.com/saaspegasus/pegasus-cli/releases))**

* Fixed a bug on certain environments where the `pegasus` command conflicted with a local `pegasus` folder, causing import errors running the CLI.
* Apps created with `startapp` now use a `POST` for deletion instead of a `GET`.
* Deletion now includes a modal confirmation (Tailwind and Bulma builds only).

### Upgrading

[Section titled “Upgrading”](#upgrading-8)

If you’re using Docker the `make upgrade` command won’t work out-of-the-box due to the change in how requirements files are managed. You will first have to rebuild your containers with:

```bash
make build
```

or

```bash
docker compose build
```

After that, you should be able to run `make upgrade` as normal.

*Nov 1, 2024*

## Version 2024.10

[Section titled “Version 2024.10”](#version-202410)

This release upgrades Kamal deployment to Kamal 2 and dramatically simplifies the Kamal deployment process.

### Kamal 2 deployment and related changes

[Section titled “Kamal 2 deployment and related changes”](#kamal-2-deployment-and-related-changes)

In the upgrade to Kamal 2, the following changes were made:

* Updated Kamal to run from the root project directory instead of the `deploy` subdirectory.
  * Also moved the config file was also moved from `deploy/config/deploy.yml` to `config/deploy.yml`
* Moved environment secrets from `deploy/.env` to `.kamal/secrets` to match Kamal 2’s recommendation.
* Kamal can now be installed and run with Docker without any additional workarounds [as described here](https://kamal-deploy.org/docs/installation/) The custom docker set up instructions have been removed.
* Kamal is now run as root by default, which dramatically simplifies the server setup process. There is now no need to run any manual steps to set up your server.
* Kamal now creates and manages its own docker network.
* Traefik has been dropped in favor of `kamal-proxy` for the proxy server, as per the new Kamal defaults.
* The `.gitignore` and `.dockerignore` files were updated to reflect the new structure.
* Added `apps.web.middleware.healthchecks.HealthCheckMiddleware` to workaround Kamal health checks and Django security features, [as outlined here](https://github.com/basecamp/kamal/issues/992#issuecomment-2381122195).
* Removed unnecessary media directory set up from `Dockerfile.web`. It is recommended to use an external storage service for media files and not the Docker container.

In addition, there were a few changes that affect projects that aren’t using Kamal:

* `apps.web.locale_middleware` was moved to `apps.web.middleware.locale`
* `docker_startup.sh` was moved from the `deploy` folder to the project root.

The [Kamal documentation](/deployment/kamal) has been updated to reflect these changes.

### Other fixes

[Section titled “Other fixes”](#other-fixes-1)

* **Subscriptions in a “past due” state are now treated as “active” for the purposes of feature gating and accessing the billing portal.** This is more consistent with [how Stripe treats subscriptions in this state](https://docs.stripe.com/api/subscriptions/object#subscription_object-status). (Thanks Luc for suggesting!)
* Fixed a bug where several `make` targets mistakenly included a `--no-deps` flag which would fail if your database container was not running. (Thanks Gary for reporting!)
* Fixed an issue where Stripe subscription webhooks weren’t properly handled if you were using the embedded Stripe pricing table. (Thanks Andrew for reporting!)
* Fixed an issue introduced in 2024.9 where Stripe ecommerce webhooks weren’t always processed correctly.
* Added a migration file to automatically work around [this dj-stripe issue](https://github.com/dj-stripe/dj-stripe/issues/2038) so that it wasn’t a manual process.

*Oct 15, 2024*

## Version 2024.9.3

[Section titled “Version 2024.9.3”](#version-202493)

This release is mainly [an update to the CLI](https://github.com/saaspegasus/pegasus-cli/releases/tag/v0.3):

### CLI updates

[Section titled “CLI updates”](#cli-updates)

* **You can now generate apps that work seamlessly with Pegasus teams** (will use `BaseTeamModel` and add the team slug and permissions checks to all urls and views).
* The CLI now generates a default `admin.py` config for each data model.
* User foreign keys now use `settings.AUTH_USER_MODEL` instead of being hardcoded to `apps.users.models.CustomUser`.

### Other changes

[Section titled “Other changes”](#other-changes-4)

* Fixed an issue where HTMX links without href tags weren’t showing a pointer cursor on some CSS frameworks.
* Add default region to Redis and Postgres configurations in `render.yaml` to make it easier to find/replace them when changing your project’s region. (Thanks Jacob for suggesting!)

*Sep 26, 2024*

## Version 2024.9.2

[Section titled “Version 2024.9.2”](#version-202492)

This release fixes a bug that prevented the CLI from running on Windows machines. Thanks Jonathan for reporting!

If you don’t want to upgrade you can just `pip install pegasus-cli==0.2.1` to apply the fix.

*Sep 20, 2024*

## Version 2024.9.1

[Section titled “Version 2024.9.1”](#version-202491)

This release fixes a few things in the 2024.9 release.

* Updated the `bootstrap_ecommerce` management command to create `ProductConfiguration` objects for all active Products in Stripe.
* Fixed an issue on the ecommerce homepage where a closing `</div>` tag was misplaced if a product didn’t have a default price set.

*Sep 18, 2024*

## Version 2024.9

[Section titled “Version 2024.9”](#version-20249)

There are two big updates in this release:

1. The Pegasus CLI, which allows you to instantly spin up new apps.
2. E-Commerce/Payments improvements.

### The Pegasus CLI

[Section titled “The Pegasus CLI”](#the-pegasus-cli)

The [Pegasus CLI](https://github.com/saaspegasus/pegasus-cli/) is a standalone command-line tool that allows you to instantly spin up new Django apps. You can specify as many data models as you want and it will generate a starting CRUD interface for each of them.

Here’s a quick demo:

**At the moment the CLI only supports HTMX build of Pegasus.** A React-based implementation is planned for a future date.

Huge thanks to Peter for his excellent [Pegasus example apps](https://github.com/pcherna/pegasus-example-apps-v2) project which served as a reference for implementing the CRUD application and pagination.

### E-Commerce / Payments demo improvements

[Section titled “E-Commerce / Payments demo improvements”](#e-commerce--payments-demo-improvements)

This is a series of updates designed to make it easier to build a functional end-to-end application on top of the e-commerce demo.

* Added a `ProductConfiguration` model to attach additional metadata to products.
* E-Commerce product URLs and views now use the `ProductConfiguration` `slug` field instead of the Stripe Product IDs.
* Added a `@product_required` decorator that can be used to restrict access to views based on whether the user has purchased a product.
* Added a demo “access product” page that shows how to use the `@product_required` decorator.
* Added `user_owns_product` and `get_valid_user_purchase` helper functions.
* Improved the navigation and use of breadcrumbs in the demo UI.
* **See upgrade notes for information about migrating previous data to the new set up.**

See also: the updated [Payments docs](/payments).

### Other Changes

[Section titled “Other Changes”](#other-changes-5)

#### Added

[Section titled “Added”](#added-4)

* **Added `django-htmx` and `django-template-partials` as first-class dependencies to HTMX builds.** These libraries are used by the CLI and will be used for more HTMX-based functionality moving forwards.
* Added `make manage` command to run arbitrary `manage.py` commands in a docker environment. E.g. `make manage ARGS='createsuperuser'`.
* Added the ability to pass arguments to `make test` in docker. E.g. `make tests ARGS='apps.teams --keepdb'`. (Thanks David for the suggestion!)

#### Changed

[Section titled “Changed”](#changed-6)

* Changed links on the tailwind signup page to use `pg-link` class instead of explict tailwind classes. (Thanks Peter for the suggestion!)
* Silenced extraneous djstripe warnings when running tests. (Thanks Chris for the suggestion!)
* Added `.vscode` and vs workspace files to the project `.gitignore`.
* Switched from `assert` statements to `raise ValueError` in the e-commerce Stripe checkout confirmation view.
* Moved some of the currency helper functions out of the `subscriptions` app into `utils.billing` so they can be used in ecommerce workflows even if subscriptions are disabled.
* Set `PYTHONUNBUFFERED` and `PYTHONDONTWRITEBYTECODE` in docker compose file for python containers. (Thanks Richard for the suggestion!)
* Upgraded Django to 5.1.1.

#### Fixed

[Section titled “Fixed”](#fixed-6)

* Fixed a typo in the help text for the `bootstrap_ecommerce` command.
* Fixed a bug where `user_teams` context processor could cause a crash if auth middeware didn’t run (for example, on a 500 error page in production).

### Upgrade Notes

[Section titled “Upgrade Notes”](#upgrade-notes)

If you have existing `Purchase` data in your application you will need to migrate it to the new `ProductConfiguration` structure.

This is a three-step process:

First you will need to apply the database updates, but allow `Purchase.product_configuration` to be null. Instead of running `./manage.py migrate` you will have to run the following command:

```bash
./manage.py migrate ecommerce 0002
```

After running this, you can run the following command to migrate the existing data:

```bash
./manage.py migrate_ecommerce
```

The `migrate_ecommerce` management command will:

1. Create `ProductConfiguration` objects for all products in `settings.ACTIVE_ECOMMERCE_PRODUCT_IDS`
2. Create `ProductConfiguration` objects for all products referenced in existing `Purchase` models.
3. Set `purchase.product_configuration` to the new `ProductConfiguration` object for each `Purchase`.

Finally, you can make the `Purchase.product_configuration` field non-null, by running:

```bash
./manage.py migrate ecommerce 0003
```

**New projects, or projects without any existing purchase data can skip these steps and run `./manage.py migrate` directly.** However, you may still want to run `./manage.py migrate_ecommerce` to populate `ProductConfiguration` objects for your active products.

*Sep 17, 2024*

## Version 2024.8.2

[Section titled “Version 2024.8.2”](#version-202482)

This is a maintenance release that includes a number of mostly small fixes and updates, and updates Django to version 5.1.

### Fixed

[Section titled “Fixed”](#fixed-7)

* **Fixed a few styling issues on Bulma builds**:

  * Disabled dark mode. The styling for Dark mode was not fully supported by Bulma and led to strange-looking layouts.
  * Fixed an issue where the active tab wasn’t properly highlighted in certain cases on Bulma builds.

* Fixed an issue with sqlite builds where the default `DATABASE_URL` would cause the DB to switch to Postgres. (Thanks Harry and Richard for reporting!)

* Switched allauth from [Twitter](https://docs.allauth.org/en/latest/socialaccount/providers/twitter.html) (which seems no longer supported) to [Twitter Oauth2](https://docs.allauth.org/en/latest/socialaccount/providers/twitter_oauth2.html), which still works. (Thanks Bandi for reporting!)

* Fixed an issue introduced in version 2024.8 which caused Heroku Docker deploys to fail. Heroku [does not support caching](https://stackoverflow.com/a/78901250/8207), so it has been removed from Heroku Docker builds. (Thanks Richard for reporting!)

* Fixed a bug where the `team_nav_items.html` and `team_selector.html` templates could be accidentally included even if you built without teams.

* Changed the (unused) `text-muted` css class to `pg-text-muted` in a handful of places on Tailwind builds. (Thanks Peter for reporting!)

* Removed unused `AWS_S3_CUSTOM_DOMAIN` variable from `.env` files.

### Changed

[Section titled “Changed”](#changed-7)

* **Upgraded Django to version 5.1.**
* Upgraded all Python packages to their latest versions.
* Updated Pegasus color CSS variables to use the DaisyUI variables, so that they change when you change DaisyUI themes. (Thanks Peter for the suggestion!)
* Removed `custom.mk` if your project was not generated with a `Makefile`. (Thanks Finbar for reporting!)
* Removed “Containers started” message from `make start` command that never executed. (Thanks Richard for reporting!)
* Better style inputs of type `time` and `datetime-local` in forms on all CSS frameworks. (Thanks Peter for reporting and fixing!)
* Simplified Bulma navbar to use bulma native classes instead of custom CSS. (See upgrade note below.)
* Updated default Github repo in `app-spec.yml` to use raw project slug instead of the hyphenated version. (Digital Ocean deployments, only, thanks Richard for suggesting)
* Moved `SERVER_EMAIL` and `DEFAULT_FROM_EMAIL` from `settings_production.py` to main `settings.py` file, and made it possible to set them via the environment/`.env` file.
* Added many more common settings and secrets to the Kamal `deploy.yml` file.

### Documentation

[Section titled “Documentation”](#documentation-1)

* Improved the documentation on [customizing the Material Bootstrap theme](/css/material).
* Added documentation for [deploying multiple apps to the same VPS with Kamal](/deployment/kamal/#cookbooks).

### Upgrading

[Section titled “Upgrading”](#upgrading-9)

* Bulma builds may need to add the `is-tab` class to `navbar-items` in the top nav to mimic the updated navbar styling.

*August 23, 2024*

## Version 2024.8.1

[Section titled “Version 2024.8.1”](#version-202481)

This is a maintenance release which upgrades HTMX to version 2.0 and fixes a handful of minor bugs.

### Changed

[Section titled “Changed”](#changed-8)

* **Upgraded HTMX to [version 2.0](https://htmx.org/posts/2024-06-17-htmx-2-0-0-is-released/).** See upgrade note below.

### Fixed

[Section titled “Fixed”](#fixed-8)

* Fixed a bug on some environments where `make build-api-client` would wrong relative to the wrong directory. (Thanks Ben for finding and fixing!)
* Downgraded Postgres from 16 to 14 on Digital Ocean deployments, due to [an issue with permissions on version 16](https://www.digitalocean.com/community/questions/how-can-i-create-a-postgres-16-user-that-has-permission-to-create-tables-on-an-app-platform-dev-database) that was causing new Digital Ocean deployments to fail. (Thanks Panagiotis for reporting!)
* Switched the default celery pool to [solo](https://docs.celeryq.dev/en/stable/internals/reference/celery.concurrency.solo.html) in development, to fix issues running on Windows. See [updated docs](/celery).
* Updated in-app help hint to recommend running `./manage.py bootstrap_ecommerce` instead of `./manage.py djstripe_sync_models price`.

### Upgrading

[Section titled “Upgrading”](#upgrading-10)

Htmx 2.0 requires loading new extensions. If you were loading HTMX extensions in your own templates, you will have to upgrade the location of those to the 2.0 versions.

Before:

```html
<script src="https://unpkg.com/htmx.org/dist/ext/ws.js" defer></script>
```

After:

```html
<script src="https://unpkg.com/htmx-ext-ws@2.0.0/ws.js" defer></script>
```

*August 13, 2024*

## Version 2024.8

[Section titled “Version 2024.8”](#version-20248)

This is a maintenance release with many small updates and fixes.

### Added

[Section titled “Added”](#added-5)

* **Added test cases for subscription decorators, feature gating, and views.** These can be extended/adapted to test custom subscription logic. Also added utility functions to create test products, subscriptions and mock requests.
* Added a test that will fail if your project is missing any database migrations. [More on this concept here](https://adamj.eu/tech/2024/06/23/django-test-pending-migrations/).
* **Added an example landing page to Tailwind builds, based largely on [Scriv’s landing page](https://scriv.ai/).**
* Added `TURNSTILE_KEY` and `TURNSTILE_SECRET` to Kamal’s default secrets.
* Added a section on configuring static files to the [production checklist](/deployment/production-checklist/#check-your-static-file-setup).

### Changed

[Section titled “Changed”](#changed-9)

* **Code is now automatically formatted for all projects.** The “Autoformat code” check box has been renamed to “Enable linting and formatting” and now only controls whether `ruff` and the pre-commit hooks are included in the project download. Projects that had already enabled auto-formatting are unaffected by this change. (See upgrade notes below.)
* **The example landing pages are now used as the project’s landing page instead of being listed in the examples**. (Bulma and Tailwind builds only.)
* **Team invitation emails are now better styled, matching the same format as account emails.** (Thanks EJ for the suggestion!)
* The `EMAIL_BACKEND` setting is now configurable via an environment variable. Also, added a commented-out example of how to set email settings for a production email provider (Mailgun).
* Apt and pip packages are now cached across Docker builds, which should result in faster build times after the first build. (Thanks Tobias for the suggestion!)
* Improved the display format of “role” in the team invitation list. (thanks Andy for the suggestion!)
* Change `user/` to `YOUR_GITHUB_USERNAME/` in the Digital Ocean `app-spec.yml` file to make it more obvious that it should be edited. (Thanks Stephen for suggesting!)
* Changed the UI of social logins on the “sign in” page to match that of the “sign up” page on the Material Bootstrap theme. This makes the implementation more extensible and more consistent with other CSS frameworks.
* **Upgraded all Python packages to the latest versions.**

### Fixed

[Section titled “Fixed”](#fixed-9)

* Fixed a bug where the formatting `make` targets were still calling `black` and `isort` instead of `ruff`. `make black` is now `make ruff-format` and `make isort` is now `make ruff-lint`.
* Fixed a bug where the sign up view tests would fail in your environment if `settings.TURNSTILE_SECRET` was set. (Thanks Finbar for reporting!)
* Fixed translations on the user profile form field names.
* Removed `svg` as an option for profile picture uploads, to prevent the possibility of using it as an XSS attack vector. ([More info on this threat here](https://medium.com/@rdillon73/hacktrick-stored-xss-via-a-svg-image-3def20968d9)).
* Disable debug toolbar in tests, which fixes test failures under certain conditions.
* Bumped the Postgres version used by Digital Ocean deployments from 12 to 16. Digital Ocean has deprecated support for version 12. (Thanks Stephen for reporting!)
* Simplified how the list of social login buttons is rendered, and make social login buttons work when configuring social applications in settings (previously buttons only showed up if you configured apps in the database). See upgrade note below.

### Removed

[Section titled “Removed”](#removed-2)

* Deleted the “sticky header” html and CSS code that was only used on the example landing pages.

### Upgrade Notes

[Section titled “Upgrade Notes”](#upgrade-notes-1)

* If you had **not** been using auto-formatting until now, you should first follow the instructions for [migrating to auto-formatted code](/cookbooks/#migrating-to-auto-formatted-code) prior to upgrading to this release. Otherwise you will likely get a lot of formatting-related merge conflicts when trying to upgrade.
  * If you already enabled auto-formatting (most projects), you don’t need to do anything.
* If you had previously configured allauth social applications in the database *and* in your settings file, you may see a duplicate “Login with XXX” button on the sign up and login pages. To fix this, remove the social application from either your settings or the database.

*August, 7, 2024*

## Version 2024.6.1

[Section titled “Version 2024.6.1”](#version-202461)

This is hotfix release that addresses a few issues from yesterday’s update:

* Fix app styles accidentally being purged during the Docker build process. This caused styling on Docker-based deployments for tailwind builds. (Thanks Steve for reporting!)
* Moved channels url import to after Django initialization. This fixes an `AppRegistryNotReady` error when deploying asynchronous apps with the AI chat app enabled. (Thanks Roman for reporting!)
* Don’t create the periodic task to sync subscriptions unless per-unit billing is enabled.

*June 6, 2024*

## Version 2024.6

[Section titled “Version 2024.6”](#version-20246)

This is a feature release with a few big updates and a lot of smaller ones.

### AI model changes

[Section titled “AI model changes”](#ai-model-changes)

The library used for non-OpenAI LLMs has been changed from [`llm`](https://github.com/simonw/llm) to [`litellm`](https://docs.litellm.ai/docs/). Reasons for this change include:

* It has far fewer additional dependencies.
* It supports async APIs out of the box (for most models).
* The `llm` library is more targeted for the command line use-case, whereas `litellm` offers similar functionality as a native Python library with a cleaner API.

Litellm can still be used with all common AI models, including OpenAI, Anthropic/Claude, and local models (via ollama). For details on getting started with `litellm` see the updated [AI documentation](/ai/llms).

### Formatting and linting now use Ruff

[Section titled “Formatting and linting now use Ruff”](#formatting-and-linting-now-use-ruff)

Black and isort have been replaced with [ruff](https://github.com/astral-sh/ruff)—a Python linter/formatter that offers the same functionality as those tools but is much faster.

Additionally, Pegasus will now remove unused imports from your files automatically, both when building your project and if you have set up `pre-commit`.

This change should be a relatively seamless drop-in replacement, though you may see some new lint errors in your projects which you can choose to address.

### Spam prevention updates

[Section titled “Spam prevention updates”](#spam-prevention-updates)

There has been a dramatic increase in spam-bots over the last month. Many of these bots target seemingly-innocuous functionality like sign up and password reset forms.

This version includes a few updates to help combat these bots. First, you can now easily add [Cloudflare turnstile](https://www.cloudflare.com/products/turnstile/) to your sign up forms, which will present the user with a captcha and should help reduce bot sign-ups. See [the turnstile documentation](/configuration/#turnstile) for information on setting this up.

Additionally, the `ACCOUNT_EMAIL_UNKNOWN_ACCOUNTS` setting has been set to `False` by default. This prevents “forgot password” and “magic link” emails from being sent out to unknown accounts. It should also help reduce unnecessary email sending.

Finally, the [admin dashboard](#admin-dashboard) no longer shows users with unconfirmed email addresses if you have set `ACCOUNT_EMAIL_VERIFICATION = 'mandatory'`. This helps filter out likely bots from the report to provide clearer visibilty of people actually signing up for your app.

### Complete changelog

[Section titled “Complete changelog”](#complete-changelog-1)

Below is the complete set of changes in this release.

#### Added

[Section titled “Added”](#added-6)

* **Added configurable captcha support on sign up pages, using [Cloudflare turnstile](https://www.cloudflare.com/products/turnstile/).** See [the turnstile documentation](/configuration/#turnstile) for more information on setting this up. (Thanks Troy, Jacob, Robert and others for suggesting.)
* Added API views for two-factor authentication, and to change the logged-in user’s password. (Thanks Finbar for suggesting!)
* Add UI to tell users they need a verified email address prior to setting up two-factor auth.
  * Also added a `has_verified_email` helper class to the `CustomUser` model.
* Added tests for the delete team view for both team admins and members. (HTMX builds only)
* Added test for team member removal permissions.
* Add display and sort on the number of active members in the teams admin.

#### Fixed

[Section titled “Fixed”](#fixed-10)

* Fixed a bug where team names longer than 50 characters could cause a crash during sign up.
* Fixed a bug where multi-factor authentication QR codes had a dark background when dark mode was enabled (Tailwind builds only). (Thanks Artem for reporting!)
* Fixed a bug where it was possible to bypass two-factor-authentication when using the API authentication views. (Thanks Finbar for reporting and helping with the fix!)
* Fixed a bug where deleting the user’s only team while impersonating them resulted in a temporary crash. (Thanks EJ for reporting!)
* Fixed a bug where creating an API key crashed if your user’s first + last name combined to more than 40 characters. (Thanks Luc for reporting!)
* Improved the UI feedback when LLMs fail (e.g. if your API key is wrong or ollama is not running).
* Removed the `static/css` and `static/js` directories from the `.dockerignore` file so that other project files can be included in these directories. Also updated the production Docker build process so that any existing files are overwritten by the built versions. (Thanks Raul for reporting!)
* Made some performance improvements to the production Dockerfile build (don’t rebuild the front end if there are no changes in the dependent files).
* Better support trialing subscriptions with no payment methods. The subscription UI will now show the date the trial ends and won’t log errors about missing invoices. (Thanks Jarrett for reporting!)

#### Changed

[Section titled “Changed”](#changed-10)

* **Upgraded all Python packages to the latest versions.**

* **Upgraded all JavaScript packages to the latest versions.**

* **Non-OpenAI builds now use `litellm` instead of `llm`.** See above. (Thanks Sarthak for the suggestion!)

* **Changed the formatter/linter from `black` and `isort` to [ruff](https://github.com/astral-sh/ruff).** See above.

  * Also addressed a handful of minor linting errors that came up as a result of this change.
  * Codebase linting is now substantially faster.
  * Unused imports are now automatically removed when building your projects.

* **Celerybeat now uses the `django-celery-beat` library to store tasks in the database instead of on the filesystem.** This improves support for celerybeat on Docker-based platforms. (Thanks Peter and Artem for the suggestion!)
  * Also added a migration to save the default scheduled tasks in the database.

* The login API response has changed, to allow for two-factor auth prompts, and more machine-readable status fields.

* Removed the no-longer-used `use_json_field=True` argument from wagtail `StreamField`s.

* The admin dashboard no longer shows users with unconfirmed email addresses if you have set `ACCOUNT_EMAIL_VERIFICATION = 'mandatory'`.

* The admin dashboard now includes sign ups from the current date, by default.

* Changed behavior when team role checks fail from raising a `TeamPermissionError` to returning a 403 response, and updated affected tests. One side effect of this is that the stack traces are removed from successful test runs.

* Secret keys should no longer change every time you build your Pegasus project. They are also now clearly prefixed with `django-insecure-` to indicate that they should be changed in production.

* Updated the default OpenAI chat model to gpt-4o.

* Upgraded the openapi client generator to version 7.5.0 and also pinned the version used by `make build-api-client` to the same one.

* Team IDs are now optional on the create team page (HTMX builds only).

* Add clearer error message when charts are broken due to api config issue. (Thanks Yngve for reporting!)

* Added `assume_scheme="https"` to form `URLField`s to be compatible with Django 6 behavior.

* Added `FORMS_URLFIELD_ASSUME_HTTPS = True` to be compatible with Django 6 behavior.

* Set `ACCOUNT_EMAIL_UNKNOWN_ACCOUNTS = False` by default, so that “forgot password” emails do not get sent to unknown accounts. This can help prevent spam bots.

#### Removed

[Section titled “Removed”](#removed-3)

* Removed `black` and `isort` from dev-requirements, since they have been replaced by `ruff`.
* Removed `llm` library and associated code, since it has been replaced by `litellm`.
* Removed no longer used `TeamPermissionError` class.

#### Standalone front end

[Section titled “Standalone front end”](#standalone-front-end)

The following changes affect the experimental [standalone front end](/experimental/react-front-end):

* **The standalone React front end now supports two-factor-authentication.**
* Improve the UI when you have login issues in the standalone React front end.

*June 5, 2024*

## Version 2024.5.3

[Section titled “Version 2024.5.3”](#version-202453)

This is a hotfix release that fixes a bug where the landing and dashboard page image was accidentally removed if you built without the examples enabled.

*May 21, 2024*

## Version 2024.5.2

[Section titled “Version 2024.5.2”](#version-202452)

This is a hotfix release that fixes a bug that prevented the team management page from loading in certain browsers if you built with a React front end and with translations enabled. Thanks Finbar for reporting!

* Added `defer` keyword to various bundle scripts so they are loaded after the JavaScript translation catalog.
* Updated references to `SiteJS` to run on the `DOMContentLoaded` event to allow for usage of the `defer` tag.

*May 16, 2024*

## Version 2024.5.1

[Section titled “Version 2024.5.1”](#version-202451)

This is a hotfix release that fixes issues running the [experimental React frontend](/experimental/react-front-end) in Docker. Thanks Mohamed for reporting this!

* Fix `api-client` path in the frontend docker container and add to `optimizeDeps` in vite config.
* Mount `node_modules` as an anonymous volume in the frontend docker container, so it is not overwritten.
* Automatically create `./frontend/.env` when running `make init` if it doesn’t exist.

*May 14, 2024*

## Version 2024.5

[Section titled “Version 2024.5”](#version-20245)

This is a major release with several big updates. Here are a few highlights:

### New AI models

[Section titled “New AI models”](#new-ai-models)

In addition to using OpenAI chat models, you can now build the Pegasus AI chat applicaiton with the [`llm` library](https://github.com/simonw/llm). This lets you run the chat application against any supported model—including the Anthropic family (Claude 3), and local models like Llama 3.

Additionally, the image generation demo now supports Dall-E-3 and Stable Diffusion 3. For complete details, see the new [AI documentation](/ai/images).

### Health Checks

[Section titled “Health Checks”](#health-checks)

A new setting allows you to turn on health checks for your application, powered by [django-health-check](https://django-health-check.readthedocs.io/en/latest/). This will create an endpoint (at `/health` by default) that pings your database, Redis instance, and Celery workers and returns a non-200 response code if there are any identified issues.

These endpoints can be connected to a monitoring tool like [StatusCake](https://www.statuscake.com/) or [Uptime Robot](https://uptimerobot.com/) so that you can be alerted whenever your site is having issues.

See the section on [monitoring](/deployment/production-checklist/#set-up-monitoring) in the production checklist for more information.

### Allauth updates

[Section titled “Allauth updates”](#allauth-updates)

The [django-allauth](https://docs.allauth.org/en/latest/) library was updated to the latest version, which enabled several useful changes.

The first is a “sign in by email code” option which can be used in addition to the standard username/password and social option. Users can request a code be sent to their registered email and can then use that to login. See [the magic code documentation](/configuration/#enabling-sign-in-by-email-code) to enable/disable this.

The second is using the recent [multi-factor authentication](https://docs.allauth.org/en/latest/mfa/index.html) support added to allauth in favor of the third-party `django-allauth-2fa` library. This reduces dependencies and puts all of authentication functionality on a standard path moving forwards.

The complete release notes are below:

### Added

[Section titled “Added”](#added-7)

* **Added an optional health check endpoint at /health/.** (see above for details)
* **Added an option to connect the chatbot to other LLMs**. (see above for details)
* **The AI image generation now supports Dall-E 3 and Stability AI.**
* **All generated projects now include a `LICENSE.md` file.** The goal of the license file is not to change how Pegasus can be used in any way, but rather to document those terms in the codebase itself (previously they were only documented on the [terms page](https://www.saaspegasus.com/terms/)). For more information you can see the new [license page](https://www.saaspegasus.com/license/).
* **Added support for “magic-code login”, where a user can login to the site by requesting a code to their email address.** [Documentation.](/configuration/#enabling-sign-in-by-email-code)
* **Google cloud run builds now support Redis.** For details, see the [updated documentation](/deployment/google-cloud). (Thanks Forrest for suggesting!)
* Added a `custom.mk` file where you can add additional `make` targets without worrying about future Pegasus upgrades. (Thanks John for proposing this!)

### Changed

[Section titled “Changed”](#changed-11)

* Upgraded allauth to the latest version (0.62.1).
* **Migrated two-factor authentication from the third-party `django-allauth-2fa` to the `django-allauth` built-in implementation.** See upgrade notes below for migrating existing projects.
* Refactored how many allauth views work to be compatible with their new template override system.
* **Bootstrap and Bulma builds: Move sidebar navigation into the mobile menu instead of having it take up the top of the screen on mobile screens**, similar to how things already worked on Tailwind and Material. (Thanks Luc for the nudge!)
  * This includes splitting out the menu items into their own sub-template files so they can be included in both menus.
* Inline buttons are now spaced using the `gap` CSS property instead of the `pg-ml` class on individual buttons.
* `Alpine.start()` is now called on `DOMContentLoaded` loaded event instead of using `window.load`. This makes Alpine-powered UIs more responsive, especially when used on pages with lots of images.
* **Updated external JavaScript imports to use [the `defer` keyword](https://www.w3schools.com/tags/att_script_defer.asp) for slightly better page load performance.** (See upgrade note.)
  * Also updated inline JavaScript code in a handful of places to be compatible with deferred scripts.
* Added a Github logo to connected Github accounts on profile page.
* **The AI image demo and code has been moved to a first-class Pegasus application / tab.**
* Update the docker container registry used by Google Cloud to reflect the latest version in Google. Also push more Google Cloud configuration variables out of the Makefile and into the environment variables. (Thanks Erwin for reporting!)
* Added additional `.env` files to `.dockerignore` for Google Cloud builds.
* Bumped django to the latest `5.0.6` release.

### Fixed

[Section titled “Fixed”](#fixed-11)

* **SQLite build now properly parse `DATABASE_URL` if it is set. This fixes issues deploying to certain platforms when building with SQLite.** (Thanks Manasvini for reporting!)
* Updated allauth documentation links in the README to point to the new [allauth docs site](https://docs.allauth.org/). (Thanks Shantu for reporting!)

### Removed

[Section titled “Removed”](#removed-4)

* Removed several no-longer-needed allauth template files.
* Removed deprecated “version” field from the dev `docker-compose.yml` file. (Thanks Moyi for reporting!)
* Removed no-longer-used `pg-ml` css spacing class.
* Removed redundant type=“text/javascript” declarations from a few `<script>` tags.
* Removed unused HTMX script import from employee app demo page.
* Removed the no-longer-used `openai_example` app (functionality has been moved to `apps.chat` and `apps.ai_images`).
* Removed the no-longer-needed `AccountAdapter` class. This class was previously used to add two-factor support to login, which is now handled natively by allauth.

### Upgrading

[Section titled “Upgrading”](#upgrading-11)

**Two-factor authentication**

If you are using two-factor authentication you must run:

```bash
python manage.py migrate_allauth_2fa
```

Which will bring across existing device set ups and recovery codes. **If you don’t do this, you will remove two-factor-authentication configuration for all users who have set it up, compromising their security.**

**JavaScript defer changes**

The change of adding the `defer` keyword to `<script>` imports could have unintended consequences if you were relying on functions / functionality in your scripts being available on page load. This would most likely manifest as a browser JavaScript error of the form: `Uncaught ReferenceError: htmx/SiteJS/etc. is not defined`.

To resolve this, make sure all additional dependencies are also loaded with `defer` (for external scripts), or only referenced after the `'DOMContentLoaded'` event (for inline scripts). Alternatively, you can remove the `defer` keyword from the `<script>` tags in `base.html` or affected templates to restore the previous behavior.

*May 9, 2024*

## Version 2024.4.2

[Section titled “Version 2024.4.2”](#version-202442)

This is a maintenance release with a number of fixes and small changes. The most notable change is that the OpenAI chat example is now fully asynchronous.

### Added

[Section titled “Added”](#added-8)

* **Kamal deployments now support celerybeat for scheduled tasks out-of-the-box.** (Thanks Peter for the suggestion!)
* Added an example celerybeat configuration to the built-in examples.

### Changed

[Section titled “Changed”](#changed-12)

* **The websocket OpenAI chat example is now fully asynchronous.** This should substantially improve the number of concurrent sessions supported by the app.
* Use alpine to disable submit and clear input in the OpenAI chat example (thanks Artem for the suggestion!)
* Renamed “OpenAI Demos” tab to “AI Demos”.
* Renamed `get_chatgpt_response` task to `get_chat_response`.
* Change the default admin ordering for Users to date joined, descending.
* Google cloud builds only: `.env.production` is no longer included in Pegasus builds, since it was ignored by git. Instead `.env.production.example` is included. (Thanks Naveed for reporting!)
* Attach Stripe Customer to User/Team in `provision_subscription` function instead of the view, which makes it work in webhook processing as well.

### Fixed

[Section titled “Fixed”](#fixed-12)

* **Fixed a bug where non-admins of teams could not view their own team settings/members.** (Thanks Bernard for reporting!)
* Fixed a bug where deleted subscriptions with `canceled_at_period_end=True` could cause a crash when trying to view them. This bug would typically only manifest in test mode or if you manually deleted subscriptions in Stripe.
* Fixed a crash when looking up the currency for a deleted subscription.
* Added a constraint to the `Membership` model to disallow users being “added” to a team more than once. (Thanks Zac for reporting!)
* Fix typo instructing you to “comment out” mailgun settings instead of “uncomment” them. (Thanks Adam for reporting!)
* Google cloud builds only: added `--platform linux/amd64` to the `gcp-build` make target, to address [build/deploy issues from Mac M2s](https://stackoverflow.com/a/68766137/8207). (Thanks Naveed for reporting!)

### Documentation

[Section titled “Documentation”](#documentation-2)

* Improved the [instructions for running Kamal with Docker](https://docs.saaspegasus.com/deployment/kamal/#running-kamal-with-docker). Thanks EJ and Simon for the help with this!

*April 22, 2024*

## Version 2024.4.1

[Section titled “Version 2024.4.1”](#version-202441)

This is a hotfix/security release that fixes an issue where the `deploy/.env` file was not properly ignored by the `.dockerignore` when using Kamal deployment. This resulted in credentials being included in built Docker containers.

You are affected if you:

1. Deployed your application with Kamal.
2. Made your built Docker image publicly available.

If this is the case it is recommended to immediately upgrade and cycle any credentials that were listed in `deploy/.env`. Sorry about the inconvenience! Thanks to Denis for reporting and to Erwin for pointing out the security implications.

Note: if you’d like to patch this issue without upgrading, you can replace `.env` in your `.dockerignore` file with `**/.env`.

*Apr 17, 2024*

## Version 2024.4

[Section titled “Version 2024.4”](#version-20244)

There are two major updates in this release, a new websocket-based streaming chat UI, and upgrading Bulma to version 1.0.

### Streaming Chat UI

[Section titled “Streaming Chat UI”](#streaming-chat-ui)

The OpenAI Chat demo now streams responses in real time. This provides a much better user experience for chat applications, as the user doesn’t stare at a “loading” screen for a long time waiting for the complete response.

This feature is currently only supported on HTMX builds. It will be automatically enabled if you enable the “asynchronous” build option. If you do not enable async you will still be able to use the old UI.

You can watch a demo of this and learn how it’s built in this video: [Building a ChatGPT clone with Django, Channels, and HTMX](https://www.youtube.com/watch?v=8JSiiPW4S0A).

### Bulma upgrade to 1.0

[Section titled “Bulma upgrade to 1.0”](#bulma-upgrade-to-10)

[Bulma 1.0](https://github.com/jgthms/bulma/releases/tag/1.0.0) was released in late March and Pegasus has been updated to support it. The UI will change slightly but there should not be any breaking or substantial changes as a result of this upgrade. See details below.

### New

[Section titled “New”](#new)

* **OpenAI Chat demo now supports streaming responses.** This is only turned n for HTMX builds with asynchronous support enabled. Big thanks to Artem for the implementation support!

### Updated

[Section titled “Updated”](#updated-1)

* **Upgraded Bulma to 1.0.** Related changes (bulma builds only):

  * Switched all variables from Sass variables to CSS variables.
  * Updated syntax of all responsive CSS to use `@include mixins` instead of `+from`, `+until`, etc.
  * Switched how bulma is initialized from `@import` to `@use`.
  * Removed some unnecessary variable declarations from `site-bulma.scss`

* **Upgraded other JavaScript packages to their latest versions.**

* Upgraded Django to 5.0.4

### Fixed

[Section titled “Fixed”](#fixed-13)

* Fixed a bug where the standalone front end Dockerfile did not install the right dependencies. In some cases, this caused the front end to not start properly.
* Fixed a bug where viewing a non-existent team would cause a 500 error instead of a 404.
* Removed some unused code in the OpenAI chat example if you were building with React.

*April 5, 2024*

## Version 2024.3

[Section titled “Version 2024.3”](#version-20243)

This is a big feature release! The main goal of the release is to make it easier to use Pegasus with separate front ends and mobile applications. Here are the highlights:

### API Authentication and JWT support

[Section titled “API Authentication and JWT support”](#api-authentication-and-jwt-support)

Pegasus now optionally includes API endpoints for registering, authenticating and verifying users (via JSON web tokens or JWT). This provides all the pieces needed to make your Pegasus application a backend to a standalone front end, for example a React or Next.js SPA, or a mobile application.

You can read more about this feature in the [Authentication API documentation](/apis/#authentication-apis).

### Standalone React (Vite) Front End (Experimental)

[Section titled “Standalone React (Vite) Front End (Experimental)”](#standalone-react-vite-front-end-experimental)

In addition to the authentication API support, Pegasus now includes an optional standalone React demo application built with React, [Vite](https://vitejs.dev/) and [React Router](https://reactrouter.com/en/main).

The demo application includes sign up and login workflows, helper components to manage authentication and protected routes, and a port of the employee demo application (using the same code as the Pegasus version).

You can watch a demo below and learn more about it in [the React front end documentation](/experimental/react-front-end).

### Teams Navigation Updates

[Section titled “Teams Navigation Updates”](#teams-navigation-updates)

Application navigation now uses a new team selector component. This allows users to quickly see their team list and switch between teams directly from any page. Team management has also been moved under this component, and the previous team section of the navigation was removed.

### Complete release notes

[Section titled “Complete release notes”](#complete-release-notes)

#### Added

[Section titled “Added”](#added-9)

* **API Authentication and JWT support.** See above.
* **An Experimental Standalone React (Vite) Front End**. See above.

#### Changed

[Section titled “Changed”](#changed-13)

* **Team navigation overhaul**. See above.

* **Made changes to the Employee demo app to support being shared with the standalone front end.**

  * Move `BrowserRouter` declaration outside the `EmployeeApplication` component so the routes can be used in different routers.
  * Change all `Link` and `Route` declarations in `EmployeeApplication` to be relative paths instead of absolute.
  * Pass image references into the app as props instead of relying on an externally defined constant (`STATIC_FILES`). This allows the application to be served from multiple URL endpoints without modification.
  * Pass `urlBase` to the nested components, so that they can route back to different paths (e.g. when employees are saved).
  * Switch the department choice field from a passed-in `EMPLOYEE_DEPARTMENT_CHOICES` data structure to the `DepartmentEnum` object that is included with the API client.
  * Change file extension for several components from `.js` to `.jsx`.

* **Made changes to the JavaScript api client to support being shared with the standalone front end**

  * **Moved the api-client from `assets/javascript/api-client` to an `api-client` folder in the root of the repository.**
  * **The api client is now installed as a linked local dependency in `package.json` instead of referenced as part of the code.** This makes it easier to move the api client code or install it as a hosted npm package. Also updated all references to the api-client to reflect this change.
  * Renamed the `api-client` make target to `build-api-client` to avoid conflicting with the filesystem folder.
  * **The API client is now built dynamically, just in time, when you create your project. Also updated the API client version to 7.4.0.** This may result in slight differences in generated API client code, but the resulting code should be *more* correct and there should not be any breaking changes to existing Pegasus functionality.

* Be more explicit in the webpack config about using babel-loader presets instead of relying on `babelrc`

* Exclude frontend from the base type check config in `tsconfig.json`. The front end is checked independently.

* Auto-size the navigation column in `app_home.html` (Bootstrap builds only).

* Make ALLOWED\_HOSTS configurable by environment variables in both dev and production. (Thanks Shawn for suggesting)

* **Removed `.env.docker`. Docker development environments are now managed by `.env` (same as native environments).** Also updated the documentation on this.

* Added a search input to Team admin UI.

* Added a `signup_closed.html` template which improves the styling of the “signups closed” page if you turn off public signups. (Thanks EJ for the suggestion!)

* Added an `account_inactive.html` template which improves the styling of the “inactive account” page if an inactive user tries to login. (Thanks Lauren for the suggestion!)

* Improved the contrast on help text in dark mode. (Tailwind builds only)

* Changed the main icon on the landing page and dashboard from the old rocket to the current SaaS Pegasus rocket.

* Added a “Built with SaaS Pegasus” line to the default generated footer.

* Bump Django to latest 5.0.3 release.

#### Fixed

[Section titled “Fixed”](#fixed-14)

* Fixed hard-coded reference to the Pegasus dev project in Google Cloud media configuration in `settings_production.py`
* Fixed a bug where the two-factor QR codes were very difficult to scan in dark mode. (Tailwind builds only)
* Made certain account pages (password reset, two-factor auth, etc.) darker in dark mode. (Tailwind builds only)
* Removed a redundant check for empty subscription from `view_subscription.html` (thanks Rob for reporting!)
* Fixed a bug that caused errors displaying prices in secondary currencies if they prices had decimals in them. (Thanks Matthew for reporting and the fix!)
* Fixed team signup test if you have disabled signups. (Thanks Saif for reporting and proposing the fix!)
* Fixed a bug where links to the user dashboard were accidentally missing if you disabled user impersonation. (Thanks Simon for finding!)

### Upgrade notes

[Section titled “Upgrade notes”](#upgrade-notes-2)

If you are using Docker in development you might need to move/copy your `.env.docker` file to `.env` when you update your project.

*Mar 22, 2024*

## Version 2024.2.4

[Section titled “Version 2024.2.4”](#version-202424)

This is another minor hotfix release. Details:

* Fixed Google Cloud `Makefile` targets to use the built project’s ID instead of the Pegasus development project’s ID. (Thanks Daan for reporting!)
* Minor changes to `fly.toml` to fix errors on certain environments/versions. (Thanks Denis for reporting!)

*Feb 26, 2024*

## Version 2024.2.3

[Section titled “Version 2024.2.3”](#version-202423)

This is a hotfix release that restores the `deploy/` folder that was accidentally not present on certain Google Cloud builds. *Thanks Yogesh for reporting!*

*Feb 24, 2024*

## Version 2024.2.2

[Section titled “Version 2024.2.2”](#version-202422)

This is a big Pegasus release with a new Github integration for creating and upgrading projects, as well as an overhaul of the Google Cloud deployment support and many small updates and fixes from the community.

### New Github distribution model

[Section titled “New Github distribution model”](#new-github-distribution-model)

You can now create and upgrade your projects directly on Github! This is a much smoother experience than the previous zip file model (which is still available). You can also connect an existing project to Github by following the [instructions here](/github/#connecting-an-existing-project-to-github).

For more details see the screencast below, and the updated [Getting Started](/getting-started) and [Upgrading](/upgrading) pages.

A few code changes were needed to support this workflow (in particular, it’s no longer possible to deliver files which were in the `.gitignore` file):

* Pegasus no longer ships with a `.env` or `.env.docker` file and instead these must be created from `.env.example`.
* `.env.example` will now use Docker-based URLs for your Postgres and Redis database if you build with Docker enabled.
* Added `make setup-env` command to create your `.env.docker` file from `.env.example`.
* Updated the `make init` create your `.env.docker` file if it doesn’t already exist.
* Updated the setup documentation to reflect the above changes.

### Overhauled Google Cloud Deployment

[Section titled “Overhauled Google Cloud Deployment”](#overhauled-google-cloud-deployment)

The Google Cloud deployment support has been completely overhauled and brought in line with other deployment plastforms. These are the major changes (affecting Google Cloud deployments only):

* Updated the Google Cloud set up and [setup documentation](/deployment/google-cloud) based on the latest Google guide.
* Google Cloud now uses the same Dockerfile as other deployment options.
* Google Cloud now uses whitenoise for Static files, the same as other deployment options. It still uses Google Cloud Storage for media files.
* Added `Makefile` targets for Google Cloud options for building, pushing, and deploying.
* Deleted legacy `cloudmigrate.yaml` and `cloud_run.sh` files.
* Simplified the `prod-requirements.in` file.
* Fixed a bug where uvicorn was not correctly installed in production for async builds.
* Fixed various settings to work with the latest Google Cloud guides and best practices and simplified many of the other settings.
* Updated the Django storages set up for the latest Django 4.2 / 5.0 settings.

*Big thanks to Conrad, Rob, Troy, and Nathan for helping find and work through these changes.*

### Other Fixes

[Section titled “Other Fixes”](#other-fixes-2)

* Include djstripe webhook url endpoints if building with ecommerce and not subscriptions. (Thanks Emiliano for reporting!)
* Fixed a bug where a Social App in the database for a provider that was not configured would cause a crash.
* Fixed a bug where teams tests would fail if `ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE` was enabled. (thanks Saif for reporting and the fix!)
* Fixed a bug where social button icons would not work with manifest file storage.

### Other Changes

[Section titled “Other Changes”](#other-changes-6)

* Updated most `make` targets that run commands in Docker to not require the `web` container to be running. They will now spin up and remove temporary containers instead. (Thanks Artem for the suggestion!)
* Slightly improve styling of page that shows when there are social authentication errors (thanks Finbar for the contribution!)
* Make `USE_HTTPS_IN_ABSOLUTE_URLS` setting configurable via an environment variable.
* (Render only) Make the casing of booleans in `render.yaml` consistent.
* (Kamal only) Added more environment variable declarations to the default Kamal setup.
* (fly.io only) Overhauled the `fly.toml` deployment file to be consistent with fly’s latest format and removed unnecessary parts.
* (Bulma only) updated the sign up form so that the password(s) come before the team name to be consistent with other CSS frameworks.
* (Bulma only) allow changing the email address you sign up from when accepting a team invitation.

### Documentation updates

[Section titled “Documentation updates”](#documentation-updates)

* Overhauled [Google Cloud setup docs](/deployment/google-cloud).
* Added Github instructions to [upgrading documentation](/upgrading).
* Added Github instructions to [getting started](/getting-started).

*Feb 21, 2024*

## Version 2024.2.1

[Section titled “Version 2024.2.1”](#version-202421)

This release fixes the OpenAI demo to be compatible with the latest Python library:

* Fix ChatGPT example to work with latest OpenAI API.
* Fix Dall-E example to work with latest OpenAI API.
* Update a Github action to latest version that was missed in the last release.

*Feb 5, 2024*

## Version 2024.2

[Section titled “Version 2024.2”](#version-20242)

This release adds Django 5.0 support, upgrades all dependencies to their latest versions, and includes a handful of other changes.

Details:

* **Support Django 5.0.** Django 4.2 LTS should also work, but 5.0 will be the default version tested and used moving forwards.
* **Upgraded all Python dependencies to their latest versions.**
* **Upgraded all JavaScript dependencies to their latest versions.**
* Upgraded all Github actions to use latest versions.
* Simplified the process for building the front end API client with Docker (thanks Finbar for the pointer!). [Api client docs](/apis/#generating-the-api-client) have been updated as well.
* Update links to all Django documentation to link to the latest stable release, instead of a specific version.
* Fixed a schema warning for the user signups dashboard API.
* Update link to the guide to celery progress bars to the new blog post url.
* Simplified the process of setting up your ecommerce config to a new management command: `./manage.py bootstrap_ecommerce`.
  * Also refactored related code to be shared between ecommerce and subscriptions.
* Added `subscription_is_active` helper function, to remove duplicate code that was running the same check. Also updated [the documentation](/payments/#set-up-your-development-environment).
* Fixed a bug where if you marked a subscription to be canceled at the period end and weren’t running webhooks, the subscription page would crash.
* Added `staff_member_required` decorator to all superuser-only views, to ensure that the user is also active, and staff. (Thanks Felipe for the suggestion!)
* Removed `tailwindcss/forms` plugin, which conflicted with some default DaisyUI form elements and wasn’t needed. (thanks Artem and Alex for the suggestion!)
* Added better styling for the socialaccount connections page. (thanks Finbar for the contribution!)

*Feb 2, 2024*

## Version 2024.1.2

[Section titled “Version 2024.1.2”](#version-202412-1)

This is a minor/hotfix release that fixes a few issues related to fly.io deployments due to changes in the default values used by fly. It also updates the [fly documentation](/deployment/fly) to use the latest `flyctl` workflow for launching new applications.

*Thanks to Naveed for reporting this.*

*January 15, 2024*

## Version 2024.1.1

[Section titled “Version 2024.1.1”](#version-202411-1)

This is a minor/hotfix release that disables self-hosting media files with Kamal deployment, since this wasn’t working well for production environments.

For now it is recommended to use S3 to host media files with Kamal, though this may change in the future.

To get the hotfix without upgrading you can just remove these two lines from your `deploy.yml` file:

```yaml
volumes:
  - "{your-app-slug}-media:/code/media"
```

*January 9, 2024*

## Version 2024.1

[Section titled “Version 2024.1”](#version-20241)

This is a minor/hotfix release with some small updates/fixes to the group chat UI and Kamal deployment:

* Fixes an issue where there were missing templates if you installed with asynchronous support and without OpenAI. (Thanks Jose for reporting!)
* Chat templates have now been moved to `web/chat` so it is clear they can be re-used across apps.
* Added tests that would have caught the above issue.
* Renamed `TestLoginRequiredView` to `TestProfileViews` to be more clear what it is doing.
* Bumped Django to the latest 4.2.9 bugfix release.
* Don’t run Celery with gevent in Kamal deployments, since it is not necessary and not always installed. (Thanks Luis for reporting!)
* Use `settings_production` in Kamal deployments by default, instead of requiring manually setting the environment variable. (Thanks Luis for reporting!)

*January 3, 2024*

## Version 2023.12.1

[Section titled “Version 2023.12.1”](#version-2023121)

This hotfix release changes the `multiarch` value in Kamal deploys to `true`, which fixes errors when deploying from Mac / Windows machines to Linux servers (thanks Luis for reporting). There was also an overhaul of the [Kamal docs](/deployment/kamal).

If you want the hotfix without upgrading, you can just set `multiarch: true` in the `builder` section of your `deploy.yml` file.

*December 20, 2023*

## Version 2023.12

[Section titled “Version 2023.12”](#version-202312)

The big update in this release is official support for deploying Pegasus apps onto any linux server. This allows you to deploy Pegasus apps onto any VPS, like Linodes, Digital Ocean Droplets, or Amazon EC2 / Lightsail instances. The deployment uses Docker containers, managed using [Kamal](https://kamal-deploy.org/). You can deploy your entire application onto a single server (the default), multiple servers, or mix-and-match between self-hosted and managed services (e.g. Amazon RDS) with an easily customizable configuration.

For more details, see the new [Pegasus Kamal documentation](/deployment/kamal).

Below are the complete release notes:

### Added

[Section titled “Added”](#added-10)

* **Added support for deploying to any linux server using the new Kamal deployment option. [Documentation](/deployment/kamal).**
* **Added first-class support for “login with Github.”**
* Added a basic `.dockerignore` file.
* Added an optional argument to `make npm-install` for installing individual packages, and added a `make npm-uninstall` target for uninstalling packages. (Thanks Gary for the suggestion/contribution!)

### Changed

[Section titled “Changed”](#changed-14)

* **Load `request.team` in `TeamsMiddleware` even if the user doesn’t have access to the team if `team_slug` is passed to the view. Since authorization is done in the view decorators like `login_and_team_required` this should be safe, and makes it easier to create team views that don’t require authentication.**
  * Also updated tests to reflect this new behavior.
* Only show social apps which have been created in the database on the sign up and login pages, and clean up/standardize how social app code/buttons are added.
  * Also switch social logins to use POST and remove `SOCIALACCOUNT_LOGIN_ON_GET = True` from settings.
* **Add a `customer` object to the `CustomUser` model when ecommerce is enabled, and re-use the same customers when a user makes multiple purchases.**
* Silence `dj-stripe` warning about Stripe keys being kept in settings. This is standard practice for Pegasus applications.
* Mock out JavaScript translations and remove translation-based views when building without translations enabled. This should slightly improve page-load times when not using translations.
* Explicitly set `DEBUG=False` in the Render production environment.
* Explicitly set default region on fly.io deployments.
* Changed postgres connection strings from `postgres://` to `postgresql://`. Either one works in Django, but only the latter works with sqlalchemy, so using it allows the same connection string to be used with both tools.
* **Upgraded everything to run Node 20 instead of Node 18.**
* **Upgraded the base Docker images from bullseye (Debian 11) to bookworm (Debian 12).**
* **Overhauled the production Docker setup to use a [multi-stage build](https://docs.docker.com/build/guide/multi-stage/). This should allow for faster build times (partial builds can run in parallel) as well as faster rebuild time, as more steps are able to be cached more often.**
* Profile picture media files are now deleted when the associated user is deleted.
* Default the `PORT` variable used by django in production deployments to `8000` if not specified in the environment.
* Changed django database engine from `django.db.backends.postgresql_psycopg2` to `django.db.backends.postgresql` (these behave the same, but the latter is now recommended).

### Fixed

[Section titled “Fixed”](#fixed-15)

* Fixed description of `dev-requirements.txt` to indicate it installs development, not production requirements. (Thanks Yngve for reporting!)
* Fixed 500 error when trying to accept an invitation that was already accepted.
* Removed duplicate DB lookups on invitation acceptance page.
* Set avatar image filenames to be randomly generated. This fixes an issue where, under certain media configurations, uploaded profile pictures with the same filename could “clobber” each other.
* Fix test failures when manifest storage was configured, by overriding the `STORAGES` setting in affected tests.
* Fixed 500 error when attempting to manage social app connections from the profile page, due to extending a deleted `allauth` template.
* Attempt to add more `INTERNAL_IPS` to `settings.py` when using Docker in development, to get Django debug toolbar to show up. (Thanks Artem for reporting/contributing!)
* Fixed issue with missing `$PORT` reference caused fly.io deployments to sometimes fail.

### Removed

[Section titled “Removed”](#removed-5)

* Removed migration to auto-create social apps in the database.
* Cleaned up template imports in a few places.

### Upgrade notes

[Section titled “Upgrade notes”](#upgrade-notes-3)

The `TeamsMiddleware` change may change the access rules of views that were relying on the absence of `request.team`, to control authorization, instead of using `login_and_team_required` or similar approaches.

The removed migration file (`/web/migrations/0002_create_allauth_providers.py`) should not be removed if you have already run the migration on your environment. Keeping it in the repository won’t do any harm.

*December 12, 2023*

## Version 2023.11.1

[Section titled “Version 2023.11.1”](#version-2023111)

This is a hotfix release that fixes an issue with calling dj-stripe’s `get_subscriber_model` utility when teams were enabled by adding an `email` property to the `Team` object. The `email` property was accidentally not added for certain build configurations.

You can manually apply this change by adding the following property to the `Team` model, in `apps/teams/models.py`:

```python
@property
def email(self):
    return self.membership_set.filter(role=roles.ROLE_ADMIN).first().user.email
```

Thanks to Charley and Emilien for reporting!

*Nov 10 2023*

## Version 2023.11

[Section titled “Version 2023.11”](#version-202311)

This is a hotfix release that fixes the Node.js docker installation according to [these nodesource changes](https://github.com/nodesource/distributions#new-update-%EF%B8%8F).

You can also manually apply this change by replacing the current node installation steps with the following code in your `Dockerfile.dev` and `Dockerfile.web`.

```plaintext
# install node/npm
RUN curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | \
    gpg --dearmor -o /usr/share/keyrings/nodesource.gpg


RUN echo \
  "deb [signed-by=/usr/share/keyrings/nodesource.gpg] https://deb.nodesource.com/node_18.x nodistro main" | \
  tee /etc/apt/sources.list.d/nodesource.list && \
    apt-get update && \
    apt-get install nodejs -yqq
```

Thanks to Finbar on Slack for reporting and suggesting the fix!

*November 1, 2023*

## Version 2023.10.1

[Section titled “Version 2023.10.1”](#version-2023101)

This is a minor release addressing a few small issues raised in the `2023.10` release.

* **Upgrade docker containers from `python:3.11-buster` to `python:3.11-bullseye`. This change substantially improves performance on certain Mac builds.**
* Upgrade django to the latest 4.2.6 security release.
* Reduce db queries on the e-commerce home page.
* Don’t show “buy” links on the e-commerce page if the products do not have a default price set.
* Change default value of `ALLOWED_HOSTS` to `["*"]` and allow overriding it via an environment variable.
* Clean up whitespace in `user_dashboard.html`.

*Oct 9, 2023*

## Version 2023.10

[Section titled “Version 2023.10”](#version-202310)

This is a major release with three big updates: Async/Websocket support, an E-Commerce application, and an admin user dashboard.

### Async / Websocket support

[Section titled “Async / Websocket support”](#async--websocket-support)

Pegasus now supports asynchronous Django and Websockets. Included is an example group chat application that leverages these capabilities. Watch the video below for more details, or see the new [async / websocket documentation](/async):

### E-Commerce (One-Time Payment) Application

[Section titled “E-Commerce (One-Time Payment) Application”](#e-commerce-one-time-payment-application)

The previous Stripe Payments example has been converted into a full-blown E-Commerce store. You can manage your products in Stripe and sync them to your application with a few lines of configuration. Customers can purchase specific items and everything is linked to your Stripe dashboard.

Watch the video for more details, or see the new [E-Commerce documentation](/payments)::

### Admin Dashboard

[Section titled “Admin Dashboard”](#admin-dashboard)

An admin-facing dashboard has been added. The dashboard lets you see User sign ups to your application over time, and is filterable by date range. It’s a useful tool to see how your app is growing, and a good launching point for building out more dashboard capabilities.

Screenshot:

![Admin Dashboard](/_astro/user-dashboard.BjBCLGZd_Z1IuCIF.webp)

Below are the complete release notes including several other substantial changes and supporting work for the above.

### Added

[Section titled “Added”](#added-11)

* **Added asynchronous and websocket support via a new build option.** [Documentation](/async).

  * **Related: Added the group chat example application if you enable asynchronous support.**
  * Related: Added `websocket_reverse` and `websocket_absolute_url` helper functions and tests.
  * Related: Added `.pg-message-sender` helper CSS class.
  * Related: If building with async your app will use `asgi` instead of `wsgi`.

* **Added the E-Commerce example application via a new build option.** [Documentation](/payments).

* **Added the admin dashboard.**
  * Related: Added an admin-only user signup API

* Added a `pg-link` helper class to style links (especially on Tailwind and Material builds). Also applied this style to a few places.

* Added basic tests for some of the example views.

* Added an example of customizing existing DaisyUI themes to the [Tailwind docs](/css/tailwind).

* Added `absolute_url` template tag for generating full URLs in e.g. email templates, and added tests for it.

### Changed

[Section titled “Changed”](#changed-15)

* **Added the `feature_gate_check` and `get_feature_gate_check` helper functions, for more fine-grained control of feature gate checking.** See the updated [feature-gating documentation](/subscriptions/#feature-gating) for more information.
  * Related: Modified the `active_subscription_required` decorator to use this function.

* Reduced number of DB queries made when provisioning a subscription.

* Made subscription provisioning an atomic action to reduce race conditions between Stripe Checkout callbacks and webhooks.

* Stripe subscription webhooks now explicitly only process checkout sessions that were created by the subscriptions application. This was done to enable apps to handle both e-commerce and subscription payments, and is handled by adding (and checking) a “source” value on the checkout session metadata.

* Created a `TestLoginRequiredViewBase` base test class, to test logged-in views, and updated existing tests to use it.

* Removed uppercase characters from `TestLoginRequiredView` test methods.

* Upgraded Chart.js to the latest version, and moved it to be installed from NPM instead of a CDN.

* Changed the example charts to use the NPM-installed Chart.js.

* Moved `get_stripe_module` to `apps.utils.billing` so it can be used by the e-commerce app and subscriptions.

* **Upgraded `django-allauth` to latest version (0.57.0).**

  * Related: Added a migration to create default `SocialApp` models for all enabled providers, otherwise the signup and login pages crash.
  * Related: Blank out help-text on the sign up form’s password input.
  * Related: Added `allauth.account.middleware.AccountMiddleware` to `MIDDLEWARE`
  * Related: Fixed links to allauth docs in the generated README file.

* Upgraded Django to the latest 4.2.5 security release.

* Set `DEBUG=False` when running `collectstatic` on production Docker builds.

* Added some fields to the default `CustomUserSerializer`.

* Added `created_at` field to chat message admin list display / list filter.

* Removed some unused imports from subscription views.

* Refactored chat message list into a standalone template.

### Fixed

[Section titled “Fixed”](#fixed-16)

* Fixed absolute paths to Android-specific favicons to be relative. (Thanks Alexander for reporting!)
* Fixed issue where mobile menu content sometimes did not appear in front of page content on Tailwind builds.
* The object lifecycle home example view now requires login.
* Fixed issues with calling dj-stripe’s `get_subscriber_model` utility when teams were enabled, by adding an `email` property to the `Team` object, and implementing `DJSTRIPE_SUBSCRIBER_MODEL_REQUEST_CALLBACK`, and added a test case that confirms this works moving forwards.
* Fix styling of date inputs on all CSS frameworks.
* Fixed tab highlighting of the “impersonate a user” navigation on the Bootstrap Material theme.

### Removed

[Section titled “Removed”](#removed-6)

* **Removed the previous Payments example.** Apps should refer to the new E-Commerce app to use one-time payments.

  * Related: Removed all migrations from the example app, which now has no models.
  * Related: Removed the previous Payments documentation.

* Removed the “removing Stripe” cookbook from the documentation. Stripe is no longer included unless you build with the E-Commerce example or Subscriptions enabled.

### Upgrade Notes

[Section titled “Upgrade Notes”](#upgrade-notes-4)

* To migrate an existing application to use asynchronous / websockets, you will have to set `DEBUG` in your production *environment* (not `settings_production.py`). More information in the [async documentation](/async).

*Oct 4, 2023*

## Version 2023.9.2

[Section titled “Version 2023.9.2”](#version-202392)

This is a hotfix release that bumps `django-environ` from `0.11.1` to `0.11.2` which fixes an issue with ”$” in certain situations in environment variables. [details](https://github.com/joke2k/django-environ/issues/490)

Thanks Geoff for reporting!

*Sep 22, 2023*

## Version 2023.9.1

[Section titled “Version 2023.9.1”](#version-202391)

This is a hotfix release with a few small fixes and updates:

* Updated the version of `celery[redis]` to `5.3.4` since `5.3.3` was inexplicably deleted from PyPI.
* Fixed a crashing issue on the two-factor auth configuration pages caused by the recent `allauth-2fa` update. (Thanks Matthew for reporting and suggesting the fix)
* Added tests for a few logged-in views, including one that would have caught the two-factor issue above.
* Properly show errors if you enter the wrong two-factor token when trying to remove two-factor auth from your account.

*Sep 18, 2023*

## Version 2023.9

[Section titled “Version 2023.9”](#version-20239)

2023.9 has two main updates: Stripe embedded pricing table support, and a substantially improved Wagtail experience.

### Stripe Embedded Pricing Table

[Section titled “Stripe Embedded Pricing Table”](#stripe-embedded-pricing-table)

This release adds support for [Stripe’s embedded pricing table](https://stripe.com/docs/payments/checkout/pricing-table), which is a far simpler alternative to creating a pricing page than doing it natively in your application.

The pricing table was added as a new build configuration option. Once enabled, the previous subscription UI will be replaced by Stripe’s UI, and all changes to the pricing table can be made directly within Stripe.

The pricing table option opens up a number of new billing options, including multi-currency support and free trials, though it does not support per-unit billing very well. For complete details, see the [updated subscription documentation](/subscriptions).

### Wagtail Enhancements

[Section titled “Wagtail Enhancements”](#wagtail-enhancements)

The big Wagtail change is that most content pages now use Wagtail’s `StreamField` instead of `RichTextField`. This allows you to stitch together arbitrary blocks of content in all your pages, instead of being forced into a single rich text model. It also enables re-use of individual structured components. You can [read more about Wagtail `StreamField` here](https://docs.wagtail.org/en/v5.1.1/topics/streamfield.html).

There were also several smaller improvements.

*If you’re upgrading from a previous version, see the upgrading notes below.*

### Complete release notes

[Section titled “Complete release notes”](#complete-release-notes-1)

#### Added

[Section titled “Added”](#added-12)

* **Stripe: Added embedded pricing table support, via a new build option.**
* Wagtail: Added `social_image` field to all content models (using `BaseContentPage`), so you can define a custom image to use for `og:meta` tags for any individual page.
* Wagtail: Added a `CaptionBlock`, for captioning images or code, which you can use as a reference to add additional block types to your app.
* Wagtail: Added a migration to port previous `RichTextField`s to `StreamField`s.
* Added tests for `get_image_url` template tag.

### Changed

[Section titled “Changed”](#changed-16)

* **Wagtail: Migrated `ContentPage.body` and `BlogPage.body` to use `StreamField` instead of `RichTextField`. This provides much more flexibility in laying out your pages and working with many different section types.**
* Wagtail: All content models now extend from `BaseContentPage` so that you can add fields that should be shared among all your different types of content.
* Wagtail: Updated the `bootstrap_content` management command to be compatible with the new structure.
* **Upgraded nearly all Python packages to their latest versions.** `django-allauth` was not upgraded, due to it having a large release just a few days ago.
* **Upgraded all JavaScript packages to their latest versions.**
* **Subscriptions: official support for multiple currencies ([docs](/subscriptions/#supporting-multiple-currencies)) (Stripe pricing-table only)**
* **Subscriptions: official support for free trials ([docs](/subscriptions/#free-trials))**
* **Subscriptions: Overhauled the [Subscriptions documentation](/subscriptions) to make it clearer, and add the new pricing UI setting.**
* Subscriptions: Moved the `checkout_success` endpoint to be a global `confirm` endpoint instead of a team-specific endpoint.
* Subscriptions: Improved display of subscription price line items when using metered billing.

### Fixed

[Section titled “Fixed”](#fixed-17)

* Subscriptions: Fixed bug that caused trialing subscriptions to not be counted as active.
* Subscriptions: Show the correct currency in subscription details page if using Stripe’s [multi-currency support](https://stripe.com/docs/payments/checkout/present-local-currencies?platform=multi-currency-prices). (Thanks Mario for reporting.)
* Fixed bug in `get_image_url` template tag that prevented it from properly resolving relative media URLs. Also added tests for this case.
* Updated the `bootstrap_subscriptions` management command to be compatible with the latest version of `dj-stripe`.
* Fixed a bug where the active products API would always crash if you had not defined `ACTIVE_PRODUCTS`

### Removed

[Section titled “Removed”](#removed-7)

* Removed no-longer-supported `DJSTRIPE_USE_NATIVE_JSONFIELD` setting.

### Upgrade notes

[Section titled “Upgrade notes”](#upgrade-notes-5)

It is recommended to read through [the dj-stripe 2.8 release notes](https://github.com/dj-stripe/dj-stripe/releases/tag/2.8.0) to confirm you aren’t affected by any backwards-incompatible changes.

Customers switching to the new Stripe embedded pricing table will need to move any product information (including names, descriptions and feature lists) from `metadata.py` into their Stripe product and pricing page configuration.

Customers upgrading from existing wagtail installations that have been customized may need to do additional work to update their content models to StreamFields. Look at the `0002_convert_stream_fields.py` migration and apply the same pattern to any other fields you want to migrate.

*September 1, 2023*

## Version 2023.8.2

[Section titled “Version 2023.8.2”](#version-202382)

This is another bugfix release that fixes docker-based deployments (Digital Ocean, Heroku Docker, and fly.io). To get the fix you don’t need to upgrade, just change the node version in your `Dockerfile.web` from 16 to 18. The updated line should look like this:

```plaintext
RUN \
  echo "deb https://deb.nodesource.com/node_18.x buster main" > /etc/apt/sources.list.d/nodesource.list && \
```

Thanks Matthias and Alexander for reporting this.

*Aug 30, 2023*

## Version 2023.8.1

[Section titled “Version 2023.8.1”](#version-202381)

This is a bugfix release that fixes deployment to render.

To get the fix you don’t need to upgrade, just add these two lines to your `envVars` section in `render.yaml` to explicitly bump the node version used from 14 to 18.

```yaml
      - key: NODE_VERSION
        value: 18.17.1
```

Thanks Greg and Michiel for the bug report and suggested fix.

*Aug 21, 2023*

## Version 2023.8

[Section titled “Version 2023.8”](#version-20238)

This release adds official support for three marketing email platforms (Mailchimp, ConvertKit, and Email Octopus), adds dark mode on Tailwind builds, and has the usual smaller updates and fixes.

### Added

[Section titled “Added”](#added-13)

* **First class support for marketing email lists.** You can now select a platform (Mailchimp, ConvertKit, Email Octopus, or none), and your build will be customized for that platform, including settings/environment variables, and automatically subscribing new sign ups to your email list (if properly configured). See the updated [mailing list documentation](/configuration/#mailing-list) for more details.
* Added a management command to send test emails: `./manage.py send_test_email cory@example.com`. Useful when troubleshooting/changing how your server sends email.
* **Added dark mode support for TailwindCSS builds.** Your app should automatically use dark mode if the user’s browser is configured for it. Components that weren’t properly styled for dark mode now are. If you spot any issues please report them!
* The `get_next_unique_slug` helper function can now take filter arguments, so you can have unique fields dependent on other fields (for example, if you want to have slugs which are unique per team).
* Added tests for `get_next_unique_slug` (including testing the new functionality).
* Added view tests for the signup process with various edge-cases around team names.Docker
* Added a `Makefile` target, and documentation for rebuilding the API client with Docker. [Documentation](/apis/#generating-the-api-client) (Big thanks to Finbar for helping on this)

### Fixed

[Section titled “Fixed”](#fixed-18)

* Removed empty JavaScript files in certain builds that were causing `npm type-check` to fail. (Thanks George for reporting!)
* Only try to log mailing list errors to Sentry if building with Sentry enabled.
* Fixed a bug in `get_next_unique_slug` that was failed if you passed in a custom `slug_field_name`. Also added a test that would have caught it.
* Fixed a bug where unicode team names were creating teams with an empty slug, which was causing a crash on logging in.
* Fixed a typo in the `Makefile` (thanks Arno for reporting!)
* \[Documentation] Fixed issue in the digital ocean setup docs that was accidentally resulting in the creation of two Postgres databases, one of which was unused. (Thanks Thomas for reporting!
* Removed links to user profile and signout views from the app navigation if there is no signed in user.

### Changed

[Section titled “Changed”](#changed-17)

* **Upgraded all JavaScript packages to their latest (as of late July) versions.**
* Use the project’s slug in the `package.json` name instead of “pegasus”.
* Changed Twitter change social card format to `summary_large_image`
* In the ChatGPT functionality, new chats are now not created until the first message is sent to them (HTMX only). This prevents empty chats from being created.
* Improved link styling of chats on tailwind builds
* Changed “loading-dots” CSS class to “add-loading-dots”, to prevent conflict with DaisyUI class with the same name.
* Users’ chats are now sorted by last modification time, descending.
* Profile picture validation now includes backend file-type checks, to avoid users uploading incorrect/malicious profile pictures. (Thanks Edward for reporting)
* Stopped explicitly specifying a `platform: `in `docker-compose.yml`, and instead always fall back to the OS’s default platform.
* Added `.jsx`, `.ts`, and `.tsx` as content roots in `tailwind.config.js`.

### Upgrading

[Section titled “Upgrading”](#upgrading-12)

If you were previously using the mailchimp email functionality, you will need to edit your project and select “Mailchimp” under “Email Marketing Platform” to keep using it.

*Aug 8, 2023*

## Version 2023.7

[Section titled “Version 2023.7”](#version-20237)

This is a large maintenance release with many improvements and a few new features.

### Added

[Section titled “Added”](#added-14)

* **Expanded the built-in timezone support (if building with internationalization).** This includes:

  * A new timezone setting on the User model/profile.
  * A middleware that sets and unsets the timezone based on the user’s setting.
  * A built-in list of default timezones.

* **Added the option to remove compiled static files at Pegasus build time.** If checked, your Pegasus build will not include any static files, and they will be added to the `.gitignore` file. This is useful to check after you have set up static file builds as part of a CI/CD pipeline.

* **Added optional support for enabling Django’s [admin docs](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/admindocs/#module-django.contrib.admindocs) via a new project setting.**

* Added improved Docker support for ARM / Mac M2 architectures, via a new project build option. This should improve the performance using Docker for affected OS’s.

### Changed

[Section titled “Changed”](#changed-18)

* **Removed all React dependencies and supporting code when building without React and without the built-in examples.**
* Made order of example navigation and example homepage cards consistent.
* Placed HTMX object lifecycle demo before the Vue one.
* Better styling of terms link in signup forms (Tailwind builds only)
* Moved `page_js` block to the bottom of the `<body>` in the base template. This allows using other imported libraries (e.g. site-bootstrap.js) in inherited templates. (Thanks Finbar for suggesting)
* Switched `UserLocaleMiddleware` to use the “new” style of Django middleware, using `__call__` instead of `process_request` and `process_response`.
* Bumped Django version to the latest 4.2.3 security release.

### Fixed

[Section titled “Fixed”](#fixed-19)

* **Refactored how custom components are added to Tailwind to follow the official guidance on [build-time imports](https://tailwindcss.com/docs/using-with-preprocessors#build-time-imports).** This fixes an issue where multiple style declarations of some classes were included, causing some CSS overrides to not work out of the box. It also results in improved CSS compile times and reduced output file sizes. Additionally, some tailwind styles were moved out of the main `site-tailwind.css` file and into other imported files. (Thanks Tyler for reporting and suggesting the fix!)
* More gracefully handle when a Stripe subscription is deleted (usually in test mode), by logging an error and clearing it from the associated user/team object.
* Added try/catch around Docker hostname setting for debug toolbar, which failed when running outside Docker on some OS’s. (Thanks Geoff for the reporting/fixing)
* Moved inline comments in `.env.example` that failed on some environments. (Thanks Geoff for reporting/fixing)
* Stopped running `collectstatic` while building Docker containers on Google Cloud Run deployments, since the static files are managed outside the container for that platform. (Thanks Alexander for reporting)

*Jul 9, 2023*

## Version 2023.6.1

[Section titled “Version 2023.6.1”](#version-202361)

This is a hotfix release that fixes a bug in the new Alpine.js form/attrs released in 2023.6 for some CSS Frameworks.

*Jun 17, 2023*

## Version 2023.6

[Section titled “Version 2023.6”](#version-20236)

This is a minor release with some form updates and a bugfix for material Bootstrap builds.

### Added

[Section titled “Added”](#added-15)

* Added the ability to specify attrs on form fields, along with special helper parsing for Alpine.js forms.
* Added a forms example using Alpine.js to demonstrate Alpine.js form functionality, including hiding/showing a field based on the value of another field, rendering field values in labels, and changing the style of a field based on its value. The example is available at <http://localhost:8000/pegasus/forms/alpine/>.
* Added [documentation on forms](/forms) in Pegasus.
* Added `.pg-bg-danger` and `.pg-bg-success` helper classes for setting success/danger background colors.

### Fixed

[Section titled “Fixed”](#fixed-20)

* Fixed some styling issues with Bootstrap 5.3 and the material theme.
* Fixed the documentation for how to customize variables when using Bootstrap.

*Jun 12, 2023*

## Version 2023.5.1

[Section titled “Version 2023.5.1”](#version-202351)

This is a small hotfix release, that includes a fix to a build error when using Bootstrap 5.3 (release yesterday).

Details:

* **Fix build errors when using Bootstrap 5.3** (Thanks Allan for reporting/fixing).
* Remove `WAGTAILADMIN_BASE_URL` setting if not building with wagtail.
* Remove some accidentally included tailwind CSS files when not building with tailwind.
* Update the default copyright year in site footer to 2023 if JavaScript was not enabled.
* Add `date_joined` to user admin list display / filter.
* Cropped message content in Chat admin page.
* Added a note to README about configuring Redis if not using Docker (thanks Chris for suggesting)

*May 31, 2023*

## Version 2023.5

[Section titled “Version 2023.5”](#version-20235)

The big feature this release is a major enhancement to the OpenAI ChatGPT integration. This release also upgrades to Django 4.2 LTS and comes with the usual fixes and improvements.

### Chat UI Overhaul

[Section titled “Chat UI Overhaul”](#chat-ui-overhaul)

Here’s a 3-minute demo video of the new ChatGPT functionality:

**Details:**

* Made the Chat UI interactive using HTMX/React (depending on your project configration) and Celery, and greatly improved chat styling.
* Moved chat example to a new chat app.
* Added a chat history model and use it so that chats now have memory.
* Added a chat list view unique to each user.
* Added a `render_markdown` template filter, for converting Markdown to HTML in a template
* Added serializers and admin for chat models.
* Automatically set chat names based on the contents of the first message.
* Add ability to set which chat model you use with the new `OPENAI_MODEL` setting.
* Add `chat.css`/`chat.sass` files for framework-specific chat styling, with many helper UI classes related to the chat UI.
* Removed previous Chat UI, including `PromptForm` class, and related view/template.

### Other updates in this release

[Section titled “Other updates in this release”](#other-updates-in-this-release)

#### Added

[Section titled “Added”](#added-16)

* Added `makemigrations` and `migrate` steps to README on sqlite builds (thanks Patrick for suggesting).
* Added `{% block top_nav_app %}` to `app_base.html` to the material theme, so that the app nav can be overridden in sub-templates
* Added make targets for running black (`make black`), isort (`make isort`), and both (`make format`)
* Added `devtool: "eval-cheap-source-map"` to `webpack.config.js` to prevent source map warnings on Chrome. (Thanks Brett for suggesting)

#### Changed

[Section titled “Changed”](#changed-19)

* **Upgraded Django to 4.2 LTS, Wagtail to 5.0, and a handful of other Python packages to their latest versions.**
* Switched from deprecated `DEFAULT_FILE_STORAGE` and `STATICFILES_STORAGE` settings to `STORAGES` setting (added in Django 4.2).
* Set `EMAIL_SUBJECT_PREFIX` to be your app’s name. This will be prepended to server admin emails.
* Added a 5MB file size limitation to profile pictures, and delete old profile pictures when new ones are uploaded. (Thanks Jonathan for the suggestions!)

#### Fixed

[Section titled “Fixed”](#fixed-21)

* Fixed a bug where the app would crash if people signed up but already had an account, when teams were enabled.
* Fixed crashing issues with running `./manage.py bootstrap_content` (and, resultingly, `make init`) multiple times in a row.
* Removed accidentally included `team_nav.html` file on some CSS frameworks when teams was not enabled.
* Fixed a bug where the `teams/manage/<path:path>` url route was accidentally included in HTMX builds and not included in React builds.
* Fixed a bug where profile picture upload styling wasn’t applied on some CSS frameworks.

### Removed

[Section titled “Removed”](#removed-8)

* Removed deprecated `USE_L10N` setting.

*May 18, 2023*

## Version 2023.4.2

[Section titled “Version 2023.4.2”](#version-202342)

Another small hotfix release:

* Fixes crash on `robots.txt` if you built without wagtail.
* Added tests that would have caught the above issue (and also check other important pages).
* Removed unused `TermsSignupForm` when building with teams enabled.

*Apr 25, 2023*

## Version 2023.4.1

[Section titled “Version 2023.4.1”](#version-202341)

This release fixes two bugs:

* Fixes crash on sign up under certain conditions when teams was not enabled.
* Fixes crash when saving user profile data when API keys were not enabled.

Thanks to Simon for reporting these!

*April 21, 2023*

## Version 2023.4

[Section titled “Version 2023.4”](#version-20234)

This is a large maintenance release with many upgrades, cleanups, and a few small fixes. The biggest changes are upgrading the default Python version to 3.11, Node version to 18, and Docker compose version to 2.

### Python 3.11 update

[Section titled “Python 3.11 update”](#python-311-update)

This release makes Python 3.11 the default supported version for everything in Pegasus. Details:

* **Changed default Python version to 3.11.** Older version of Python (back to 3.8) are still expected to work, but are no longer actively tested.
* Updated references in README and docs to use 3.11 everywhere.
* Updated development Docker image to use 3.11.
* Updated all deploy targets to default to 3.11.
* Updated `black` and `isort` configs to 3.11.
* Updated Github Actions to run tests on 3.11 only. Older versions can still be added back manually.
* **Upgraded most Python packages to latest compatible Python 3.11 versions.** Django was not upgraded to 4.2, because Wagtail has not released support for it yet. If you aren’t using Wagtail, you can upgrade to 4.2 now with no known issues.

### Node 18 update

[Section titled “Node 18 update”](#node-18-update)

This release makes Node 18 the default supported version for everything in Pegasus. Details:

* **Changed default Node version to 18**. Node 16 is still expected to work, but is not actively tested.
* Updated references in README and docs to use 18 everywhere.
* Updated development Docker image to use 18.
* Updated all deploy targets to default to 18.
* Updated Github Actions to run tests on 18 and 19 only. Older versions can be manually added back.
* **Upgraded all node packages to their latest versions.**

### Docker compose update

[Section titled “Docker compose update”](#docker-compose-update)

This release switches Docker compose to use version 2. Version 1 will be removed from Docker in a few months. More details in the [Docker docs](https://docs.docker.com/compose/compose-v2/).

Details:

* Switched all instances of `docker-compose` (v1) to `docker compose` (v2) in the `Makefile`.
* Update all documentation to use `docker compose` instead of `docker-compose`

### Requirements update

[Section titled “Requirements update”](#requirements-update)

This release updates the Python requirements files (again). Apologies for the iteration on this—trying to find the best long-term workflow and hopefully this is it.

* The `requirements/dev-requirements.txt` (and `.in`) file no longer includes everything in `requirements/requirements.txt`. It now only has the requirements used *only* in development. And is (still) constrained to use the same requirements as `requirements/requirements.txt` if any duplicate packages are included, as [described here](https://pip-tools.readthedocs.io/en/latest/#workflow-for-layered-requirements).
* Added a `dev-requirements.txt` file in the root of the project to install both normal and dev-requirements.
* Updated usages of dev-requirements to use the new system, e.g. in Github Actions.

### Other changes

[Section titled “Other changes”](#other-changes-7)

Smaller updates in this release are below.

#### Added

[Section titled “Added”](#added-17)

* **You can now automatically remove the teams example. Uncheck “include Teams example” in your project settings.**
* Added an “I agree to terms” checkbox on sign up for all CSS frameworks.
* Added link to impersonate a user to the app navigation on tailwind builds.
* Added a basic `robots.txt` file that disables crawling on the admin and wagtail admin sites. (Thanks Alex for suggesting)
* Added `OPENAI_API_KEY` to `.env` file if building with OpenAI examples enabled.

#### Changed

[Section titled “Changed”](#changed-20)

* Switched template setting to use `loaders` instead of `APP_DIRS` and disable template caching in development (thanks Michael for suggesting)
* Add apps directory to places Tailwind looks for templates, so that any CSS classes defined there are properly applied.

#### Fixed

[Section titled “Fixed”](#fixed-22)

* Fixed a bug where `./manage.py bootstrap_content` didn’t work if you didn’t have translations enabled.
* Fixed a bug where `black` and `isort` occasionally conflicted on import styles.
* Changed a few single-quotes strings in commented code to use double-quotes to match black styling.
* Added a missing trailing slash in a teams url.
* Added a default empty string to `AWS_ACCESS_KEY_ID` in `settings.py` (this avoids potential crashes running `collectstatic` if it wasn’t set in the environment).
* Fixed a bug where custom form classes were not applied to input fields on Tailwind. (thanks Lars for reporting)
* Always include `"allauth.socialaccount"` in `INSTALLED_APPS`, otherwise deleting users fails. (thanks Jonathan for reporting)

#### Removed

[Section titled “Removed”](#removed-9)

* Removed internal subscriptions API endpoints from the generated API documentation and API clients. If you’d like to keep these, you can remove the `exclude=True` line from the `extend_schema` declaration in `subscriptions/views/api_views.py`, and then [rebuild the API client](/apis/#generating-the-api-client).

#### Documentation

[Section titled “Documentation”](#documentation-3)

* Overhauled the documentation on working with [virtual environments](/python/packages) and made `venv` the default recommendation over `virtualenv`.

### Upgrading / breaking changes

[Section titled “Upgrading / breaking changes”](#upgrading--breaking-changes)

* If you don’t have Docker compose V2 installed you will need to install it to continue using the `Makefile`. This is recommended, since V1 is being removed from Docker Desktop soon.
* There are no known breaking changes related to the Python and Node upgrades, but it is recommended to upgrade your projects if you haven’t already. You may need to [rebuild your Python requirements](/python/packages/#working-with-requirements) on older versions to get backports packages.

*April 20, 2023*

## Version 2023.3.5

[Section titled “Version 2023.3.5”](#version-202335)

A hotfix release, which fixes an issue introduced in `2023.3` where alpine.js was not properly included in the base template if you built with React instead of HTMX.

This resulted in the subscription selection UI not appearing properly.

*March 25, 2023*

## Version 2023.3.4

[Section titled “Version 2023.3.4”](#version-202334)

Another minor release with a few small fixes.

### Changed

[Section titled “Changed”](#changed-21)

* Add `restart: unless-stopped` to web container docker-compose config, so that the web process still restarts on things like syntax errors. (Thanks Moritz for suggesting)
* Code formatting checks in Github Actions now run on the entire codebase instead of just the diffs in pull requests.

### Fixed

[Section titled “Fixed”](#fixed-23)

* Upgraded `cryptography` to version `39.0.2` which patches some high-severity vulnerabilities. (Thanks Michael for reporting)
* Fixed an issue with `boto3` accidentally not being included in requirements files when you enabled S3 media. (Thanks Elliott for reporting)
* Fixed an issue caused by [this issue behavior in Github Actions](https://github.com/actions/runner/issues/1189) that always caused code formatting checks to fail. (Thanks Elliott for reporting)

*March 22, 2023*

## Version 2023.3.3

[Section titled “Version 2023.3.3”](#version-202333)

The main feature in this minor version is an OpenAI demo, showing how you can quickly integrate ChatGPT and DALL-E 2 into your Pegasus apps.

Here’s a 3-minute demo video:

There are also some small fixes (details below).

### Added

[Section titled “Added”](#added-18)

* ChatGPT and DALL-E 2 demos. To use these you need to check the “OpenAI demos” box in your project settings.
* You can now disable translations when building, which removes locale files and related code.

### Changed

[Section titled “Changed”](#changed-22)

* `dev-requirements.in` and `prod-requirements.in` now constrain package versions to those included in `requirements.in`. This should prevent library version conflicts between files.
* Remove `apps.utils.slug` and related test code if not building with teams enabled.
* Remove entire JavaScript API client if not building with any APIs enabled.
* Remove `storage_backends` if not building with S3 media support.

## Fixed

[Section titled “Fixed”](#fixed-24)

* Removed extraneous packages that were accidentally be included in `dev-requirements.txt` even if you had built without certain features enabled. If you saw a big diff after running `pip-compile requirements/dev-requirements.in` on a recent build, this was why.
* Made all package versions consistent between `requirements.txt` and `dev-requirements.txt`

*March 14, 2023*

## Version 2023.3.2

[Section titled “Version 2023.3.2”](#version-202332)

This release fixes two small bugs (introduced in `2023.3`):

* Fixed a syntax error in `render.yaml` that caused deployments to fail. Also removed unnecessary variables from that file if you weren’t using subscriptions or sentry.
* Fixed an issue in the code formatting CI setup that caused the formatting checks to fail on commits made directly to a branch. Now formatting CI is only run on pull requests.

*March 6, 2023*

## Version 2023.3.1

[Section titled “Version 2023.3.1”](#version-202331)

This release fixes a bug (introduced in `2022.12`) that caused the `AUTH_PASSWORD_VALIDATORS` setting to be ignored when building with teams enabled.

You can also manually patch this bug with the following change:

In `apps/teams/forms.py` replace this line:

```python
        cleaned_data = super(SignupForm, self).clean()
```

with

```python
        cleaned_data = super().clean()
```

Apologies to any affected users! Will be adding a test for this in a future release.

*March 5, 2023*

## Version 2023.3

[Section titled “Version 2023.3”](#version-20233)

This release includes several new features as well a lot of maintenance work. These are the biggest changes:

### Code formatting

[Section titled “Code formatting”](#code-formatting)

Pegasus will (optionally) now auto-format your Python code using [black](https://black.readthedocs.io). In addition to formatting, Pegasus now ships with [pre-commit hooks](https://pre-commit.com)—which you can install to ensure your code matches the expected format—and adds format checks to your Github actions CI. Much more detail can be found in the new [code formatting docs](/code-structure/#code-formatting). This option is enabled by default for new projects, and it’s recommended that all existing Pegasus projects upgrade to this format, as it will make future merges/upgrades much easier. Guidance on upgrading [can be found here](/cookbooks/#migrating-to-auto-formatted-code).

### S3 production media support

[Section titled “S3 production media support”](#s3-production-media-support)

You can now use S3 to store your project’s production media with just a few lines of configuration. To use S3, enable the “Use S3 for storing public media files” option in your project’s configuration, and then follow the new [S3 media documentation](/configuration/#setting-up-s3-media-storage).

### Django debug toolbar

[Section titled “Django debug toolbar”](#django-debug-toolbar)

Pegasus now (optionally) ships with the popular [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar) package. You can enable this option in your project configuration, and it will be enabled by default in development environments and turned off in production. More details in [the documentation](/configuration/#django-debug-toolbar).

### Alpine.js support

[Section titled “Alpine.js support”](#alpinejs-support)

The [Alpine.js](https://alpinejs.dev/) library has been officially added as a dependency to all Pegasus builds. Using Alpine allows replacing large amounts of custom JavaScript with a small amount of markup. The subscriptions UI was updated to use Alpine, and more features will move to Alpine in the future.

*Below is the complete changelog for this release:*

### Added

[Section titled “Added”](#added-19)

* **Added pre-commit/black support, as described above and in the [code formatting docs](/code-structure/#code-formatting)**
* **Added django-debug-toolbar, as described above and in [the `debug-toolbar` documentation](/configuration/#django-debug-toolbar)**
* **Added S3 media support, as described above and in the [S3 media documentation](/configuration/#setting-up-s3-media-storage).**
* **Added Alpine.js as a top-level JavaScript dependency, included on all pages.**
* **Added `dev-requirements.in` and `dev-requirements.txt`, for requirements that should only be installed in development (e.g. `pip-tools`, `debug-toolbar`, `black`, etc.**
* Added health checks to Docker postgres and redis, to ensure they are ready before other containers start. (thanks Moritz for suggesting!)
* Added a `make npm-dev` command to build front end for development in Docker.
* Added a wrapping `meta` block to `base.html` to make overriding the page-level metadata more flexible. Wagtail blog post pages now use this to override the page title and description for social sharing.
* Added `.direnv` and `.envrc` files to `.gitignore`
* Added global `[x-cloak]` style to hide elements in Alpine.

### Changed

[Section titled “Changed”](#changed-23)

* **Migrated subscription selection flow from JavaScript to Alpine.js** and deleted a lot of custom JavaScript code that was no longer necessary as a result.
* Updated `ProductWithMetadata` serialization format remove monthly/annual/default prices, and add a dictionary of prices based on billing interval.
* As a result, **Pegasus now supports more than two billing intervals (you can now add any of Annual / Monthly / Weekly / Daily)**
* Migrated help text under the billing interval selector to the `PlanIntervalMetadata` helper class and removed front-end styling.
* Added `payment_amount` field to the Product/Price API serializer.
* **Removed stripe packages, dependencies, and all related code/styles if you build without subscriptions and without examples.** (thanks Brett for suggesting!)
* Moved stripe `card_element.html` component to `pegasus/examples/payments/components/card_element.html`, and only include it if you build with examples.
* Upgraded generated API client to version 6.4.0, and regenerated the API client.
* Upgraded django to 4.1.7 and celery-progress to 0.2.
* Added `SOCIALACCOUNT_LOGIN_ON_GET = True` to `settings.py`. This removes the extra confirmation page for social sign ups, improving the UX, though does open up a minor security risk [outlined here](https://github.com/pennersr/django-allauth/blob/master/ChangeLog.rst#security-notice-1). Remove this line if you prefer to keep the extra page.
* Saving a user profile now shows a confirmation message. (thanks Viktor for suggesting!)
* `make upgrade` now rebuilds your `requirements.txt` files and your front end. (thanks Brett for suggesting!)
* `STRIPE_LIVE_MODE` is now automatically set to `True` in Render deployments. (Thanks Adrian for suggesting!)
* Regenerated translation files for latest code changes.

### Fixed

[Section titled “Fixed”](#fixed-25)

* Removed “https” prefix from fly.io host checks, which caused them to fail.
* Fixed the url in the “Add a Password” link on the user’s profile to go to the set password page. This link is only visible if the user signs up via social auth. (Thanks Blake for reporting)
* Added a workaround for an allauth bug that causes occasional 500 errors when users tried to sign in with a social account that was already tied to an existing email address, by using a `CustomSocialSignupForm`.
* [Details here](https://github.com/pennersr/django-allauth/blob/master/ChangeLog.rst#backwards-incompatible-changes-). (Thanks Simon for finding and fixing!)
* Fixed issue with `make npm-type-check` not being available if Wagtail wasn’t enabled.
* Stop logging errors adding people to the mailing list if they were already on it.
* Improved styling of documentation link when subscriptions were improperly configured dn Tailwind builds.

### Removed

[Section titled “Removed”](#removed-10)

* Removed helper functions on `ProductWithMetadata` related to monthly/annual pricing (e.g. `monthly_price`).
* Removed the no-longer-used `get_payment_metadata_from_request` helper function.
* Removed the no-longer-used `catch_stripe_errors` decorator.
* Removed legacy styling markup from subscription details page. (thanks Viktor for reporting!)

### Documentation

[Section titled “Documentation”](#documentation-4)

* **Added write up about [the front end files](/front-end/design-patterns).**
* **Added write up about managing [test vs live Stripe products](/subscriptions/#stripe-in-production)**
* **Improved the [internationalization/translation docs](/internationalization).**
* **Added [a cookbook for how to enable auto-formatting on your existing project](/cookbooks/#migrating-to-auto-formatted-code).**

*March 3, 2023*

## Version 2023.2

[Section titled “Version 2023.2”](#version-20232)

This release was driven by feedback from the Pegasus community. It includes many library upgrades (including updating to the latest Django), the ability to build without the Pegasus examples, and small changes and fixes.

### Added

[Section titled “Added”](#added-20)

* **You can now build Pegasus projects without the built-in examples.**
* More type hints to return values in subscriptions module.
* `SubscriptionWrapper` object now has a `products` property to get associated Stripe products.

### Changed

[Section titled “Changed”](#changed-24)

* **Upgraded all Python libraries to their latest versions (including Django to 4.1.6)**
* **Upgraded all JavaScript libraries to their latest versions.**
* **Update HTMX installation to use the webpack build pipeline. (HTMX builds only)**
* Set CSRF token on the site body, for usage in HTMX, as [outlined here](https://django-htmx.readthedocs.io/en/latest/tips.html#make-htmx-pass-the-csrf-token).
* Added site name to admin sign up notification.
* Built-in admin emails now fail silently and don’t cause sign-up errors if email sending fails.
* Made it possible to configure `ACCOUNT_EMAIL_VERIFICATION` separately by environment, so it can be enabled in production but disabled in dev.
* Made it possible to view/edit User’s selected language in the Django admin.
* Updated `make pip-compile` to also compile your production requirements file (if relevant).
* Fly.io HTTP checks will now run using the site’s configured HTTP HOST header.

### Fixed

[Section titled “Fixed”](#fixed-26)

* Fixed a bug introduced in 2022.12 that resulted in a duplicate team being created when users created an account while accepting a team invitation (Bootstrap and Tailwind only).
* Cleaned up styling of Monthly/Annual selector buttons on subscription UI (Tailwind only).
* Made icons in menus consistent sizes, to prevent minor alignment issues with wider/narrower icons (Tailwind only).
* Fixed an issue preventing user profile data from being saved if internationalization was enabled, but only a single language was configured.

### Upgrading

[Section titled “Upgrading”](#upgrading-13)

If you don’t want to upgrade Django to 4.1 this upgrade *should* be backwards compatible. Pin the Django version to 3.2.x in your requirements file and [rebuild requirements](/python/packages/#working-with-requirements).

*Feb 1, 2023*

## Version 2022.12

[Section titled “Version 2022.12”](#version-202212)

This is a maintenance release with many small fixes and quality-of-life improvements suggested by the community.

Happy holidays!

### Added

[Section titled “Added”](#added-21)

* Added a `make upgrade` target to update docker containers and a local database after upgrading.
* Added a Redis instance to Github actions CI setup, so that any tests which depend on Redis can run without modification.
* Added default error pages and url routes for 400 and 403 errors.

### Changed

[Section titled “Changed”](#changed-25)

* **Updated usage of `.env` files. Python environments now use `.env`, docker uses `.env.docker`, and the example was renamed from `.env.dev.example` to `.env.example`. [Details here](/configuration).** See upgrade notes.
* **Invitations can now only be accepted from the email address that was invited.** See upgrade notes.
* Blog posts in wagtail are now listed in descending order (by date)
* Optimized the `Dockerfile.dev` so that requirements are installed prior to copying the complete source code of the project. This results in substantially reduced image build times when requirements have not changed.
* Replaced instances of `%` string formatting with `str.format()`
* Update `make pip-compile` and `make requirements` build targets to also build production requirements. (thanks Brett!)
* Updated error pages to use a shared base template.
* Added translation markup to a handful of places.

### Fixed

[Section titled “Fixed”](#fixed-27)

* Remove `customer` from the user admin for team builds (this was causing the User admin to error for team-based builds if subscriptions were enabled).
* Update the `bootstrap_content` management command to publish content (in addition to creating it).
* Fixed crashing error on `@active_subscription_required` decorator if user was not logged-in.
* Fixed image responsiveness on Wagtail blog posts on Bootstrap-based builds.
* Set `LOGIN_URL` in settings, which prevents issues arising if you change the default location of `allauth` urls.
* Fixed image styling on the teams list page if you weren’t a member of any teams. (htmx builds)
* Fixed a minor markdown-styling issue in the README.
* Automatically sync Stripe API keys from settings/environment to database when running `bootstrap_subscriptions`. This fixes the following error on new projectsc: “You don’t have any API Keys in the database. Did you forget to add them?”
* Removed unused import of C3 styles from the charts example template.
* Fixed a static image reference on the example pricing page.

### Upgrade notes

[Section titled “Upgrade notes”](#upgrade-notes-6)

**`.env` updates**

The moving around of `.env` files may impact existing development environments. For those using Docker, it is recommended to rename your `.env.dev` to `.env.docker`.

**Invitation changes**

If you wish to preserve the previous behavior that allowed accepting an invitation from any email address:

1. Remove the email address validation check in `apps.teams.forms.TeamSignupForm` by deleting these three lines:

```python
    if invite.email != email:
        raise forms.ValidationError(_(
            'You must sign up with the email address that the invitation was sent to.'
        ))
```

2. In `templates/account/signup.html` make the email field editable by changing the following line

```jinja
    <input type="hidden" name="{{ form.email.name }}" value="{{ invitation.email }}"/>
```

to:

```jinja
    {% render_text_input form.email %}
```

*Dec 27 2022*

## Version 2022.11.1

[Section titled “Version 2022.11.1”](#version-2022111)

This release is a minor/hotfix update with a few small changes.

### Added

[Section titled “Added”](#added-22)

* Added `clear_cached_subscription` helper function to `SubscriptionModelBase`

### Changed

[Section titled “Changed”](#changed-26)

* Upgraded dj-stripe to 2.7.2. This fixes several crashing errors when using more complex subscription/billing models.

### Fixed

[Section titled “Fixed”](#fixed-28)

* Catch and fix Stripe errors when trying to view a cancelled subscription that has not been synchronized with Stripe

*Nov 4 2022*

## Version 2022.11

[Section titled “Version 2022.11”](#version-202211)

There are a number of big updates in this release.

### Feature: Feature flag support

[Section titled “Feature: Feature flag support”](#feature-feature-flag-support)

Pegasus now supports using feature flags with waffle. For full details, see the new [feature flag documentation](/flags).

Included in the implementation:

* A custom `Flag` model that allows turning features on and off for an entire `Team`.
* A new example page showing how to use feature flags in Python, Django templates, and JavaScript
* Added some helper CSS classes to display badges (used in the example)

### Cleanup: Settings Overhaul

[Section titled “Cleanup: Settings Overhaul”](#cleanup-settings-overhaul)

The main change is to move most configurable settings into environment variables (now managed by [`django-environ`](https://django-environ.readthedocs.io/en/latest/)), and reduce the number of settings files used.

Supporting/related work:

* **Switch environment variables in settings to use `django-environ` and made more settings configurable via environment variables.**
* Support configuring database with single `DATABASE_URL` setting if defined.
* Moved redis configuration to default `settings.py` and allow overriding with environment variables.
* Renamed all platform-specific settings files (e.g. `settings_heroku.py`) to `settings_production.py`.
* **Removed `settings_docker.py` which was used in development with Docker. Docker-specific settings are now overridden via environment variables in the `.env.dev` file.**
* Replaced usage of `django-heroku` with normal settings. Previously this was used to configure the database URL and whitenoise for Heroku. Both of those changes have been rolled into the default settings files.

### Feature: Render deployment option

[Section titled “Feature: Render deployment option”](#feature-render-deployment-option)

Pegasus now officially supports deploying to [Render](https://render.com/). See the new [Render deploy documentation](/deployment/render).

### Feature: Fly.io deployment option

[Section titled “Feature: Fly.io deployment option”](#feature-flyio-deployment-option)

Pegasus now officially supports deploying to [fly.io](https://fly.io/). See the new [Fly.io deploy documentation](/deployment/fly).

### Feature + Cleanup: Subscription updates

[Section titled “Feature + Cleanup: Subscription updates”](#feature--cleanup-subscription-updates)

Most of these changes are backend cleanups to help improve future Subscription work. *Full support for multiple subscriptions and metered billing will hopefully be in an upcoming release.*

**Enabled backend support for subscriptions with multiple products.**

Related changes:

* Switched all references of djstripe’s deprecated `Plan` model to use the `Price` model.
* Updated Subscription serialization to support multiple items / prices / products and changed `PlanSerializer` to `PriceSerializer`.
* Changed suffix in property names in `ProductWithMetadata` class from `_plan` to `_price`.
* `active_subscription_required` decorator now checks all prices/products associated with a subscription if `limit_to_plans` is specified.
* Removed `get_product_and_metadata_for_subscription` and `get_subscription_metadata` functions.
* Added `SubscriptionWrapper` class to help encapsulate more complex subscription logic to a single place, and use it instead of `Subscription` objects and lots of extra context variables in templates.
* Added `InvoiceFacade` class to provide a few utilities to help display a Stripe Invoice object.

**Enabled backend support for [usage-based/metered billing](https://stripe.com/docs/billing/subscriptions/usage-based).**

Related changes:

* Fixed crashes on subscription signup and details pages if your plan was configured with metered billing.
* Added demo form for reporting usage to Stripe for metered plans.

**Changed the Stripe Customer object to be associated with the Team (instead of the User) for Team-based projects.**

Related changes:

* Remove `customer` from the `CustomUser` model and add it to `SubscriptionModelBase` (which will go to the `Team` on team-based builds)
* Set the `DJSTRIPE_SUBSCRIBER_MODEL` to the Team object, if using teams.
* Updated logic that gets/sets the customer to use the Team instead of the user.
* No longer force using the logged-in User’s email address at checkout (for team based builds), so they can specify a different billing email.
* No longer re-use credit cards / Customers when the same user signs up for subscriptions in multiple teams.

*See the upgrading guide below for details on navigating this change.*

### Other Changes

[Section titled “Other Changes”](#other-changes-8)

* **Upgraded font awesome to the latest version (6.2) and load the CSS from a CDN.**
* Upgraded djstripe to version 2.6.2
* Added user and team metadata to the Stripe subscription object during Checkout, so Subscriptions can be more easily linked back to your app from the Stripe Dashboard.
* Added translation markup to a handful of pages.
* Switched Google / Twitter brand icons to be displayed inline, and use icon-sized images.
* **Replaced “icon” CSS class with “pg-icon” to avoid conflicts with framework classes.** In particular, this fixes some issues with Creative Tim themes beyond what’s included in Pegasus.
* Removed icons from subscription plan selector.
* **Use whitenoise for static files in development if deployment is configured for it.** This makes development environments more like production, though is largely invisible.
* **All docker-based deployments now build front end assets as part of the deploy step**. Previously this was only done for Heroku-based deploys.
* **All docker-based deployments are now based off the `buster` image.**
* Added `--noinput` to heroku migrations command.
* Deployments that run Celery now run it with the `--beat` option by default, and a concurrency of 2.
* Increased length of generated secret key in production environment files.
* Upgraded Node versions that run on CI to 16, 18, and 19 to reflect the current releases.
* Upgraded Github actions versions for several steps to fix Node deprecation warnings.
* Production Dockerfiles now run gunicorn by default (this can be overridden in the platform-specific tools, e.g. to run celery)
* Rebuilt the JavaScript API client to reflect the latest API views and serializers.

### Other Fixes

[Section titled “Other Fixes”](#other-fixes-3)

* Fixed all schema warnings from `drf-specatcular`, by adding inline serializers or annotations to several APIs.
* Fixed styling bug in showing a user’s connected accounts on Tailwind builds.
* Properly hide delete button text on small screens in HTMX object demo.
* Replaced many instances of `trans` with `translate` and `blocktrans` with `blocktranslate`.
* Set the page title of Wagtail blog posts to the blog post title.
* Fix active tab highlighting in examples navigation for some CSS frameworks.

### Removed

[Section titled “Removed”](#removed-11)

* Deleted no-longer-needed static images for Twitter / Google logos.
* Removed unused “is-small” class from various icon markup.
* Removed unused styling block for `th` elements in `subscriptions.sass`

### Upgrading

[Section titled “Upgrading”](#upgrading-14)

The major change that requires care in upgrading is the migration of the `customer` field from the User to the Team for team-based builds.

If you do NOT have any live customers associated with your Users the migration process is standard, just run `./manage.py makemigrations` followed by `./manage.py migrate`. **Note: this will drop all User—>Customer relationships.**

If you DO have live customers associated with your Users, and you want to preserve this data, the migration process is more complicated:

First, add the following line *back* to the `CustomUser` model:

```python
   customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
```

Next, create and run migrations:

```bash
./manage.py makemigrations
./manage.py migrate
```

Next you need to move the `Customer` from the user to their team. You can do this by running:

```bash
./manage.py migrate_customers_to_teams
```

If the customer only had a single subscription, it will be correctly applied to the right team. If the customer had multiple subscriptions, the command will print out errors *which you must resolve manually*. You can either choose to drop this information, or associate the customer with a single Team.

Once you are happy with how you’ve migrated the data you can remove the `customer` field from above from the user, and run `./manage.py makemigrations` followed by `./manage.py migrate` to drop it from the user table.

Feel free to reach out in #support on Slack if you need any assistance with this process!

*Nov 4 2022*

## Version 2022.10

[Section titled “Version 2022.10”](#version-202210)

This release adds two-factor authentication, and has a number of smaller improvements and fixes.

### Added

[Section titled “Added”](#added-23)

* **Two-factor authentication.** Users can now set up two-factor authentication on their account (using Google Authenticator or similar), and will be required to enter a token to login. This is configured from the user’s profile page. More [documentation here](/configuration/#two-factor-authentication).

### Changed

[Section titled “Changed”](#changed-27)

* Improved UI feedback in React Teams UI and Employee example when the API client can’t load data.
* Wagtail and admin login pages now redirect to the main login page (this prevents users from bypassing two-factor authentication, if enabled).
* Added top navigation bar to tailwind account pages.
* The teams middleware will now raise a 404 if a user tries to access a page associated with a team they were not a member of. Previously this was only enforced by the `login_and_team_required` decorator, not the middleware. Also added/updated tests for this case.
* Added type hints in a few more places.
* Made minor improvements to API schemas, including fixing some warnings that arose during schema generation.
* Upgraded generated API client to version 6.2.0, and brought in changes from above schema changes.
* Upgraded Django to the latest security LTS release (3.2.16)

### Fixed

[Section titled “Fixed”](#fixed-29)

* Fix an issue in Bootstrap builds where some material styles were being applied to the initial download even if you didn’t choose the material theme.
* Fixed a bug where certain pages would fail to load if teams were enabled but the logged in user was not a member of any teams.

*October 6, 2022*

## Version 2022.9

[Section titled “Version 2022.9”](#version-20229)

The major addition in this release is support for internationalization, a.k.a. translating your app into multiple languages. Here is a quick demo:

This includes support for text localization in Python, Django templates, JavaScript and Wagtail. Translations can be set anonymously (via a cookie) or based on the logged-in user’s selected language.

See the new [Internationalization docs](/internationalization) for more information.

Major related changes:

* Added a language selector to the site footer for users who aren’t logged in.
* Added a `language` field to the `CustomUser` model and profile page.
* Added `UserLocaleMiddleware` to set the user’s language whenever they are logged-in.
* Update wagtail bootstrap code to generate localizable pages.
* Added translations markup to a substantial subset of code across Django views, templates and JavaScript. More translation markup will be added incrementally with new releases.
* Replaced `trans` templatetag with `translate` in a number of places.

### Other Changes

[Section titled “Other Changes”](#other-changes-9)

* **Attach team models to the request in middleware instead of view decorator.** This means that `request.team` will be available on every request, so team navigation will be available even on pages like a user profile that are not team-specific. For details see the updated [teams middleware docs](/teams/#middleware), as well as the upgrade notes below.
* Added tests for the above middleware, and updated other tests to be compatible with it.
* Added a context processor so that `team` is always available in the template context. Also removed code setting `team` in context in `TeamObjectViewMixin`.

### Fixes

[Section titled “Fixes”](#fixes)

* Don’t show pages on the blog index if they are published then unpublished (Wagtail only, thanks Peter for reporting!)

### Upgrade notes

[Section titled “Upgrade notes”](#upgrade-notes-7)

* If you use *teams* and are upgrading from a older version you must make sure that your middleware includes `apps.teams.middleware.TeamsMiddleware`. It should be placed directly after `django.contrib.auth.middleware.AuthenticationMiddleware`.

*September 1, 2022*

## Version 2022.8.2

[Section titled “Version 2022.8.2”](#version-202282)

This is another hotfix release. Thanks Daniel and Jacob for reporting bugs!

* Fix error loading API Schema file when building without API keys enabled.
* Added a test that would have caught the above error.
* Removed unused site-bundle.js file.
* Fix pyyaml requirements conflict when installing with Google Cloud enabled.

*August 5, 2022*

## Version 2022.8.1

[Section titled “Version 2022.8.1”](#version-202281)

This is a hotfix release with a few fixes from the last build. Thanks to Jim and Logan for quickly reporting issues!

### Fixes

[Section titled “Fixes”](#fixes-1)

* Fix environment variable name used for database port in settings.py.
* Removes accidentally added text from the landing page (Tailwind builds only).
* Added instructions to run `./manage.py makemigrations` when setting up a database to the README.

*August 3, 2022*

## Version 2022.8

[Section titled “Version 2022.8”](#version-20228)

The major addition in this release is official support for Tailwind CSS. There were also a number of smaller fixes and improvements.

### Official Tailwind CSS support

[Section titled “Official Tailwind CSS support”](#official-tailwind-css-support)

Pegasus now officially supports [Tailwind CSS](https://tailwindcss.com/)! Here’s a 3-minute walkthrough:

Some of the larger changes to the Tailwind functionality include:

* Upgraded TailwindCSS to version 3 and all dependencies to the latest versions.
* Added a [daisyUI](https://daisyui.com/) dependency and overhauled most of the tailwind templates with daisyUI components.
* Overhauled navigation bar and menus, and added a daisyUI-based mobile dropdown menu for mobile navigation.
* All Tailwind pages are now mobile-friendly.
* Added `tailwindcss/typography` plugin for content.
* Improved tailwind-based Django form rendering and integrated the forms with daisyUI components.
* Improved styling of app notifications/messages.
* Added modal dialogs to the team deletion and membership removal workflows (team builds only).
* Removed many no-longer-used classes form `site-tailwind.css`.

See the updated [Tailwind docs](/css/tailwind) for more information and customization options.

### Other Additions

[Section titled “Other Additions”](#other-additions)

* **Pegasus now ships with a default, customizable logging configuration.** [Documentation](/configuration/#logging).
* Added several new helper CSS classes, including `pg-content` (for content), `pg-columns-reversed` (for reversed columns), `pg-align-items-center` (a flexbox utility), and various `pg-text-` classes for coloring text.

### Other Changes

[Section titled “Other Changes”](#other-changes-10)

* **React-based team deletion now works like the HTMX version, with a pop-up confirmation modal.** The “Delete” button was removed from the team list UI.
* **Deleting a team/user will now automatically cancel any subscription associated with that team/user.** (thanks Florian for reporting!)
* **Updated many templates to use `pg-` Pegasus helper CSS classes instead of CSS-framework-specific ones.** Affected places include: several places in the Pegasus examples, `app_home.html`, the user `profile_form.html` and social account connections page, the React teams editing UI, subscription helper pages, default landing page, password reset pages, team invitation pages, user impersonation, wagtail / blog pages, 404 / 500 pages and more.
* Replaced underscores with hyphens in example URLs.
* Increased margins between buttons and forms/controls in a few templates.
* Improved styling of the default email management page.
* Upgraded several NPM packages to the latest versions including Bootstrap version to 5.2.
* Overhauled [CSS docs](/css/overview).
* Mark `help_text` as safe in form\_tags (allows adding links and other HTML to your help text)
* Add trailing slash to urls in `apps/web/urls.py`.
* Updated default CI configuration to build all pull requests (was previously all pull requests to `main` only)

### Other Fixes

[Section titled “Other Fixes”](#other-fixes-4)

* **Fixed bug where non-admins did not see a link to manage their own membership from the team details page.** (React builds only)
* Fixed styling issues with some tables on small screens.
* Removed empty if/else block from `team_nav.html` if building without subscriptions.
* Fixed a bug in `@active_subscription_required` decorator where an invalid subscription could cause a crashing error instead of redirecting to the subscription management page. (thanks Jon for reporting!)
* In object home examples, list “four” technologies instead of “three”

*August 1, 2022*

## Version 2022.7.1

[Section titled “Version 2022.7.1”](#version-202271)

This is a hotfix release that fixes an “Undefined variable” error when building the front end with the Bootstrap Material theme, and Bootstrap 5.2.

More details on the root issue can be [found here](https://github.com/twbs/bootstrap/issues/36785).

*July 22, 2022*

## Version 2022.7

[Section titled “Version 2022.7”](#version-20227)

This release was largely focused on addressing technical debt and further modernizing some of the front end code that ships with Pegasus.

Due to the large number of updates, a few major changes have been grouped together.

### Added TypeScript support

[Section titled “Added TypeScript support”](#added-typescript-support)

The Pegasus front-end build pipeline now supports [TypeScript](https://www.typescriptlang.org/). You can continue to write code in normal JavaScript, or introduce TypeScript incrementally on new code, on a file-by-file basis. Future versions of Pegasus are likely to incrementally port more code to TypeScript, similar to how types have been incrementally introduced into the Python code.

Related changes:

* Added TypeScript transpilation to the front end build pipeline.
* Added `npm run type-check` and `npm run type-check-watch` targets.
* Added `make npm-type-check` target for Docker environments.
* Run type checks as part of the Github Actions front end build step

### Upgraded all JavaScript packages

[Section titled “Upgraded all JavaScript packages”](#upgraded-all-javascript-packages)

The `npm-check-updates` command was run on the entire front end, and with the exception of TailwindCSS, *every package in `package.json` was upgraded to the latest version*.

Some of the larger updates (for which there were also code changes to make them compatible) include:

* Upgraded Vue.js from version 2 to version 3 and made Employee app compatible with Vue 3.
* Upgraded React to version 18 and react-router to version 6, and updated all code to be compatible with new versions.

### Overhauled the API documentation and API clients

[Section titled “Overhauled the API documentation and API clients”](#overhauled-the-api-documentation-and-api-clients)

This release removed the deprecated CoreAPI-based API schemas and JavaScript client and replaced it with OpenApi3 schemas (using [drf-spectacular](https://drf-spectacular.readthedocs.io/)) and generated client code. For more information on using APIs in your Pegasus app, see the new [API docs](/apis).

Details related to this change:

* Added new `drf-spectacular` Python dependency and removed the `coreapi` Python dependency.
* Added `@extend_schema` markup to most APIs to improve and simplify the generated OpenAPI3 schemas
* **Added new default endpoints for the OpenAPI3 schema.yml file, Swagger API docs, and Redoc API docs.**
* **Added a new TypeScript API client that ships with the front end code.**
* Updated all JS client code to use the new client, including the employee demos, React-based team management views, and chart demo.
* Removed no-longer-used coreAPI helper functions from `assets/javascript/api.js`.
* Removed no-longer-needed `assets/javascript/teams/api.js`.
* Removed no-longer-needed `app.Api` from the front end code.
* Added `openapitools.json` to `.gitignore`
* Added [documentation related to these changes](/apis).

### Other Additions

[Section titled “Other Additions”](#other-additions-1)

* `project_meta` context processor now includes `server_url` (the absolute URL of your app) in the context.
* `get_server_root` helper function to support the above.
* Doc strings for helper functions in `apps/web/meta.py`
* Type hints for various helper methods inside Django models.
* Add `pip-tools` to dev Dockerfile so `requirements.txt` can be built in the container. (Thanks Brett for the suggestion!)
* Add `make pip-compile` target for rebuilding `requirements.txt` and `make requirements` file for rebuilding requirements.txt, and rebuilding/restarting your Docker containers.
* Team management URL is now included in team API urls. (React UI only)

### Other Fixes

[Section titled “Other Fixes”](#other-fixes-5)

* Properly handle team name and slug validation in team editing UI (React UI only)
* Changing the team slug now properly refreshes the page, so links don’t break. (React UI only)
* Fixed typo in variable name in `get_team_api_url_templates`.

### Other Changes

[Section titled “Other Changes”](#other-changes-11)

* **Switched chart examples and supporting code from `c3.js` to [`Chart.js`](https://www.chartjs.org/).**
* Upgraded Django to the latest LTS security release (3.2.14).
* Dev docker set up now starts celery with the beat flag enabled.
* Increased the top margin between the navigation and content in content base template. (Bootstrap only, thanks Will for suggesting!)
* Deleted some accidentally-included commented out code in the Vue employee demo.

*July 8, 2022*

## Version 2022.6

[Section titled “Version 2022.6”](#version-20226)

The main feature of this release is a brand-new integration with Wagtail. [Wagtail](https://wagtail.org/) is a powerful CMS (Content Management System) built on top of Django. You can use it to create rich websites that can be edited directly via an authoring admin interface without writing any code. It’s great for creating marketing sites, blogs, and other mostly-static content.

You can learn more about Wagtail and Pegasus in this 5-minute overview, or by heading over to the [Wagtail documentation](/wagtail).

Complete release notes are below:

### Added

[Section titled “Added”](#added-24)

* **Pegasus now supports Wagtail! [Documentation](/wagtail).** There are a fair number of changes to support this work, most of which are only relevant if you enable wagtail support. The main ones includ a new `content` app, a large number of new Python package dependencies (all stemming from `wagtail`), and some updates to the site navigation.
* **Pegasus now generates a sitemap for you.** [Documentation](/page-metadata/#sitemaps).
* **Responsive HTML email templates were added for the default email confirmation and password reset emails.**
* Add `get_protocol` helper function to return the string “http” or “https” depending on `settings.USE_HTTPS_IN_ABSOLUTE_URLS`

### Changed

[Section titled “Changed”](#changed-28)

* Social sign ups will now automatically create a default team if not there.
* The `login_and_team_required` decorator now falls back to the default team from the session/user if not available from URL (thanks Van for the suggestion)
* Add link to the profile page to set a password if the user only has a social account setup.
* Improve the default UI for setting a password.
* Split the top navigation for the app template into its own template (`top_nav_app.html`). (Material Theme Only)
* Show top navigation menu even if user is logged in (but hide the sign up / sign in buttons) (Material Theme Only)
* Increase top margin on 404 and 500 error pages (Bootstrap only)
* Reduced whitespace in some html templates.
* Changed reference of `djstripe_sync_plans_from_stripe` to `bootstrap_subscriptions` in subscription error message.
* Removed “\[project name]” prefix from signup / password reset emails
* Refactor: use `get_protocol` and f-strings in `absolute_url` helper function
* Removed “More coming soon” text from the Pegasus examples homepage.

### Fixed

[Section titled “Fixed”](#fixed-30)

* Fixed `pyparsing` version conflict between regular and production requirements (Google Cloud builds only)
* Fixed subscription price displays when using graduated pricing. (Thanks Lachlan for reporting)
* Remove Heroku Dockerfile from build if not using it

*June 21, 2022*

## Version 2022.5

[Section titled “Version 2022.5”](#version-20225)

This release improves many of the details of the Stripe subscriptions integration. To streamline these changes, Stripe Elements support has been removed, and subscriptions will be Checkout-based moving forwards.

The release also many small fixes and improvements.

### Added

[Section titled “Added”](#added-25)

* **Re-use the Stripe `Customer` object when a User has multiple subscriptions / payments (by saving it on the User model). This prevents users from having to re-enter their cards multiple times.**
* **Added an `active_subscription_required` decorator for easier subscription feature-gating. [Docs](/subscriptions/#using-the-active_subscription_required-decorator)**
* **Added a periodic task to sync subscriptions with Stripe every day when per-seat billing is enabled.**
* Added a slug field to `ProductMetadata` to be able to uniquely refer to products in code.
* Added `sync_subscription_model_with_stripe` helper function (logic was previously only in `sync_subscriptions` management command)
* Stripe subscriptions are now created with a human-readable description with the team/user associated with the subscription.
* Show expiration date on subscription details when auto-renewal has been turned off
* Docker projects now include a `.env.dev.example` file to use as a reference for sharing across team members (the `.env.dev` file that ships with Pegasus was .gitignored)
* Added Docker-based instructions for running tests while watching for changes.
* Add `lang="en"` to base template for improved accessibility

### Fixed

[Section titled “Fixed”](#fixed-31)

* Fixed bootstrap button CSS classes in a few templates to use the `pg-` class styles instead of the legacy Bulma version. (thanks Lisa for reporting)
* Removed unreachable template code in `view_subscription.html`.
* Removed accidental references to teams from user-based subscription views.
* Fixed subscription payment display amount when subscription quantity is > 1
* `URLField` now renders with same styles as other inputs
* Don’t sync Stripe subscriptions if they don’t need to be changed (per-seat billing only)
* Don’t show hidden labels for inputs in `render_field`/`render_form` tags
* Fixed typo in `update_billing_date_on_membership_deletion` doc string

### Changed

[Section titled “Changed”](#changed-29)

* **Upgraded Python packages to their latest versions.**
* **Heroku-based docker deployments now use a `buster` base image instead of `alpine`. This helps to simplify build issues when adding certain packages / libraries.**
* Simplified team-based subscription views to no longer have redundant functions
* Improved layout of `socialaccount/signup.html` (shown when someone signs up with a social account but the email is already in use). (thanks Lisa for reporting)
* Updated migration file in api app to match latest expected column sizes
* `upgrade_subscription_checkout.html` template has been combined with `upgrade_subscription.html`
* Upgrade htmx version from 1.5 to 1.7
* Improved error message when running `bootstrap_subscriptions` with bad Stripe credentials
* Extracted `get_price_display_with_currency` helper function from `get_friendly_currency_amount`
* Increased size of titles in socialaccount templates.
* Reduced whitespace in HTML templates that were modified from 4-spaces to 2-spaces.
* Added `celerybeat-schedule` to `.gitignore`

### Removed

[Section titled “Removed”](#removed-12)

* **The deprecated Stripe elements support for subscriptions has been removed. Subscriptions require using Checkout moving forwards.**

*May 30, 2022*

## Version 2022.4.2

[Section titled “Version 2022.4.2”](#version-202242)

This is a hotfix release, which adds a missing closing `</div>` tag to the signup template on Tailwind builds when not using teams.

*April 27, 2022*

## Version 2022.4.1

[Section titled “Version 2022.4.1”](#version-202241)

This is a hotfix release, which fixes the `make init` command to start containers in the background so that migrations will properly run.

*April 26, 2022*

## Version 2022.4

[Section titled “Version 2022.4”](#version-20224)

Version 2022.4 is a mix of new features and maintenance improvements. Major updates include new “Login with Twitter” functionality, allowing users to manage their own social accounts, and some Docker development improvements.

### Added

[Section titled “Added”](#added-26)

* **Added “login with Twitter” as a first-class supported authentication option.**
* **Users can now see and manage (connect and disconnect) social accounts (Google and Twitter) from their profile pages.**
* Added new Docker makefile targets, including `make start-bg` to run docker containers in the background (previous default behavior), and `make restart` to restart docker containers
* Added view to simulate errors (by raising an Exception). This is helpful for testing Sentry integrations.
* Added ability to override page titles in templates using the `{% page_title %}` block.
* Added better page titles to several app pages.
* Continued adding translation markup in user-facing text that was modified (this will be an incremental effort towards full-site translation)

### Changed

[Section titled “Changed”](#changed-30)

* **Upgraded version of node that runs in the Docker container from 14 to 16.**
* **Sentry is now a first-class build option enabled in the UI. If enabled, it will be automatically included in requirements and configured in `settings.py`.**
* README file now includes Docker-specific instructions for everything that was included (Docker builds only)
* Made more settings variables configured via environment variables.
* Docker `make start` command now runs in the foreground instead of in the background.
* Merged `meta.html` partial template into `base.html` to enable overridding blocks inside of it.
* The `socialicon` CSS class is now shared in all CSS frameworks and also sets the max width/height of the icon.
* Updated outdated Django docs references to Django 3.2
* Extracted social login buttons to their own templates which are shared on signup and login pages.
* Upgraded Django to 3.2.13

### Fixed

[Section titled “Fixed”](#fixed-32)

* Filter out inactive (archived) Stripe prices/plans from the list of plans

### Removed

[Section titled “Removed”](#removed-13)

* Removed `dev-requirements` files. Pip tools should now be installed with `pip install --upgrade pip-tools`.
* No longer call `npm install` in the `Dockerfile`, since it wasn’t working as expected.
* Cleaned up unnecessary `type="application/javascript"` markup from many `<script>` tags.

### Documentation

[Section titled “Documentation”](#documentation-5)

* Added [page metadata documentation](/page-metadata) for working with project / page metadata (e.g. page titles).
* Updated the [upgrading documentation](/upgrading) to recommend a branch-based approach.
* Updated the [Sentry documentation](/configuration/#sentry) with the new setup and testing instructions.

*April 22, 2022*

## Version 2022.3

[Section titled “Version 2022.3”](#version-20223)

The main feature of this release is [Github Actions](https://github.com/features/actions) support. Pegasus projects can now (optionally) run back end tests and build the front end automatically on Github.

This should work automatically for all projects out-of-the-box. See [the documentation](/github-actions) for more details.

### Added

[Section titled “Added”](#added-27)

* [Github Actions support](/github-actions).

### Changed

[Section titled “Changed”](#changed-31)

* Postgres database settings can now be configured by environment variables directly in `settings.py`
* Upgrade default Python version to 3.9 (including in all Docker files)
* Development Dockerfile now installs all npm packages when being built (thanks Brian for suggesting)
* Upgraded \~all Python packages to their latest versions, apart from leaving Django on 3.2 LTS

### Fixed

[Section titled “Fixed”](#fixed-33)

* More consistent support for using Celery with all versions of Heroku and Redis secure/insecure URLs (thanks Brett for reporting).

This release also introduces a new versioning convention, where future releases will be named: `yyyy.mm` or `yyyy.mm.n` in the case of multiple releases in the same month. This was done to make it clearer to customers when they last upgraded, because the previous release numbers were not meaningful, and because the author had developed decision fatigue about when to declare a “1.0” release.

*March 28, 2022*

## Version 0.22.1

[Section titled “Version 0.22.1”](#version-0221)

This is a hotfix release that fixes a crashing bug with Heroku deployments that don’t use Redis (thanks James for reporting).

*March 15, 2022*

## Version 0.22

[Section titled “Version 0.22”](#version-022)

The main feature of this release is a new front-end theme for Pegasus based off of the [Material Kit](https://www.creative-tim.com/product/material-kit) and [Material Dashboard](https://www.creative-tim.com/product/material-dashboard) products from Creative Tim.

You can get a sense of the theme in this 3-minute video:

This release also adds support for Django 4.0. See note below for details.

### Added

[Section titled “Added”](#added-28)

* New Bootstrap Material theme based on Creative Tim’s Material Kit / Material Dashboard
* Added breadcrumbs to the Employee demo app pages
* Unofficial support for Django 4.0 (see note below).

### Package upgrades

[Section titled “Package upgrades”](#package-upgrades)

* `dj-stripe` to 2.6.1

### Changed

[Section titled “Changed”](#changed-32)

* All tables are now responsive (scrollable) on Bootstrap builds
* Add vertical gutters to columns on Bootstrap builds
* Better spacing of grid layouts in the examples
* Default pegasus form input styling is now handled with `pg-input-group` class
* Updated `djstripe_settings` import to be compatible with new version
* Added top navigation bar to various account templates (password reset, password change, etc.). (thanks James for suggesting!)
* Use `render_field` in more account templates
* Heroku runtime now uses Python 3.8.12 (thanks Allan for reporting!)

### Fixed

[Section titled “Fixed”](#fixed-34)

* Fixed widget class overrides from not being populated for some widgets. This also fixes “select all” functionality in the Django admin for Bootstrap builds. (Thanks Will for reporting!)
* Fixed connection strings for Redis on Heroku if you were not on the free tier, by adding `?ssl_cert_reqs=none` to Redis connection strings. (Thanks Reid for reporting!)
* Fixed 500 error in payments example if the “Pay” button was clicked before the JavaScript on the page fully loads.
* Replaced references to deprecated `ugettext` translation functions with `gettext` versions.
* Removed unused `manage/<path:path>` url route in HTMX-based teams builds (thanks Peter for reporting!)

### Django 4.0 support

[Section titled “Django 4.0 support”](#django-40-support)

This version unofficially supports Django 4.0, however still ships with 3.2.12.

This is due to one issue with the `dj-stripe` dependency [generating migration files](https://github.com/dj-stripe/dj-stripe/pull/1607) that may cause migration problems across multiple Pegasus environments (e.g. dev and prod, or two developer machines). This is a very similar issue to the one described in the [0.14.2 release notes](/release-notes/#version-0142).

If you wish to use Django 4.0, update the pinned version to 4.0.2 (or latest) in your `requirements.txt` file after downloading Pegasus, and all should work.

*Feb 28, 2022*

## Version 0.21.1

[Section titled “Version 0.21.1”](#version-0211)

This maintenance release simplifies how users are accessed via API key authentication, to make it easier to transition views. It mostly undoes a small handful of changes from the 0.21 release.

### Changed

[Section titled “Changed”](#changed-33)

* `HasUserAPIKey` permission class now populates `request.user` with the associated user, if a valid `UserAPIKey` is present.
* API Views and Viewsets now continue to access users via `request.user` instead of the `get_user()` helper functions
* `TeamSerializer` now accesses the user from the request instead of the explicit `["user"]` context.

### Removed

[Section titled “Removed”](#removed-14)

* Now-redundant `UserAPIKeyMixin` class

*Feb 4, 2022*

## Version 0.21

[Section titled “Version 0.21”](#version-021)

This release has one major feature: API Keys. You can get an overview in this 2-minute video or check out [the documentation](/apis) for details.

There are also a number of smaller fixes and upgrades.

### Added

[Section titled “Added”](#added-29)

* API Key support! See the new [API key documentation](/apis) for details.
* Example `DJSTRIPE_WEBHOOK_SECRET` to `.env.dev` file for local Docker deployments

### Package upgrades

[Section titled “Package upgrades”](#package-upgrades-1)

* `django` to 3.2.11
* `psycopg2-binary` to 2.9.3 (fixes installation issues on latest macOS processors) (thanks Eric for reporting!)
* `djangorestframework` to 3.13.1

### Changed

[Section titled “Changed”](#changed-34)

* Updated how some type hints are done to reduce potential for circular imports caused by typing
* Updated headings of account pages to be more consistent with rest of site

### Fixed

[Section titled “Fixed”](#fixed-35)

* Added missing closing `</section>` tag to `templates/accounts/password_change.html` (thanks Peter for reporting!)
* Removed redundant tailwind imports from `assets/styles/pegasus/tailwind.css` which were causing duplicate CSS definitions in the generated `site-tailwind.css` file (thanks Anna for reporting!)
* Fixed bug that triggered an error when subscribing new users to a Mailchimp email list
* The Docker development setup now works on the latest macOS processors

### Removed

[Section titled “Removed”](#removed-15)

* Building for multiple CSS frameworks has been removed. To try different CSS frameworks you will need to edit your project and download each codebase separately.

### Deprecated

[Section titled “Deprecated”](#deprecated-1)

**The following features will likely be removed in an upcoming release. Let me know if you would miss these!**

* **Stripe Elements support is deprecated and will be removed in favor of Stripe Checkout.**

*Feb 2, 2022*

## Version 0.20

[Section titled “Version 0.20”](#version-020)

This release involves a substantial update to Pegasus’s subscriptions functionality. The biggest new feature is that per-seat (also known as per-unit) billing is now supported (for Stripe Checkout only). Team-based installments can now create and manage subscriptions based on the number of users in the team, with built-in infrastructure to track changes and keep them in sync with Stripe.

You can find a 6-minute overview of the feature in this video:

The implementation is customizable and can also be used by non-team builds with some additional configuration. See [the updated Subscription documentation](/subscriptions/#per-unit--per-seat-billing) for an overview of this functionality, and bear in mind that it’s a little complicated with several moving parts!

There were many code changes to support this work-as well as future planned improvements to the subscriptions module. Additionally there were a number of smaller, unrelated updates and fixes.

You can read the complete notes below. The format for this release (and likely future releases) was borrowed from [keep a changelog](https://keepachangelog.com/). The most significant changes are in **bold**. Also please note the announcement of a few features that will be removed soon!

### Added

[Section titled “Added”](#added-30)

* **Support for per-unit / per-seat billing. See [the docs on using this](/subscriptions/#per-unit--per-seat-billing)**
* `SubscriptionSerializer` class for including Subscription objects in APIs
* Management command and logic to sync subscriptions when team membership changes (useful for per-seat billing workflows)
* APIs for creating Stripe checkout and portal sessions and returning the URL to be used by JavaScript front ends
* Stripe webhook support for provisioning a subscription after a sucessful checkout session
* Allow specifying promotion codes when using Stripe Checkout
* Add ability to override display prices for individual billing plans
* Celery on Digital Ocean app platform now supports multiple processes (using gevent)
* More type hints in various places

### Package upgrades

[Section titled “Package upgrades”](#package-upgrades-2)

* Upgrade Django version to 3.2.10 LTS
* Upgrade dj-stripe to 2.5.1

### Changed

[Section titled “Changed”](#changed-35)

* **Changed URLs of Stripe integration API calls to be more consistent**
* **Removed `subscriptions.views.helpers` and merged into `subscriptions.helpers`**
* **Moved `SubscriptionModelMixin` from `apps.subscriptions.helpers` to `apps.subscriptions.models.SubscriptionModelBase` and made it an abstract model**
* Add `created_at` to `Membership` admin
* Add `subscription` and `has_active_subscription` to `Team` serializer
* Moved `ProductWithMetadataAPI` to `api_views` module
* Access `stripe` through `get_stripe_module` helper function
* Extract Stripe checkout and portal session creation to helper functions
* Extract subscription provisioning to helper function
* Add several properties and methods to `SubscriptionModelBase` to help track and use per-seat billing
* Removed redundant extra functions in `apps.subscriptions.checkout_views`
* Prices on subscriptions are no longer centered (it looked silly with only 1 or 2 plans)
* **Prices on subscription page for annual plans now display total amount with billing interval (e.g. $300/year) instead of monthly price ($25/month)**
* Changed `get_friendly_currency_amount` helper function to take a `Plan` object instead of an amount and a currency.

### Fixed

[Section titled “Fixed”](#fixed-36)

* Team and invitation list APIs now require authentication (results in a 403 instead of 500 error when accessed anonymously)
* Archived products are not included in the default product list generated by `bootstrap_subscriptions`
* Automatically select the first plan if none is configured as the default
* Don’t crash displaying subscription plan prices for subscriptions with tiered pricing (instead displays “Unknown”
* Removed some subscriptions templates when building without subscriptions for certain CSS frameworks.
* \[tailwind-only] Removed reference to team name from logged-in homepage when not building with teams

*Dec 23, 2021*

### Deprecated

[Section titled “Deprecated”](#deprecated-2)

**The following features will likely be removed in an upcoming release. Let me know if you would miss these!**

* **Building for multiple CSS frameworks is deprecated and will be removed in the next release.**
* **Stripe Elements support is deprecated and will be removed in favor of Stripe Checkout the next release.**

## Version 0.19

[Section titled “Version 0.19”](#version-019)

This release has two major updates - improved team member management and improved Heroku deployment support.

**Improved Team member management**

Most of the changes below are summarized in this video:

From a user’s perspective there are three main updates:

* Admins can now change any team members’ role from the new “member details” page.
* Admins can also remove anyone from a team.
* All team members (including admins) can leave teams they belong to.

The following supporting changes were also made:

* Added a comprehensive test suite supporting the above workflows.
* Fixed a bug that prevented re-inviting the same email address to a team even if the previous invitation had already been accepted. Duplicate pending invitations are still prevented. This change also removed the DB constraint requiring team and email address to be unique.
* Fixed bug where “resend invitation” and “cancel invitation” buttons were incorrectly showing up for non-admins.
* Added helper `is_admin` method to team `Membership` objects.
* Added a `CustomUserSerializer` to pass user information to the front end.
* Added the `user_id` field to `MembershipSerializer`
* Add the site name to body of team email invitations.
* Add `__str__` function to team `Membership` objects.
* Introduce `TeamPermissionError` exception class and start using it for permission-related failures.
* Added better display of front-end validation issues when issuing invitations fails.
* Various bits of formatting and cleanup in teams React code.

**Heroku deployment improvements**

A few updates were made to make deployments to Heroku containers faster and more comprehensive:

* Bump `cryptography` to `3.4.8` and remove no-longer-necessary dependencies from production dockerfiles. This results in vastly improved build times for Heroku docker deployments.
* Build the front end files as part of Heroku container deployments
* Run database migrations by default on Heroku container deployments
* Set various production-recommended settings in `settings_heroku.py`. For more details see the new [production checklist](/deployment/production-checklist) in the documentation.

**Other minor updates**

* Added fall back to `username` on User display functions if the user does not have an associated email address.
* Extracted logic for opening modals to a shared JavaScript function (Bulma builds only).
* Remove commented out / unused code from `templates/web/components/top_nav.html` and modal dialogs. (Tailwind builds only).
* Bump `django` to `3.2.8`
* Add `pg-text-muted` helper CSS class
* Add some more type hints to URL helpers
* Extracted React form validation logic to `ValidationErrors` component.

**Upgrade Notes**

If you are upgrading from a previous version you should *not* merge any changes in the teams migration files, and run `./manage.py makemigrations` and `./manage.py migrate` to remove the DB constraint on team invitations after upgrading.

*Oct 27, 2021*

## Version 0.18.1

[Section titled “Version 0.18.1”](#version-0181)

This hotfix release fixes a bug affecting React builds that caused the sign up page to be broken.

*Oct 3, 2021*

## Version 0.18

[Section titled “Version 0.18”](#version-018)

This release adds a new Django + [HTMX](https://htmx.org/) implementation of Pegasus’s team management functionality. Now, you can choose whether to use React or HTMX for your teams UI.

This choice is configured by the new “Front-End Framework” setting in your project’s Pegasus settings. The setting currently only impacts the Teams UI (and has no impact on Pegasus builds that don’t use teams), but will be extended in future releases.

The HTMX teams UI also has a few user-facing improvements:

* You can now choose a role when inviting new team members.
* Team deletion has moved to the team details page, and now has a confirmation dialog.
* Editing the team name and ID now require the team admin role.

Additionally, there are bug fixes and code-related improvements throughout the teams functionality:

* Fixed “sign out” link on invitation acceptance page.
* Improved workflow when attempting to accept an invitation to a team you already belong to.
* Broke the teams `views.py` file into multiple Python modules.
* Set `team_membership` on `request` object in team decorator functions, so it can be easily accessed in views/templates.
* Cleaned up bits of HTML in existing teams React implementation.
* Various doc strings, type hints, and formatting cleanup throughout code.
* Combined `accept_invitation` and `accept_invitation_confirm` into a single view.
* Remove a few teams-related templates when not building with teams enabled.

Finally, there were minor updates to other functionality:

* Bootstrap JavaScript is now built and used from the local install instead of using a pinned CDN. (Bootstrap builds only)
* Extract Mailchimp mailing list logic to its own module and add [mailing list documentation](/configuration/#mailing-list).
* Fix quirks in HTMX example when back-end validation fails.
* Minor cleanup of HTMX example code.
* Rename `payments` and `tasks` view modules to `payments_views` and `tasks_views`.
* Upgrade Django to `3.2.7`.
* Changed default value of `USE_HTTPS_IN_ABSOLUTE_URLS` setting to `False`

**Potentially breaking changes**

The change of the default value of `USE_HTTPS_IN_ABSOLUTE_URLS` could impact production environments that have not overridden this setting. In particular, it would cause Stripe checkout / portal callbacks and invitation emails to have `http` links instead of `https` links.

To fix this, add `USE_HTTPS_IN_ABSOLUTE_URLS = True` to all production settings files / environments.

*Sep 28, 2021*

## Version 0.17.1

[Section titled “Version 0.17.1”](#version-0171)

This fixes a crashing issue when resending team invitations.

*Sep 8, 2021*

## Version 0.17

[Section titled “Version 0.17”](#version-017)

This release adds an HTMX demo, a Teams example app, and more.

This video provides a 4-minute overview of the key features, or read on for details.

**The HTMX object demo**

The object demo application now has an [htmx](https://htmx.org/) implementation. HTMX is a library that allows you to build rich, single-page, interactive experiences by adding HTML attributes.

The provided demo application is a single page app with no native JavaScript, backed by Django forms.

**The Teams Example app**

This release also adds a Teams example app, which has Create, Read, Update, Delete (CRUD) views for an example model that is part of a team (called a “Player”).

As part of this work, a new base model class, `BaseTeamModel` was added which can be extended to create models that belong to a Team.

Additionally, two view mixin classes, `LoginAndTeamRequiredMixin` and `TeamAdminRequiredMixin` were added, which can be used to easily create class-based model views on Team models. A test suite for these mixins was also added.

More details can be found in the [Teams documentation](/teams).

*A big thanks to Peter Cherna, who’s [Pegasus example apps](https://github.com/pcherna/pegasus-example-apps/) was a big inspiration for this example.*

**Other changes**

* Add generic breadcrumbs CSS classes compatible with Bulma, Bootstrap and Tailwind (used by teams example)
* Default all Pegasus apps to using `BigAutoField` instead of `AutoField` (see upgrade notes)
* Use f-strings instead of string templates in management commands
* Reduce indentation level in some html template files

**Upgrade notes**

The default ID for all Pegasus models was changed from `AutoField` to `BigAutoField`. If you are upgrading a project using `AutoField` you should *not* merge any changes to initial migration files in the affected apps. Then you can either:

1. To change your apps from `AutoField` to `BigAutoField`, run `./manage.py makemigrations` and `./manage.py migrate`
2. To keep using `AutoField`, change the setting back to `AutoField` in `apps.py` for all Pegasus apps.

*Aug 24, 2021*

## Version 0.16.2

[Section titled “Version 0.16.2”](#version-0162)

This release upgrades `django-hijack` from 2.3 to 3.0 and adds hijack links to the admin site.

*Aug 11, 2021*

## Version 0.16.1

[Section titled “Version 0.16.1”](#version-0161)

This minor release fixes styling issues with Tailwind builds that were accidentally introduced in 0.16.

*Aug 9, 2021*

## Version 0.16

[Section titled “Version 0.16”](#version-016)

This is a grab-bag release of mostly cleanup work and bug fixes.

***Please review the breaking changes closely if you are upgrading an existing project! Not doing so could lead to unexpected behavior and demo data loss!***

**Potentially breaking changes:**

* Changed the `login_and_team_required` and `team_admin_required` view decorators to no longer allow superusers to access the views. It is recommended to use the new user impersonation feature to allow superusers to access teams they don’t belong to.
* Removed `user_can_access_team` and `user_can_administer_team` helper functions which provided team access to superusers.
* Removed `attrs` library dependency and switched its usages to `dataclasses`.
* The `Employee` example data model has moved, and running `migrate` will drop all of your demo `Employee` data.

**New: Improved Django form support:**

* Added a Django forms implementation of the employee / object demo
* Rename `bootstrap_form_fields` and `bulma_form_fields` templatetags to `form_fields` if not using multiple-css-framework support
* Add `render_form_fields` helper function to render an entire form. (Note: this currently only supports text-style, checkbox, and select input types.)
* Add `render_checkbox_input` to bootstrap form rendering tags
* Added a basic non-model form example

**Fixes:**

* Fix cryptography build issue affecting Heroku docker deployments
* Improve textarea styling on Bootstrap forms
* Better default styling of checkboxes in Bootstrap forms.
* Don’t require that `team_slug` be the first argument to a url to use the team-based decorator functions.

**Cleanup:**

* Upgrade Django to 3.2.6
* Remove redundant `null=True` from user avatars
* Added more type hints
* Split object / employee example out into its own app and template folder.
* Added help text to employee example model fields
* Changed some navigation and text around the employee app example
* Remove inline style declarations from a few examples
* Added some instructions about initializing your database to the README
* Update migrations to be compatible with latest Django / Pegasus code

**Upgrade notes:**

If you receive a warning like this when generating Database migrations:

*You are trying to change the nullable field ‘avatar’ on customuser to non-nullable without a default; we can’t do that (the database needs something to populate existing rows).*

It is safe to choose option 2, “Ignore for now…”. There won’t be any NULL values in the database, since Django automatically populates `FileField`s with an empty string.

*Aug 6, 2021*

## Version 0.15

[Section titled “Version 0.15”](#version-015)

Version 0.15 is a major release with two big features: Stripe Checkout and User Impersonation.

For 3-minute summary you can watch the video below, or read on for details.

**Stripe Checkout Support**

Now you can use [Stripe Checkout](https://stripe.com/payments/checkout) for payments instead of - or in addition to - the Stripe Elements-based embedded UI. Stripe Checkout support has been added to the subscriptions page, as well as the payment example. You can build new Pegasus projects with Checkout, Elements, or toggle between them via a `settings.py` setting.

**User Impersonation**

This release also adds optional user impersonation functionality for superusers, allowing admins and support staff to “login as” another user with a few clicks. This is a great tool for troubleshooting user-specific issues. This feature depends on [django-hijack](https://github.com/django-hijack/django-hijack) and can be disabled at build time.

**Other updates**

* Make http/https in absolute URLs (e.g. email invitations) configurable via the `USE_HTTPS_IN_ABSOLUTE_URLS` setting
* Start adding type hints to the codebase, primarily in helper functions. More coming soon!
* Added more tests for teams helper functions
* Split out `subscription/views.py` into multiple files to make it clearer which views affect which functionality.
* Break `upgrade_subscription.html` into multiple files to support elements and checkout-based flows.
* Improve default string representation of user model
* Improve the default styling of select widgets (Bootstrap builds only)
* Clean up doc strings and code for team API permission helpers (teams builds only)
* Rename `teams.util` to `teams.helpers` to be consistent with other apps (teams builds only)
* Fix issue with `apps/subscriptions/__init__.py` not being created for certain configurations
* Various minor cleanups of whitespace, url ordering, etc.

*July 22, 2021*

## Version 0.14.5

[Section titled “Version 0.14.5”](#version-0145)

Another grab-bag of minor fixes and improvements.

* Reduce scope of hiding file inputs to just the profile upload form
* Add `NoNewUsersAccountAdapter` to allow disabling public sign ups for an app
* Extract Bulma and Bootstrap form rendering to helper template tags
* Fix subscription details start date display (subscriptions builds only)
* Explicitly set `DEFAULT_AUTO_FIELD` to `AutoField` in settings to remove runtime warnings.
* Minor README improvements
* Upgrade Django to 3.2.5

Changes only affecting builds with teams enabled:

* Fix error on sign up if email passes front-end validation but fails back-end validation
* Change `/teams/` URL to go to the teams management page instead of API docs
* Improve styling of teams page when no teams exist on Bootstrap
* Fix React warning in teams JavaScript

*July 15, 2021*

## Version 0.14.4

[Section titled “Version 0.14.4”](#version-0144)

A very minor release:

* Don’t include `djstripe` and associated settings in `INSTALLED_APPS` if not using subscriptions

*June 30, 2021*

## Version 0.14.3

[Section titled “Version 0.14.3”](#version-0143)

A very minor release:

* Update Django to 3.2.4
* Remove `DEFAULT_AUTO_FIELD` declaration from settings. This was causing issues with allauth migrations being generated, as a result of [this issue](https://github.com/pennersr/django-allauth/pull/2829). Until more libraries have worked around these migration issues, Pegasus will just ship with the default setting.

*June 17, 2021*

(v-0-14-2)=

## Version 0.14.2

[Section titled “Version 0.14.2”](#version-0142)

This release upgrades `dj-stripe` to version `2.4.4` which should fix cross-environment migration issues.

**Upgrade notes:**

Projects using a “clean” 0.14 or 0.14.1 release may have been affected by [this issue in dj-stripe](https://github.com/dj-stripe/dj-stripe/issues/1344) where running `makemigrations` automatically generated a migration file inside the `dj-stripe` library code. Local app migrations would then add a dependency to this migration, which would not be available on other environments.

This often manifested as an error along the lines of the following when setting up a second environment:

```plaintext
django.db.migrations.exceptions.NodeNotFoundError:
  Migration .0003_auto_20210524_1532 dependencies reference nonexistent parent node ('djstripe', '0008_auto_20210521_2314')`
```

To fix this there are a few steps:

1. You should explicitly uninstall and reinstall `dj-stripe` instead of just installing requirements to ensure the generated migration file is removed. `pip uninstall dj-stripe && pip install dj-stripe==2.4.4`
2. You should rebuild your own app’s migrations to no longer depend on the generated `dj-stripe` migration, by deleting the bad files and re-running `makemigrations` on a fresh environment.
3. You will need to “fake” migrations for any existing DBs, by manually deleting relevant rows from the `django_migrations` table and then running `./manage migrate <appname> --fake` for each affected app.

Please reach out for support on Slack if you run into any issues with this, and I’m happy to help!

*May 26, 2021*

## Version 0.14.1

[Section titled “Version 0.14.1”](#version-0141)

This is a minor release including the latest Django security updates, the official Bootstrap 5.0 version, and a few small features and fixes.

* Fix incorrectly generated `urls.py` if you built with teams and without subscriptions
* Add password confirmation field to sign up pages if configured by allauth
* Add `project_settings` example for passing project-level settings to templates via context processor
* Update `bootstrap` to `5.0.1`.
* Update `django` from `3.2` to `3.2.3`
* Remove unused `kombu` dependencies from requirements.

**Changes affecting [experimental features](/experimental/react-front-end) only:**

* Slightly improved styling of Tailwind sign up page

*May 19. 2021*

## Version 0.14

[Section titled “Version 0.14”](#version-014)

Version 0.14 is a major release with a focus on Teams and package upgrades. It also upgrades Pegasus to Django’s 3.2 LTS release. Details are below:

**Teams Upgrade**

* Make team name optional on signup, and auto-generate a team if none specified.
* Update team-based URL-routing to be more consistent (put all team urls behind `/a/team-slug/`)
* Migrate teams React code to functional components / hooks
* Add URL-routing and back button support to teams page
* Restrict ability to edit/delete teams to team admins only
* Restrict ability to manage team invitations via API to team admins only
* Add manage/view team page to main team navigation
* Other minor teams JS cleanup (replace `var` with `const`, etc.)
* Delete `team_nav.html` when not using teams
* Improve loading screen for teams page and extract to shared component

**Package Upgrades**

* Upgrade all python packages to latest versions (including Django to 3.2 LTS)
* Updated settings file to the version that ships with Django 3.2
* Update formatting of requirements files to the latest version used by `pip-tools`
* Upgrade all JS packages to latest versions
* Switch from deprecated node-sass to dart-sass

**Other updates**

* Set base URL in React object demo from Django
* Fix doc strings of npm-related `make` commands
* Extract logic for getting CoreAPI JavaScript client to a shared function
* Add support for celery workers to Digital Ocean deployments (and [updated docs](/deployment/digital-ocean))
* Add `make dbshell` docker command to get a database shell
* Remove some tailwind files that were accidentally included in non-tailwind builds

**Changes affecting [experimental features](/experimental/react-front-end) only:**

* Improve Tailwind styling of examples, teams and other built-in pages
* Add `@tailwind/forms` plug in for improved form styling
* Split Pegasus Tailwind CSS classes into a new file to mirror Bootstrap/Bulma implementations
* Fix collectstatic errors when building with tailwind and whitenoise (affected Heroku and Digital Ocean deployments)
* Remove broken landing page and pricing page examples, and point people to Tailwind UI instead

**Upgrade notes:**

* Django added the new [Default primary key field type](https://docs.djangoproject.com/en/stable/ref/settings/#default-auto-field) setting. If you wish to use the default in 3.2 you will have to add DB migrations for it. Otherwise you can change the value of `DEFAULT_AUTO_FIELD` to `'django.db.models.AutoField'` in your `settings.py` file.
* Bootstrap users may need to run `npm update bootstrap` before building static assets to get all styling of the examples working again.

*April 28, 2021*

## Version 0.13.2

[Section titled “Version 0.13.2”](#version-0132)

This is a minor release primarily focusing on an improved Docker experience and updates to the experimental TailwindCSS support:

* Update development `Dockerfile` from `alpine` to `buster` and install front-end dependencies.
* Add `Makefile` with self-documenting targets for various common operations ([see docs](/docker))
* Update generated `README` with better Docker instructions
* Use double quotes for description and name settings to reduce issues with apostrophes

Changes affecting [experimental features](/experimental/react-front-end) only:

* Properly support for using PurgeCSS with Tailwind
* Include (purged) Tailwind bundle files with Pegasus

*March 10, 2021*

## Version 0.13.1

[Section titled “Version 0.13.1”](#version-0131)

This is a minor maintenance release with a few small changes and fixes.

* Fix Docker image when deploying to Heroko containers
* Fix SSL mixed content issues on Heroku Docker builds
* Remove teams JavaScript files if not using teams.
* Add `body_wrapper` block for overriding the whole base template
* Label closing `endblock` tags in base template
* Add `.DS_Store` files to `.gitignore`
* Minor compatibility fixes to `teams` CSS.

*February 24, 2021*

## Version 0.13.0

[Section titled “Version 0.13.0”](#version-0130)

This release adds support for the [Bootstrap CSS framework](https://getbootstrap.com/) and includes several changes to how the CSS files are structured in Pegasus. See the new [CSS documentation](/css/overview) for an overview of the new structure.

Major changes:

* Full support for Bootstrap CSS!
* Restructure CSS files, creating framework-level subfolders, splitting `site-base` and `site-<framework>` files out, and making Sass imports implicit in the Bulma files.
* Examples CSS overhaul, converting styles to `pg-` classes and adding the `pegasus/<framework>.sass` files to style examples and JavaScript.

Minor changes:

* Improved UI of object demo tables on small screens.
* Remove unused “tagline” CSS styles and replace with the CSS frameworks’ vertical centering utilities.
* Update progress bar styles to use CSS variables instead of Sass variables.
* Remove unused redundant “section” classes from a number of places.
* Split profile page into multiple HTML templates.
* Remove duplicate cookie-handling code JavaScript on profile page and use the same JS code used in other places.
* Remove unused `plan-price` and `plan-tagline` classes from subscription page.
* Fixed bad reference to `subsriptions.sass` when not building with subscriptions.
* Remove unused `has-vcentered-cells` class.
* Start splitting out teams JavaScript into multiple files.
* Remove redundant `custom-file-upload` CSS class.
* Add /404 and /500 endpoints for viewing custom 404 and 500 pages.
* Remove unnecessary raw string formatting from severeal `urls.py` files.
* Upgrade Django to `3.1.6`

*February 8, 2021*

## Version 0.12.1

[Section titled “Version 0.12.1”](#version-0121)

This release continues the overhaul of the Pegasus CSS and templates to include experimental support for the Bootstrap CSS framework. Details on using Bootstrap [can be found here](/css/bootstrap).

Changes affecting everyone:

* Fix “view subscription” page start date display, and accommodate when start date is not set in Stripe.
* Default `ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True` to avoid double-login after email confirmation.
* Move navbar avatar styling to standalone `navbar.sass` file to be shared across CSS frameworks.
* Change navbar avatar class and CSS from `.avatar` to `.navbar-avatar`.
* Split subscription details on the “view subscription” page into its own component templates.
* Split hero section on the “upgrade subscription” page into its own component templates.
* In `subscriptions.sass`, use css variables instead of sass variables for colors.
* On subscription page, change “upgrade-features” selector from an ID to a class in HTML and CSS.
* Remove unused styles from `subscriptions.sass`
* Clean up whitespace in a number of files

Changes affecting experimental features:

* Booststrap CSS build! [Details here](https://docs.saaspegasus.com/experimental#bootstrap-css-support).
* Building for multiple CSS frameworks now includes Bootstrap (along with Bulma and Tailwind)
* Building for Tailwind now overwrites Bulma templates instead of maintaining them in a separate directory.

*January 26, 2021*

## Version 0.12.0

[Section titled “Version 0.12.0”](#version-0120)

This release is a set of changes laying the groundwork for future Pegasus improvements.

*Existing Pegasus users will need to upgrade their installer to use the latest version (`pip install --upgrade pegasus-installer`)*

**Experimental support for Tailwind CSS**

More details can be found in the [Tailwind documentation](/css/tailwind).

*Note: this feature is not yet fully supported and is in an experimental pre-release.*

**Simplified upgrade process**

Pegasus now saves your configuration when you install it, to simplify the upgrade process. Instructions on upgrading can be found on the [“upgrading” page](/upgrading).

**Additional related changes and fixes**

* Remove `package-lock.json` from Pegasus for improved compatibility across NPM / OS versions. It is recommended to run `npm install` and then check in the resulting `package-lock.json` file to source control. More details can be found in the [front end docs](/front-end/overview).
* Switch some styling from Sass variables to CSS variables (e.g. colors) for compatibility with multiple CSS frameworks
* Add a `site-base.sass` file for base Pegasus styles that aren’t dependent on any CSS framework.
* Fix issue with `PlanSerializer` and `dj-stripe` version 2.4.1
* Remove no-longer-used `subscription_title.html` template.
* Remove no-longer-used tooltip styles
* Remove unused HTML from subscriptions upgrade page and split it out into partial templates
* Change a few default settings, e.g. project and author name.
* Upgrade django to 3.1.5.

*January 13, 2021*

## Version 0.11.3

[Section titled “Version 0.11.3”](#version-0113)

This release overhauls the Payments example to use the Stripe `PaymentIntent` API and [support 3DS / SCA cards](https://stripe.com/docs/strong-customer-authentication).

Minor changes:

* Upgrade `dj-stripe` to `2.4.1`
* Pull `DJSTRIPE_WEBHOOK_SECRET` setting from environment variable if available

If you are upgrading from a previous installation, you may need to change the following two values in `settings.py`:

```python
DJSTRIPE_FOREIGN_KEY_TO_FIELD = 'id'  # change to 'djstripe_id' if not a new installation
DJSTRIPE_USE_NATIVE_JSONFIELD = True  # change to False if not a new installation
```

*December 17, 2020*

## Version 0.11.2

[Section titled “Version 0.11.2”](#version-0112)

* Fixes to subscription workflow when using a trial period - automatically refresh page after card is accepted and support 3D-Secure validation for credit cards when using a trial.

*December 9, 2020*

## Version 0.11.1

[Section titled “Version 0.11.1”](#version-0111)

* Fix bug in development Dockerfile from a new OS dependency introduced by the `django-allauth` upgrade.

*December 7, 2020*

## Version 0.11.0

[Section titled “Version 0.11.0”](#version-0110)

This release is a grab-bag of fixes and upgrades based on recent feedback.

* Force users to reconfirm their email when changing it and email verification is enabled
* Switch from `extract-text-webpack-plugin` to `mini-css-extract-plugin` for CSS handling in Webpack
* Rename `assets/index.js` to `assets/site.js` to support more styles in the future.
* Use randomly generated identicons for users instead of a default empty profile picture
* Move `.env.dev.example` to `.env.dev` and `.env.production.example` to `.env.production` so they don’t have to be copied to get running (Docker builds only)
* Clean up payments UI a little
* Remove accidentally included `team_admin.html` template when not building with teams
* Remove accidentally included `Dockerfile.dev` template when not building with Docker
* Remove unused CSS classes from examples
* Upgrade various NPM packages to latest versions
* Upgrade `django-allauth` to `0.44.0`
* Upgrade `django` to `3.1.4`

*December 2, 2020*

## Version 0.10.5

[Section titled “Version 0.10.5”](#version-0105)

This release adds native support for deploying to Digital Ocean app platform. See the [deployment guide](/deployment/digital-ocean) for details.

Additional updates:

* Remove duplicate `ACCOUNT_EMAIL_VERIFICATION` declaration in `settings.py`
* Rename development `Dockerfile` to `Dockerfile.dev` for clarity and ease of deployment to other platforms
* Fix SSL / mixed content errors when deploying on Google Cloud Run

*Nov 17, 2020*

## Version 0.10.4

[Section titled “Version 0.10.4”](#version-0104)

This release adds experimental native support for deploying to Google Cloud Run. More details can be found in the [deployment guide](/deployment/google-cloud).

Additional updates:

* Fix static file references to favicons.
* Upgrade `certifi` to `2020.11.8`
* Rename `heroku-requirements.txt` to `prod-requirements.txt` to be consistent across platforms (Heroku builds only)
* Switch production Docker images from Python-alpine to Python-slim (Docker builds only)

*Nov 10, 2020*

## Version 0.10.3

[Section titled “Version 0.10.3”](#version-0103)

This release adds native support for deploying to Heroku using Docker containers. More details can be found in the new [deployment guide](/deployment/overview).

Additional minor updates:

* Upgrade `urllib` to `1.25.11`
* Allow requirements to load from multiple sources when using Docker
* Add static directories and config files to `.gitignore`

*Nov 5, 2020*

## Version 0.10.2

[Section titled “Version 0.10.2”](#version-0102)

This release adds support for using [Docker](https://www.docker.com/) in development. More details can be found in the new [Docker documentation](/docker).

*Oct 28, 2020*

## Version 0.10.1

[Section titled “Version 0.10.1”](#version-0101)

This release adds [Heroku](https://www.heroku.com/) deployment support. More details can be found in the new [deployment guide](/deployment/overview).

*Oct 26, 2020*

## Version 0.10.0

[Section titled “Version 0.10.0”](#version-0100)

This is largely a maintenance release with mostly minor updates and fixes, but there are enough library upgrades that it warrants a version bump.

* Upgrade all Python packages including upgrading to Django 3.1.2
* Upgrade all npm packages
* Add a new API for products and metadata at `/subscriptions/api/active-products/`. Also includes adding some serialization classes and helper functions to subscriptions models. *Subscriptions only.*
* Fix a bug where clicking on “Dashboard” didn’t always take you to the right team. Also set team ID in the request session so it can be accessed across requests, and add `get_default_team` helper function to pull the last/current team from a request. *Teams only.*
* Fix default styling of textarea widgets in Django forms
* Use `const` and `let` in subscriptions page JavaScript
* Add `has-vcentered-cells` table formatting class to center table rows, and use in teams UI and object lifecyle demos
* Remove unnecessary `subscriptions.sass` file when Pegasus is built without subscriptions enabled

*Oct 14, 2020*

## Version 0.9.0

[Section titled “Version 0.9.0”](#version-090)

This release is a large overhaul of the React example that ships with Pegasus, including:

* Add url-routing support. Add/edit URLs now update and are linkable. This also enables back button support
* Add validation feedback missing / bad data
* Switch all components from using classes to [hooks](https://reactjs.org/docs/hooks-intro.html)
* Split React components out into their own files
* Better loading UX

Other minor updates:

* Upgrade Django to 3.0.10 (3.1 support coming soon)
* Upgrade various JavaScript dependencies
* Generate random `SECRET_KEY` for each new installation
* Upgrade to Bulma 0.9.0
* Remove some spacing utility classes in favor of the ones that ship with bulma

Upgrading:

**Existing Pegasus users will need to upgrade the installer to run this.**

```bash
pip install --upgrade pegasus-installer>=0.0.2
```

*Sep 4, 2020*

## Version 0.8.3

[Section titled “Version 0.8.3”](#version-083)

* Fix default styling of number inputs in forms.
* Default `ACCOUNT_CONFIRM_EMAIL_ON_GET` to `True` if using email confirmation.
* Fix issue building front end on certain newer versions of nodejs/npm
* Upgrade `celery-progress` from `0.0.10` to `0.0.12`

*Aug 31, 2020*

## Version 0.8.2

[Section titled “Version 0.8.2”](#version-082)

This release fixes an edge case in the invitation accepting logic that didn’t work if a user left the page and came back later.

*Aug 24, 2020*

## Version 0.8.1

[Section titled “Version 0.8.1”](#version-081)

A minor maintenance/bugfix release:

* Fixed a bug in the invitation workflow that prevented invitations from being accepted when creating accounts with social logins. Note that this requires changing the `ACCOUNT_ADAPTER` setting to `'apps.teams.adapter.AcceptInvitationAdapter'`
* Make site branding in the navigation stay visible on mobile devices
* Make it more obvious that `settings.SECRET_KEY` should be overridden.
* Upgrade Django to 3.0.9

*Aug 21, 2020*

## Version 0.8.0

[Section titled “Version 0.8.0”](#version-080)

Stripe billing portal integration is here!

You can now use Stripe’s new [customer portal](https://stripe.com/docs/billing/subscriptions/customer-portal) to manage subscriptions in your app.

Supported operations and configurations include upgrading and downgrading subscriptions, subscription cancellations (both immediately, and at period end), and subscription renewals.

Additional documentation can be found in the [subscription docs](/subscriptions).

Details and other changes:

* Added “manage billing” redirect to subscription pages if you have an active subscription, which goes to the Stripe customer portal
* Added webhook functionality to sync subscription changes and cancellations made via the Stripe portal
* Removed built-in “Cancel” option and supporting code.
* Upgraded `stripe` library to version `2.48.0`
* Removed the `.customer` field from `CustomUser` object. Customers are now always accessed via their associated subscriptions.
* Removed a lot of no-longer-needed code from `SubscriptionModelMixin` related to accessing subscriptions from the `.customer` field. References to `.stripe_subscription` should be changed to simple `.subscription` on the `CustomUser` and `Team` objects.
* Added `avatar` to `CustomUser` admin.
* Fixed bug where “http\://” was incorrectly assigned to the `Site.domain` object (fixes issues using `absolute_url`)

*July 16, 2020*

## Version 0.7.4

[Section titled “Version 0.7.4”](#version-074)

This is another minor release with mostly small fixes and updates to the front end.

* Added number formatting of Salary to object demo examples
* Fixed styling of number form inputs
* Removed unnecessary imports from `assets/index.js`
* Fixed incorrect distinction between `dependencies` and `devDependencies` in `package.json`
* Upgraded React to 16.13.1
* Moved React object lifecycle example to a `react` subfolder
* Started splitting up React object lifecycle demo into multiple files, and refactoring it to use hooks
* Renamed React object lifecycle example bundle file from `object-lifecycle-bundle.js` to `react-object-lifecycle-bundle.js`
* Removed unused “bower\_components” exclusion in `webpack.config`

*July 13 2020*

## Version 0.7.3

[Section titled “Version 0.7.3”](#version-073)

* Upgraded to Django 3.0.7
* Fixed display of renewal details in subscription view to work with the latest Stripe Prices API
* Added ability to resend invitations from the team management page
* Added sort order to team member list (by email address)
* Cleaned up teams JavaSript (removed console logging statements, updated whitespace, removed commented code)

*June 30 2020*

## Version 0.7.2

[Section titled “Version 0.7.2”](#version-072)

* Improved styling of Stripe credit card forms in subscriptions and payments examples
* Fixed bug in subscriptions where not setting a default plan prevented the UI from working
* Fixed bug where monthly subscriptions would not work if you also had a quarterly or 6-month price configured
* Changed the order of some examples in examples home page and navigation

*June 17 2020*

## Version 0.7.1

[Section titled “Version 0.7.1”](#version-071)

* **Added ability to cancel a Subscription directly on the site.** [Demo](https://www.saaspegasus.com/subscriptions/) (you have to create a Subscription first)
* Don’t show password change links if using social authentication (thanks Yaniv!)

*June 11, 2020*

## Version 0.7.0

[Section titled “Version 0.7.0”](#version-070)

Pegasus now supports [Vue.js](https://vuejs.org/)!

Version 0.7 adds a Vue.js implementation of the Object Lifecycle demo so you can start with a foundation of either React or Vue.

Minor changes:

* Added `Membership` inline admin editing to `Teams` model (thanks Troels!)
* Added a few more spacing utility css classes to `utilities.sass`

*June 5, 2020*

## Version 0.6.1

[Section titled “Version 0.6.1”](#version-061)

* Upgrade `requests` to version `0.23.0` to fix installation version conflict.

*May 26, 2020*

## Version 0.6.0

[Section titled “Version 0.6.0”](#version-060)

This release begins the move of Pegasus’s core functionality out of the “pegasus” app and into the user-defined apps. It’s a relatively big release from a code perspective, although there is very little new / changed in terms of functionality.

### Philosophy

[Section titled “Philosophy”](#philosophy)

The philosophy guiding this change is “your starting code base should be as understandable as possible”.

Historically, Pegasus has attempted to separate “Pegasus-owned” files from “user-owned” files. The thinking behind this structure was that Pegasus upgrades and code merges would be as easy as possible since - in theory - users would not need to modify anything in the “Pegasus-owned” space.

In practice, the line between “Pegasus-owned” and “user-owned” was fuzzy, and customizing an application often required editing files in the “Pegasus-owned” space. So the benefit was not realized.

Furthermore, this split caused the initial codebase to be more confusing, since core functionality was split across two places.

### Changelog

[Section titled “Changelog”](#changelog)

Changes related to the restructure above include:

* Moved all base templates from `templates/pegasus/` to `templates/web/`
* Moved team invitation templates from `templates/pegasus/email/` to `templates/teams/email/`
* Merged `pegasus/apps/users` and all related code into `apps/users`
* Merged `pegasus/apps/teams` and all related code into `apps/teams`
* Removed `pegasus/apps/components` and moved code to more specific apps - further details below
* Moved `promote_user_to_superuser` management command into `users` app
* Moved `bootstrap_subscriptions` management command into `subscriptions` app
* Moved `google_analytics_id` context processor to web app
* Moved `meta.py` from pegasus app to web app
* Moved `pegasus/utils/subscriptions.py` to `apps/subscriptions/helpers.py`
* Added `apps.utils` and moved most of `pegasus.utils` there
* Moved `pegasus/decorators.py` to `apps/utils/decorators.py`
* Moved `PegasusBaseModel` to `apps.utils` and renamed to `BaseModel`
* Removed unused `stripe.py` file (replacing functionality with equivalent functions in `djstripe`)
* Removed “Pegasus” from API url names
* Moved non-example JS imports out of `pegasus/Pegasus.js` and into `App.js`
* Lowercased (and kebab-cased) all JS file names for consistency
* Moved sass files from `assets/styles/pegasus`, to `assets/styles/app`
* Renamed various layout classes, e.g. `pegasus-two-column`, `pegasus-message`, etc. to `app-[name]`
* Moved `static../../assets/images/pegasus/undraw/` folder to `static../../assets/images/undraw`
* Removed unused `pegasus/teams/serializers.py` file

Other changes and fixes include:

* Fix accepting an invitation if you’re already signed in
* Remove subscription-related fields from team and user models if not using subscriptions
* Only ship base migration files for users and teams, and have applications manage their own migrations
* Improved checks and error-handling around accepting invitations multiple times
* Upgraded `bulma` CSS framework to `0.8.2`
* Upgraded `node-sass` to `4.14.1`
* Ran `npm audit fix` to update other JS library dependencies
* Upgraded `pip-tools` and other packages in `dev-requirements.txt`
* Added backend check to the payments example, to show how to prevent client-side exploits
* Improve password reset email copy
* Use `$link` color in `$navbar-item-active-color` and `$menu-item-active-background-color`
* Externalized styles on progress bar demo

### A Note on Database Migrations

[Section titled “A Note on Database Migrations”](#a-note-on-database-migrations)

Historically, Pegasus has shipped with complete database migrations. However, maintaining a set of migrations for each possible Pegasus configuration or forcing all configurations to use the same DB schema has proven unwieldy. Thus, migrations are now expected to be managed *outside of Pegasus*.

For new users, the only change is that prior to running `./manage.py migrate` for the first time, you must first run `./manage.py makemigrations`.

For existing users you can either keep your current migrations folder, or you can run `./manage.py makemigrations` and then `./manage.py migrate --fake`. If you have changed the user or team models, then you should keep your current folder.

*May 19, 2020*

## Version 0.5.2

[Section titled “Version 0.5.2”](#version-052)

* Fixed default Postgres DB settings (adding host and port)

* Removed Stripe webhooks from project urls if not using subscriptions

* Fixed but where subscription and teams templates were still being included even if not enabled for a project

* upgrade `celery-progress` to 0.0.10

* Cleaned up progress bar demo

  * Used javascript cookie library for CSRF token
  * Switched from `var` to `const` in a few places
  * Removed debug logging statements

*May 7, 2020*

## Version 0.5.1

[Section titled “Version 0.5.1”](#version-051)

Version 0.5.1 is a minor maintenance release with a few minor bug fixes and bits of cleanup:

* Upgraded Django to 3.0.5
* Fixed bug where certain input types were getting overridden in Django Forms (thanks Yaniv for reporting!)
* Fixed bug with Object Lifecycle and Charts demos not working on Team installations (thanks Greg for reporting!)
* Moved example chart JavaScript to the webpack pipeline and share Api access variables (thanks Greg for the suggestion!)
* Switch `admin.py` files to use the `@admin.register` decorator syntax

*April 17, 2020*

## Version 0.5

[Section titled “Version 0.5”](#version-05)

This is the biggest release to Pegasus since it’s launch. Read below for all the details.

### Subscriptions!

[Section titled “Subscriptions!”](#subscriptions)

Added the [Stripe Subscriptions feature](https://www.saaspegasus.com/content/subscriptions-overview).

Documentation for subscriptions can be [found here](/subscriptions).

#### Model changes

[Section titled “Model changes”](#model-changes)

* Added a `subscription` field to `Team` and `CustomUser` objects, and a `customer` field to `CustomUser`.
* Added `SubscriptionModelMixin` helper class for accessing / checking subscription status on a model.

### Javascript build changes

[Section titled “Javascript build changes”](#javascript-build-changes)

* Added `Pegasus.js` and made different modules available in front end code (see subscriptions upgrade page example usage).

### Sass / CSS changes

[Section titled “Sass / CSS changes”](#sass--css-changes)

* Added `tooltip` utilities.
* Added a few margin helper classes (e.g. `my-1`, `my-2` )

### New Python Library Dependencies

[Section titled “New Python Library Dependencies”](#new-python-library-dependencies)

* [attrs](https://www.attrs.org/en/stable/)
* [dj-stripe](https://dj-stripe.readthedocs.io/en/stable/)

### New JavaScript Library Dependencies

[Section titled “New JavaScript Library Dependencies”](#new-javascript-library-dependencies)

* [js-cookie](https://github.com/js-cookie/js-cookie)

### Small fixes and changes:

[Section titled “Small fixes and changes:”](#small-fixes-and-changes)

* Moved app-specific templates from inside the apps to global templates directory as recommended by Two Scoops of Django
* Remove redundant raw prefix on some `path` url declarations
* Reduced some duplicate access to `team` object when already available via the `request` object.
* Made team permission template tags more consistent with rest of site (also allow access to superusers)
* Removed `PEGASUS_USING_TEAMS` and `pegasus_settings` context processor. All config is now handled at installation time instead of by settings variables.
* Catch Stripe card errors in the payments example
* Upgraded various `npm` packages
* Upgraded Bulma to 0.8.0

### Documentation

[Section titled “Documentation”](#documentation-6)

* Added release notes page (this one)
* Added [subscriptions overview page](/subscriptions)
* Updated “delete teams code” cookbook to reflect latest team changes (all the backend work is now done for you on installation)

*March 30, 2020*

## Version 0.4 and earlier

[Section titled “Version 0.4 and earlier”](#version-04-and-earlier)

Release notes for earlier versions are no longer publicly available.

# Subscriptions

> Implement SaaS subscriptions with Stripe billing, pricing tables, webhooks, customer portals, and per-seat or usage-based pricing models.

## Overview

[Section titled “Overview”](#overview)

Subscriptions in Pegasus have three components which must all be setup in order for them to work correctly.

1. **Stripe Billing data**. This is configured in Stripe.
2. **Local Stripe models**. These are synced automatically from Stripe to your local database, using [`dj-stripe`](https://github.com/dj-stripe/dj-stripe).
3. **Pegasus metadata**. This is configured in `apps/subscriptions/metadata.py` and used to augment the data from Stripe.

The easiest way to set up all three is to follow the guide below.

## Getting Started

[Section titled “Getting Started”](#getting-started)

Complete the following steps in order to set up your first subscription workflow.

### Choose your billing setup

[Section titled “Choose your billing setup”](#choose-your-billing-setup)

If you haven’t already, [set up Pegasus and create an account](/getting-started). In your project settings you will see several options related to subscriptions.

![Subscriptions Project configuration](/_astro/subscriptions-config.dhr47Tfp_1eld1g.webp)

The first option is your *billing model*. Most projects should choose *standard*, which lets you create multiple plans with different monthly or annual prices. Choose *per unit* if you want to charge a variable cost based on the number of units used, for example, if you want to charge for every team-member. [Metered billing](https://stripe.com/docs/billing/subscriptions/usage-based), while not officially supported is largely compatible with the standard model.

The second option is your *pricing UI*. If you’re on a standard model or metered billing, it’s recommended to use Stripe’s [embedded pricing table](https://stripe.com/docs/payments/checkout/pricing-table). If you’re using per-unit billing, it’s recommended to choose “managed by your application”.

If all of this is intimidating, don’t worry! You can always change these things later. If you’re unsure what you want to use, it is recommended to choose “standard” and “embedded pricing table” to start, as that is the simplest setup and works well for most projects.

### Set up your billing model in Stripe

[Section titled “Set up your billing model in Stripe”](#set-up-your-billing-model-in-stripe)

Before setting up your development environment for subscriptions, you’ll need to create your billing model in Stripe. You should do this in a test account for development. You’ll eventually be able to copy everything to production once you’re happy with the set up.

[Stripe’s documentation](https://stripe.com/docs/billing/subscriptions/build-subscriptions?ui=checkout#create-pricing-model) has guidance on doing this. At a minimum you should create at least one product with a “recurring” price. If you want to offer multiple pricing plans, create one product for each plan. If you want to offer both monthly and annual pricing, make sure every product you add includes both a “monthly” and a “yearly” price.

If you are using the Stripe embedded pricing table, you may also want to add product descriptions and [features](https://stripe.com/docs/payments/checkout/pricing-table#product-features), as these will be used on your pricing page.

If you are using the Stripe embedded pricing table, you should also set it up now, following the [Stripe pricing table documentation](https://stripe.com/docs/payments/checkout/pricing-table).

### Set up your development environment

[Section titled “Set up your development environment”](#set-up-your-development-environment)

Once you’ve created your billing model on Stripe, follow these instructions to set up your development environment.

1. Update the `STRIPE_*` variables in your project’s [`.env` file](/configuration/#settings-and-environment-files) to match the keys from Stripe. See [this page](https://stripe.com/docs/keys) to find your API keys.

2. Run `./manage.py bootstrap_subscriptions`. If things are set up correctly, you should see output that includes information about each product / price that you created, and an output starting with `ACTIVE_PRODUCTS = `containing the products you just created. This step will also automatically update your API keys in the Django admin, as described in [dj-stripe’s instructions](https://dj-stripe.dev/api_keys/#adding-new-api-keys).

3. Next, if you are *not* using the Stripe embedded pricing table:

   1. Paste the `ACTIVE_PRODUCTS` output from the previous step into `apps/subscriptions/metadata.py` overriding what is there. Update any other details you want, for example, the “description” and “features” fields.
   2. Optionally edit the `ACTIVE_PLAN_INTERVALS` variable in `apps/subscriptions/metadata.py` if you don’t plan to include both monthly and annual offerings.

4. Alternatively, if you *are* using the Stripe embedded pricing table set the `STRIPE_PRICING_TABLE_ID` variable in your settings/environment to the pricing table ID you created in Stripe.

Now login and click the “Subscription” tab in the navigation. If you’ve set things up correctly you should see a page that looks like this (it will look slightly different if you are using the Stripe pricing table, or a different CSS framework):

![Subscription Example](/_astro/subscription-example.DVF58m4B_CQWsG.webp)

## Configuring the pricing table

[Section titled “Configuring the pricing table”](#configuring-the-pricing-table)

### Using the embedded Stripe pricing table

[Section titled “Using the embedded Stripe pricing table”](#using-the-embedded-stripe-pricing-table)

The following 5-minute video walks through setting up an embedded pricing table in your project.

Here are the detailed instructions:

If you are using the Stripe embedded pricing table, then all customization happens within the Stripe dashboard. You can change the products, names, descriptions, images, and features by editing the products in Stripe with the desired changes. You can also change the color scheme and other options.

After setting up your pricing table, you should add a custom confirmation URL for each product. This tells Stripe to return to your application to properly process the subscription after it is purchased.

To do this, edit your pricing table, and under “Payment settings” change the confirmation page setting to “Don’t show confirmation page (Redirect customers to your website.)”. It should look like this:

![Stripe Confirmation Page](/_astro/stripe-confirmation-page.d7OnvnxW_cKNJs.webp)

In the URL box, put the following address for (for development), leaving `{CHECKOUT_SESSION_ID}` exactly like it is written:

```plaintext
http://localhost:8000/subscriptions/confirm/?session_id={CHECKOUT_SESSION_ID}
```

In production, enable https, and replace `localhost:8000` with the url of our site. E.g.

```plaintext
https://<yoursite>/subscriptions/confirm/?session_id={CHECKOUT_SESSION_ID}
```

*Make sure you check the option to apply this change to all prices* if you’re using monthly and annual pricing. And then *repeat this process for every product in the pricing page*.

**If you don’t make this change, you will not see subscriptions updated unless you are also running webhooks.**

### Using the in-app pricing table

[Section titled “Using the in-app pricing table”](#using-the-in-app-pricing-table)

If you are using the in-app pricing table, your pricing table configuration is handled in `metadata.py`. You can modify `ACTIVE_PRODUCTS` and `ACTIVE_PLAN_INTERVALS` and see how the page changes.

Whenever you make changes in Stripe, you will need to re-run `./manage.py bootstrap_subscriptions`, and incorporate any necessary changes into the `ACTIVE_PRODUCTS` list.

More background and details on this set up can be found in this [Django Stripe Integration Guide](https://www.saaspegasus.com/guides/django-stripe-integrate/).

## Customer Portal

[Section titled “Customer Portal”](#customer-portal)

Pegasus uses the [Stripe Billing Customer Portal](https://stripe.com/docs/billing/subscriptions/customer-portal) for subscription management after subscription creation To set up the portal you must also enable it in the Stripe dashboard, as outlined in [Stripe’s integration guide](https://docs.stripe.com/customer-management/integrate-customer-portal#configure).

After that, most of the set up should be handled by Pegasus.

**To use the portal you will also need to set up webhooks as per below. Updates made in the portal will not show up if webhooks are not running.**

Pegasus ships with webhooks to handle some common actions taken in the billing portal, including:

* Subscription upgrades and downgrades
* Subscription cancellation (immediately)
* Subscription cancellations (end of billing period)

In the Stripe dashboard, you will need to subscribe to a minimum of `customer.subscription.updated` and `customer.subscription.deleted` to ensure subscription changes through the portal make it to your app successfully.

For more advanced use cases, read through [Stripe’s integration guide](https://docs.stripe.com/customer-management/integrate-customer-portal).

## Webhooks

[Section titled “Webhooks”](#webhooks)

Webhooks are used to notify your app about events that happen in Stripe, e.g. failed payments. More information can be found in [Stripe’s webhook documentation](https://stripe.com/docs/webhooks).

Pegasus ships with webhook functionality ready to go, including default handling of many events taken in Stripe’s checkout and billing portals. That said, you are strongly encouraged to test locally using [Stripe’s excellent guide](https://stripe.com/docs/webhooks/test).

### Webhooks in development

[Section titled “Webhooks in development”](#webhooks-in-development)

In development, the easiest way to set up webhooks is with the [Stripe CLI](https://stripe.com/docs/stripe-cli).

First install the CLI and set it up. Then print your CLI secret with:

```bash
stripe listen --print-secret
```

Or with Docker (no install required):

```bash
docker run --network host --rm -it stripe/stripe-cli listen \
  --print-secret \
  --api-key sk_test_<your_key>
```

Then you can set up your webhook endpoint by running:

```bash
./manage.py bootstrap_dev_webhooks --secret <your_secret>
```

This will create a webhook endpoint for `djstripe` in your application. The `bootstrap_dev_webhooks` will also output a stripe command you can then use to listen for webhooks.

It will look something like this, with the `<uuid>` replaced by your own webhook endpoint’s ID:

```bash
stripe listen \
  --forward-to http://localhost:8000/stripe/webhook/<uuid>/"
```

Or in Docker:

```bash
docker run --network host --rm -it stripe/stripe-cli listen \
  --forward-to  localhost:8000/stripe/webhook/<uuid>/ \
  --api-key sk_test_<your_key>
```

### Webhooks in production

[Section titled “Webhooks in production”](#webhooks-in-production)

The webhook setup changed significantly in version 2025.4.1. If you are on version 2025.4.1 or later, follow these steps, which are taken from the [dj-stripe docs](https://dj-stripe.dev/2.9/usage/webhooks/). For versions earlier than 2025.4.1 see the next section.

* As a superuser, visit the Django admin of your site and navigate to djstripe -> Webhook endpoints -> Add webhook endpoint (or /admin/djstripe/webhookendpoint/add/).

* Select your Stripe account, check “Live mode” and verify the Base url matches your server’s domain, e.g. <https://www.example.com>.

* Under “Advanced” verify the API version is correct.

* Under “Advanced”, choose the enabled events you want to listen for. At a minimum you want:

  * `checkout.session.completed`
  * `customer.subscription.updated`
  * `customer.subscription.deleted`
  * You can add other webhooks as well, (or choose `*` to enable all webhooks) but these are the minimum set required for subscriptions and the billing portal to work properly.

* Verify the other settings (the defaults should be fine) and click “Save”.

After completing these steps, visit your [Stripe dashboard](https://dashboard.stripe.com/webhooks) and confirm the new webhook endpoint has been synced to Stripe. Secrets are managed by dj-stripe, and the webhook should be working!

In production, you should not need to run `stripe listen --forward-to localhost:8000/stripe/webhook/` (or the Docker equivalent).

Once webhooks are properly set up, all underlying Stripe data will be automatically synced from Stripe with no additional setup required on your part.

#### Legacy setup before Pegasus 2025.4.1:

[Section titled “Legacy setup before Pegasus 2025.4.1:”](#legacy-setup-before-pegasus-202541)

**These instructions are only for projects running prior to Pegasus version 2025.4.1. For recent projects, use the instructions above.**

* Navigate to this page [Webhooks](https://dashboard.stripe.com/webhooks) (assuming you’re logged into Stripe).
* Toggle off test mode in the top right corner.
* Click on `Add endpoint`.
* In the `Endpoint URL` field, enter the following URL, replacing `yourserver.com` with your server’s domain name. Note: **the trailing slash is required.**
  * `https://yourserver.com/stripe/webhook/`
* Click on `Select Events to Listen To`.
* Search for `checkout.session.completed`, `customer.subscription.updated`, and `customer.subscription.deleted`, and select them. These events are connected by default (see `apps/subscriptions/webhooks.py` for the source code). You can add other webhooks as well, but these are the minimum set required for subscriptions and the billing portal to work properly.
* Write a description if needed and then click `Add endpoint`.
* **Ensure to set `DJSTRIPE_WEBHOOK_SECRET` in your `settings.py` or as an environment variable.** This value can be found in the Stripe dashboard where you configure your webhook and may be referred to as the `Signing Secret`.

### Custom Webhook Handling

[Section titled “Custom Webhook Handling”](#custom-webhook-handling)

You may want to do more than just update the underlying Stripe objects when processing webhooks, for example, notifying a customer or admin of a failed payment.

Pegasus ships with an example of executing custom logic from a webhook in `apps/subscriptions/webhooks.py`. This basic example will mail your project admins when a Subscription is canceled.

More details on custom webhooks can be found in the [dj-stripe documentation](https://dj-stripe.dev/2.9/usage/webhooks/).

## Supporting multiple currencies

[Section titled “Supporting multiple currencies”](#supporting-multiple-currencies)

If you use Stripe’s embedded pricing table you get multi-currency support out of the box. Follow [the Stripe guide](https://stripe.com/docs/payments/checkout/present-local-currencies?platform=multi-currency-prices) to set your products and prices up for multiple currencies.

If you use an in-app pricing table, Stripe will still present your prices to customers in local currencies, but the pricing table itself will display the prices in your default currency.

## Free trials

[Section titled “Free trials”](#free-trials)

You can easily enable free trials using the option in Stripe’s embedded pricing table. Your customers will be able to sign up with their credit cards for a trial and will have the same experience in your application as someone who is paying for the plan. They’ll be able to update their status from the customer portal, and once the trial period ends they will be billed.

If you’re using trials you must set up webhooks to be notified whether the customer subscribes or cancels at the end of their trial.

It is also possible to use free trials without the embedded pricing table. To do so, you need to add a `trial_end` or `trial_period_days` value to the `subscription_data` in `create_stripe_checkout_session`, as described in [the Stripe documentation](https://stripe.com/docs/billing/subscriptions/trials).

## Feature-Gating

[Section titled “Feature-Gating”](#feature-gating)

Pegasus ships with a demo page with a few feature-gating examples, which are available from a new Pegasus installation under the “Subscription Demo” tab.

These include:

1. Changing content on a page based on the user/team’s subscription.
2. Restricting access to an entire page based on the user/team’s subscription.
3. Showing subscription details like plan, payment details, and renewal date.

### Using the `active_subscription_required` decorator

[Section titled “Using the active\_subscription\_required decorator”](#using-the-active_subscription_required-decorator)

One common use-case is restricting access to a page based on the user’s subscription.

Pegasus ships with a decorator that allows you to do this. You can use it as follows:

```python
@login_required
@active_subscription_required
def subscription_gated_page(request, subscription_holder=None):
    return TemplateResponse(request, 'subscriptions/subscription_gated_page.html')
```

If the user doesn’t have an active subscription, they’ll be redirected to the subscription page to upgrade.

You can also restrict access based on a specific plan (or set of plans), as follows:

```python
@login_required
@active_subscription_required(limit_to_plans=["pro", "enterprise"])
def subscription_gated_page(request, subscription_holder=None):
    return TemplateResponse(request, 'subscriptions/subscription_gated_page.html')
```

In this case the user will only be allowed to view the page if they have a pro or enterprise plan.

### Using the `get_feature_gate_check` helper function

[Section titled “Using the get\_feature\_gate\_check helper function”](#using-the-get_feature_gate_check-helper-function)

For more fine-grained control you can use the `get_feature_gate_check` helper function. This takes in two arguments, the `subscription_holder` (usually a User or Team), and optionally the same `limit_to_plans` list above, and returns a `FeatureGateCheckResult`, which includes whether the check passed (subscription holder has a subscription of the right type), and an optional message explaining the answer.

Example usage:

```python
from apps.subscriptions.feature_gating import get_feature_gate_check




def my_view(request):
    check_result = get_feature_gate_check(request.team, ["professional"])
    if check_result.passed:
        do_actions_pro_only()
    else:
        logging.info(f"Pro actions skipped: {check_result.message}")
```

## Per-Unit / Per-Seat Billing

[Section titled “Per-Unit / Per-Seat Billing”](#per-unit--per-seat-billing)

Pegasus supports per-unit / per-seat billing. Choose this option when building your project to enable it. **It is not recommended to use the Stripe embedded pricing table if you are using per-unit billing.**

For Team-based builds the default unit is Team members. For non-Team builds you will have to implement your own definition of what to use for billing quantities.

Here is [a short video walkthrough of this feature](https://youtu.be/v_ayMEj924w).

### Choosing your billing model

[Section titled “Choosing your billing model”](#choosing-your-billing-model)

Refer to the [Stripe documentation](https://stripe.com/docs/products-prices/pricing-models) for how to set this up in your Price model. You can use any of:

* Standard pricing (e.g. $10/user)
* Package pricing (e.g. $50 / 5 new users)
* Tiered pricing (graduated or volume) (e.g. $50 for up to 5 users, $5/user after that)

### Displaying prices on the subscriptions page

[Section titled “Displaying prices on the subscriptions page”](#displaying-prices-on-the-subscriptions-page)

For per-unit billing you can no longer display a single upgrade price since it is dependent on the number of units.

To avoid displaying an “unknown” price when showing the subscription, you can add a `price_displays` field to your `ProductMetadata` objects that takes the following format:

```python
ProductMetadata(
    stripe_id='<stripe id>',
    name=_('Graduated Pricing'),
    description='A Graduated Pricing plan',
    price_displays={
        PlanInterval.month: 'From $10 per user',
        PlanInterval.year: 'From $100 per user',
    }
),
```

This will show “From $10 per user” or “From $100 per user” when the monthly or annual plan is selected, respectively.

#### Per-seat pricing and the embedded pricing table.

[Section titled “Per-seat pricing and the embedded pricing table.”](#per-seat-pricing-and-the-embedded-pricing-table)

**Though it is possible to use the pricing table with per-seat billing, it is not recommended.**

This is because Stripe does not allow you to pass per-seat quantities with the Pricing Table, so if you use the pricing table with per-seat pricing, your users will be able to choose the number of “seats” (quantity) when they check out.

This is different from the expected behavior, which is that your app sets the quantity explicitly based on the number of team members (or your own business logic, for user-based builds). Since Pegasus is set up to automatically update the subscription quantity based on the “usage” in your application, this could result in your users buying a certain number of seats, and then unexpectedly having the price change to the amount they are actually using.

You can disable Pegasus automatically updating the per-seat quantity, and then modify your application’s business logic to be based off the “quantity” property of the user/team’s subscription, though this is not an officially supported workflow.

### Keeping your Stripe data up to date

[Section titled “Keeping your Stripe data up to date”](#keeping-your-stripe-data-up-to-date)

When changes are made that impact a user’s pricing, you will need to notify Stripe of the change. This should happen automatically every 24 hours as long as you have enabled celery and celerybeat. You can also trigger it manually via a management command `./manage.py sync_subscriptions`.

To ensure this command works properly, you must implement two pieces of business logic:

1. You must update the billing model’s `billing_details_last_changed` field any time the number of units has change.
2. You must override the `get_quantity` function on your billing model to tell Stripe how many units it contains.

**If you use Teams with per-seat billing this will be automatically handled for you by default.** All you have to do is run the management command or connect it to a periodic task.

For User-based, or more complex billing models with Teams you will have to implement these changes yourself.

#### A User-based example

[Section titled “A User-based example”](#a-user-based-example)

Here’s a quick example of how you might do this with User-based billing.

Let’s say your app allows users to define workspaces and they are billed based on the number of workspaces they create.

You might have a workspace model that looks like this:

```python
class Workspace(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='workspaces')
    # other workspace fields here
```

Then you would want to update the `billing_details_last_changed` field of the `CustomUser` object every time a workspace was added or removed (step 1, above). That might look something like this, using [Django signals](https://docs.djangoproject.com/en/stable/topics/signals/):

```python
@receiver(post_save, sender=Workspace)
def update_billing_date_on_workspace_creation(sender, instance, created, **kwargs):
    if created:
        instance.user.billing_details_last_changed = timezone.now()
        instance.user.save()




@receiver(post_delete, sender=Workspace)
def update_billing_date_on_workspace_deletion(sender, instance, **kwargs):
    instance.user.billing_details_last_changed = timezone.now()
    instance.user.save()
```

The other piece of code you would need to add is associating the `get_quantity` function on the user with the number of workspaces they have.

You’d want to add a method like this to `CustomUser`:

```python
class CustomUser(SubscriptionModelBase, AbstractUser):
    # other stuff here


    def get_quantity(self):
        return self.workspaces.count()
```

## Stripe in Production

[Section titled “Stripe in Production”](#stripe-in-production)

In development, you will use your Stripe test account, but when it comes time to go to production, you will want to switch to the live account.

This entails:

1. Setting `STRIPE_LIVE_MODE` to `True` in your settings/environment.
2. Populating `STRIPE_LIVE_PUBLIC_KEY` and `STRIPE_LIVE_SECRET_KEY` in your environment.
3. Updating your `ACTIVE_PRODUCTS` to support both test and live mode (see below)

### Managing Test and Live Stripe Products

[Section titled “Managing Test and Live Stripe Products”](#managing-test-and-live-stripe-products)

When you run `bootstrap_subscriptions` Pegasus will generate a list of your `ACTIVE_PRODUCTS` that includes hard-coded Stripe Product IDs. This works great in development, but presents a problem when trying to enable live mode.

One way to workaround this is to replace the hard-coded product IDs with values from your django settings.

E.g. in `apps/subscriptions/metadata.py` change from:

```python
ACTIVE_PRODUCTS = [
    ProductMetadata(
        stripe_id='prod_abc',  # change this line for every product
        slug='starter',
        ...
```

To:

```python
ACTIVE_PRODUCTS = [
    ProductMetadata(
        stripe_id=settings.STRIPE_PRICE_STARTER,  # to something like this
        slug='starter',
        ...
```

Then in your `settings.py` file, you can define these values based on the `STRIPE_LIVE_MODE` setting:

```python
STRIPE_LIVE_MODE = env.bool("STRIPE_LIVE_MODE", False)


STRIPE_PRICE_STARTER = "prod_xyz" if STRIPE_LIVE_MODE else "prod_abc"
```

You will have to do this for each of your products.

## Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

**Stripe is not returning to the right site after accessing checkout or the billing portal.**

There are two settings that determine how Stripe will call back to your site.

If Stripe is returning to the *wrong site entirely* it is likely a problem with your Django `Site` configuration. See the documentation on [absolute URLs](/configuration/#absolute-urls) to fix this.

If Stripe is returning to the correct site, *but over HTTP instead of HTTPS* (or vice versa) then you need to change the `USE_HTTPS_IN_ABSOLUTE_URLS` setting in `settings.py` or a production settings file.

**Subscriptions are not being created in your app when using the embedded pricing table.**

Make sure that you have updated the confirmation page for every product and every price to `https://<yoursite>/subscriptions/confirm/?session_id={CHECKOUT_SESSION_ID}` as described above.

You can also turn on webhooks to fix this, though it’s recommended to use the custom confirmation page to provide a better user experience.

**Stripe webhooks are failing with a signature error.**

If you get an error like “No signatures found matching the expected signature for payload” or similar there are a few things to check:

First, double check all of your API keys and secrets in your environment/settings files. These are:

* `STRIPE_LIVE_PUBLIC_KEY` and `STRIPE_LIVE_SECRET_KEY` (for live mode), or `STRIPE_TEST_PUBLIC_KEY` and `STRIPE_TEST_SECRET_KEY` (for test mode)
* `STRIPE_LIVE_MODE` should match whether you’re in live / test mode.
* `DJSTRIPE_WEBHOOK_SECRET` should match the secret from the Stripe dashboard.

**Getting “DataError: value too long for type character varying(9)” from webhooks**

This is caused by an issue in `dj-stripe` where a database column is not large enough to support values that were added by Stripe in API version xxx.

There are two recommended workarounds to this:

1. Downgrade your Stripe API version. The most recent supported version is `2023-10-16`. Your API version can be found in the “Developers” section of the Stripe dashboard.
2. Manually add a database migration to your project to increase the size of the column. If you build with Pegasus version 2024.10 or later, this migration will be automatically added to your project. Otherwise, see below for instructions on adding it.

Run:

```bash
python manage.py makemigrations web --empty`
```

Then copy the following into the generated file:

```python
class Migration(migrations.Migration):
    dependencies = [
        ("web", "0001_initial"),
        ("djstripe", "0012_2_8"),
    ]


    operations = [
        migrations.RunSQL(
            "ALTER TABLE djstripe_paymentintent ALTER COLUMN capture_method TYPE varchar(255);"
        ),
    ]
```

*You can [read more about this issue and workarounds here](https://github.com/dj-stripe/dj-stripe/issues/2038#issuecomment-2119244742).*

# Using Teams

> Build multi-tenant applications with team-based data models, role-based permissions, and collaborative user management features.

Teams are designed to provide sandboxes for groups of users collaborating on single project. Users can join one or more teams, invite other users to their teams, and give different team members different roles.

Pegasus provides the building blocks to setup a team-based application. Some of those building blocks are documented here.

**Note: all of the following examples assume you have setup Pegasus with teams enabled.**

## Example App

[Section titled “Example App”](#example-app)

Pegasus ships with an optional built-in example application demonstrating the basics of working with team-based models and views.

The example app includes:

1. A data model that belongs to a team.
2. A set of class based views for working with that data model, limited to the context of a team.

#### Third party examples

[Section titled “Third party examples”](#third-party-examples)

A Pegasus user Peter Cherna has created some more [example applications](https://github.com/pcherna/pegasus-example-apps/) that demonstrate additional team-based examples, including functional views, pagination, APIs and working with “global” objects.

They are a great place to start for inspiration and getting something up and running quickly!

*Note: the example apps are not officially sanctioned/supported by Pegasus—though features from them will be continually incorporated into future releases.*

## Data Models

[Section titled “Data Models”](#data-models)

Teams use three primary models - `apps.users.CustomUser`, `apps.teams.Team`, and `apps.teams.Membership`.

The `Membership` model uses [Django’s “through” support](https://docs.djangoproject.com/en/stable/ref/models/fields/#django.db.models.ManyToManyField.through) to extend the `User`/`Team` relationship with additional fields.

By default, a `role` field is added to represent the `User`’s role in the `Team` (admin or member).

### Team-based models

[Section titled “Team-based models”](#team-based-models)

Data models that “belong” to a Team can subclass `BaseTeamModel`.

In addition to always including a `.team` field, this model also has an additional manager called `for_team` that will automatically filter querysets based on the current team (set by the [context variable](#team-context-variable)). This is useful to use to provide strict access to your data models (if they should never be accessed outside a team).

These two statements are approximately equivalent:

```python
MyTeamModel.for_team().filter(...)
MyTeamModel.objects.filter(team=get_current_team(), ...)
```

See the example app for additional usage examples. For more strict logic around team queries, see [the strict team access section](#strict-team-access).

## Team Context variable

[Section titled “Team Context variable”](#team-context-variable)

From version 2025.11, a [ContextVar](https://docs.python.org/3/library/contextvars.html) is available to keep track of the current team.

The team is set automatically in views by the [middleware](#middleware) or by using the `current_team` context manager like this:

```python
a_team = Team.objects.get(slug='a-team')
with current_team(team):
    # get_current_team() will return the `a_team` object inside this block
    call_code_that_uses_the_curent_team()
    MyModel.for_team().all()  # only returns objects with `team=a_team`
```

## Team-based Views

[Section titled “Team-based Views”](#team-based-views)

At its core, all Team-based views need the following:

### Urls

[Section titled “Urls”](#urls)

See `apps.team.urls` for an example of how to set these up in your apps, and your main `apps.{project}.urls` file for how to add them to your site’s URLs.

Anything that goes into `team_urlpatterns` in `apps.{project}.urls` will automatically be added under the URL `https://example.com/a/<team_slug>/`. The `team_slug` is a human-readable, URL-friendly version of the team name that is auto-generated for you.

### Middleware

[Section titled “Middleware”](#middleware)

The `apps.teams.middleware.TeamsMiddleware` must be included in the list of middleware. It must be placed after `django.contrib.auth.middleware.AuthenticationMiddleware`. The purpose of this middleware is to set `request.team` and `request.team_membership` based on the current request. It will attempt to load the team as follows:

* From the `team_slug` in the request path if available
* From the current session if available
* From the user’s list of teams if available

If the `team_slug` is available from the request path but it does not match a team that the user has access to then the request will terminate with a 404. Apart from this the middleware does not do any validation of the team or the team membership. That is left to the decorators described below.

### Views

[Section titled “Views”](#views)

See `apps.team.views` for example team views. All views that are referenced under `team_urlpatterns` must contain `team_slug` as the first argument.

In addition to adding this field, you will likely want to use one of the built-in permission decorators (see below) to ensure the logged-in user can access the selected team.

Additionally, you will have to scope any data model access to the relevant Team in any Database/ORM queries you make inside your views.

## Permission Control

[Section titled “Permission Control”](#permission-control)

Pegasus includes two convenience decorators for use in team views. These can be found in `apps.teams.decorators`.

#### The `login_and_team_required` decorator

[Section titled “The login\_and\_team\_required decorator”](#the-login_and_team_required-decorator)

This decorator can be used to ensure that the logged in user has access to the team in the view. It requires your view takes in a `team_slug`, as in the example views. It can be used in functional views like this:

```python
@login_and_team_required
def a_team_view(request, team_slug):
    # other view logic here
    return render(request, 'web/my_template.html', context={
        'team': request.team,
    })
```

Or in class-based views like this:

```python
@method_decorator(login_and_team_required, name='dispatch')
class ATeamView(View):
    # other view details go here
```

If the current user does not have access to the team they will see a 404 page. If no user is logged in they’ll be redirected to a login view, just like the `login_required` decorator.

### The `team_admin_required` decorator

[Section titled “The team\_admin\_required decorator”](#the-team_admin_required-decorator)

The `team_admin_required` decorator works just like the `login_and_team_required` decorator, except in addition to checking team membership the role is also checked and if the user doesn’t have “admin” access they will not be able to access the view.

### The `LoginAndTeamRequiredMixin` and `TeamAdminRequiredMixin` classes

[Section titled “The LoginAndTeamRequiredMixin and TeamAdminRequiredMixin classes”](#the-loginandteamrequiredmixin-and-teamadminrequiredmixin-classes)

These mixins provide the same functionality as the decorators, but are designed to work with Django’s generic class-based views. They can be used like this:

```python
class ATeamModelListView(LoginAndTeamRequiredMixin, ListView):
    model = MyModel
```

See the example app for more details.

### Template tags

[Section titled “Template tags”](#template-tags)

In addition to the decorators, you can also use template tags to check user / team access from a template.

This can be useful for hiding/showing certain content based on a user’s team role. The `is_member_of` filter can be used to check team membership, and the `is_admin_of` filter can be used to check if *a* user is a team admin. For example, the following will show only if the logged in user is an admin of the associated team:

```jinja
{% load team_tags %}
{% if team and request.user|is_admin_of:team %}
  <p>You're an admin of {{team.name}}.</p>
{% elif team and request.user|is_member_of:team %}
  <p>You're a member of {{team.name}}.</p>
{% else %}
  <p>Sorry you don't have access to {{team.name}}.</p>
{% endif %}
```

### Adding Roles

[Section titled “Adding Roles”](#adding-roles)

The permission system is designed to be simple enough to easily use, but extensible enough that you can customize it to match your project’s needs.

Here’s how you can add a new role to your app:

#### 1. Define the New Role in `roles.py`

[Section titled “1. Define the New Role in roles.py”](#1-define-the-new-role-in-rolespy)

First, you need to add your new role constant and update the choices in `apps/teams/roles.py`:

```python
ROLE_ADMIN = 'admin'
ROLE_MEMBER = 'member'
ROLE_MODERATOR = 'moderator'  # Add your new role here


ROLE_CHOICES = (
    # customize roles here
    (ROLE_ADMIN, 'Administrator'),
    (ROLE_MEMBER, 'Member'),
    (ROLE_MODERATOR, 'Moderator'),  # Add your new role choice here
)
```

Technically, this is all that’s needed, as this will cause the role to show up in the invitation UI and allow it to be used in team memberships.

However, you’ll probably also want to use the role in your app permissions system. To do that, you should also add a helper function for the new role if you want to use it in permission checks:

```python
def is_moderator(user: CustomUser, team) -> bool:
    if not team:
        return False


    from .models import Membership
    return Membership.objects.filter(team=team, user=user, role=ROLE_MODERATOR).exists()
```

#### 2. Update the Membership Model (if needed)

[Section titled “2. Update the Membership Model (if needed)”](#2-update-the-membership-model-if-needed)

The `Membership` model in `models.py` already uses `roles.ROLE_CHOICES` for its role field, so it will automatically pick up your new role. However, you might want to add a helper method to the `Membership` model:

```python
class Membership(BaseModel):
    # ... existing code ...


    def is_moderator(self) -> bool:
        return self.role == roles.ROLE_MODERATOR
```

#### 3. Add a new decorator (if needed)

[Section titled “3. Add a new decorator (if needed)”](#3-add-a-new-decorator-if-needed)

If you’d like to use the role in decorators, similar to `@team_admin_required` you can do so by adding a new function to `apps/teams/decorators.py`:

```plaintext
# import the and use function you created in step 1
from .roles import is_admin, is_member, is_moderator


def team_moderator_required(view_func):
    return _get_decorated_function(view_func, is_moderator)
```

#### 4. Use the role

[Section titled “4. Use the role”](#4-use-the-role)

You’ll need to update any views or logic that handle role-based permissions, by calling the helper functions and decorators you’ve defined above.

The specifics here will depend on the role you’ve added and the goals you’re trying to achieve with it.

## Cookbooks

[Section titled “Cookbooks”](#cookbooks)

### Strict team access

[Section titled “Strict team access”](#strict-team-access)

If you want to ensure that your data models are only ever accessible in the context of a team, you can change the declaration of the manager classes on `BaseTeamModel` as follows:

```python
class BaseTeamModel(BaseModel):
    """
    Abstract model for objects that are part of a team.
    """


    team = models.ForeignKey(Team, verbose_name=gettext("Team"),
                             on_delete=models.CASCADE)


    # rename the global manager to `all_objects`.
    # This will be used in the Django admin, but any calling code
    # using `.objects` will automatically filter by team.
    all_objects = models.Manager()


    # Override `.objects` with the TeamScopedManager to always filter
    # queries by the current team.
    objects = TeamScopedManager()




    class Meta:
        abstract = True
```

You can also set `settings.STRICT_TEAM_CONTEXT = True` to fail hard if `.objects` is ever called without a valid team set.

If you make this change, you never need to add `.filter(team=team)` to any of your queries, as the filter will be applied automatically anytime you reference `TeamModel.objects`.

### Partially using teams

[Section titled “Partially using teams”](#partially-using-teams)

Many projects might want to use teams in the background but hide them from users. This can be useful in certain scenarios:

* If you know you want to use teams eventually, but haven’t built out support for them yet.
* If your application has different user types, some of which belong to teams and some of which don’t.

The recommended way to handle this situation is to **enable teams in Pegasus, but hide/restrict them in the UI**. In this world, all users will still belong to a default team (which is created for them automatically), and all models are associated with teams. However, the concept of teams will be hidden from users until you decide to make them visible.

This allows you to easily “turn on” teams when you are ready, or migrate a user from a “non-team” to a “team” account, while being able to use the same underlying business logic and not have to deal with complicated data migrations.

To achieve this, you should do something like the following:

1. Build your application with teams enabled. This will provide the data models and URL scaffolding to work with teams, and make using teams later much easier.
2. Hide the `team_name` field from the signup form (`signup.html`), and let teams be auto-created for new users.
3. Hide the team-related items from the application navigation (entry point is `app_nav.html`).
4. (Optional) Hide/remove out the team-based url mappings (entry point is `teams/urls.py`). Do this if you don’t want people to be able to access team-related functionality even if they navigate to the right URL in the browser.
5. Continue building your application using the team-based models and URL patterns, but don’t expose them to the user.

If you follow these steps it should be relatively easy to expose teams down the line instead of having to deal with a complicated migration. That process will mostly involve un-hidng the team functionality that was hidden.

Supporting team and non-team users

If you have different categories of users, some on teams and some not, then instead of hiding the functionality mentioned above, you should instead conditionally enable it based on the type of user that is logged in.

# Information about Templates

> Overview of Django template structure and organization in Pegasus projects for building consistent user interfaces.

*This documentation is a work in progress*

All Pegasus templates are found in `/pegasus/templates/`. These include Pegasus’s own templates, as well as overridden templates from other apps.

Pegsaus’s templates are found in `/pegasus/templates/pegasus`.

The `app` directory contains templates within the application, e.g. after sign in.

Any `components` subdirectory contains partial templates relevant to that directory. E.g. `app/components` contains partial templates used within the application.

# Upgrading and Changing your Project Settings

> Upgrade Pegasus projects to new versions using GitHub integration, git branches, or patch files with conflict resolution strategies.

There are several ways to update your Pegasus project. These methods can be used to upgrade your project to a new Pegasus version, or when changing anything in your project configuration.

## Using the Github integration (recommended)

[Section titled “Using the Github integration (recommended)”](#using-the-github-integration-recommended)

The easiest way to upgrade your project is to use the built-in Github integration. If you created your project with Github, you should be able to make any changes you want to your project configuration and then create a pull request with the updated code from the “Download” page.

If you did not create your project with the Github you can still use this method. First follow the instructions for [connecting an existing project to Github](/github/#connecting-an-existing-project-to-github). After completing that step, you should be able to submit updates to your project via pull request, just like above.

You can watch a demo of this set up here:

Note: Whenever you merge Pegasus pull requests you should **use the Github option to “Create a merge commit”**. Do NOT use “Squash and merge” or “Rebase and merge”, as they could prevent future updates from merging cleanly into your project.

## Manually, using branches

[Section titled “Manually, using branches”](#manually-using-branches)

If you don’t want to, or can’t, use the Github integration, you can manually upgrade your project with git branches. Note that this is a longer and more complicated process than using the Github integration, which handles most of these steps for you.

With this option you maintain a “pure” Pegasus branch in your repository with no other modifications. Then, you merge this branch into your main app when you upgrade.

This process is outlined below, and also in the below screencast which shows a live example on a real Pegasus project.

Here are the steps to take:

### 1. Create a branch for the upgrade

[Section titled “1. Create a branch for the upgrade”](#1-create-a-branch-for-the-upgrade)

First [checkout the first commit](https://stackoverflow.com/questions/43197105/how-do-you-jump-to-the-first-commit-in-git) in your repository and create a new branch from there.

After finding and checking out the initial commit, run:

```bash
git branch pegasus
git checkout pegasus
```

*Note: if you created the `pegasus` branch when you set up your codebase you can skip this step. Alternatively, if you don’t have any commit with pure pegasus code, see the instructions at the bottom of this page to create one.*

Next, make sure the branch is up-to-date with your current Pegasus version:

1. Download your Pegasus project on your *current* version and unzip the code.
2. Copy the `.git` folder from your main project into the downloaded codebase.
3. Make sure you are on the `pegasus` branch (`git checkout pegasus`)
4. Commit all changes (`git add .` then `git commit -am "ready to upgrade"`)

### 2. Upgrade the code in the branch

[Section titled “2. Upgrade the code in the branch”](#2-upgrade-the-code-in-the-branch)

1. Upgrade your project on saaspegasus.com
2. Download the latest codebase and unzip the code.
3. Copy the `.git` folder from step 1 into this new folder.
4. Commit all changes (`git add .` then `git commit -am "upgrade to latest Pegasus"`)

### 3. Merge into your main branch

[Section titled “3. Merge into your main branch”](#3-merge-into-your-main-branch)

1. Checkout the (latest/current) main branch (`git checkout main`)
2. Merge the code (`git merge pegasus`)

Alternatively you may wish to do this in a new branch and then submit a pull request to the main branch from there:

1. Create a new branch off of the main branch (`git checkout main; git checkout -b upgrade-pegasus`)
2. Merge the code (`git merge pegasus`)

In the merging step you should look at the modifications being made, and you may have to manually resolve conflicts that come up. You may also need to run `./manage.py makemigrations` to create any database migrations that were not included with Pegasus.

## Manually, using patches (if you can’t use Github or branches)

[Section titled “Manually, using patches (if you can’t use Github or branches)”](#manually-using-patches-if-you-cant-use-github-or-branches)

You can also follow a similar process to the above using Git patches. Patches do not require working in the same repository or having a previously created branch.

At a high level you will:

1. Create a patch file containing the changes in the upgrade.
2. Apply the patch to your app.

Here we’ll walk through the steps in more detail.

### 1. Creating the patch file

[Section titled “1. Creating the patch file”](#1-creating-the-patch-file)

Follow these steps to create your patch file:

1. Download a “clean” version of your Pegasus project on your *current* version, and commit it to a git branch or repository.
2. Upgrade your Pegasus version (or change your configuration), and download the new codebase.
3. Copy your `.git` directory from your “clean” project in step 1 into your new project in step 2. E.g. `cp -r path/to/yourapp/.git path/to/newapp/`.
4. In your new project directory, *commit all of the changes* in a single commit.
5. Create a patchfile for the commit using [git-format-patch](https://git-scm.com/docs/git-format-patch). The recommended command to run is `git format-patch -1 HEAD`.

You should now see a file in your repository root with a name like `0001-branch-details.patch`. This is your patch file.

### 2. Applying the patch file

[Section titled “2. Applying the patch file”](#2-applying-the-patch-file)

Now return to your main branch in your application’s repository.

First, use [git-apply](https://git-scm.com/docs/git-apply) to apply the patch. The recommended command to run is:

```bash
git apply --ignore-space-change --ignore-whitespace --reject /path/to/<patchname>.patch
```

substituting the path/name of the patchfile created above.

This command will do a best-effort application of the patch.

For each affected file:

1. If updates could be applied cleanly, the file will be updated with the contents of the applied patch.
2. If updates could not be applied cleanly, a new diff file called `<filename>.rej` will be created, showing the diff that could not be applied.

If the file was partially updated then the file will be modified *and* the remaining changes will be visible in the `<filename>.rej` file.

The last step of the upgrade process is to go through each file and:

1. If the file has been modified, look at the modifications, see if you want them, and commit/reject them as necessary.
2. If the file has a `<filename>.rej` file, look at the proposed diff and see if you want to manually apply it, or ignore it.

After you have merged all changes to a file, you should delete the `<filename>.rej` file.

To understand the format of the `<filename>.rej` files, take a look at the [unified diff format](https://en.wikipedia.org/wiki/Diff#Unified_format). Basically changes will look like the below, with a line starting with a minus sign, indicating a removal, and a plus sign indicating an addition.

In this example, the type annotations were added to the function signature:

```bash
-def is_member(user, team):
+def is_member(user: CustomUser, team: apps.teams.models.Team) -> bool:
```

## Conflict Resolution Tips and Tricks

[Section titled “Conflict Resolution Tips and Tricks”](#conflict-resolution-tips-and-tricks)

The most time-consuming part of an upgrade is typically resolving conflicts between changes you’ve made and changes in the updated Pegasus release. Here are some tips and tricks for managing this process.

### Make sure resolutions are recorded

[Section titled “Make sure resolutions are recorded”](#make-sure-resolutions-are-recorded)

Git has a feature called [rerere](https://git-scm.com/book/en/v2/Git-Tools-Rerere), which stands for “reuse recorded resolution”. This feature allows you to ask Git to remember how you’ve resolved a conflict so that the next time it sees the same conflict, Git can resolve it for you automatically. Enabling this feature will make future merges much smoother as each conflict will only have to be resolved once.

The easiest way to ensure rerere is enabled is to use the Github integration. If that’s not possible, you can enable it locally by running:

```bash
$ git config --global rerere.enabled true
```

### Resolving Database Migrations

[Section titled “Resolving Database Migrations”](#resolving-database-migrations)

It can be quite common for there to be conflicting database migrations during an upgrade. This can happen when Pegasus modifies data models, you change your project settings in a way that updates models, or you customize Pegasus models in your own code.

To resolve any issues with database migrations, follow the following steps:

1. Always commit your migration files to source control. This makes it easier to have a consistent state across environments and builds.
2. Before doing an upgrade, make sure your project migrations are up to date (`manage.py makemigrations` should do nothing).
3. After doing an upgrade, if Pegasus adds or changes any migration files, *discard those changes*.
4. After merging the code and discarding any changes to migrations introduced by Pegasus, re-run `manage.py makemigrations` on the upgraded code, and commit the result to source control.
5. Run `manage.py migrate` to update the database.

Basically, **you should always keep your migration history and throw away any changes Pegasus proposes to existing migration files.** Then re-run `makemigrations` on the merged code.

### Resolving Python Package “generated” files (e.g. `uv.lock`)

[Section titled “Resolving Python Package “generated” files (e.g. uv.lock)”](#resolving-python-package-generated-files-eg-uvlock)

Python packages in Pegasus have lock files that are dynamically generated from other files:

* If you’re using uv, your `uv.lock` is generated from `pyproject.toml`.
* If you’re using pip-tools, your `requirements.txt` is generated from `requirements.in`.

In either case, the easiest way to resolve the conflicts in these files is:

1. *Merge* the source file (`pyproject.toml` or `requirements.in`).
2. Accept all of SaaS Pegasus’s proposed changes to the generated file. While merging your main branch to the pegasus update branch you can run `git checkout --ours uv.lock` to achieve this.
3. Regenerate the generated file, using `uv sync` or `pip-compile`.
4. Manually inspect the new library versions and update them as needed.

The end result of this should be that you get all of Pegasus’s pinned versions, and then manually choose which of your own dependencies (if any) to update.

### Resolving bundled static files

[Section titled “Resolving bundled static files”](#resolving-bundled-static-files)

Conflicts in any built static files should be resolved by:

1. Deleting the files entirely.
2. Re-running `npm run build` / `npm run dev` and committing the result.

## Post-merge steps

[Section titled “Post-merge steps”](#post-merge-steps)

After upgrading you may also need to reinstall requirements (`pip install -r requirements.txt`), npm packages (`npm install`), etc. depending on what has changed.

You will also need to rebuild your front end if you’ve made any changes there (`npm run dev` or `npm run build`)

If you are using docker you can use the ‘upgrade’ make target to do this:

```bash
make upgrade
```

This will rebuild the Docker images and create and run any database migrations that are needed. **Note: your web container needs to be running when you run this or it will fail.**

## If you don’t have a “pure” Pegasus branch

[Section titled “If you don’t have a “pure” Pegasus branch”](#if-you-dont-have-a-pure-pegasus-branch)

In some cases you may not have a “clean” Pegasus branch. This could happen if you did substantial development before your first commit, merged Pegasus into another project, or did several upgrades.

In this case you can fake a pure Pegasus branch by taking the following steps. *Note: this process destroys `git blame` for most of your project.*

1. Save your current code (from the “main” branch).
2. Make a new branch (e.g. called “pure-pegasus”)
3. Download your codebase from saaspegasus.com on the *last release your project used/upgraded to*.
4. Put the unmodified download of Pegasus 2022.3 onto that branch, without any of your own code. The easiest way to do that is to copy the `.git` folder into your downloaded project and immediately commit the result. This will “brutally” overwrite all your customizations in your git history. *Note this commit id.*
5. Then repeat this process, but instead, do the reverse. Copy the `.git` folder from the Pegasus download back into your (unmodified) copy of the `main` code and again commit the result. This will create a single commit containing all customizations you’ve made to your project.
6. Review this code and merge it back into `main`. If you did everything correctly you should have two huge commits but the pull request will contain no changes.

After this process git will believe that the pure pegasus code is fully merged to `main`. You can then use the commit id you noted in step 4 as the starting point for your upgrade ([step 1](#1-create-a-branch-for-the-upgrade)), and jump to [step 2 above](#2-upgrade-the-code-in-the-branch).

# Wagtail CMS

> Add content management system capabilities with Wagtail CMS for blogs, marketing pages, and rich editorial experiences.

[Wagtail](https://wagtail.org/) is a powerful CMS (Content Management System) built on top of Django. You can use it to create rich websites that can be edited directly via an authoring admin interface without writing any code. It’s great for creating marketing sites, blogs, and other mostly-static content.

Pegasus optionally ships with a built-in Wagtail instance that can be used as a starting point for adding a content section and blog to any Pegasus app.

## Video Overview

[Section titled “Video Overview”](#video-overview)

This video provides an overview of the Pegasus/Wagtail functionality:

## Pegasus and Wagtail

[Section titled “Pegasus and Wagtail”](#pegasus-and-wagtail)

If you want to try Wagtail make sure you enable the “Use Wagtail” option in the Pegasus codebase creator.

After you set up your application run:

```bash
./manage.py bootstrap_content
```

to initialize a few pages of content. If you use Docker, the `make init` target will do this automatically for you.

Out-of-the-box, Pegasus will create a “content” are of your site (available at the `/content/` URL), a blog index page (available at `/content/blog/`) and a few example blog posts. All your content can be edited via the Wagtail admin UI (available to superusers at `/cms/` by default).

The data models for your app’s content are in the `apps/content/` folder, and can be modified or extended in the `models.py` folder there.

For more information on Wagtail, check out their [excellent documentation](https://docs.wagtail.org/).

## Adding Blog Posts

[Section titled “Adding Blog Posts”](#adding-blog-posts)

For blog posts to show up properly, their parent page should be the “Blog” index page, and their type should be “Blog page”.

You can add new blog posts by following these steps:

1. Open the Wagtail admin at the `/cms/` url.
2. In the sidebar, click on “Pages” and then the arrow (>) next to “Welcome to your content area!”, then click on “Blog”.
3. On the Blog page, click “add child page” and choose the “Blog page” option.
4. Fill in the details of your blog post
5. On the bottom of the page, click the up arrow (^), and click “Publish”.

## Customizing Wagtail

[Section titled “Customizing Wagtail”](#customizing-wagtail)

Pegasus’s default wagtail set up is intentionally bare-bones and is meant to provide a starting point for hosting a simple blog attached to your site.

Wagtail can be used to build any complicated site and UI you can imagine. One of the most powerful features in Wagtail is the [`StreamField` functionality](https://docs.wagtail.org/en/stable/topics/streamfield.html) which allows you to combine other Wagtail components into a “stream-like” UI. Your blogs and content pages will have a basic implementation using `StreamField` to get your started.

### Wagtail CRX (CodeRed Extensions)

[Section titled “Wagtail CRX (CodeRed Extensions)”](#wagtail-crx-codered-extensions)

Some Pegasus customers recommend [Wagtail CRX](https://github.com/coderedcorp/coderedcms) as a great way to build more complicated websites with Wagtail. Wagtail CRX ships with a large number of components that can be used in StreamFields to build rich, dynamic content.

The previous version of Wagtail CRX was called CodeRed, it only supported Bootstrap version 4. Wagtail CRX now supports Bootstrap 5 (the version used by Pegasus).

### Internationalization

[Section titled “Internationalization”](#internationalization)

Pegasus ships with Wagtail fully configured to support internationalization using the `wagtail.locales` and `wagtail.contrib.simple_translation` apps bundled with Wagtail.

There are [alternative plugins](https://docs.wagtail.org/en/stable/advanced_topics/i18n.html#translation-workflow) available which provide more advanced translation support if necessary.

By default, Wagtail is configured to use the same set of languages as Django:

```python
LANGUAGES = WAGTAIL_CONTENT_LANGUAGES = [
    ('en', 'English'),
    ('fr', 'French'),
]
```

Full details on Wagtail localization can be found in the Wagtail [documentation](https://docs.wagtail.org/en/stable/advanced_topics/i18n.html).

Details on the Pegasus configuration for internationalization can be found on the [internationalization](/internationalization) page.

## Alternatives to Wagtail

[Section titled “Alternatives to Wagtail”](#alternatives-to-wagtail)

Some companies prefer to manage their marketing sites completely separate from their application. In this scenario it’s recommended to create a separate marketing site using something like Wordpress, Webflow, Wix, Squarespace, or any number of other options. You can host this site at `yourdomain.com` and then host your Pegasus app separately at `app.yourdomain.com` (or similar).

If you choose to set up your content this way, you should build Pegasus without wagtail.

# AI Integrations for Development

> Set up AI-powered coding assistants with Cursor, Claude Code, and Junie, including rules files and MCP tools for enhanced Pegasus development workflow.

As of version 2025.4, Pegasus includes tooling for integrating with AI-powered coding assistants and tools. These will be constantly edited, expanded on, and improved as the community is able to provide more feedback on them.

## Video overview

[Section titled “Video overview”](#video-overview)

See below for a demo of how you can use these tools to help you with development.

## LLM-Friendly Documentation

[Section titled “LLM-Friendly Documentation”](#llm-friendly-documentation)

This documentation has llm-friendly markdown files that can be copy/pasted or linked to in any LLM or AI-coding assistant.

There is an [llms.txt](/llms.txt) index file with further links to other files you can use, including the [llms-small.txt file](https://docs.saaspegasus.com/llms-small.txt) (a compact version of the documentation with the essentials), and the [llms-full.txt file](https://docs.saaspegasus.com/llms-full.txt), with the complete documentation.

All llm files are formatted in markdown.

## Rules Files

[Section titled “Rules Files”](#rules-files)

Pegasus ships with a set of rules files that are designed to be used with coding assistants. These rules are broken out into various sections---e.g. architecture, general guidelines, and guidelines for specific programming languages and frameworks. The rules have been custom developed for Pegasus applications and contain best-practices and information for building on Pegasus.

When the tool supports it (e.g. in Cursor), these rules files will be organized and labeled in ways that allow for them to be automatically included in the appropriate contexts.

You can edit your rules freely after downloading your project. They are provided as a quick way to get started.

## MCP

[Section titled “MCP”](#mcp)

Pegasus also includes a default MCP setup containing two tools, a database inspector (Postgres builds only), and a web browser. You can use these tools to give your AI assistants access to your database + schema and let them work directly with your application in a browser.

See the demo video above for more detail.

## Working with Cursor

[Section titled “Working with Cursor”](#working-with-cursor)

[Cursor](https://www.cursor.com/) is an AI code editor (IDE). If you enable the Cursor integration, your rules files will be saved to the `/.cursor/rules/` directory and will be labeled to be automatically included based on the context. For example, the Python coding guidelines will be included anytime you’re editing a `.py` file.

The MCP setup for Cursor will be saved to `.cursor/mcp.json`, and should be discoverable by Cursor there.

You can modify the rules files and MCP set up in your Cursor settings or by editing the files by hand.

## Working with Claude Code

[Section titled “Working with Claude Code”](#working-with-claude-code)

[Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) is a command-line coding assistant built by Anthropic. If you enable the Claude code integration, your rules will be collapsed into a single, organized `CLAUDE.md` file for Claude to use.

Additionally, the MCP setup will be saved to `.mcp.json` and should be automatically discovered by claude.

### The Github Workflow file

[Section titled “The Github Workflow file”](#the-github-workflow-file)

You can also optionally enable a Github workflow file for Claude. When this is enabled, you will be able to mention @claude on any Github issue or pull request to trigger a claude code update.

In order for this to work, you will have to add an `ANTHROPIC_API_KEY` to your repository secrets. You can learn more in the [Claude code docs](https://docs.anthropic.com/en/docs/claude-code/github-actions) and [Github secrets docs](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions).

## Working with Junie

[Section titled “Working with Junie”](#working-with-junie)

[Junie](https://www.jetbrains.com/junie/) is the coding assistant built by JetBrains (makers of PyCharm). If you enable the Junie integration, your rules will be collapsed into a single, organized `.junie/guidelines.md` file for Junie to use.

## Other tools

[Section titled “Other tools”](#other-tools)

If you’re using a different tool, it is recommended to choose one of the two above when building your project and then copy the files to wherever your tool expects them. Choose “Cursor” if you want the rules files split up, and “Claude” if you prefer a single rules file.

Also, if you’d like support or help configuring a different tool, email <support@saaspegasus.com> and let me know!

# Image Models

> Generate images with AI models including DALL-E-2, DALL-E-3, and Stability AI using OpenAI and Stability AI API keys in your Django application.

Pegasus includes an optional example app for generating images with multiple different models, including [Dall-E-2](https://openai.com/index/dall-e-2) and [Dall-E-3](https://openai.com/index/dall-e-3) and [Stability AI](https://stability.ai/) (Stable Diffusion 3).

## Configuration

[Section titled “Configuration”](#configuration)

To use the Dall-E models, you must set `OPENAI_API_KEY` in your environment, and to use Stability AI, you must set `STABILITY_AI_API_KEY`.

You can choose which model you want to use from the dropdown on the image generation page.

# LLMs and Chat

> Integrate LLM chat interfaces with OpenAI GPT models, Claude, or local models using Ollama. Supports streaming, async APIs, and multiple authentication methods.

Pegasus comes with an optional Chat UI for interacting with LLMs. This section covers how it works and the various supported options.

## Configuring LLM

[Section titled “Configuring LLM”](#configuring-llm)

You can configure the models you want to use by setting the `LLM_MODELS` and `DEFAULT_LLM_MODEL` values in your `settings.py`. For example:

```python
LLM_MODELS = {
    "gpt-3.5-turbo": {"api_key": env("OPENAI_API_KEY", default="")},
    "gpt-4o": {"api_key": env("OPENAI_API_KEY", default="")},
    "claude-3-opus-20240229": {"api_key": env("ANTHROPIC_API_KEY", default="")},
    "ollama_chat/llama3": {"api_base": env("OLLAMA_API_BASE", default="http://localhost:11434")},  # requires a running ollama instance
    "xai/grok-4-fast-reasoning": {"api_key": env("GROK_API_KEY", default="")},
}
DEFAULT_LLM_MODEL = env("DEFAULT_LLM_MODEL", default="gpt4o")
```

The chat UI will use whatever is set in `DEFAULT_LLM_MODEL` out-of-the-box, but you can quickly change it to another model to try different options.

For further reading, see the documentation of the [litellm Python API](https://docs.litellm.ai/docs/completion), and [litellm providers](https://docs.litellm.ai/docs/providers).

## Running open source LLMs

[Section titled “Running open source LLMs”](#running-open-source-llms)

To run models like Mixtral or Llama3, you will need to run an [Ollama](https://ollama.com/) server in a separate process.

1. [Download](https://ollama.com/download) and run Ollama or use the Docker [image](https://hub.docker.com/r/ollama/ollama)

2. Download the model you want to run:

   ```bash
   ollama pull llama3
   # or with docker
   docker exec -it ollama ollama pull llama3
   ```

   See the [documentation](https://docs.litellm.ai/docs/providers/ollama) for the list of supported models.

3. Update your django settings to point to the Ollama server. For example:

   ```python
   LLM_MODELS = {
       "ollama_chat/llama3": {"api_base": "http://localhost:11434"},
   }
   DEFAULT_LLM_MODEL = "ollama_chat/llama3"
   ```

4. Restart your Django server.

## The Chat UI

[Section titled “The Chat UI”](#the-chat-ui)

The Chat UI has multiple different implementations, and the one that is used for your project will be determined by your build configuration.

If you build with asynchronous functionality enabled *and* htmx then it will use a websocket-based Chat UI. This Chat UI supports streaming responses for OpenAI models, and is the recommended option. It is also currently the only option that supports the chat widget that can be embedded on any page.

If you build without asynchronous functionality enabled, the chat UI will instead use Celery and polling. The React version of the chat UI also uses Celery and polling. This means that [Celery must be running](/celery) to get responses from the LLM.

### The Chat widget

[Section titled “The Chat widget”](#the-chat-widget)

*The chat widget is currently only available if your project is using HTMX and Async.*

The chat widget is a small component that can be embedded on any page of your app. By default, it is included in your `chat_home.html` file, so you can view a demo of the widget from the “AI Chat” tab in your app.

#### Adding the chat widget to a page

[Section titled “Adding the chat widget to a page”](#adding-the-chat-widget-to-a-page)

To add the chat widget to a page, you can follow the example in `chat_home.html`. There are two steps:

First, include the component at the end of the `<body>` tag. If you’re extending the `app_base.html` file this will be at the end of the `{% block app %}` block.

```jinja
{% block app %}
...
{% include "chat/components/chat_overlay.html" %}
{% endblock app %}
```

Then, add the `ws_initialize.js` in your page JavaScript:

```jinja
{% block page_js %}
<!-- If using vite -->
  {% vite_asset 'assets/javascript/chat/ws_initialize.ts' %}
<!-- If using webpack -->
  <script src="{% static 'js/chat-ws-initialize-bundle.js' %}" defer></script>
{% endblock page_js %}
```

If you want to add the chat widget to all pages in your app, you can add it to the `base.html` file. For all logged-in pages, you can add it to the `app_base.html` file.

## Using Agents

[Section titled “Using Agents”](#using-agents)

As of version 2025.9.1, Pegasus includes a set of example agents that you can use as a foundation for building your own agents. These agents are built with [Pydantic AI](https://docs.pydantic-ai.com/), and include:

* A weather and location lookup agent, with tools to do geo-lookups and access current weather information.
* A chatbot to interact with employee application data models, with tools to work with employee data.
* A chatbot to interact with system database, with MCP tool to access postgres data.
* A tool to send emails.

For more information on these agents and how they work, you can watch this video:

### Setting the agent model and keys

[Section titled “Setting the agent model and keys”](#setting-the-agent-model-and-keys)

To change the agent model you can set the `DEFAULT_LLM_MODEL` setting in your `settings.py` file or environment variables / `.env` file.

For a list of available models, see the [Pydantic AI documentation](https://ai.pydantic.dev/models/overview/).

You will also need to set the API keys for the models you want to use in the environment, according to the Pydantic AI docs.

For example, to use any OpenAI models you need to set the `OPENAI_API_KEY` environment variable.

```bash
OPENAI_API_KEY="sk-..."
```

## Choosing an LLM model (deprecated)

[Section titled “Choosing an LLM model (deprecated)”](#choosing-an-llm-model-deprecated)

Older versions of Pegasus allowed you to choose between two options for your LLM chat: OpenAI and LiteLLM. As of version 2025.9.1, all projects will now use [LiteLLM](https://docs.litellm.ai/docs/), which fully supports OpenAI, as well as Anthropic, Google, and local models. This makes it easy to use different models depending on your specific application needs.

## Configuring OpenAI (deprecated)

[Section titled “Configuring OpenAI (deprecated)”](#configuring-openai-deprecated)

If you’re using OpenAI, you need to set `OPENAI_API_KEY` in your environment or settings file (`.env` in development). You can also change the model used by setting `OPENAI_MODEL`, which defaults to `"gpt-4o"`.

See [this page](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key) for help finding your OpenAI API key.

# Using Digital Ocean Spaces for Django Media (in addition to AWS services)

> Configure Digital Ocean Spaces for Django media storage while using AWS SES for email, with detailed deployment settings for django-storages.

Community Guide

The following guide was contributed by Neil Bartlett and Finbar, members of the Pegasus community. Any questions or issues using it should be directed to the #deployment channel of the community Slack.

This guide documents how to use a different media storage (in this case, Digital Ocean Spaces), while still using some Amazon services (in this case, SES for email), deployed to Digital Ocean App Platform.

The main issue/insight is that `django-storages` allows for [different settings/environment variables](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#authentication-settings), e.g. `AWS_S3_ACCESS_KEY_ID` vs `AWS_ACCESS_KEY_ID` or `AWS_S3_SECRET_ACCESS_KEY` vs `AWS_SECRET_ACCESS_KEY`.

This means you can use a different AWS key for S3, SES, or any other service.

Many of the steps would be the same when deploying to other platforms, but some of the details around where to put variables or access a shell/console would be different.

Here’s a detailed walkthrough:

[This post](https://testdriven.io/blog/django-digitalocean-spaces/) is useful but contains a lot of errors. So read it to get an idea of the process, but don’t follow it exactly.

First [use `s3cmd`](https://docs.digitalocean.com/products/spaces/reference/s3cmd-usage/) to make sure that Spaces is correctly setup.

Once you can see your buckets from `s3cmd`, then you have correctly set up the space and the access keys. BUT note to do the above you need an access key with All Permissions set. This is probably overkill for the access key for running the app — but was needed to configure `s3cmd`.

Next, setup all the following in the `app-spec.yaml`. This feels like over spec’ing but I found all settings are necessary. Replace REPLACEME-XXXXXXX, the -aws-region, the-digital-ocean-region, my-bucket-name with your settings. Note AWS\_S3\_ENDPOINT\_URL could be written using `app-spec.yaml` reference syntax but I wanted to be sure so it is explicit.

```yaml
  - key: AWS_DEFAULT_REGION
    scope: RUN_TIME
    value: the-aws-region
  - key: AWS_ACCESS_KEY_ID
    scope: RUN_TIME
    value: REPLACEME-XXXXXXXX
  - key: AWS_SECRET_ACCESS_KEY
    scope: RUN_TIME
    value: REPLACEME-XXXXXXXX
  - key: SERVER_EMAIL
    scope: RUN_TIME
    value: noreply@example.com
  - key: DEFAULT_FROM_EMAIL
    scope: RUN_TIME
    value: info@example.com
  - key: EMAIL_BACKEND
    scope: RUN_TIME
    value: anymail.backends.amazon_ses.EmailBackend
  - key: AWS_S3_REGION_NAME
    scope: RUN_TIME
    value: the-digital-ocean-region
  - key: AWS_S3_ACCESS_KEY_ID
    scope: RUN_TIME
    value: REPLACEME-XXXXXXXX
  - key: AWS_S3_SECRET_ACCESS_KEY
    scope: RUN_TIME
    value: REPLACEME-XXXXXXXX
  - key: AWS_STORAGE_BUCKET_NAME
    scope: RUN_TIME
    value: my-bucket-name
  - key: AWS_S3_ENDPOINT_URL
    scope: RUN_TIME
    value: https://the-digital-ocean-region.digitaloceanspaces.com
  - key: USE_S3_MEDIA
    scope: RUN_TIME
    value: "true"
  - key: PUBLIC_MEDIA_LOCATION
    scope: RUN_TIME
    value: media
  - key: MEDIA_URL
    scope: RUN_TIME
    value: https://my-bucket-name.the-digital-ocean-region.digitaloceanspaces.com/media
```

This will redeploy the app.

Then, in the digital ocean app platform console run:

```bash
env | grep AWS
```

This should give the same settings as in the app-spec.

The pure settings alone did not work: I had to remove the `USE_S3_MEDIA` code from `settings.py` and in `setting_production.py` add the equivalent but using the S3 variants of the environment variables. I could have just edited the stuff in `settings.py`. Part of the issue is that the precedence in the `django-storages` has internal variables take precedence over env variables, so if there are internal variables being used they will override the `app-spec.yaml` settings. Also note that `AWS_S3_ADDRESSING_STYLE` is probably important to override. I could not get it to work without being explicit about this. I prob should have added this to `app-spec.yaml`.

```python
USE_S3_MEDIA = env.bool("USE_S3_MEDIA", default=False)
if USE_S3_MEDIA:


    # We are assuming the app-spec.yaml or the .env file has set the production values
    # But seems we need to pull in some here


    # Media file storage in S3
    # Using this will require configuration of the S3 bucket


    AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_ENDPOINT_URL = env("AWS_S3_ENDPOINT_URL")
    AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME")
    AWS_S3_ADDRESSING_STYLE = env("AWS_S3_ADDRESSING_STYLE", default="path")
    AWS_S3_USE_SSL=True
    PUBLIC_MEDIA_LOCATION = "media"


    STORAGES["default"] = {
        "BACKEND": "apps.web.storage_backends.PublicMediaStorage",
    }
```

Run the shell from the Digital Ocean console. Run `python3 manage.py shell` and import the settings and make sure there not any settings that are taking prceedence over the `app-spec.yaml` that you are not expecting:

```python
from <myapp>.settings import *
print(AWS_ACCESS_KEY_ID)
print(AWS_S3_ACCESS_KEY_ID)
print(AWS_SECRET_ACCESS_KEY)
print(AWS_S3_SECRET_ACCESS_KEY)
print(AWS_DEFAULT_REGION)
print(AWS_S3_REGION)
```

This is just the “starter” list. If things are not working add more from the `app-spec.yaml` list. Run a test directly from the django shell:

```python
from storages.backends.s3boto3 import S3Boto3Storage
from io import BytesIO
import logging


logging.basicConfig(level=logging.DEBUG)
logging.getLogger('botocore').setLevel(logging.DEBUG)


storage = S3Boto3Storage()
print("Bucket:", storage.bucket)
print("Endpoint:", storage.connection)


test_file = BytesIO(b"Hello, DigitalOcean!")
test_file_name = "test_upload.txt"


storage.save(test_file_name, test_file)
```

If this works then things are set up.

**Targetted debugging**

In the django shell. You can use with to target override the default settings. This is very handy to pin things down.

```python
from django.test.utils import override_settings
from io import BytesIO


with override_settings(
    AWS_STORAGE_BUCKET_NAME='penalty-mentor-spaces',
    AWS_S3_ENDPOINT_URL='https://tor1.digitaloceanspaces.com',
    AWS_S3_REGION_NAME='tor1',
    AWS_S3_ADDRESSING_STYLE='path',
    AWS_DEFAULT_ACL='public-read',
    AWS_S3_USE_SSL=True,
):
    from storages.backends.s3boto3 import S3Boto3Storage
    storage = S3Boto3Storage()
    print("Bucket Name:", storage.bucket)
    print("Endpoint URL:", storage.connection)
    test_file = BytesIO(b"Hello, DigitalOcean!")
    test_file_name = "test_upload.txt"
    storage.save(test_file_name, test_file)
Finally use the actual class that Pegasus is using
from apps.web.storage_backends import PublicMediaStorage
storage = PublicMediaStorage()
print("Bucket Name:", storage.bucket)
print("Endpoint URL:", storage.connection)
test_file = BytesIO(b"Hello, DigitalOcean!")
test_file_name = "test_upload.txt"
storage.save(test_file_name, test_file)
Note also for debugging useful to set
import logging


logging.basicConfig(level=logging.DEBUG)
logging.getLogger('botocore').setLevel(logging.DEBUG)
```

either in `settings_production.py` or the django shell.

# Automating Deployment to Cloud Run using GitHub Actions

> Automate Pegasus deployment to Google Cloud Run using GitHub Actions with service accounts, Artifact Registry, and CI/CD pipelines.

Community Guide

The following guide was contributed by Daan Vielen, a member of the Pegasus community. Any questions or issues using it should be directed to the #deployment channel of the community Slack.

This guide walks you through setting up a GitHub Action to automatically deploy your Django application to Google Cloud Run when the tests pass on the `main` branch.

## What You’ll Do:

[Section titled “What You’ll Do:”](#what-youll-do)

1. Create two Google Cloud service accounts with appropriate permissions: one for deployments and one for running the application.
2. Store GCP credentials and configuration in GitHub Secrets.
3. Write the deployment workflow that triggers upon successful completion of the test workflow.
4. Use Artifact Registry for storing your Docker images.
5. Clearly distinguish between the deployment service account (DEPLOY\_SERVICE\_ACCOUNT) and the service account used to run the Cloud Run application (SERVICE\_ACCOUNT). This distinction ensures security by limiting each service account’s access to only the necessary resources.

***

## **Step 1: Create the Google Cloud Service Accounts**

[Section titled “Step 1: Create the Google Cloud Service Accounts”](#step-1-create-the-google-cloud-service-accounts)

### **1.1 Set Up Your Google Cloud Project**

[Section titled “1.1 Set Up Your Google Cloud Project”](#11-set-up-your-google-cloud-project)

First, set an environment variable for your Google Cloud project ID and deployment service account email. This ensures that all the commands referencing these values are consistent and reusable.

```bash
# Set your project ID (replace "replace-with-your-project-id" with your actual project ID)
export PROJECT_ID="replace-with-your-project-id"


# Set the deployment service account email and the service account email that will run the Cloud Run application
export DEPLOY_SERVICE_NAME="cloud-run-deployer"
export DEPLOY_SERVICE_ACCOUNT="${DEPLOY_SERVICE_NAME}@${PROJECT_ID}.iam.gserviceaccount.com"


# Set the service account that will run the Cloud Run application
export SERVICE_ACCOUNT="cloud-run-app@$PROJECT_ID.iam.gserviceaccount.com""cloud-run-deployer@$PROJECT_ID.iam.gserviceaccount.com"
```

### **1.2 Create the Deployment Service Account**

[Section titled “1.2 Create the Deployment Service Account”](#12-create-the-deployment-service-account)

We will create a **separate deployment service account** (DEPLOY\_SERVICE\_ACCOUNT) for the following reasons:

1. **Security**: By using a dedicated service account for deployments, you can limit its permissions to only what’s necessary for deploying the application and avoid granting unnecessary access to other resources.
2. **Impersonation**: The deployment service account (used by GitHub Actions) needs to impersonate another service account that is used to **run** the Cloud Run application. This allows it to delegate specific tasks (like database access, secret access, etc.) to that service account.

Run the following command to create the **deployment service account** (DEPLOY\_SERVICE\_ACCOUNT):

```bash
# Create the deployment service account
gcloud iam service-accounts create $DEPLOY_SERVICE_NAME \
    --description="Service account for deploying to Cloud Run" \
    --display-name="Cloud Run Deployer" \
    --project="$PROJECT_ID"
```

### **1.3 Grant Permissions to the Deployment Service Account**

[Section titled “1.3 Grant Permissions to the Deployment Service Account”](#13-grant-permissions-to-the-deployment-service-account)

The deployment service account (used by GitHub Actions to deploy the Cloud Run service) needs permissions to deploy applications and impersonate the service account that runs your Cloud Run application.

Grant the following roles to the **deployment service account** (DEPLOY\_SERVICE\_ACCOUNT):

```bash
# Grant Cloud Run Admin role (allows deploying to Cloud Run)
gcloud projects add-iam-policy-binding "$PROJECT_ID" \
    --member="serviceAccount:$DEPLOY_SERVICE_ACCOUNT" \
    --role="roles/run.admin"


# Grant Storage Admin role (to push Docker images to Artifact Registry)
gcloud projects add-iam-policy-binding "$PROJECT_ID" \
    --member="serviceAccount:$DEPLOY_SERVICE_ACCOUNT" \
    --role="roles/artifactregistry.repoAdmin"


# Grant Service Account User role (to allow the deployment service account to impersonate the service account that runs the Cloud Run application)
# Only for deploying cloud run
gcloud iam service-accounts add-iam-policy-binding $SERVICE_ACCOUNT \
    --member="serviceAccount:$DEPLOY_SERVICE_ACCOUNT" \
    --role="roles/iam.serviceAccountUser" \
    --project="$PROJECT_ID"
```

In the above command, replace `$SERVICE_ACCOUNT` with the service account that will **run** the Cloud Run application (more details on this later).

### **1.4 Create and Download the Deployment Service Account Key**

[Section titled “1.4 Create and Download the Deployment Service Account Key”](#14-create-and-download-the-deployment-service-account-key)

Now generate the deployment service account key, which you will upload to GitHub as a secret.

```bash
# Create and download the service account key
gcloud iam service-accounts keys create ~/cloud-run-deployer-key.json \
    --iam-account=$DEPLOY_SERVICE_ACCOUNT \
    --project="$PROJECT_ID"
```

This will generate a JSON key file (cloud-run-deployer-key.json). Save this file as you will need it to authenticate GitHub Actions with Google Cloud.

***

## **Step 2: Store GCP Credentials in GitHub Secrets**

[Section titled “Step 2: Store GCP Credentials in GitHub Secrets”](#step-2-store-gcp-credentials-in-github-secrets)

1. Go to your GitHub repository.
2. Navigate to **Settings** > **Secrets and variables** > **Actions**.
3. Click **New repository secret** and add the following secrets:

* **GCP\_DEPLOY\_SA\_KEY**: The content of your cloud-run-deployer-key.json file. Copy the entire contents of the JSON file.
* **DEPLOY\_SERVICE\_ACCOUNT**: The service account that will **deploy the Cloud Run application**.
* **GCP\_PROJECT**: Your Google Cloud project ID (you already set this as `$PROJECT_ID` in the terminal).
* **CLOUDRUN\_NAME**: The name of your Cloud Run service.
* **IMAGE\_URL**: The URL for your container image. It typically follows the format: REGION-docker.pkg.dev/\[PROJECT\_ID]/\[REPOSITORY]/\[IMAGE\_NAME]:latest.
* **REGION**: The Google Cloud region where your Cloud Run service is deployed (e.g., us-central1).
* **DATABASE\_ADDRESS**: The Cloud SQL instance connection name (format: project:region:instance).
* **APPLICATION\_SETTINGS**: Key reference for secrets manager (format: application\_settings:latest).
* **SERVICE\_ACCOUNT**: The service account that will **run the Cloud Run application**.

***

## **Step 3: Create the deploy.yml File**

[Section titled “Step 3: Create the deploy.yml File”](#step-3-create-the-deployyml-file)

Now that the test workflow is in place and runs successfully, we’ll create a deployment workflow that triggers when the tests pass.

In this deployment workflow, we will use the `DEPLOY_SERVICE_ACCOUNT` environment variable in both shell commands and GitHub Actions.

1. In your GitHub repository, create the following directory structure:

   ```bash
   .github/
     workflows/
   ```

2. Inside the workflows folder, create a file named deploy.yml and add the following content:

   ```yaml
   name: Deploy to Cloud Run


   on:
     workflow_run:
       workflows: ["Run Django Tests"]
       types: [completed]
       branches: [main]


   jobs:
     on-success:
       if: ${{ github.event.workflow_run.conclusion == 'success' }}
       runs-on: ubuntu-latest


       steps:
         - name: Checkout code
           uses: actions/checkout@v3


         - name: Authenticate with Google Cloud
           uses: google-github-actions/auth@v1
           with:
             credentials_json: ${{ secrets.GCP_DEPLOY_SA_KEY }}


         - name: Configure Google Cloud
           run: |
             gcloud config set project ${{ secrets.GCP_PROJECT }}
             gcloud config set run/region ${{ secrets.REGION }}
             gcloud config set account ${{ secrets.DEPLOY_SERVICE_ACCOUNT }}


         - name: Authenticate Docker to push images to Artifact Registry
           run: |
             gcloud auth configure-docker ${{ secrets.REGION }}-docker.pkg.dev --quiet


         - name: Build Docker image
           run: |
             docker build -t ${{ secrets.IMAGE_URL }} . -f Dockerfile.web --platform linux/amd64


         - name: Push Docker image to Artifact Registry
           run: |
             docker push ${{ secrets.IMAGE_URL }}


         - name: Deploy to Cloud Run
           run: |
             gcloud run deploy ${{ secrets.CLOUDRUN_NAME }} \
               --region ${{ secrets.REGION }} \
               --update-env-vars DJANGO_SETTINGS_MODULE=agenda.settings_production \
               --image ${{ secrets.IMAGE_URL }} \
               --set-cloudsql-instances ${{ secrets.DATABASE_ADDRESS }} \
               --set-secrets APPLICATION_SETTINGS=${{ secrets.APPLICATION_SETTINGS }} \
               --service-account ${{ secrets.SERVICE_ACCOUNT }} \
               --allow-unauthenticated
   ```

***

## **Step 4: Test the Deployment Workflow**

[Section titled “Step 4: Test the Deployment Workflow”](#step-4-test-the-deployment-workflow)

Once everything is set up, test the workflow by making a change in the `main` branch or opening a pull request.

1. Push the changes or create a pull request targeting the `main` branch.
2. The `test` workflow will run automatically.
3. If the tests pass successfully, the `deploy.yml` workflow will trigger, deploying the new changes to Cloud Run.

# Bootstrap

> Customize Bootstrap 5 themes in Pegasus with Sass variables, JavaScript integration, and Material Kit alternatives for responsive web design.

There are two Bootstrap themes, both of which use Bootstrap version 5.

## Choosing your theme

[Section titled “Choosing your theme”](#choosing-your-theme)

The default Bootstrap theme is based off the default settings that ship with Bootstrap. It provides a simple, practical starting point that is easy to customize and extend. This theme is recommended for all new projects using Bootstrap.

There is also a deprecated theme is based on Creative Tim’s [Material Kit](https://www.creative-tim.com/product/material-kit) and [Material Dashboard](https://www.creative-tim.com/product/material-dashboard) products. White this theme is flashier than the default theme, it has been retired due to developer experience issues. It is not recommended except for legacy projects, as support will be dropped in the future.

## Customizing the theme

[Section titled “Customizing the theme”](#customizing-the-theme)

Pegasus’s file structure is based on [the Bootstrap documentation](https://getbootstrap.com/docs/5.0/customize/sass/#importing). Any of the variables used in Bootstrap can be changed by modifying the `assets/styles/site-bootstrap.scss` file.

A complete list of available variables can be found in `./node_modules/bootstrap/scss/variables`.

Try adding the following lines to your file (after importing `functions`) to see how it changes things:

```scss
// Configuration
@import "~bootstrap/scss/functions";


$primary: #2e7636;  // change primary color to green
$body-color: #00008B;  // change main text to blue


// rest of file here...
```

**You’ll have to run `npm run dev` to see the changes take.** For more details on building the CSS files, see the [front end documentation](/front-end/overview).

The [Bootstrap documentation](https://getbootstrap.com/docs/5.0/customize/sass/) has much more detail on customizing your theme!

## Working with JavaScript in Django templates

[Section titled “Working with JavaScript in Django templates”](#working-with-javascript-in-django-templates)

If you want to call bootstrap JavaScript from a Django template file, you can make the bootstrap library (or subsets of it) available on the browser window.

To make all of bootstrap available, you can modify `site-bootstrap.js`b to just be these lines:

```javascript
require('./styles/site-bootstrap.scss');
window.bootstrap = require('bootstrap');
```

After [rebuilding the front end](/front-end/overview) you can then call bootstrap in a Django template like this:

```jinja
{% block page_js %}
<script>
  document.addEventListener('DOMContentLoaded', function() {
    const onLoadModal = new bootstrap.Modal(document.getElementById('onLoadModal'));
    onLoadModal.show();
  });
</script>
{% endblock %}
```

This example will open the modal with ID `onLoadModal` on page load.

Alternatively, you can add individual bootstrap javascript modules via `site-bootstrap.js` like this:

```javascript
require('./styles/site-bootstrap.scss');
// <other require statements here>
window.Modal = require('bootstrap/js/dist/modal');  // modals (used by teams)
```

And then call it in a Django template like this (with no `bootrap.` prefix):

```javascript
const onLoadModal = new Modal(document.getElementById('landing-page-modal'));
```

# Bulma

> Customize Bulma CSS framework using Sass variables for colors, typography, and styling in your Pegasus application.

Bulma is readily customizable via [Sass variables](https://bulma.io/documentation/customize/variables/). Any of the variables used by Bulma can be changed by modifying the `assets/styles/site-bulma.scss` file.

Try adding the following lines to the top of your file to see how it changes things:

```scss
$primary: #2e7636;  // change primary color to green
$body-color: #00008B;  // change main text to blue
```

**You’ll have to run `npm run dev` to see the changes take.** For more details on building the CSS files, see the [front end documentation](/front-end/overview).

# CSS File Structure

> Understand Pegasus CSS file organization with framework-independent styles and framework-specific overrides compiled from assets to static directories.

CSS source files live in the `assets/styles` folder, and are compiled into the `static/css` folder. Some Pegasus styles are written using [Sass](https://sass-lang.com/), which provides many benefits and features on top of traditional CSS.

**Modifying CSS requires having a functional [front-end build setup](/front-end/overview).**

All versions of Pegasus contain two main sets of styles:

* Styles that are *framework-independent* are contained and imported in `assets/styles/app/base.sass` and compiled into `static/css/site-base.css`.
* Styles that *extend or override the CSS framework* are contained in `assets/styles/app/<framework>/` and compiled into `static/css/site-<framework>.css`.

This split is not required, and you can optionally combine everything into a single file by importing the styles from `base.sass` into your framework file and deleting `site-base.css`.

# The Material Theme (deprecated)

> Legacy Material Design theme based on Creative Tim's Material Kit and Dashboard, now deprecated with maintenance-only support until 2025.

This feature is deprecated

This theme was removed in version 2025.10. It is recommended to switch to [Tailwind CSS](/css/tailwind).

This means that the theme is in maintenance-only mode, and support will be dropped by the end of 2025. Existing projects can continue using the theme, but new projects should not, and new Pegasus features will eventually not be developed and tested on the theme.

The reason for this is that several Pegasus customers have complained about the lack of documentation and support for this theme from its maintainer, Creative Tim. Additionally, their process around updating the theme has entailed releasing large, poorly-documented updates which have been difficult for me to incorporate back into Pegasus.

The following documentation is for people already using the material theme.

## Customizing the Material theme

[Section titled “Customizing the Material theme”](#customizing-the-material-theme)

The customization process outlined above largely works for the Material theme as well.

For example, you can change the primary color from the default magenta to a dark green by adding the following lines towards the top of `assets/styles/site-bootstrap.scss`:

```scss
// Configuration
@import "~bootstrap/scss/functions";


// add these lines
$primary: #2e7636;  // change primary color + gradients to green
$primary-gradient: #2e7676;
$primary-gradient-state: #2e7676;
```

You will also have to [build your front end](/front-end/overview) to see the changes.

Material has more customization options than the default theme, which can be found in the [Material Dashboard documentation](https://www.creative-tim.com/learning-lab/bootstrap/overview/material-dashboard). The theme files live in the `assets/material-dashboard` folder. You can see the modifications that have been made for Pegasus support [on Github here](https://github.com/creativetimofficial/material-dashboard/compare/master...czue:pegasus-tweaks). In particular, a few bugs have been fixed, and the unused pro files have been removed.

Creative Tim offers pro versions of [Material Dashboard](https://www.creative-tim.com/product/material-dashboard-pro) and [Material Kit](https://www.creative-tim.com/product/material-kit-pro) which are helpful if you want to have access to more pages / components. These should integrate seamlessly with the Pegasus theme.

### Enabling Material’s JavaScript

[Section titled “Enabling Material’s JavaScript”](#enabling-materials-javascript)

Pegasus doesn’t ship with the Material theme JavaScript built in. If you would like to use their JavaScript functionality (required for many of their components) you can take the following steps:

1. Download [the `material-kit.min.js` file from Creative Tim’s Github repository](https://github.com/creativetimofficial/material-kit/blob/master/assets/js/material-kit.min.js).
2. Copy it into your Django static directory. For example, to `<project_root>/static/js`
3. Add it to the `<head>` section of your `base.html` template (or wherever you want to use it):

```jinja
<script src="{% static 'js/material-kit.min.js'%}"></script>
```

After completing these steps, the Material Kit JavaScript functionality should work.

# Choosing a CSS Theme

> Compare TailwindCSS, Bootstrap, Bulma, and Material Design themes with screenshots, features, and recommendations for Django projects.

There are four CSS themes available in Pegasus.

**If you don’t know which one you want, we recommend TailwindCSS.** It is the most popular choice, easiest to customize, and supports themes and dark mode out-of-the-box.

In addition to Tailwind, there is a [Bootstrap 5](https://getbootstrap.com/) theme, a [Bulma](https://bulma.io/) theme, and a deprecated theme based on Creative Tim’s [Material Kit](https://www.creative-tim.com/product/material-kit) and [Material Dashboard](https://www.creative-tim.com/product/material-dashboard) products (not recommended).

The look and feel of the site is slightly different for each framework, but the overall layout is the same. Below are screenshots of the app in each of the four themes.

*If you’re not sure which framework you want to use, you can change the setting on your project and download multiple copies of the codebase to try out different ones.*

**Tailwind CSS:**

Light mode:

![Tailwind Home](/_astro/tailwind-home-light.DygBNhqu_Z2fPlyk.webp)

Dark mode:

![Tailwind Home (Dark Mode)](/_astro/tailwind-home-dark.BJVKg2e7_Z1FmxUO.webp)

**Bootstrap Default Theme:**

![Bootstrap Home](/_astro/bootstrap-home.DaBA-2Xi_Z1uk4rA.webp)

**Bulma:**

![Bulma Home](/_astro/bulma-home.DfnQnVsO_Z22ki8O.webp)

**Bootstrap Material Theme (Deprecated):**

![Material Home](/_astro/material-home.HxW3zxce_1iKN8t.webp)

# Pegasus CSS

> Cross-framework CSS classes with pg- prefixes for consistent styling across Bootstrap, TailwindCSS, and Bulma using Sass @extend and @apply.

In addition to your app’s CSS, Pegasus also ships with its own set of CSS classes to provide compatibility across different frameworks. These classes are typically proxies for similar classes provided by the underlying frameworks themselves, and are created using the Sass [`@extend` helper](https://sass-lang.com/documentation/at-rules/extend) or Tailwind’s [`@apply` helper](https://tailwindcss.com/docs/reusing-styles#extracting-classes-with-apply).

Pegasus CSS classes are defined in `pegasus/<framework>.sass/css`, and they all begin with `pg-`. You are welcome to leave them in and use them throughout your project, or you can replace them with the framework-specific names (for example, replacing all instances of `pg-column` with `column` on Bulma, or `col-md` on Bootstrap).

The following table demonstrates some of the most common Pegasus CSS classes and their corresponding values across frameworks. If you ever need to look up what a class is doing you can look in `./assets/styles/pegasus/`.

| Pegasus Class   | Description         | Value in Bootstrap | Value in Tailwind                                               | Value in Bulma  |
| --------------- | ------------------- | ------------------ | --------------------------------------------------------------- | --------------- |
| `pg-columns`    | Wrapper for columns | `row gy-4`         | `flex flex-col space-y-4 lg:flex-row lg:space-x-4 lg:space-y-0` | `columns`       |
| `pg-column`     | Individual column   | `col-md`           | `flex-1`                                                        | `column`        |
| `pg-title`      | A title             | `h3` (element)     | `text-3xl font-bold text-gray-900 mb-2`                         | `title`         |
| `pg-subtitle`   | A subtitle          | `lead`             | `text-xl text-gray-900 mb-1`                                    | `subtitle`      |
| `pg-button-***` | A styled button     | `btn btn-***`      | `btn btn-***` (from daisyUI)                                    | `button is-***` |
| `pg-text-***`   | Colored text        | `text-***`         | `text-***` (from daisyUI)                                       | `has-text-***`  |

# Tailwind CSS

> Build modern UIs with TailwindCSS v4, DaisyUI components, shadcn/ui integration, dark mode themes, and Flowbite styling options.

Pegasus supports [Tailwind CSS](https://tailwindcss.com/) (Version 4) and it is the recommended CSS framework for most projects.

## Demo and Overview

[Section titled “Demo and Overview”](#demo-and-overview)

Here’s a quick overview of using TailwindCSS in Pegasus

## Development

[Section titled “Development”](#development)

Because TailwindCSS only includes the styles found in your HTML / JavaScript files, you will need to actively rebuild your CSS files any time you add new styles/components to your templates. The easiest way to do this is by running (after installing Node packages):

```bash
npm run dev
```

Or in Docker:

```bash
make npm-dev
```

See the [front-end docs](/front-end/overview) for more information about working with these files.

## Customization

[Section titled “Customization”](#customization)

Pegasus uses [daisyUI](https://daisyui.com/) to provide default, well-styled components with convenient CSS classes. Components from daisyUI can be brought in as needed by your app. A full list of available components can be found at the [daisyUI component library](https://daisyui.com/components/).

### Changing your themes

[Section titled “Changing your themes”](#changing-your-themes)

If you enable dark mode, Pegasus will ship with the default DaisyUI light and dark themes which are used for regular and dark mode, respectively. But DaisyUI offers a number of [out-of-the-box themes](https://daisyui.com/docs/themes/) you can use in your Pegasus app. To change themes, make sure the theme is enabled in the daisyui section of `site-tailwind.css` and specify what you want for defaults for light and dark mode as follows:

```css
@plugin "daisyui" {
  themes: cupcake --default, night --prefersdark;
};
```

Additionally, you should update the `darkMode` setting in your `tailwind.config.js`:

```javascript
module.exports = {
  // sets the "night" theme as the one used for dark mode
  darkMode: ["class", '[data-theme="night"]'],
}
```

After changing these values you will have to [rebuild your front end](/front-end/overview).

Finally, you will also have to update the default themes in your `settings.py`:

```python
LIGHT_THEME = "cupcake"
DARK_THEME = "night"
```

After this, your app should be fully styled in the new themes!

For a list of the available themes, and information about creating your on theme, see the [daisyUI theme documentation](https://daisyui.com/docs/themes/) and their online [theme generator](https://daisyui.com/theme-generator/).

### Extending themes

[Section titled “Extending themes”](#extending-themes)

If you’d like to extend one of the built-in themes you can do that in your `site-tailwind.css` file as specified in the [DaisyUI docs](https://daisyui.com/docs/themes/#-3).

For example, to change the colors of the default theme, add a section like this:

```css
@plugin "daisyui/theme" {
  name: "light";
  default: true;
  --color-primary: blue;
  --color-secondary: teal;
}
```

## Other products / themes

[Section titled “Other products / themes”](#other-products--themes)

### shadcn

[Section titled “shadcn”](#shadcn)

[shadcn/ui](https://ui.shadcn.com/) is a React component library for Tailwind. It includes many out-of-the-box components that you can install and use in your projects.

As of version 2024.11 Pegasus ships with a demo dashboard using shadcn. To enable the dashboard you have to build with the Tailwind CSS framework and check the “Use Shadcn” checkbox in your project settings.

Here’s a screenshot:

![Shadcn Demo Dashboard](/_astro/shadcn-demo.C_wZrJUK_Z2kKOhB.webp)

The dashboard is [a hybrid single-page React app](https://www.saaspegasus.com/guides/modern-javascript-for-django-developers/integrating-django-react/) served by Django. It uses the same colors as the DaisyUI theme, and will update when you change your theme, and has many interactive components. However it is *not* connected to any backend data---it is just a UI example.

#### Working with shadcn

[Section titled “Working with shadcn”](#working-with-shadcn)

The dashboard can be found in `assets/javascript/shadcn-dashboard`. Shadcn components are stored in the `assets/javascript/shadcn/components/ui` folder.

Components can be imported in other JavaScript files using the same import path syntax used by the dashboard:

```javascript
import { Button } from "@/components/ui/button"
```

You can use the [shadcn cli](https://ui.shadcn.com/docs/cli) to create components, and they should automatically be added to the right folder.

### Flowbite

[Section titled “Flowbite”](#flowbite)

[Flowbite](https://flowbite.com/) is a library with many great UI components---most of which are free and open source. Also, unlike shadcn, it does *not* use React---making it a great fit for Django templates and htmx projects.

As of version 2024.11 Pegasus ships with the option to enable flowbite, along with a page demonstrating some sample components. To enable Flowbite, choose Tailwind CSS and check the “Use Flowbite” checkbox in your project settings.

If you enable this setting, flowbite will automatically be installed and you can drop flowbite components into any Django template. The reference page has an example of a few of these components.

#### Extending Flowbite

[Section titled “Extending Flowbite”](#extending-flowbite)

The default setup shows how to use Flowbite *alongside* DaisyUI. However, if you want to use Flowbite more holistically for your application you can.

To get started, uncomment the following line in your `site-tailwind.css` file:

```plaintext
/* @import "flowbite/src/themes/default"; */
```

This will add flowbite’s default styles, which are necessary for some extended components like datatables.

### Tailwind UI

[Section titled “Tailwind UI”](#tailwind-ui)

[Tailwind UI](https://tailwindui.com/) is a great product for building more complex pages, including marketing sites and app UIs. It another great option for getting help with UI components and pages, and should integrate seamlessly with the current Pegasus templates.

Note that you will have to rebuild styles when adding TailwindUI components, as described in the “Development” section above.

## Upgrading from Tailwind 3 to 4

[Section titled “Upgrading from Tailwind 3 to 4”](#upgrading-from-tailwind-3-to-4)

Pegasus 2025.3 updates Tailwind from version 3 to version 4. This is a big upgrade, and if you have added Tailwind markup to your project you will likely need to upgrade your own code and not just rely on the Pegasus updates.

This section should help you with that process. It will be updated over time as additional questions and issues come up. If you have any problems with the migration, send a message in the community Slack!

It’s recommended to follow the following steps to upgrade your project to Tailwind 4:

1. Read through the [Tailwind Upgrade Notes](https://tailwindcss.com/docs/upgrade-guide) and confirm you’re ready to upgrade from a browser support perspective.
2. Do a [normal Pegasus upgrade](/upgrading) of your project to Version 2025.3 or later.
3. Merge all conflicts as carefully as you can.
4. Rebuild your front end (`npm install`, `npm run dev`).
5. Run your app.

At this point, your project should be running on Tailwind 4, though you should review the sections below for additional steps.

### Restoring custom themes

[Section titled “Restoring custom themes”](#restoring-custom-themes)

To restore custom themes, follow the [instructions above](#changing-your-themes) to re-apply your theme configuration (and if necessary, be sure to also remove it from `tailwind.config.js`).

Note that some DaisyUI themes look slightly different in version 5 and may require further customization for the same look-and-feel.

### Migrating non-Pegasus files

[Section titled “Migrating non-Pegasus files”](#migrating-non-pegasus-files)

You will likely want to run the [Tailwind upgrade tool](https://tailwindcss.com/docs/upgrade-guide#using-the-upgrade-tool) on your project to apply any automatic upgrades to files that aren’t managed by Pegasus.

After going through the steps above, you can re-run Tailwind’s migration tool by following these steps.

First, temporarily re-install Tailwind v3 on your project. This is required for the upgrade tool to run:

```bash
npm install tailwindcss@3
```

Next, temporarily restore the “content” section in your `tailwind.config.js` from your main branch. It should look something like this:

```javascript
  content: [
    './apps/**/*.html',
    './apps/web/templatetags/form_tags.py',
    './assets/**/*.{js,ts,jsx,tsx,vue}',
    './templates/**/*.html',
  ],
```

Finally run the upgrade tool:

```bash
npx @tailwindcss/upgrade --force
```

This should apply Tailwind’s automatic migrations to your existing HTML / JS / CSS files. Review these changes, commit the changes you want, and then undo the changes made to the `content` section above. Note that you may not want to apply some changes like shadow-downsizing, since these have already been included in Pegasus.

### DaisyUI Updates

[Section titled “DaisyUI Updates”](#daisyui-updates)

Some common DaisyUI upgrades that you may need to check include:

* Changing active navigation tab classes from `"active"` to `"menu-active"`.
* Removing `-bordered` from inputs.

## Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

### Styles aren’t working after adding new components

[Section titled “Styles aren’t working after adding new components”](#styles-arent-working-after-adding-new-components)

Every time you use a new Tailwind class you need to rebuild your front end as described in the “[Development](#development)” section above.

After doing that, if they are still not showing up, be sure that you have hard-refreshed your browser (Ctrl-Shift-R) on most browers. You can also disable browser caching when devtools are open by following these instructions [for Chrome](https://stackoverflow.com/a/23944114/8207) or [for Firefox](https://stackoverflow.com/a/48027947/8207).

If you are building your front end in Docker, be sure to also read the troubleshooting section of the [front end documentation](/front-end/overview) for potential issues with cross-platform compatibility.

# Digital Ocean

> Deploy Pegasus apps to Digital Ocean App Platform using Docker containers with PostgreSQL, Redis, and Celery support for scalable SaaS applications.

Pegasus provides native support for Digital Ocean App Platform. To build for Digital Ocean, choose the “digital\_ocean\_app\_platform” option when installing Pegasus. Then follow the steps below to deploy your app.

### Cost

[Section titled “Cost”](#cost)

Deploying a basic application to Digital Ocean App Platform can be expensive for hobby projects, with costs ranging from $20-$55/month on the smallest hardware options.

For a basic Django application the minimum requirements will be as follows

* 1 App server ($5/month)
* 1 Postgres database ($15/month)

However, if you want to use Celery the costs will increase, by adding:

* 1 Celery worker ($10/month)
* 1 Celery beat worker (if using scheduled tasks) ($10/month)
* 1 Redis database ($15/month)

*These numbers were last updated in August, 2025.*

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

If you haven’t already, create your Digital Ocean account. **You can sign up with [this link](https://m.do.co/c/432e3abb37f3) to get $100 credit and help support Pegasus.**

Next, install and configure the `doctl` command line tool by following [these instructions](https://www.digitalocean.com/docs/apis-clis/doctl/how-to/install/).

Additionally, you must connect Digital Ocean to your project’s Github repository. This can be done from inside App Platform, or by following [this link](https://cloud.digitalocean.com/apps/github/install).

### Set up Databases

[Section titled “Set up Databases”](#set-up-databases)

Before you can deploy you will need to set up databases for your application.

First, navigate to [Databases —> New](https://cloud.digitalocean.com/databases/new), and choose “PostgreSQL” and the latest version (as of this writing, v17).

You can leave most of the settings as-is, though feel free to change as you want. The smallest size should be fine for most applications getting stared.

For the database cluster name it’s recommended to use `<your-project>-db` to match the default value expected by Pegasus.

If you are planning to use Celery or Redis (Valkey), you’ll also have to create that Database.

Repeat the process above, but choosing “Valkey” for the database type. For your Redis database cluster name, it is recommended to use: `<your-project>-redis` to match the default value expected by Pegasus.

### Deploying

[Section titled “Deploying”](#deploying)

Once you’ve configured the prerequisites and set up your databases, deploying is just a few steps.

First, edit the `/deploy/app-spec.yaml` file. In particular, make sure to set your Github repository and branch. Also, if you did not use the database naming conventions above, then you will have to adjust your database `cluster_name` values to the ones you chose for Postgres and Redis/Valkey, respectively.

If you don’t need Celery, you can remove the sections related to Redis, and the workers (celery and celery-beat). This will substantially reduce the costs of running your app (the workers are $20/mo and Redis is $15/mo).

Once you’ve made all the edits to the `app-spec.yaml` file you can deploy your app by run the following command:

```plaintext
doctl apps create --spec deploy/app-spec.yaml
```

That’s it! In a few minutes your app should be online. You can [find and view it here](https://cloud.digitalocean.com/apps).

Once your app is live, you should restrict access to your Postgres and Redis/Valkey instance, by navigating to each database in the Digital Ocean console and setting your app as a “trusted source” and saving. Failure to do this may result in your app’s data and infrastructure being exposed to the public.

**After deploying, review the [production checklist](/deployment/production-checklist) for a list of common next steps**.

### Settings and Secrets

[Section titled “Settings and Secrets”](#settings-and-secrets)

App platform builds use the `settings_production.py` file. You can add settings here, and use environment variables to manage any secrets, following the pattern used throughout the file.

Environment variables can be managed in the Digital Ocean dashboard [as described here](https://docs.digitalocean.com/products/app-platform/how-to/use-environment-variables/).

### Running One-Off Commands

[Section titled “Running One-Off Commands”](#running-one-off-commands)

The easiest way to run once-off commands in your app is to click the “console” tab in app platform and just type in the command. See the screenshot below for what it looks like:

![Console Migrations](/_astro/running-migrations-do.BGGpoC46_ZmfR47.webp)

You may also need to run additional commands to get up and running, e.g. `./manage.py bootstrap_subscriptions` for initializing your Stripe plan data.

### Celery Support

[Section titled “Celery Support”](#celery-support)

Celery should work out-of-the box.

If you have issues running celery, ensure that you have created a Redis database, and that the values for the `REDIS_URL` environment variables match the name you’ve chosen.

If you need to run `celerybeat` (for scheduled/periodic tasks), you’ll have to add a second worker to your `app-spec.yaml` file. You can copy and paste the configuration for the `celery` worker, but replace the `run_command` with the following line (swapping in your app name for `your_app`):

```bash
celery -A your_app beat -l INFO
```

Note that simply adding `--beat` or `-B` to the existing Celery worker does *not* work on app platform.

# Fly.io

> Container-based Django deployment to Fly.io with PostgreSQL, Upstash Redis, and automated database migrations using Docker and flyctl CLI.

Pegasus supports container-based deployment to [Fly.io](https://fly.io/).

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

If you haven’t already, install the [flyctl CLI](https://fly.io/docs/hands-on/install-flyctl/).

The create an account with `fly auth signup` or login with `fly auth login`.

### Setup

[Section titled “Setup”](#setup)

Once you have logged in via the CLI you can create your app and the services it will need. For each of the commands below follow the prompts given.

In the example below the “Chicago, Illinois (US) (ord)” region is selected. You may change the region to suit your needs, but it should be consistent throughout the commands.

**Create your app in Fly.io**

```bash
$ fly launch --dockerfile Dockerfile.web \
      --dockerignore-from-gitignore \
      --no-deploy \
      --name {app-name} \
      --region ord
```

After running that, answer ‘yes’ to the first question:

```plaintext
An existing fly.toml file was found for app {app-name}
? Would you like to copy its configuration to the new app? Yes
```

Fly will output some details, then ask another question about customizing. Answer ‘yes’ to that as well:

```plaintext
Using dockerfile Dockerfile.web
Creating app in /path/to/app/source


We're about to launch your app on Fly.io. Here's what you're getting:


Organization: Your Name              (fly launch defaults to the personal org)
Name:         {app-name}             (specified on the command line)
Region:       Chicago, Illinois (US) (specified on the command line)
App Machines: shared-cpu-1x, 1GB RAM (most apps need about 1GB of RAM)
Postgres:     <none>                 (not requested)
Redis:        <none>                 (not requested)


? Do you want to tweak these settings before proceeding? (y/N) Yes
```

A browser tab should open where you should add a Fly Postgres database called {app-name}-db, and an Upstash Redis server. You can leave the other defaults or change the machine size as you see fit. It should look something like this:

![Fly DB config](/_astro/fly-db-config.BD0z3j2A_cySWr.webp)

Click “Confirm Settings” and then close the tab. Back on the command line, Fly will output some more things and should eventually end with a message like this:

```plaintext
✓ Configuration is valid
Your app is ready! Deploy with `flyctl deploy`
```

If you see these two lines you are ready to deploy! If not, see the “Troubleshooting” section below.

<!----
2. Create the app database

    ```bash
    $ fly postgres create --name {app-name}-db --region ord

    # ? Select Organization: My Org
    # ? Select configuration: Development - Single node, 1x shared CPU, 256MB RAM, 1GB disk
    ```

3. Attach the DB to your app

    ```bash
    $ fly postgres attach {app-name}-db -a {app-name}

    Postgres cluster {app-name}-db is now attached to {app-name}
    The following secret was added to <app name>:
      DATABASE_URL=postgres://.....
    ```

4. Create the Redis instance

    ```bash
    $ fly redis create --name {app-name}-redis --region ord

    ? Select Organization: My Org (my_org)
    ? Would you like to enable eviction? Yes
    ? Select an Upstash Redis plan Free: 100 MB Max Data Size
    Your Upstash Redis database {app-name}-redis is ready.
    Apps in the personal org can connect to at redis://.....

    ```

5. Set the `REDIS_URL` secret

    Using the Redis URL from the command above run:

    ```bash
    $ fly secrets set REDIS_URL={url}
    ```

--->

### Deploying

[Section titled “Deploying”](#deploying)

You are now ready to deploy your app. You can do this by running:

```bash
$ fly deploy
```

In a few minutes your app should be live! **After deploying, review the [production checklist](/deployment/production-checklist) for a list of common next steps**.

In particular, make sure add your app URL to the `ALLOWED_HOSTS` variable in your environment/settings as well as in the `http_service.checks` section of `fly.toml`.

### Running Database Migrations

[Section titled “Running Database Migrations”](#running-database-migrations)

Database migrations are applied in the release command during deploy. This is configured in the `fly.toml` file.

### Settings and Secrets

[Section titled “Settings and Secrets”](#settings-and-secrets)

Fly.io builds use the `settings_production.py` file. You can add settings here or in the base `settings.py` file, and use environment variables to manage any secrets, following the examples in these files.

Secrets are managed in Fly.io via the web UI or on the command line using the CLI:

```bash
$ fly secrets set MY_VAR=secret_value
```

### Running One-Off Commands

[Section titled “Running One-Off Commands”](#running-one-off-commands)

You can one-off commands via a shell:

```bash
$ fly ssh console


app $ ./code/manage.py [command]
```

### Celery Support

[Section titled “Celery Support”](#celery-support)

Out of the box, Pegasus is configured to run Celery using the [multiprocess support](https://fly.io/docs/reference/configuration/#the-processes-section) provided by Fly.io.

For alternatives see <https://fly.io/docs/app-guides/multiple-processes/>

### Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

**My release / migrate command is failing.**

If you get an error like the following when running `fly deploy`

```plaintext
  django.db.utils.OperationalError: connection to server at "localhost" (127.0.0.1), port 5432 failed: Connection refused
    Is the server running on that host and accepting TCP/IP connections?
```

it is likely that your Database is not set up properly. You can confirm if this is the case by running `fly secrets list` and making sure that you see a `DATABASE_URL` variable. If you do not see one, it is not properly connected/attach.

If you need to create a new database, you can run:

```bash
fly postgres create --name {your-app-db}
```

And you can (re-)attach a database to an app by running:

```bash
fly postgres attach {your-app-db} -a {your-app-name}
```

**My deploy keeps timing out.**

If you keep getting an error like the following:

```plaintext
Error: timeout reached waiting for health checks to pass for machine 28749e0b443558
```

You can try re-deploying with a higher timeout. For example, try running:

```bash
flyctl deploy --wait-timeout 5m
```

# Google Cloud

> Deploy Pegasus projects to Google Cloud Run with Cloud SQL PostgreSQL, Redis, Secret Manager, and Google Cloud Storage for production applications.

Pegasus can be deployed to Google Cloud Run using containers. *This feature is in beta and Celery is not yet supported.*

To build for Google Cloud, choose the “google\_cloud” option when installing Pegasus. Then follow the steps below to deploy your app.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

Pegasus deployments on Google Cloud Run loosely follow the [Django on Cloud Run](https://codelabs.developers.google.com/codelabs/cloud-run-django) guide. However, instaed of running it in the Google Cloud Shell, we’ll use the `gcloud` CLI on our development machine. This allows you to more easily work with your existing codebase.

#### 1. Set up the `gcloud` sdk.

[Section titled “1. Set up the gcloud sdk.”](#1-set-up-the-gcloud-sdk)

Though much of the setup can be completed in the cloud shell, you will need to install and configure the `gcloud` sdk on your development machine. Follow [the google installation guide](https://cloud.google.com/sdk/docs/install) for your OS.

After you install the `gcloud` SDK you will also need to authenticate your account [as described here](https://cloud.google.com/docs/authentication/provide-credentials-adc). In particular, you will need to run:

```bash
gcloud auth login
gcloud init
```

#### 2. Create and connect your project.

[Section titled “2. Create and connect your project.”](#2-create-and-connect-your-project)

Follow the instructions [in Step 2 of the Google guide](https://codelabs.developers.google.com/codelabs/cloud-run-django#1) to create a new project for your app and enable billing.

Once you’ve created your project you should be able to run:

```bash
gcloud projects list
```

On your development machine and see it.

Next run:

```bash
gcloud config set project <project_id>
```

To set the project as the default for future commands.

#### 3. Enable the Cloud APIs

[Section titled “3. Enable the Cloud APIs”](#3-enable-the-cloud-apis)

As per [step 3 of the Google guide](https://codelabs.developers.google.com/codelabs/cloud-run-django#2), run the following command to enable the services needed for your application.

```bash
gcloud services enable \
  run.googleapis.com \
  sql-component.googleapis.com \
  sqladmin.googleapis.com \
  compute.googleapis.com \
  cloudbuild.googleapis.com \
  secretmanager.googleapis.com \
  artifactregistry.googleapis.com
```

This command takes a while to finish, but should eventually output something like:

```plaintext
Operation "operations/acf.cc11852d-40af-47ad-9d59-477a12847c9e" finished successfully.
```

*We will skip step 4 of Google’s guide, since we already have a project and move on to step 5.*

#### 4. Create the backing services.

[Section titled “4. Create the backing services.”](#4-create-the-backing-services)

*This section follows [step 5 of Google’s guide](https://codelabs.developers.google.com/codelabs/cloud-run-django#4), with some minor changes.*

**First create a service account:**

```bash
gcloud iam service-accounts create cloudrun-serviceaccount
```

**Set up your environment variables:**

Everything you will need is defined in `/deploy/.env.google.example`. It is recommended that you first copy this file to `.env.google`:

```bash
cp deploy/.env.google.example deploy/.env.google
```

Then update the values in it as needed---including setting any passwords and keys to random, autogenerated values. Once you have made all the modifications to this file, load it into your environment by running:

```bash
source deploy/.env.google
```

After running the above command you should be able to run the remaining commands in the same shell and the variables will be swapped in.

```bash
gcloud artifacts repositories create containers --repository-format docker --location $REGION
```

**Create and configure the database:**

Next, create the database instance. Note that in our `.env.google` file we are changing the instance name from the guide’s `mysinstance` to something unique to your project, and storing that as an environment variable.

Note: for production you may want to use a higher value for `--tier`, however do be aware of the costs associated with doing this. [More information here](https://cloud.google.com/sql/pricing).

```bash
gcloud sql instances create $DATABASE_INSTANCE_NAME --project $PROJECT_ID --database-version POSTGRES_14 --tier db-f1-micro --region $REGION
```

This command takes a long time to run. Once it completes, create a database in the instance, again using a unique name instead of the guide’s `mydatabase`:

```bash
gcloud sql databases create $DATABASE_NAME --instance $DATABASE_INSTANCE_NAME
```

Next, create the database user. Make sure you have set/changed `DATABASE_PASSWORD` in your `deploy/.env.google` file, (and run `source deploy/.env.google` again if necessary) then run:

```bash
gcloud sql users create ${DATABASE_USER} --instance ${DATABASE_INSTANCE_NAME} --password ${DATABASE_PASSWORD}
```

And finally, grant the service account permission to access the DB:

```bash
gcloud projects add-iam-policy-binding $PROJECT_ID --member serviceAccount:${SERVICE_ACCOUNT} --role roles/cloudsql.client
```

**Create and configure Redis:**

If you are using tasks, caching, or websockets you will also need to set up Redis. To enable Redis support you first have to [create a Redis instance](https://cloud.google.com/memorystore/docs/redis/create-manage-instances).

```bash
gcloud redis instances create ${PROJECT_ID}-redis --size=1 --region=${REGION}
```

You might get prompted to enable the Redis API which you should say “yes” to. Then this will run for a long time.

After creating your Redis instance you will need to run `source deploy/.env.google` again to populate the necessary environment variables for the IP and network. You can also view these by running:

```bash
gcloud redis instances describe ${PROJECT_ID}-redis --region ${REGION}
```

**Create and configure the storage bucket:**

```bash
gcloud storage buckets create gs://${GS_BUCKET_NAME} --location ${REGION}
```

```bash
gcloud storage buckets add-iam-policy-binding gs://${GS_BUCKET_NAME} \
    --member serviceAccount:${SERVICE_ACCOUNT} \
    --role roles/storage.admin
```

**Store configuration as a secret.**

Once you have completed the above you should have everything you need in place to run your app. The final step before deploying is to save your configuration as a secret.

First create the `.env.production` file from `.env.production.example`:

```bash
cp .env.production.example .env.production
```

Then update the `DATABASE_URL`, `GS_BUCKET_NAME`, and `REDIS_URL` values in `.env.production`. You can find these values with the echo command, e.g.:

```bash
echo $DATABASE_URL
```

For Redis you will need to put in the value of REDIS\_IP which you can get from:

```bash
echo $REDIS_IP
```

Next, save these values in google cloud:

```bash
gcloud secrets create application_settings --data-file .env.production
```

And allow the service account to access it:

```bash
gcloud secrets add-iam-policy-binding application_settings --member serviceAccount:${SERVICE_ACCOUNT} --role roles/secretmanager.secretAccessor
```

### Create and deploy your docker containers

[Section titled “Create and deploy your docker containers”](#create-and-deploy-your-docker-containers)

From here on out we’ll stop using the guide, since Pegasus should handle everything else for you out of the box. Also, instead of using a `Procfile` we’ll use our own Docker container.

First make sure you have loaded your environment:

```bash
set -o allexport && source deploy/.env.google && set +o allexport
```

Now you can build your container for Google Cloud by running the following command.

```bash
make gcp-build
```

This, and all other `make` commands are defined in the `Makefile` in your project. You can see what they are doing there.

Once you’ve built your container, enable docker pushes with:

```bash
gcloud auth configure-docker
```

And then you can push it with:

```bash
make gcp-push
```

And finally deploy it with:

```bash
make gcp-deploy
```

This should deploy your application to a new container. It should output the URL for your app, which is now online!

Future deploys can be done in the same manner. Or you can use the following command as a shortcut to run everything:

```bash
make gcp-full-deploy
```

<!---
### Jobs

```bash
gcloud projects add-iam-policy-binding ${PROJECT_ID} --member serviceAccount:${SERVICE_ACCOUNT} --role roles/run.admin
```

### Database migrations

You can run migrations like this.

First crate the job:

```bash
gcloud run jobs create migrate \
  --region $REGION \
  --image gcr.io/${PROJECT_ID}/<app_id>-cloudrun \
  --set-cloudsql-instances ${PROJECT_ID}:${REGION}:myinstance \
  --set-secrets APPLICATION_SETTINGS=application_settings:latest \
  --service-account $SERVICE_ACCOUNT \
  --command migrate
```

Then set your default region:

```bash
gcloud config set run/region $REGION
```

-->

### Settings and Secrets

[Section titled “Settings and Secrets”](#settings-and-secrets)

You can use Google Secret Manager to add additional settings and secrets by adding them to `.env.production` and uploading it to Secret Manager using:

```bash
gcloud secrets versions add application_settings --data-file .env.production
```

See `settings_production.py` for examples of using these secrets in your settings file.

### Cookbooks

[Section titled “Cookbooks”](#cookbooks)

#### Automating Deployment to Cloud Run using GitHub Actions

[Section titled “Automating Deployment to Cloud Run using GitHub Actions”](#automating-deployment-to-cloud-run-using-github-actions)

If you would like to automate your Google Cloud deployment so it is deployed on every push to Github, you can refer to this community guide: [Automating Deployment to Cloud Run using GitHub Actions](/community/google-cloud-github-actions/)

# Heroku

> Deploy Pegasus apps to Heroku using Python buildpacks or Docker containers with PostgreSQL, Redis, and Celery for scalable web applications.

Pegasus supports deploying to Heroku as a standard Python application or using containers.

Before getting started, first take the following steps in Heroku:

1. In the Heroku dashboard, create a new app.
2. Set up the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line) and run `heroku login` locally.
3. Connect your app, by running `heroku git:remote -a {{ heroku_app_name }}` in your project directory.

### Building using Heroku’s Python support

[Section titled “Building using Heroku’s Python support”](#building-using-herokus-python-support)

To deploy with Heroku’s Python module, first set up Pegasus using the “heroku” deploy platform option. This will create the necessary files for the Heroku Python buildpack.

You will also need to add the `nodejs` buildpack to your application using the following command:

```bash
heroku buildpacks:add --index 1 heroku/nodejs
```

This will ensure that the front end files are built and available when the `collectstatic` command runs.

### Building using Heroku’s Docker container support

[Section titled “Building using Heroku’s Docker container support”](#building-using-herokus-docker-container-support)

To deploy to Heroku using Docker, you should build Pegasus with the “heroku docker” deployment option. This will create your production `Dockerfile`, a `heroku.yml` file you can use [to build and deploy your container](https://devcenter.heroku.com/articles/build-docker-images-heroku-yml), and additional requirements/settings needed for the Heroku platform.

After building and setting up Heroku you will also need to configure Heroku to deploy with containers by running:

```bash
heroku stack:set container
```

### Configure Django Settings

[Section titled “Configure Django Settings”](#configure-django-settings)

The Heroku deployment uses its own settings module (which extends the normal `settings.py`). To tell Heroku to use it, set the `DJANGO_SETTINGS_MODULE` config var to `{ project_slug }.settings_production`. This can be done in the “settings” tab of your Heroku application (you may need to click to reveal the Config vars) or in the CLI using the following command (replacing the `project_slug` with your app name):

```bash
heroku config:set DJANGO_SETTINGS_MODULE={ project_slug }.settings_production
```

### Disable DEBUG

[Section titled “Disable DEBUG”](#disable-debug)

Similar to setting the Django Settings, you should disable DEBUG mode in your Heroku config:

```bash
heroku config:set DEBUG=False
```

### Set up Databases

[Section titled “Set up Databases”](#set-up-databases)

To set up your Postgres database, first enable the addon in the UI or by running:

```bash
heroku addons:create heroku-postgresql
```

Database migrations should be handled automatically by Heroku.

If you want to use Redis as a cache or to use Celery, you will need to install [the Heroku Redis addon](https://elements.heroku.com/addons/heroku-redis) from the UI or by running:

```bash
heroku addons:create heroku-redis
```

### Deploying

[Section titled “Deploying”](#deploying)

Both builds can be deployed using Heroku’s standard git integration. After you’ve connected your project’s git repository to Heroku, just run:

```bash
git push heroku main
```

You can also configure Heroku to automatically build from a branch of your git repository.

**After deploying, review the [production checklist](/deployment/production-checklist) for a list of common next steps**

### Setting environment variables

[Section titled “Setting environment variables”](#setting-environment-variables)

To set environment variables run:

```bash
heroku config:set {variable_name}={ value }
```

e.g.

```bash
heroku config:set SECRET_KEY={some long randomly generated text}
```

### Additional settings configuration

[Section titled “Additional settings configuration”](#additional-settings-configuration)

If you need additional production settings, you can put them in the `settings_production.py` file, or include them as config vars like this:

```python
SECRET_KEY = env('SECRET_KEY')
```

**It is strongly advised to put any secrets in your environment instead of directly in your settings file.**

### Running one-off commands

[Section titled “Running one-off commands”](#running-one-off-commands)

You can run once-off commands using the `heroku` CLI. E.g.

```bash
heroku run python manage.py bootstrap_subscriptions
```

### Building the front end

[Section titled “Building the front end”](#building-the-front-end)

As of Pegasus version 0.19, Heroku container builds will automatically build your front end files for you. You don’t need to do anything to set this up.

If you’re using Heroku’s Python support you can also configure Heroku to build your front-end files for you.

To set this up, all you need to do is add the `heroku/nodejs` buildpack to your application from the settings page.

Just make sure that this buildpack runs *before* the `heroku/python` buildpack, so that the compiled files are available when the `collectstatic` command runs.

### Celery support

[Section titled “Celery support”](#celery-support)

The Heroku environment supports Celery out-of-the-box.

Additionally, you may need to run the following command to initialize a Celery worker:

```bash
heroku ps:scale worker=1
```

This process should be the same for Python and containerized builds.

# Kamal (Deploy to any VPS)

> Deploy Pegasus to any Linux VPS using Kamal with automated SSL certificates, load balancing, and PostgreSQL database management.

Pegasus supports container-based deployment to any Linux server using [Kamal](https://kamal-deploy.org/).

Kamal is a deployment tool that uses Docker to deploy applications to servers. It is designed to be simple to use and to work with a single server or a cluster of servers. It can also be used to deploy multiple apps to the same server.

Kamal will deploy the app as Docker containers, and will also deploy the database and any other services that are required. It will also configure a load balancer ([kamal-proxy](https://github.com/basecamp/kamal-proxy)) to route traffic to the app and configure SSL certificates using LetsEncrypt.

By default, Pegasus will run all the services on a single server, but Kamal is designed to work with multiple servers, so you can easily move services to separate servers and update the Kamal configuration in `config/deploy.yml`.

### Screencast

[Section titled “Screencast”](#screencast)

You can watch a screencast showing how to deploy to a Hetzner server with Kamal here:

Or follow along with the documentation below.

### Overview

[Section titled “Overview”](#overview)

Deploying on Kamal will require a few pieces:

1. A server running Linux (the latest Ubuntu LTS is recommended---version 24.04 as of this writing) and accessible via SSH.
2. A domain name for your app. You will need to create a DNS record pointing to your server’s IP address.
3. A Docker registry to store your images. You can use [Docker Hub](https://hub.docker.com) or any other registry.
4. A development environment where you install and configure Kamal.

We’ll walk through these in more detail in order below.

### Provision and prepare your server

[Section titled “Provision and prepare your server”](#provision-and-prepare-your-server)

The first step is to provision a server where you will host your application. Some popular choices include:

* Hetzner (get €20 credit and support Pegasus with [this link](https://hetzner.cloud/?ref=49vhF1w3TIyB)).
* Digital Ocean Droplets (get $100 credit and support Pegasus with [this link](https://m.do.co/c/432e3abb37f3)).
* [Linode](https://www.linode.com/).
* [AWS](https://aws.amazon.com/) (Lightsail or EC2).
* [Google Cloud](https://cloud.google.com/).
* [Microsoft Azure](https://azure.microsoft.com/en-us).

It is recommended to choose the latest Ubuntu LTS---version 24.04 as of this writing---for your operating system. Other operating systems might work, but are not tested or officially supported.

We also recommend at least 2GB of RAM.

Once you’ve chosen a hosting company and provisioned a server, follow the instructions provided to login (SSH) to the server. You will need to be able to log in remotely to complete the rest of the setup.

The rest of these instructions will run kamal as the root user. If you prefer to run kamal as a different user---which can prevent certain kinds of attacks---see the note below.

### Set up DNS

[Section titled “Set up DNS”](#set-up-dns)

To set up SSL you will need a DNS record pointing at your server. Create a new “A” record using whatever tool you use to manage your DNS, and point it at the IP address of the server you created above.

The most common domain to use is `www.<yourdomain>.com`.

### Create the image repository

[Section titled “Create the image repository”](#create-the-image-repository)

Before doing deployment, you need a place to store your Docker images, also known as a *Docker registry*. The two recommended options are [Docker Hub](https://hub.docker.com/) and [Amazon Elastic Container Registry (ECR)](https://aws.amazon.com/ecr/).

Docker Hub is easier to use and good if you only have a single project (covered under their free tier). Amazon ECR is much more cost-effective if you have multiple projects---typically costing only pennies per project, per month.

You can choose another registry if you want, as described in the [Kamal docs](https://kamal-deploy.org/docs/configuration).

#### Using Docker Hub

[Section titled “Using Docker Hub”](#using-docker-hub)

First create an account on [Docker Hub](https://hub.docker.com/) and note your username.

Then create a new repository, choosing a unique name for your app, and **marking it “private”**.

Finally you will need to create an access token. Go to “Account Settings” —> “Security” and make a new access token, giving it the default permissions of Read, Write, Delete. **Save this token somewhere as you will need it in the next step and will only see it once.**

#### Using Amazon ECR

[Section titled “Using Amazon ECR”](#using-amazon-ecr)

You will need an [AWS account](https://aws.amazon.com/) to use Amazon ECR.

1. Login to the AWS console and navigate to the ECR service.
2. Under “Private Registry” —> “Repositories” click “Create repository”.
3. Choose a repository name, e.g. “myaccount/myapp” and keep the remaining defaults. Click “Create”.
4. Next, in the IAM service, create an IAM user / group, giving it the `AmazonEC2ContainerRegistryFullAccess` permissions policy.
5. Create an access key for the user / group and save the credentials.
6. [Install and configure the AWS CLI](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-configure.html) on your local machine, using those credentials.

You can test that everything is working by running:

```plaintext
aws ecr get-login-password
```

And confirming it returns a (very long!) password.

For a more detailed guide on setting up Amazon ECR with Kamal, see [this detailed writeup](https://dylancastillo.co/posts/deploy-a-django-app-with-kamal-aws-ecr-and-github-actions.html).

### Install and configure Kamal

[Section titled “Install and configure Kamal”](#install-and-configure-kamal)

Finally, we can set everything up to deploy our production application with Kamal. If you have a Ruby environment available, you can install Kamal globally with:

```bash
gem install kamal
```

*Note: you may want to use [`rbenv`](https://github.com/rbenv/rbenv) to manage your environment.*

If you don’t have Ruby running you can also use Docker to install Kamal, by creating an alias command as described [in the Kamal docs here](https://kamal-deploy.org/docs/installation/).

#### Create `secrets` file in the `.kamal` directory

[Section titled “Create secrets file in the .kamal directory”](#create-secrets-file-in-the-kamal-directory)

Kamal expects a `.kamal/secrets` file in this folder which will contain all the environment variables needed for deployment. The `secrets` file should not be checked into source control. See `.kamal/secrets.example` for the required variables.

```bash
cp .kamal/secrets.example .kamal/secrets
```

#### Update the Kamal deploy.yml file

[Section titled “Update the Kamal deploy.yml file”](#update-the-kamal-deployyml-file)

The Kamal configuration is in `config/deploy.yml`. You will need to update the following values:

* Docker image repo: `image: <namespace>/<repository-name>` - this is the repository you created above. If you’re using Docker Hub, the `namespace` will typically be your username, and if you’re using ECR you can use the exact repository name you chose above.
* Docker registry settings (see below)
* Your server IP address (or hostname) `<IP-ADDRESS>` (this value is listed once per service).
* Your app domain: `host: <your site url>` in the `proxy` section at the end, if this is not already set via your project configuration.

For the registry section, if you’re using **Docker Hub**, you will need to add the username you chose above:

```yaml
registry:
  username: <DOCKER REGISTRY USERNAME>  # set this
  password:
    - KAMAL_REGISTRY_PASSWORD
```

If you’re using **Amazon ECR**, you should update it as follows:

```yaml
registry:
  server: <your aws account id>.dkr.ecr.<your aws region id>.amazonaws.com
  username: AWS
  password: <%= %x(aws ecr get-login-password) %>
```

For other registries, see the [Kamal docs](https://kamal-deploy.org/docs/configuration/docker-registry/).

#### Update the .kamal/secrets file

[Section titled “Update the .kamal/secrets file”](#update-the-kamalsecrets-file)

Next, in your `.kamal/secrets` file you should add the following variables:

* If you’re using Docker Hub, set `KAMAL_REGISTRY_PASSWORD` to the access token value you created above. If you’re using Amazon ECR, you can remove this variable.
* Choose secure, unique, and ideally random values for `POSTGRES_PASSWORD` and `SECRET_KEY`.
* Update the `DATABASE_URL` value (use the same password as `POSTGRES_PASSWORD`).

You can review other settings in `deploy.yml`, but those should be all that you need to set yourself for your first deployment.

### Deploy

[Section titled “Deploy”](#deploy)

Finally, we can use Kamal to do the rest of the setup. Run the following on your *local* machine, from the project root directory.

```bash
kamal setup
```

This will perform all the tasks necessary to deploy your application (duplicated below from the [Kamal docs](https://kamal-deploy.org/docs/installation)):

* Connect to the servers over SSH (using root by default, authenticated by your SSH key).
* Install Docker on any server that might be missing it (using get.docker.com): root access is needed via SSH for this.
* Log into the registry both locally and remotely.
* Build the image using the standard Dockerfile in the root of the application.
* Push the image to the registry.
* Pull the image from the registry onto the servers.
* Ensure kamal-proxy is running and accepting traffic on ports 80 and 443.
* Start a new container with the version of the app that matches the current Git version hash.
* Tell kamal-proxy to route traffic to the new container once it is responding with 200 OK to GET /up.
* Stop the old container running the previous version of the app.
* Prune unused images and stopped containers to ensure servers don’t fill up.

If everything is set up properly then in five or so minutes you should be able to visit your new application at the configured domain. You’re done!

### Post-deployment steps

[Section titled “Post-deployment steps”](#post-deployment-steps)

Once you’ve gotten everything set up, head on over to the [production checklist](/deployment/production-checklist) and run through everything there. In particular, you will have to set up media files using an external service like S3.

#### Manage changes after initial deployment

[Section titled “Manage changes after initial deployment”](#manage-changes-after-initial-deployment)

See the `config/README.md` file in your project repo for pointers on managing the production environment after the initial deployment.

The main command you will regularly run is `kamal deploy`, which will push new releases and configurations of your application.

### Settings and Secrets

[Section titled “Settings and Secrets”](#settings-and-secrets)

Kamal builds use the `settings_production.py` file. You can add settings here, and use environment variables to manage any secrets, following the pattern used throughout the file. If you modify `settings_production.py` (or any other code) you will need to run:

```bash
kamal deploy
```

To push the changes to your servers.

Secrets should be managed in environment variables. To add new environment variables you will need to update them in two places:

1. The variable *name* needs to be added to the `env` section at the top of `config/deploy.yml`.
2. The variable name *and value* needs to be added to `.kamal/secrets` (the same `secrets` file we’ve been using above).

You can see examples of this for variables like `DATABASE_URL` in those two files.

Once you modify your environment variable files you will need to run:

```bash
kamal deploy
```

To update the variables on the server and redeploy the app.

### Running one-off commands

[Section titled “Running one-off commands”](#running-one-off-commands)

The easiest way to run one-off commands on your server is to use the `kamal app exec` command. For example:

```bash
kamal app exec -r web 'python manage.py bootstrap_subscriptions'
```

If you want an interactive SSH-style shell you can run:

```bash
kamal app exec -i bash
```

You should now have a shell where you can run any Python/`manage.py` command.

You can also get a database shell by running:

```bash
kamal accessory exec postgres -i 'psql -h localhost -p 5432 -U <youruser>' --reuse
```

For more information see [Kamal commands](https://kamal-deploy.org/docs/commands).

### Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

#### Something went wrong during setup

[Section titled “Something went wrong during setup”](#something-went-wrong-during-setup)

If the `kamal setup` command fails it should print out the error it got. Once you’ve resolved it, you may need to set up the services individually instead of re-running it. You can do that with the commands below:

```bash
# rebuild the PostgreSQL container
kamal accessory reboot postgres


# rebuild the Redis container
kamal accessory reboot redis


# rebuild the proxy container
kamal proxy reboot


# build the proxy container (if it didn't succeed the first time)
kamal proxy boot


# deploy the app
kamal deploy
```

If deploy continues to fail, check the logs of your docker container, using:

```bash
kamal app logs
```

#### Resolving `ERROR exec /bin/sh: exec format error`

[Section titled “Resolving ERROR exec /bin/sh: exec format error”](#resolving-error-exec-binsh-exec-format-error)

If you see this error on your server/logs it is likely that the architecture used to build your image is not the same as the one running on your server.

Review the `builder` section of your `deploy.yml` file and in particular make sure `multiarch` is set to `true`. You can also explicitly build the image on the remote server, or set the target architecture using other `builder` options as described [in the kamal docs](https://kamal-deploy.org/docs/configuration#using-remote-builder-for-native-multi-arch).

#### Resolving `ERROR /bin/sh: 1: /start: not found`

[Section titled “Resolving ERROR /bin/sh: 1: /start: not found”](#resolving-error-binsh-1-start-not-found)

If you see this error on your server/logs it is likely that your `/start` script has the wrong line endings. This can happen if you edit the `./deploy/docker_startup.sh` file in certain programs on the Windows operating system.

To fix this, change the line endings of the file from CRLF to LF using your preferred text editor (you can Google or ask ChatGPT how to do this for your specific environment).

#### Health checks are failing because of `ALLOWED_HOSTS`

[Section titled “Health checks are failing because of ALLOWED\_HOSTS”](#health-checks-are-failing-because-of-allowed_hosts)

Kamal runs a “health check” during deploys to ensure your new application is ready to handle requests. This involves pinging your workers on an internal docker address and waiting for them to respond with a “200 OK” status code.

Because it’s not possible to predict the hostname for these requests, a special middleware that bypasses the host check is included in Pegasus to handle this situation.

If health checks are failing that means the middleware isn’t set up properly. The healthcheck url that kamal hits (`/up` by default), must match the path defined in `apps.web.middleware.healthchecks.HealthCheckMiddleware` (also `/up` by default).

To fix it, confirm the following things:

1. Ensure that `"apps.web.middleware.healthchecks.HealthCheckMiddleware",` is the first middleware in `settings.MIDDLEWARE`.

2. Ensure that the paths match.

   1. The kamal path is defined in the `proxy` section of `deploy.yml`, under `healthcheck`. If there is no `healthcheck` section, then it’s using the default path.
   2. The middleware path is defined in `apps/web/middleware/healthchecks.py`.

### Cookbooks

[Section titled “Cookbooks”](#cookbooks)

#### Changing your site URL

[Section titled “Changing your site URL”](#changing-your-site-url)

To change your site’s URL, do the following:

1. Set up a new DNS endpoint as outlined above.
2. Change the `host` value in your proxy configuration in `deploy.yml` to the new domain.
3. Update your `ALLOWED_HOSTS` setting / environment variable as needed.
4. Run `kamal proxy reboot`.
5. Run `kamal deploy`

Your app should now be running on your new domain.

#### Getting a database backup

[Section titled “Getting a database backup”](#getting-a-database-backup)

Here is one way to get a database dump of your server:

First you can run the following command to save a database dump to the *host* machine:

```bash
kamal accessory exec postgres 'pg_dump -h localhost -p 5432 -U <your_app_user> <your_app_db_name> > db_dump.sql' --reuse
```

This should create a file on the *host* machine at `/home/kamal/db_dump.sql`.

If you want to copy this file locally, you can run:

```bash
scp kamal@yourapp.com:db_dump.sql ./
```

Note: you may want to zip or gzip this file first if you have a large database.

#### Doing a database restore

[Section titled “Doing a database restore”](#doing-a-database-restore)

To restore a database you first put the backup file on the host:

```bash
scp ./db_dump.sql kamal@yourapp.com:
```

Then create the DB:

```bash
kamal accessory exec postgres 'createdb -h localhost -p 5432 -U <your_app_user> <your_app_db_name>' --reuse
```

After that you will need to login to the *host* machine:

```bash
ssh kamal@yourapp.com
```

And copy the database dump onto the DB machine. Run `docker ps` to get the container id of the DB machine. Then run:

```bash
docker cp db_dump.sql <CONTAINER ID>:/tmp/db_dump.sql
```

Finally, login to the DB container:

```bash
docker exec -it <CONTAINER ID> /bin/bash
```

And restore the data:

```bash
psql -h localhost -p 5432 -U <your_app_user> <your_app_db_name> < /tmp/db_dump.sql
```

#### Deploying multiple apps to the same server

[Section titled “Deploying multiple apps to the same server”](#deploying-multiple-apps-to-the-same-server)

One of the major benefits of the VPS-based approach is that you can easily host multiple apps on the same hardware, which is usually a substantial cost advantage over hosting each one on its own.

This is now supported out of the box by Kamal and Pegasus. To deploy multiple applications to the same server, just set up Kamal individually for each application and run through the steps above. Once multiple sites are set up, `kamal-proxy` will automatically route traffic to the right app based on the site URL.

#### Running Docker as a non-root user

[Section titled “Running Docker as a non-root user”](#running-docker-as-a-non-root-user)

Follow these steps if you don’t want to run kamal and Docker as the root user.

##### Manually Install Docker

[Section titled “Manually Install Docker”](#manually-install-docker)

If you don’t run kamal as root you’ll have to install Docker yourself.

You can test if Docker is installed by running `docker -v` on the command line. You should see output like the following if it is installed correctly.

```plaintext
Docker version 24.0.5, build 24.0.5-0ubuntu1~20.04.1
```

If you need to install it, you can find instructions in [Docker’s documentation](https://docs.docker.com/engine/install/ubuntu/). You only need to install Docker Engine, not Docker Desktop.

##### Prepare a user account for Kamal

[Section titled “Prepare a user account for Kamal”](#prepare-a-user-account-for-kamal)

Next, create a user for Kamal to use. You can choose any username you like. In this example we will use `kamal`. We’ll also add this user to the `docker` group so that Kamal can run docker commands.

First login to your server as a user with root access. Then run the following commands:

```bash
sudo adduser kamal --disabled-password
sudo adduser kamal --add_extra_groups docker
```

Next, add your SSH key to the `kamal` user’s `authorized_keys` file so you can login without a password. If you need to generate an SSH key you can [follow these steps](https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authentication-on-a-linux-server):

```bash
sudo mkdir -p /home/kamal/.ssh
sudo cp ~/.ssh/authorized_keys /home/kamal/.ssh/authorized_keys
sudo chown -R kamal:kamal /home/kamal/.ssh
```

Next, test the login works. Exit out of your server and on your *local machine* run:

```bash
ssh kamal@<ip-address>
```

If you’ve set everything up properly the `kamal` user should be able to login with no password.

Once you’re logged in, as a final test, ensure the `kamal` user can run docker commands by running:

```bash
docker run hello-world
```

If the command above completes without error you are ready to go!

Finally, update your `config/deploy.yml` file to specify a different user by adding an ssh section, as [described in the docs](https://kamal-deploy.org/docs/configuration/ssh/#the-ssh-user):

```yaml
ssh:
  user: kamal
```

#### Cleaning up old Images on Amazon ECR

[Section titled “Cleaning up old Images on Amazon ECR”](#cleaning-up-old-images-on-amazon-ecr)

Amazon ECR charges based on the amount of image storage you use. In order to keep costs down, you set a lifecycle policy that cleans up old images.

The following configuration can be used to clean up all but the most recent 3 images:

![ECR Lifecycle Policy](/_astro/ecr-lifecycle-rule.BOc8NbC2_1XcA2R.webp)

For more details, see [Amazon’s documentation on lifecycle policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html)

# Deployment Overview

> Compare Django deployment options including VPS, PaaS platforms like Heroku and Render, Docker containers, and Kubernetes for SaaS applications.

Pegasus---like Django---can be deployed on any standard cloud infrastructure.

The most common ways of deploying Pegasus are:

1. On a raw VPS / Virtual Machine, such Digital Ocean, Linode, or Amazon EC2 or Lightsail
2. On a platform-as-a-service (PaaS) platform, such as Heroku, or PythonAnywhere
3. In a containerized way, using Docker, and (optionally) Kubernetes

Choosing the right deployment architecture involves a complex set of trade-offs, and there’s no one-size-fits-all solution. PaaS and Docker-based solutions tend to be easier to get up and running, but can be more difficult to modify and are often more expensive at scale. Meanwhile, setting up a VPS can be error-prone but is a very cost-effective way to deploy small applications.

Much of the choice will also depend on the knowledge and comfort of you/your team with various tools and platforms. See this [Django Deployment Guide](https://www.saaspegasus.com/guides/django-deployment/) for a big-picture overview on choosing a deployment strategy.

## Deployment to any VPS

[Section titled “Deployment to any VPS”](#deployment-to-any-vps)

The easiest way to deploy your application to any Linux server is to use Pegasus’s Kamal deployment support. This will deploy your application using portable, cross-platform Docker containers. For more information on deploying to a VPS, see the [kamal deployment documentation](/deployment/kamal).

## Officially supported PaaS platforms

[Section titled “Officially supported PaaS platforms”](#officially-supported-paas-platforms)

Pegasus also ships with configuration files to deploy to select platforms out-of-the-box. The officially supported platforms are:

* [Render](/deployment/render) (Python-based)
* [Fly](/deployment/fly) (Docker-based)
* [Heroku](/deployment/heroku) (Python or Docker)
* [Digital Ocean App Platform](/deployment/digital-ocean) (Docker-based)
* [Google Cloud Run](/deployment/google-cloud) (Docker-based)

Render and Fly are comparable, and are the recommended options for staging sites or MVPs, since they are easy to set up and have a generous free tier. Digital Ocean and Heroku tend to be more expensive but have a longer track record. Google Cloud is the most copmlex to set up, but allows you to access Google’s infrastructure.

If you would like to deploy to a platform that’s not listed here, please get in touch on Slack or by emailing <support@saaspegasus.com> and I’m happy to help!

## Other options

[Section titled “Other options”](#other-options)

If, for whatever reason, you want to deploy to a VPS but don’t want to use the built in Kamal option, the Django documentation provides a good overview on [how to deploy Django to your own server](https://docs.djangoproject.com/en/stable/howto/deployment/).

Pegasus user [Mitja Martini](https://mitjamartini.com/) has documented how he [deploys his SaaS Pegasus application to a VPS using Dokku](https://mitjamartini.com/blog/2024/09/22/deploying-django-on-dokku/) (an open-source, self-hosted PaaS platform).

Pegasus user [Artem Gordinskiy](https://artem.cool/) has documented his experience [migrating Pegasus apps from Kamal to Coolify](https://artem.cool/blog/coolify-django/) (another open-source, self-hosted PaaS).

Pegasus’s [Docker support](/docker) can be used as a basis for other production environments that supports container---for example, Google Kubernetes Engine and Amazon ECS.

Please reach out in the Pegasus Slack `#deployment` channel for any help on this!

# Production checklist

> Essential Pegasus production setup checklist covering security settings, email configuration, static files, media storage, and monitoring for live applications.

The following are some recommendations for deploying production Pegasus applications.

## Run the Django deployment checklist

[Section titled “Run the Django deployment checklist”](#run-the-django-deployment-checklist)

Django provides a [deployment checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/) that helps ensure your site has some of the most important settings properly configured for production environments. It is executed by running `manage.py check --deploy` on your production server.

It’s recommended to run this on your production application and address any critical issues.

The default Pegasus configuration will contain some warnings, to help prevent misconfigurations which can affect your site’s availability. Not all warnings are serious issues and some may not be possible to address (e.g. if part of your site must be available over HTTP instead of HTTPS). After running the `manage.py check --deploy` command you should read through the documentation for any issues you get and update the relevant settings where necessary.

*Note: The “unable to guess serializer” warnings are safe to ignore, and will be fixed in a future version of Pegasus.*

## Set your `ALLOWED_HOSTS`

[Section titled “Set your ALLOWED\_HOSTS”](#set-your-allowed_hosts)

In your app’s `settings_production.py` be sure to update the [`ALLOWED_HOSTS` setting](https://docs.djangoproject.com/en/4.1/ref/settings/#allowed-hosts) with the domain(s) you want the site to be available from, replacing the `'*'` that is there by default:

```python
ALLOWED_HOSTS = [
    'example.com',  # use your app's domain here
]
```

Failure to do this opens up your site to more HTTP host header attacks.

## Update your Django Site

[Section titled “Update your Django Site”](#update-your-django-site)

In order for absolute URLs and JavaScript API clients to work, your Django site should match your application’s domain. See the documentation on [absolute URLs](/configuration/#absolute-urls) to do this.

## Set up email

[Section titled “Set up email”](#set-up-email)

If you haven’t already, you’ll want to set up your site to [send email](/configuration/#sending-email)

## Make sure your secrets are set

[Section titled “Make sure your secrets are set”](#make-sure-your-secrets-are-set)

Application secrets (e.g. API keys, passwords, etc.) are managed in environment variables. Ensure that you have configured the following variables (if you are using them):

* All apps should set `SECRET_KEY` to a long, randomly-generated value.
* If you’re using Stripe, you should set the `STRIPE_TEST_PUBLIC_KEY`, `STRIPE_TEST_SECRET_KEY`, `STRIPE_LIVE_PUBLIC_KEY`, and `STRIPE_LIVE_SECRET_KEY` config vars (or whatever subset you are using). You also need to set `STRIPE_LIVE_MODE` to `True`.
* If you set up email, ensure whatever keys/secrets you need are set.
* If you’re using Mailchimp, set `MAILCHIMP_API_KEY` and `MAILCHIMP_LIST_ID`.
* If you’re using Health Checks, set `HEALTH_CHECK_TOKENS`.

Refer to your [chosen platform’s documentation](/deployment/overview) for details on how to set environment variables in that platform.

## Sync Stripe data

[Section titled “Sync Stripe data”](#sync-stripe-data)

After setting up your Stripe variables per above, you’ll want to run:

```bash
python manage.py bootstrap_subscriptions
```

to initialize your subscription data.

See your [chosen platform’s documentation](/deployment/overview) for how to run one-off commands.

## Set up media files

[Section titled “Set up media files”](#set-up-media-files)

Some functionality, like user profile pictures, requires saving user-uploaded files. In development these are saved to the file system, but in most production environments the file system is not usable for it. Instead, you need to set up an external storage to handle these.

There is guidance on configuring media files in the [settings and configuration docs](/configuration/#storing-media-files).

The most common choice of external storage is [Amazon S3](https://aws.amazon.com/s3/), though many cloud providers have their own S3-compatible options, e.g. [Digital Ocean Spaces](https://www.digitalocean.com/products/spaces).

## Check your static file setup

[Section titled “Check your static file setup”](#check-your-static-file-setup)

By default, Pegasus uses [whitenoise](https://whitenoise.readthedocs.io/en/stable/index.html) for static files. **If you keep the default setup, you do not need to change anything.** Static files will be built and collected as part of the build process of your Docker container and should be available on your production site.

If you decide to switch to serving files externally, for example, using Amazon S3, then you may need to modify your static file set up for some platforms. This is because production secrets necessary to save files to S3 may not be available during the Docker container build.

If this is the case, you should modify your deployment set up so that `python manage.py collectstatic --noinput` is run at the same time as Django database migrations, so that the necessary secrets are available to the application. The exact way to do this will vary by deployment platform.

## Optimize your front end

[Section titled “Optimize your front end”](#optimize-your-front-end)

The front-end files that ship with Pegasus are the developer-friendly versions. In production, these should be optimized. Most Pegasus deployment configurations will handle this automatically for you, but if you need to handle it yourself, follow the guidance below.

First you should add the compiled files to your `.gitignore` as described in the [front end docs](/front-end/overview). Then, as part of your CI/CD deployment process, you should build the bundle files directly on your production server (using `npm install && npm run build`).

This will ensure that the latest, optimized version of the front-end code is always deployed as part of your production environment.

## Update other configuration options

[Section titled “Update other configuration options”](#update-other-configuration-options)

See [the configuration page](/configuration) for a larger list of options, including social login, sign up flow changes, analytics, logging, adding captchas, and so on.

## Set up monitoring

[Section titled “Set up monitoring”](#set-up-monitoring)

It’s highly recommended to enable Sentry and connect it to your application so that you can see any errors that are encountered.

It’s also recommended to enable the health check endpoint and connect it to a monitoring tool like [StatusCake](https://www.statuscake.com/) or [Uptime Robot](https://uptimerobot.com/) so that you can be alerted whenever your site or services are having an outage. The URL you should connect is: `yourdomain.com/health/`.

If you have the “Health Check Endpoint” option enabled for your project you should also ensure that you have set the `HEALTH_CHECK_TOKENS` environment variable to a secure value. This can be a comma-separated list of tokens that are required to access the health check endpoint. For example:

```plaintext
HEALTH_CHECK_TOKENS=secrettoken1,secrettoken2
```

Then your health check endpoint will only be accessible at: `https://yourdomain.com/health/?token=secrettoken1` and `https://yourdomain.com/health/?token=secrettoken2`

These URLs can then be connected to a monitoring tool to ensure that only your monitoring tool (or anyone who knows the token) can access the health check endpoint.

## Double-check your language settings

[Section titled “Double-check your language settings”](#double-check-your-language-settings)

Make sure your [internationalization settings](/internationalization/) are correct, and you don’t have any extra languages in `settings.LANGUAGES` that you don’t currently support. This is especially important if you are using Wagtail, as links to pages in unsupported languages may error or return the wrong results.

## Consider switching to `psycopg2` source distribution

[Section titled “Consider switching to psycopg2 source distribution”](#consider-switching-to-psycopg2-source-distribution)

For ease of development, Pegasus ships with the `psycopg2-binary` package which is used for connecting to PostgreSQL however the [psycopg documentation](https://www.psycopg.org/docs/install.html#psycopg-vs-psycopg-binary) recommends using the source distribution (`psycopg2`) in production environments.

The issues mentioned in the documentation mostly impact non-Docker deployments.

### Switching from `psycopg2-binary` to `psycopg2`

[Section titled “Switching from psycopg2-binary to psycopg2”](#switching-from-psycopg2-binary-to-psycopg2)

1. In `requirements/requirements.in`, replace `psycopg2-binary` with `psycopg2`
2. [Re-build](/python/packages/) your requirement TXT files

If you are using the Dockerfiles shipped with Pegasus you should not need to make any changes however if you are running your Pegasus app directly on a VM you will need to make sure the [build prerequisites](https://www.psycopg.org/docs/install.html#build-prerequisites) are installed before deploying the requirements changes.

# Render

> Deploy Pegasus applications to Render platform with PostgreSQL, Redis, automatic builds, and Celery worker support for web services.

Pegasus supports deploying to [Render](https://render.com/) as a standard Python application.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

If you haven’t already, create your Render account.

To use celery you will need to upgrade to a paid plan.

### Deploying

[Section titled “Deploying”](#deploying)

Once you’ve logged into Render you can create your app as follows:

1. In the Render dashboard, create a new blueprint
2. Connect your GitHub or Gitlab account and select your project’s repository
3. Configure the *Blueprint Name* and select the branch you want to deploy from
4. Review the configuration, add settings and click ‘Apply’

This will kick off the process to create your PostgreSQL database and Redis instances as well as deploy your web application (configured in your project’s `render.yaml` file).

**After deploying, review the [production checklist](/deployment/production-checklist) for a list of common next steps**

### Build Script

[Section titled “Build Script”](#build-script)

The `build.sh` file is run by Render to run the commands needed to build the app, as [described here](https://render.com/docs/deploy-django#create-a-build-script). This is also where “release” commands like `collectstatic` and `migrate` run.

If there are other commands (e.g. `./manage.py bootstrap_subscriptions`) that you want to run on every deploy you can add them to `build.sh`.

If you enable celery, it will use the `build_celery.sh` file, which runs the basic build steps, but not the “release” commands. You generally should not need to modify this file.

#### (Optional) Running Migrations in the Release Phase

[Section titled “(Optional) Running Migrations in the Release Phase”](#optional-running-migrations-in-the-release-phase)

If you want, you can optionally run the database migrations in the release phase using Render’s [Deploy steps](https://render.com/docs/deploys#deploy-steps) functionality.

This is not required, and notably **it is not supported on Render’s free tier**, but may lead to a more consistent deployment process.

To do this, first remove the following lines from `deploy/build.sh`:

```bash
echo "Running database migrations"
python manage.py migrate
```

Then create the following file at `deploy/pre_deploy.sh`:

```bash
#!/usr/bin/env bash
# exit on error
set -o errexit


export DJANGO_SETTINGS_MODULE={{cookiecutter.project_slug}}.settings_production


echo "Running database migrations"
python manage.py migrate
```

Finally, add the following line to your `render.yaml` file, after the `buildCommand`:

```yaml
    preDeployCommand: "./deploy/pre_deploy.sh"
```

After completing these steps, migrations will run in the pre-deploy phase.

### Settings and Secrets

[Section titled “Settings and Secrets”](#settings-and-secrets)

Render builds use the `settings_production.py` file. You can add settings here or in the base `settings.py` file, and use environment variables to manage any secrets, following the examples in these files.

Environment variables can be managed from the “Environment” tab on your app’s dashboard.

### Running One-Off Commands

[Section titled “Running One-Off Commands”](#running-one-off-commands)

You can run one-off commands in the Render shell (paid plan required) or [via SSH](https://render.com/docs/ssh).

### Celery Support

[Section titled “Celery Support”](#celery-support)

To run celery workers on Render you will need to upgrade to a paid plan.

Then in your `render.yaml` file uncomment the ‘celery’ section and rebuild from the steps above.

If you previously deployed your application you can choose “Update Existing Resources” to avoid having to recreate your app / database / redis instance.

### Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

**Sometimes Render fails to build on the first deployment.** Retrying the deployment from the same commit seems to resolve this.

### Container-based deployment

[Section titled “Container-based deployment”](#container-based-deployment)

It is possible to use Render’s docker-based support to deploy Pegasus apps, but it is not recommended because there is no “release” phase, which makes it difficult to set up things like database migrations.

More details can be found in [this support thread](https://community.render.com/t/release-command-for-db-migrations/247/7).

# Troubleshooting

> Resolve common Django deployment issues including 400 Bad Request errors, broken styles, API client problems, and misconfigured absolute URLs.

Below are some common issues related to deployment, and how to fix them.

### Page displaying a 400 Bad Request error page

[Section titled “Page displaying a 400 Bad Request error page”](#page-displaying-a-400-bad-request-error-page)

**Problem:**

Your site deploys but you get a “400 Bad Request” when opening it in a browser.

**Solution:**

This is usually caused by a misconfigured `ALLOWED_HOSTS` setting. See [the section on `ALLOWED_HOSTS`](/deployment/production-checklist/#set-your-allowed_hosts) to fix.

### App is online but all styles are broken

[Section titled “App is online but all styles are broken”](#app-is-online-but-all-styles-are-broken)

**Problem:**

Your app is working but all the pages look horrible and unstyled.

**Solution:**

It’s likely that your static file set up is not correct. If you use Pegasus-supported deployments, this shouldn’t happen, but if you’ve veered from them at all it’s a common failure mode.

To fix, Ensure that you are running `collectstatic` somewhere in your deployment pipeline, and that your `STATIC_ROOT` is properly configured. More on static files in production can be found in the [Django documentation](https://docs.djangoproject.com/en/4.1/howto/static-files/deployment/).

### JavaScript API clients not working

[Section titled “JavaScript API clients not working”](#javascript-api-clients-not-working)

**Problem**

JavaScript API clients are failing to load data. This is likely the problem if the employee React demo or the teams list UI don’t work properly.

**Solution:**

This is usually caused by a misconfigured Django site. See the documentation on [absolute URLs](/configuration/#absolute-urls) to fix.

### Invitation / account emails have the wrong links

[Section titled “Invitation / account emails have the wrong links”](#invitation--account-emails-have-the-wrong-links)

**Problem**

When you try to confirm an email address or accept a team invitation you are sent to the wrong site (e.g. localhost).

**Solution:**

This is usually caused by a misconfigured Django site. See the documentation on [absolute URLs](/configuration/#absolute-urls) to fix.

### Stripe callbacks are going to the wrong place

[Section titled “Stripe callbacks are going to the wrong place”](#stripe-callbacks-are-going-to-the-wrong-place)

**Problem**

After completing a payment in Stripe Checkout, you are redirected to the wrong place (e.g. localhost).

**Solution:**

This is usually caused by a misconfigured Django site. See the documentation on [absolute URLs](/configuration/#absolute-urls) to fix.

# Standalone React Front End

> Build decoupled React single-page applications with Vite, session authentication, API integration, and deployment to static hosting platforms.

Experimental Feature

This feature is experimental. It is likely (but not guaranteed) that it will make it into a future Pegasus release. While in the experimental phase, it may undergo significant changes, including breaking changes.

*Added in version 2024.4. Expanded in version 2025.4.1.*

SaaS Pegasus’s default React integration is based on a hybrid-model for reasons [outlined here](https://www.saaspegasus.com/guides/modern-javascript-for-django-developers/client-server-architectures/#enter-the-hybrid-architecture). The hybrid model is still recommended for the overwhelming majority of Pegasus projects using React. However, there are valid reasons to run a completely separate React front---including access to dedicated tooling and libraries, isolating your front end and back end code, and working with AI-based tools that generate single-page applications.

Pegasus experimentally ships with a decoupled front end *example* single page application that can be used as a starting point for building out a decoupled front end / SPA with React. It uses [Vite](https://vitejs.dev/) as a development server and build tool.

The features it includes are:

* A standalone Vite / React application.
* Authentication via headless allauth and sessions---including sign up, login, social login, email confirmation, two-factor authentication, and logout functionality.
* A sample profile page which shows how to retrieve data from the logged in user (via the back end APIs) and display it.
* The employee lifecycle demo that ships with Pegasus (if enabled), showing a full create, update, delete (CRUD) workflow.

The standalone front end is *only available on TailwindCSS* and uses DaisyUI for styling.

**The standalone is not intended to be a replacement for Pegasus’s UI, but a reference example you can use as a starting point to build standalone, single-page-applications with Pegasus and React.**

Here’s a demo:

And here are some technical details:

## Running the front end

[Section titled “Running the front end”](#running-the-front-end)

*If you are using Docker, your front end should start in a separate container after running `make init`.*

The front end lives in the `/frontend` folder of your project. To set it up for the first time, first go into the directory:

```bash
cd frontend
```

And install npm packages:

```bash
npm install
```

Create your `.env` file:

```bash
cp .env.example .env
```

Then run the dev server:

```bash
npm run dev
```

Note: your Django backend must also be running for the front end to work, and you must also [build your Django front end](/front-end/overview) for styles to work.

## Authentication

[Section titled “Authentication”](#authentication)

Authentication uses session-based authentication against the Django backend (previous versions of the front end used JWTs). The authentication implementation borrows heavily from the [allauth example](https://github.com/pennersr/django-allauth/tree/main/examples/react-spa) project. In particular, the `src/lib/` and `src/allauth_auth/` folders have been copied in from that project and lightly modified to work with Pegasus.

Authentication is primarily handled via *authenticated routes* and *authentication context*. You can see an example of how to set this up in the profile page.

Any page in your application that requires login can be wrapped in the `AuthenticatedRoute` component. For example, like this:

```jsx
<AuthenticatedRoute>
  <p>Hello authenticated user!</p>
</AuthenticatedRoute>
```

Alternatively, if you make a page a child of the `<Dashboard>` component this will be automatically configured for you. See `main.tsx` as an example of how this is set up.

When using the `AuthenticatedRoute`, if the user is not logged in they will be redirected to the login page. If they are logged in, they will be able to access the route, and you can assume access to the user object and other APIs that require login.

If you want to access user data you can use the `useAuthInfo` helper function which returns an `AuthContext` context. Here is a simplified example taken from the Profile page:

```jsx
import { useAuthInfo } from "../../allauth_auth/hooks";


export default function Profile() {
  const { user } = useAuthInfo();
  return <p>The user's email address is: {user?.email}</p>
}
```

## Backend API access

[Section titled “Backend API access”](#backend-api-access)

The front end uses the [same api client](/apis/#api-clients) as the backend / hybrid model. The API client is installed as a local npm package.

Authentication is handled via sessions and does not require any additional configuration. Here is a basic example from the employee app demo:

```jsx
import {PegasusApi} from "api-client";
import EmployeeApplication from "../../../../assets/javascript/pegasus/examples/react/App.jsx";
import {getApiConfiguration} from "../../api/utils.tsx";


export default function EmployeeApp() {
  const client = new PegasusApi(getApiConfiguration());
  return (
    <EmployeeApplication client={client} urlBase="/dashboard/employees" />
  );
}
```

## Routing

[Section titled “Routing”](#routing)

Routing is handled by [React Router](https://reactrouter.com/en/main).

The main routes for the project are configured in `main.tsx`, and you can also include child routes by following the pattern used by the employee demo.

## URLs in Emails

[Section titled “URLs in Emails”](#urls-in-emails)

Some workflows, like email confirmation and password reset, require sending the user a link to your site. Allauth only supports a single link for the entire application so you need to choose whether that link should go to your Django application or your React front end.

To use the React front end’s pages for these workflows, you can set `USE_HEADLESS_URLS = True` in your settings or environment variables. This will configure the [`HEADLESS_FRONTEND_URLS` setting](https://docs.allauth.org/en/dev/headless/configuration.html) to work with the built-in front end.

## Deployment

[Section titled “Deployment”](#deployment)

Big picture, you should deploy the standalone front end and Django backend separately, and use different subdomains to point to them. The most common set up is to deploy the front end to either “mydomain.com” or “[www.mydomain.com](http://www.mydomain.com)”, and then deploy the backend to “app.mydomain.com” or “platform.mydomain.com”.

### The Django Backend

[Section titled “The Django Backend”](#the-django-backend)

You will need to deploy your Django backend using any of the [standard deployment methods](/deployment/overview).

In addition to a standard deployment, you will specifically need to set the following additional settings, by overriding them in your environment variables or a production settings file:

* `FRONTEND_ADDRESS`: Your front end’s full URL, e.g. “<https://www.mydomain.com>”
* `CORS_ALLOWED_ORIGINS`: Full URLs of both your frontend and backend addresses, e.g. “<https://www.mydomain.com,https://app.mydomain.com>”
* `CSRF_COOKIE_DOMAIN`: All domains and subdomains, e.g. “.mydomain.com” (note the leading ”.”).
* `SESSION_COOKIE_DOMAIN`: Same as `CSRF_COOKIE_DOMAIN`.

### The React Frontend

[Section titled “The React Frontend”](#the-react-frontend)

The frontend can be deployed anywhere that hosts static sites, including Cloudflare Pages, Netlify, or S3.

The basic steps for deployment are to run `npm run build` and then serve the output directory as a static site.

In addition, the following environment variables need to be set during build. Do not include trailing slashes:

* `VITE_APP_BASE_URL`: Your django backend url, e.g. “<https://app.mydomain.com>”
* `VITE_ALLAUTH_BASE_URL`: The full allauth base route for your backend, e.g. “<https://app.mydomain.com/_allauth/browser/v1>”

Each static site host has their own way of configuring the above setup. Below are quick example instructions for deploying the front end on Cloudflare Pages:

1. In the Cloudflare dashboard, visit “Workers & Pages” and click “Create”

2. Under “pages”, select the option to connect a Github repository.

3. Pick your Pegasus Github repository. You may have to authenticate and provide access permissions.

4. Fill in the following settings:

   1. Build command: `npm run build`

   2. Build output directory: `dist`

   3. Root directory: `frontend`

   4. Add the following environment variables. *Note that the URLs should not end in slashes.*

      * `VITE_APP_BASE_URL: https://<your Django backend URL>`
      * `VITE_ALLAUTH_BASE_URL: https://<your Django backend URL>/_allauth/browser/v1`
      * `NODE_VERSION: 22.13.0`
      * `NPM_VERSION: 11.3.0`

5. Click “Save and Deploy”

6. After the initial deployment you can add a custom domain to your front end.

## Known Limitations

[Section titled “Known Limitations”](#known-limitations)

This is an experimental feature meant to provide a starting point for building a standalone React front end against your Pegasus app. It is *not* a complete, production-ready app, in the same way that standard Pegasus is.

Here are some of the larger limitations:

* Only a very limited subset of Pegasus functionality is available in the front end.
* The front end styles only support Tailwind CSS.
* Internationalization (translations) are not supported.

## Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

**I’m getting a “URI malformed” error when I load the app.**

This is likely because your `frontend/.env` file does not exist, or your `VITE_APP_BASE_URL` is not properly set inside it. See `frontend/.env.example` for an example `.env` file suitable for development.

## Feedback

[Section titled “Feedback”](#feedback)

If you have any feedback on this feature I would love to hear it! Feedback could include bug reports, feature requests, or any suggested architectural changes.

# Front End Design Patterns

> JavaScript design patterns for Pegasus projects including site-wide libraries, npm package integration, and SiteJS utility functions with Vite and Webpack.

This section provides guidance on common front end tasks.

## Providing site-wide JavaScript

[Section titled “Providing site-wide JavaScript”](#providing-site-wide-javascript)

Sometimes you need access to a library or piece of code you’ve written on many different pages. Pegasus has a few patterns for dealing with this.

### `site.js` and `app.js`

[Section titled “site.js and app.js”](#sitejs-and-appjs)

There are two “site-wide” JavaScript files used in Pegasus.

The `site.js` file contains code that you want loaded *on every page*. Its bundle file (`site-bundle.js`) is included in your `base.html`. This is a good place to put global code, library imports, etc. which should always be available.

The `app.js` file contains code that you want loaded \*on some pages---typically after login. This is a good place to put helper functions that are only used in a few places. The `app-bundle.js` file is *not* included by default, and so must be explicitly added to any page that needs it, like this:

Vite:

```jinja
{% load django_vite %}
{% block page_js %}
  {% vite_asset 'assets/javascript/app.js' %}
{% endblock page_js %}
```

Webpack:

```jinja
{% load static %}
{% block page_js %}
  <script src="{% static 'js/app-bundle.js' %}"></script>
{% endblock page_js %}
```

The distinction between `site` and `app` is somewhat arbitrary---if you wanted you could create page-level files for every function/module, or dump all your code into `site.js`. But it’s done to balance page speed and complexity.

The more individual JavaScript files you have, the less code will have to be loaded on any individual page. This should generally make your site faster. But it’s more complex to maintain as each new file needs to be added to your `vite.config.ts`/`webpack.config.js`.

Meanwhile, dumping everything in a single file is easier to maintain, but can lead to bulky initial page load times. After the initial load, the browser’s cache should help, so this can be acceptable for most pages (apart from your landing page / marketing site).

Because of this, Pegasus recommends keeping `site.js` lightweight, and lumping together code after login into `app.js`. But feel free to do something differently!

## Making an existing package available

[Section titled “Making an existing package available”](#making-an-existing-package-available)

To make a library available on every page, you can follow these steps. Note: there are many ways to do this, but this is the way it’s currently handled in Pegasus.

1. Install the library via `npm install <library>`.
2. Create a javascript file for the library in `assets/javascript`.
3. Expose the library via the library’s instructions. E.g. `window.library = require('library')`. This step will vary based on the library.
4. Import the library in your `site.js` or `app.js` file (see above for the distinction).
5. Rebuild your front end.

You can see an example with HTMX (version 2023.2 and later) or Alpine.js (version 2023.3 and later).

### Example: Adding simple-datatables

[Section titled “Example: Adding simple-datatables”](#example-adding-simple-datatables)

As an example, if you want to add [simple-datatables](https://github.com/fiduswriter/simple-datatables) to your project, first install it:

```bash
npm install simple-datatables
```

Then add the following lines to your `site.js` file:

```javascript
import { DataTable } from 'simple-datatables';
window.DataTable = DataTable;
```

Then you can access the `DataTable` object from any page:

```javascript
// initialize the table with id "mytable"
const dataTable = new DataTable("#mytable", {
   searchable: true,
   fixedHeight: true,
});
```

### Using the SiteJS library

[Section titled “Using the SiteJS library”](#using-the-sitejs-library)

Pegasus previously used [webpack libraries](https://webpack.js.org/guides/author-libraries/) to expose helper code, however has shifted to providing this functionality by directly updating the `window.SiteJS` object.

If you’d like to add utility functions to sitewide JavaScript, you can update this object in any front end file. For example in `app.js` we add modal functionality as follows:

```javascript
import { Modals as AppModals } from './web/modals';


// Ensure SiteJS global exists
if (typeof window.SiteJS === 'undefined') {
  window.SiteJS = {};
}


// Assign this entry's exports to SiteJS.app
window.SiteJS.app = {
  Modals: AppModals,
}
```

Then, as long as you import the `app-bundle.js` file (as per above), you will have all the exported code available via the `SiteJS` library. So you can run:

```javascript
const modal = SiteJS.app.Modals.initializeModal();
```

The convention for using this functionality is:

```javascript
SiteJS.<package-name>
```

Where `<package-name>` is the name of the file in the `module.exports` section of `vite.config.ts`/`webpack.config.js`. You can look at existing Pegasus examples to get a better sense of how this works.

Note that this functionality was first built on Webpack libraries, but has since been made explicit in the code and is only a *convention*. You can use any other convention you want, but this is the one that Pegasus uses.

# Migrating from Webpack to Vite

> Step-by-step guide to migrate Pegasus projects from Webpack to Vite bundler with React JSX file extensions and template updates.

This page describes how to migrate your project from Webpack to Vite.

There is also a video walkthrough of the process here:

## 1. Upgrade your project to 2025.5

[Section titled “1. Upgrade your project to 2025.5”](#1-upgrade-your-project-to-20255)

First upgrade your project to 2025.5 [according to the normal process](/upgrading). Do *not* change your bundler setting at this stage.

Do normal testing and verification that everything is working with Webpack on version 2025.5.

## 2. React only: Rename all `.js` files using JSX to `.jsx`

[Section titled “2. React only: Rename all .js files using JSX to .jsx”](#2-react-only-rename-all-js-files-using-jsx-to-jsx)

Vite is stricter than Webpack about file extensions, so any file that uses JSX syntax (i.e. React code), needs to be in a file with a `.jsx` extension.

After changing the extensions of your files you may need to tweak your JavaScript imports. You’ll also need to modify your `webpack.config.js` file if any referenced files have changed.

## 3. Change your bundler setting from “Webpack” to “Vite” and do another Pegasus upgrade

[Section titled “3. Change your bundler setting from “Webpack” to “Vite” and do another Pegasus upgrade”](#3-change-your-bundler-setting-from-webpack-to-vite-and-do-another-pegasus-upgrade)

Next, in your project settings, change the bundler to “Vite” and perform another upgrade.

This should handle *most* of the Webpack —> Vite migration for you, including migrating your npm packages, build commands, and built-in CSS / JavaScript bundles.

During this step *do not delete your `webpack.config.js` file*, as you’ll want to reference it for the next step.

## 4. Add your custom CSS / JavaScript exports to your vite config

[Section titled “4. Add your custom CSS / JavaScript exports to your vite config”](#4-add-your-custom-css--javascript-exports-to-your-vite-config)

Next find the `entry` section of your project’s `webpack.config.js` that configures your exported bundle files. It will look something like this, though the exact files listed will depend on your project settings:

```javascript
entry: {
    'site-base': './assets/site-base.js',  // base styles shared between frameworks
    'site-tailwind': './assets/site-tailwind.js',  // required for tailwindcss styles
    site: './assets/javascript/site.js',  // global site javascript
    app: './assets/javascript/app.js',  // logged-in javascript
    dashboard: './assets/javascript/shadcn-dashboard/index.jsx',
    teams: './assets/javascript/teams/teams.jsx',
    'edit-team': './assets/javascript/teams/edit-team.jsx',
    'chat': './assets/javascript/chat/chat.jsx',
  },
```

Importantly, *if you have added or changed anything in this section, you will need to re-apply those changes to the `build.rollupOptions.input` section of `vite.config.ts`.* The section that you need to modify will look something like this:

```javascript
  build: {
    rollupOptions: {
      input: {
        'site-base': path.resolve(__dirname, './assets/site-base.js'),
        'site-tailwind': path.resolve(__dirname, './assets/site-tailwind.js'),
        'site': path.resolve(__dirname, './assets/javascript/site.js'),
        'app': path.resolve(__dirname, './assets/javascript/app.js'),
        'dashboard': path.resolve(__dirname, './assets/javascript/shadcn-dashboard/index.jsx'),
        'teams': path.resolve(__dirname, './assets/javascript/teams/teams.jsx'),
        'edit-team': path.resolve(__dirname, './assets/javascript/teams/edit-team.jsx'),
        'chat': path.resolve(__dirname, './assets/javascript/chat/chat.jsx'),
      },
```

You should update this in the same pattern with any changes you have made to your webpack config.

## 5. Update your front end file references in templates

[Section titled “5. Update your front end file references in templates”](#5-update-your-front-end-file-references-in-templates)

Finally, update any Django templates you had that imported bundle files. Specifically, reference that look something like this:

```jinja
{% block page_js %}
  <script src="{% static 'js/app-bundle.js' %}" defer></script>
{% endblock %}
```

Will need to be updated to:

```jinja
{% block page_js %}
  {% vite_asset 'assets/javascript/app.js' %}
{% endblock %}
```

Note that this uses the *source* file path instead of the bundle file.

You will also need to add `{% load django_vite %}` to the top of the template. And if the flie uses React you’ll also need to add the `{% vite_react_refresh %}` tag to the `page_js` section.

## 6. Update Webpack libraries

[Section titled “6. Update Webpack libraries”](#6-update-webpack-libraries)

*Most projects won’t need to do this.*

If you have added any code that relies on [Pegasus’s `SiteJS` library](/front-end/design-patterns/#using-the-sitejs-library) you will need to update it to explicitly expose itself on the window object.

In the associated JavaScript file (in this case `library.js`), you need to change something like:

```javascript
export MyLibrary;
```

To:

```javascript
if (typeof window.SiteJS === 'undefined') {
  window.SiteJS = {};
}


window.SiteJS.library = {
  MyLibrary: MyLibrary,
}
```

## 7. Rebuild and run your front end

[Section titled “7. Rebuild and run your front end”](#7-rebuild-and-run-your-front-end)

Finally, rebuild and run your front end, according to the [vite docs](/front-end/vite):

```bash
npm install
npm run dev
```

And confirm everything is working as expected. Once everything is working as expected, you can delete your `webpack.config.js` file.

If you run into any issues during the migration, reach out via standard support channels.

# Front End Overview

> Modern JavaScript build pipeline with Vite or Webpack, TypeScript support, CSS compilation, and hybrid Django template integration architecture.

*This page documents the front end files that are integrated into Django. See [the standalone front end docs](/experimental/react-front-end) for the separate React front end.*

## Architecture

[Section titled “Architecture”](#architecture)

Pegasus’s front-end architecture is a hybrid model, with a front-end codebase that is compiled and used directly in Django templates via Django’s static files infrastructure.

There are two setups, one built on top of Webpack, and a more modern one built on top of Vite. The architecture of these is very similar, just built on different tools.

Big picture, the front end consists of a build tool ([Vite](https://vite.dev/) or [Webpack](https://webpack.js.org/)) and a compiler ([esbuild](https://esbuild.github.io/) or [Babel](https://babeljs.io/)) which compiles the front-end code into bundle files that can be referenced using Django’s static file system, as represented in the diagram below.

**Vite**

![Vite Build Pipeline](/_astro/js-pipeline-with-django-vite.QgrpxV9D_ZmxfJY.webp)

**Webpack** ![Build Pipeline](/_astro/js-pipeline-with-django.CTtPRtGS_ZpXqRz.webp)

Pegasus’s styles use either the [Tailwind](https://tailwindcss.com/), [Bootstrap](https://getbootstrap.com/) or [Bulma](https://bulma.io/) CSS frameworks, and building the CSS files is included as part of the front-end build pipeline. For more details on CSS in Pegasus, see the [CSS documentation](/css/overview).

**For a much more detailed overview of the rationale behind this architecture, and the details of the set up see the [Modern JavaScript for Django Developers](https://www.saaspegasus.com/guides/modern-javascript-for-django-developers/) series.**

## Choosing a front end build tool

[Section titled “Choosing a front end build tool”](#choosing-a-front-end-build-tool)

Pegasus currently lets you choose between Vite and Webpack as the primary build tool for your front end. Choosing is relatively simple: **if you don’t know what you want, use Vite**.

Vite is faster, more modern, and includes a number of features not supported by webpack, including:

1. Hot Module Replacement (HMR)---a development feature that lets code changes in your front end files automatically update without a full-page reload.
2. Code splitting---a production feature that breaks your front end files into individual bundles that encapsulate code dependencies. This leads to less redundant JavaScript and faster page loads.

The main reason to choose Webpack is if you are already using it and don’t want to switch tools. See [this video](https://www.youtube.com/watch?v=qVwRygtffiw) for more on the benefits of Vite over Webpack.

## Front-end files

[Section titled “Front-end files”](#front-end-files)

The source front-end files live in the `assets` directory, while the compiled files get created in the `static` directory.

Generally you should only ever edit the front-end files in `assets` directly, and compile them using the instructions below.

## Prerequisites to building the front end

[Section titled “Prerequisites to building the front end”](#prerequisites-to-building-the-front-end)

To compile the front-end JavaScript and CSS files it’s expected that you have installed:

* [Node.js](https://nodejs.org/)
* [NPM](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

Pegasus is developed and tested on the latest LTS releases, which (at the time of this writing) are Node version 22 and npm 11. Later versions will likely work, but aren’t regularly-tested.

It’s recommended to use [`nvm`](https://github.com/nvm-sh/nvm) to manage different node/npm environments more easily. `nvm` is essentially `virtualenv` for Node.js/npm.

Alternatively, you can build and run your front end with Docker. However, this has been known to cause performance problems in some environments.

## Initial setup

[Section titled “Initial setup”](#initial-setup)

Once you’ve installed Node and NPM, you can install your front end dependencies by running:

```bash
npm install
```

or in Docker:

```bash
make npm-install
```

In your project’s root directory. This will install all the dependencies necessary to build the front end.

It will also generate a `package-lock.json` file. **It is recommended that you add the `package-lock.json` to source control for consistency across installations.**

## Building in Development

[Section titled “Building in Development”](#building-in-development)

The development set up is slightly different between Vite and Webpack. For details see these links:

* [Vite in Development](/front-end/vite/#vite-in-development)
* [Webpack in Development](/front-end/webpack/#development-with-webpack)

## Building for production

[Section titled “Building for production”](#building-for-production)

To build for production, run:

```bash
npm run build
```

or in Docker:

```bash
make npm-build
```

This will compress your files, remove logging statements, etc. In most [supported deployment set ups](/deployment/overview), this will be run automatically for you as part of your deployment.

## TypeScript and type checking

[Section titled “TypeScript and type checking”](#typescript-and-type-checking)

Since the 2022.6 release, Pegasus includes TypeScript as part of the front end code. You can write TypeScript or JavaScript code and it will be transpiled to work in a browser as part of the build pipeline.

The build pipeline does *not* explicitly do type checking. To do type checking you can run:

```bash
npm run type-check
```

Or in Docker:

```bash
make npm-type-check
```

Type checks will also automatically run on new pull requests if you have enabled Github Actions on your project.

# Troubleshooting

> Fix Docker cross-platform file watching issues with webpack polling configuration for Windows and other development environments.

## Changes are not being picked when running `make npm-watch` in a Docker container

[Section titled “Changes are not being picked when running make npm-watch in a Docker container”](#changes-are-not-being-picked-when-running-make-npm-watch-in-a-docker-container)

Some Docker configurations do not properly pick up file-system changes across operating systems. This can be a problem, e.g. when running on certain Windows environments. This causes changes made to not be automatically picked up.

This can be fixed by updating `webpack.config.js` to use polling by adding this:

```javascript
module.exports = {
   //...
   watchOptions: {
      poll: 1000,
   },
};
```

Alternatively, you can switch to installing/running NPM natively instead of in Docker. This is a good option if you are also getting poor performance, which can also be caused by cross-platform issues.

# Vite-Specific Instructions

> Configure Vite with django-vite for fast development server, Hot Module Replacement, and seamless Django template integration.

## Vite architecture overview

[Section titled “Vite architecture overview”](#vite-architecture-overview)

The Vite integration with Django is managed by [`django-vite`](https://github.com/MrBin99/django-vite). Big picture this works in two ways:

1. In *development* front end assets are served directly from Vite’s server
2. In *production* front end assets are built and served through Django’s static files system.

This toggle is configured through the `"dev_mode"` setting in your default `DJANGO_VITE` config in `settings.py`. Out of the box, this setting is tied to the `settings.DEBUG` flag.

## Vite in Development

[Section titled “Vite in Development”](#vite-in-development)

Unlike Webpack, Vite does *not* use bundle files in development. Instead, your front end files are served by Vite’s development server (which is configured though `django-vite`).

This workflow makes gives you the benefit of added speed and fast page updates without reloading your browser, but it does mean that **your Vite server must be running at all times during development**.

To run your Vite server and serve your front end files you should run:

```bash
npm run dev
```

Or in Docker:

```bash
make npm-dev
```

This command will also automatically refresh your front end whenever any changes are made.

## Adding files to Django templates

[Section titled “Adding files to Django templates”](#adding-files-to-django-templates)

To add CSS / JS files to Django templates you can use the `vite_asset` template tag from django-vite:

```jinja
{% load django_vite %}
{% vite_asset '<path to your asset>' %}
```

If you are using React you also need to add the `vite_react_refresh` tag to get HMR working:

```jinja
{% load django_vite %}
{% vite_react_refresh %}
{% vite_asset '<path to your React asset>' %}
```

## Configuration

[Section titled “Configuration”](#configuration)

The [django-vite docs](https://github.com/MrBin99/django-vite) provide details about the vite configuration. Here is the relevant declaration from `settings.py`:

```python
DJANGO_VITE = {
    "default": {
        "dev_mode": env.bool("DJANGO_VITE_DEV_MODE", default=DEBUG),
        "manifest_path": BASE_DIR / "static" / ".vite" / "manifest.json",
    }
}
```

This should work without modification for most projects. If for some reason you want to change your vite server port or base path in `vite.config.ts` you will have to make corresponding changes to your `django-vite` settings as per their documentation.

## Production

[Section titled “Production”](#production)

In production, the above configuration should work out of the box. Production builds will disable `settings.DEBUG` via the environment variable, which will in turn disable vite’s dev mode.

Environment variables and settings.DEBUG

You should always override `settings.DEBUG` via an environment variable or `.env` file. This ensures that the value is set at the top of `settings.py`, which in turn overrides the `dev_mode` setting of `django-vite`. If instead you set `DEBUG = False` in `settings_production.py` this will not properly override the value, and django-vite will still use dev mode in your production app.

If you need more fine-grained control, or want to test a production build, you can also explicitly set the `DJANGO_VITE_DEV_MODE` environment variable to `false`.

You will also need to set up [Django’s static file serving](https://docs.saaspegasus.com/deployment/production-checklist/#check-your-static-file-setup). Again, if you’re using a supported Pegasus deployment mode, this should be already handled for you.

# Webpack-Specific Instructions

> Use Webpack for Django front-end builds with dev-watch mode, bundle compilation, and static file management for JavaScript and CSS assets.

## Development with Webpack

[Section titled “Development with Webpack”](#development-with-webpack)

Whenever you make modifications to the front-end files you will need to run the following command to rebuild the compiled JS bundles and CSS files:

```bash
npm run dev
```

You can also set it up to watch for changes by running:

```bash
npm run dev-watch
```

or in Docker:

```bash
make npm-watch
```

## Bundled Static Files and Source Control

[Section titled “Bundled Static Files and Source Control”](#bundled-static-files-and-source-control)

For ease of initial set up, the front-end bundle files can be optionally included with the Pegasus codebase. This allows you to get up and running with Pegasus without having to set up the Webpack build pipeline.

However, keeping these files in source control will typically result in a lot of unnecessary changes and merge conflicts. Instead, it is recommended that you add the compiled CSS and JavaScript bundle files to your `.gitignore` so they are no longer managed by source control, and have your developers build them locally using the steps above. **You can switch to this workflow by unchecking the “include static files” option in your project configuration.**

For production deployment, see the [production guidance](/deployment/production-checklist/#optimize-your-front-end) on this.

# How to connect a marketplace app to a Pegasus project

> Connect marketplace apps like Scriv to Pegasus projects via GitHub integration with proper configuration matching and commit synchronization.

Follow these steps to connect a marketplace app to a Pegasus project. We’ll do this for \[scriv], but the process should be the same for other apps built on Pegasus.

First, [follow the getting started guide](https://www.saaspegasus.com/store/product/scriv/get-started/) to clone the repository and set up your own fork.

Next, create new Pegasus project for your app from [the projects page](https://www.saaspegasus.com/projects/). **You should choose the same config choices as the marketplace app**, which you can find in the `pegasus-config.yaml` file in the repository root.

You can also refer to [this screenshot](/images/scriv-pegasus-config.png) for how the configuration should look as of September, 2024.

Next, connect your Pegasus project to your Github repository:

1. From the project page, select “Get Code”.
2. On the “Push to Github” tab, click “Add a repo”.
3. Set the owner and name to the fork you created above. This should be your existing fork of Scriv, not a new repository.
4. Click “Add Repo”.

You will be prompted to authenticate with Github. If you haven’t already, you should set that up according to [the Github guide](https://docs.saaspegasus.com/github/#connecting-your-account).

After connecting your Github, you will be prompted to enter a commit ID according to the last Pegasus commit in the repository. It will look something like this:

![Set Commit](/_astro/scriv-set-commit.DlLeMv0R_B4zY0.webp)

In the “Commit id” field, enter the commit ID of the most recent Pegasus update, which you can get from the table below:

| Codebase            | Commit ID                                  | Pegasus Version | Last Updated |
| ------------------- | ------------------------------------------ | --------------- | ------------ |
| Scriv               | `dbee5f634503f9d37b061c7a682e59db3bfece06` | 2025.4.1        | April, 2025  |
| Translation Creator | `673e3cf37ffeb3472c0eedf3a38e924ee7a3c0ab` | 2025.3          | March, 2025  |

Enter the commit ID and click “Set Commit ID”.

Now you should be able to click “Submit Pull Request” and your Pegasus project will sync with your marketplace codebase. Once this completes you should have a Github pull request with a small number of changes. You may need to resolve conflicts on this pull request (when in doubt, accept the `main` branch changes). Once you have resolved all conflicts, merge the pull request.

Your marketplace is now connected to your Pegasus project! You can change settings, upgrade, and submit pull requests from Pegasus and they will go to your marketplace app repo.

If you have any questions or issues with this process, [get in touch via the support channels](https://www.saaspegasus.com/support/).

# Working with Scriv

> Deploy and customize Scriv chat widget application with Fly.io integration, Docker configuration, and npm package publishing options.

## Deployment

[Section titled “Deployment”](#deployment)

Out of the box, Scriv is set up to deploy to fly.io via the standard SaaS Pegasus setup. If you’d like to deploy to fly, you will first need to make the following changes to your `fly.toml` file:

* (Recommended) Choose a new `app` name that’s unique to your project.
* In the `http_service.checks.headers`, change the `Host` variable to the domain you are deploying to.

After that, you should be able to follow the [standard Pegasus deployment instructions](/deployment/fly/).

### Deploying to a different platform

[Section titled “Deploying to a different platform”](#deploying-to-a-different-platform)

If you’d rather deploy Scriv somewhere else, you can use the `Dockerfile.web` in the repo as a foundation for any other docker-based platform. If you want to use a Pegasus-supported platform you can also generate the necessary files by creating a new project on Pegasus and copying them into your Scriv repository, or by [connecting Scriv to a Pegasus project](/marketplace/connecting) and then changing the deployment platform in your project settings. The latter option is only recommended if you plan on making other configuration changes, since the process of connecting a project is more work than just copying the files across.

## The Chat Widget

[Section titled “The Chat Widget”](#the-chat-widget)

The chat widget is a component that allows you to add a chat interface to your website. You can find the source code and more information in the [`components/scriv-chat`](https://github.com/saaspegasus/scriv/tree/main/components/scriv-chat) directory of the repository.

### Publishing your own Chat Widget Package

[Section titled “Publishing your own Chat Widget Package”](#publishing-your-own-chat-widget-package)

To publish your own version of the chat widget, you can do the following:

1. Customize the chat widget by modifying `components/scriv-chat/src/components/scriv-chat/scriv-chat.tsx`.

   1. Edit the `SCRIV` variable to match your own site.
   2. Modify the “Powered by” section at the bottom.

2. Replace `scriv-chat` with your own package name in `components/scriv-chat/package.json`, and modify any other relevant variables.

3. Publish the package, by getting set up on [npmjs.com](https://www.npmjs.com/) and then running `npm publish`.

## Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

### Knowledge sources not indexing

[Section titled “Knowledge sources not indexing”](#knowledge-sources-not-indexing)

Knowledge sources are indexed by a background task that runs via [Celery](/celery). If your knowledge sources aren’t indexing, the most likely cause is that celery is not running correctly.

The first thing to check is whether Celery is running. If you’re using Docker, Celery should run automatically with the correct parameters as part of the docker compose setup.

If you’re not using Docker, you will have to run it manully, and specify the additional “background” queue argument:

```plaintext
celery -A scriv worker -l INFO --pool=solo  -Q celery,background
```

If Celery is running properly, you should see logs whenever you add / rebuild a knowledge source. If the knowledge sources still aren’t being added, check the logs for any errors.

You can also manually trigger a knowledge source index by running the following command:

```plaintext
./manage.py build_index <index_id>
```

The `index_id` argument can be found in the Django admin, or in the URL when viewing the knowledge source.

# Working with Python Packages (pip-tools)

> Manage Python dependencies with pip-tools using requirements.in files, pip-compile commands, and Docker container rebuilds for package management.

This feature is deprecated

Using pip-tools has been deprecated in favor of uv. See [the uv docs](/python/uv) and [migration guide](/cookbooks/#migrating-from-pip-tools-to-uv).

Legacy Pegasus projects use [pip tools](https://github.com/jazzband/pip-tools) to manage Python dependencies. This allows for more explicit dependency management than a standard `requirements.txt` file.

### Requirements Files

[Section titled “Requirements Files”](#requirements-files)

Pegasus has multiple requirements files, which live in the `requirements/` folder. For each set of requirements there are two files, one ending in `.in` and the other ending in `.txt`.

The files ending in `requirements.in` have the first-class packages your app depends on. They do not have versions in them, though you can add version numbers if you want to. **These are the files that you should edit when adding/removing packages**.

The files ending in `requirements.txt` have the full list of packages your app depends on, including the dependencies of your dependencies (recursively). This file is automatically generated from the `.in` counterpart, and **should typically not be edited by hand**.

The `requirements.in`/`.txt` files are the main requirements for your application, `dev-requirements.in`/`.txt` files are requirements for development-only, and `prod-requirements.in`/`.txt` are for production-only.

### Working with requirements

[Section titled “Working with requirements”](#working-with-requirements)

To modify the requirements files, you first need to install `pip-tools`. It is included as a dependency in the `dev-requirements.txt` file so if you’ve followed the local setup steps it should already be installed.

Then follow the instructions below, depending on what you want to do:

#### Adding or removing a package

[Section titled “Adding or removing a package”](#adding-or-removing-a-package)

To add a package, add the package name to `requirements/requirements.in`. To remove a package, remove it from `requirements/requirements.in`.

After finishing your edits, rebuild your `requirements.txt` file by running:

```bash
# native version
pip-compile requirements/requirements.in


# docker version
make pip-compile
```

After running this you should see the package and its dependencies added to the `requirements.txt` file.

From there you can install the new dependencies, as [described below](#installing-packages).

#### Upgrading a package

[Section titled “Upgrading a package”](#upgrading-a-package)

To upgrade a package, you can run the following command. In this example we are upgrading `django`:

```bash
# native version
pip-compile --upgrade-package django requirements/requirements.in


# docker version
make pip-complie ARGS="--upgrade-package django"
```

To upgrade *all* packages, you can run:

```bash
# native version
pip-compile --upgrade requirements/requirements.in


# docker version
make pip-compile ARGS="--upgrade"
```

From there you can install the new dependencies, as [described below](#installing-packages).

#### Installing Packages

[Section titled “Installing Packages”](#installing-packages)

If you’re running Python natively, you can install your packages with the following command. Run this after activating your virtual environment:

```bash
pip install -r requirements/requirements.txt
```

In Docker your Python packages are installed at container *build* time. This means that any time you want to change your installed new packages, you have to rebuild your container.

You can do this by running

```bash
docker compose build
```

Confusingly, running `pip install` or `docker compose exec web pip install` does *not* work.

#### The `make requirements` shortcut for Docker

[Section titled “The make requirements shortcut for Docker”](#the-make-requirements-shortcut-for-docker)

Pegasus ships with a convenience target for rebuilding requirements with Docker. Any time you make changes to a `requirements.in` file you can run it with:

```bash
make requirements
```

Behind the scenes this will:

1. Rebuild all your `-requirements.txt` files from your `-requirements.in` files with `uv`.
2. Rebuild your containers (installing the new packages).
3. Restart your containers.

For more information, see the [docker documentation](/docker/#updating-python-packages).

# Python Environment Setup

> Set up Pegasus development environments using Docker, uv package manager, virtual environments, or IDE integration for Django projects.

## Choosing between Docker and native Python

[Section titled “Choosing between Docker and native Python”](#choosing-between-docker-and-native-python)

You can either run Python in a Docker container or natively on your development machine, through various different options.

Docker provides a more consistent way to package your application, however it is slower, takes more resources, and can be more complex to integrate with IDEs, debuggers, and other development tools.

Native Python can be slightly more difficult to set up (primarily on Windows), but once it is working it is typically easier to work with.

Using Docker or uv is recommended. You can try either of these and switch if you run into problems.

## Using Docker

[Section titled “Using Docker”](#using-docker)

See the [Docker documentation](/docker) to set up your development environment with Docker.

Docker environments support using uv or pip-tools as a package manager. Uv is recommended, and pip-tools is only for legacy projects. For help adding and removing Python packages after setup, see the documentation for [uv](/python/uv) or [pip-tools (deprecated)](/python/packages).

## Using uv

[Section titled “Using uv”](#using-uv)

It’s recommended that new projects not using docker use [uv](https://docs.astral.sh/uv/) to manage their Python environments. It is faster and simpler to use than other alternatives, and can even install and set up Python for you.

***Note: uv support is only available from Pegasus version 2024.12 onwards. To use uv you must select it under the “Python package manager” setting in your project configuration.***

To set up Python with uv, first [install uv](https://docs.astral.sh/uv/getting-started/installation/). *Pegasus requires uv version 0.5 or higher.*

On Linux / Mac:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

On Windows:

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

After installing `uv`, go into your project directory and run:

```bash
uv sync
```

This should:

1. Install the right version of Python (if necessary).
2. Create a new virtual environment in a `.venv` folder inside your project.
3. Install all the project dependencies.

To see if it worked, run:

```bash
uv run manage.py shell
```

If you get a Python shell that looks something like this, it worked!

```plaintext
$ uv run manage.py shell
Python 3.12.6 (main, Sep  9 2024, 22:11:19) [Clang 18.1.8 ] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>
```

You should be able to use `uv run` to run any Python command on your project, or you can run:

```bash
source .venv/bin/activate
```

in your project root to use `python` and other commands normally.

## Using Native / System Python (with Virtual Environments and pip-tools)

[Section titled “Using Native / System Python (with Virtual Environments and pip-tools)”](#using-native--system-python-with-virtual-environments-and-pip-tools)

The following are other options---which are typically recommended for developers who are already familiar with Python and one of these choices.

Unlike `docker` and `uv`, most of these require having Python installed on your machine, so if you haven’t already, first install Python version 3.12+:

* On Mac and windows you can [download Python 3.12 installers from here](https://www.python.org/downloads/).
* On Ubuntu it’s recommended to [use the deadsnakes repo](https://www.debugpoint.com/install-python-3-12-ubuntu/).

*Note: running on older Python versions may work, but 3.12 is what’s tested and supported.*

After installing Python, set up your virtual environment through one of the following methods:

#### Using your IDE

[Section titled “Using your IDE”](#using-your-ide)

Many IDEs will manage your environments for you. This is a great and simple option that you won’t have to fiddle with. Check your specific IDE’s docs for guidance on how to do this.

* [Virtual environments in VS Code](https://code.visualstudio.com/docs/python/environments)
* [Virtual environments in PyCharm](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html)

**Be sure to choose Python 3.12 when setting up your virtual environment.** If you don’t see 3.12 as an option, you may need to install it first.

#### Using venv

[Section titled “Using venv”](#using-venv)

The easiest way to set up a virtual environment manually is to use Python’s built in [`venv` tool](https://docs.python.org/3/library/venv.html#module-venv):

```bash
python3.12 -m venv /path/to/environment
```

In the command below, you should replace `python3` with the Python version you are using, and `/path/to/environment/` with the location on your system where you want to store the environment. This location can be somewhere in your project directory (`.venv` and `venv` are common choices) or anywhere else on your system. `/home/<user>/.virtualenvs/<project>` is a common choice that works well with `virtualenvwrapper` (see below).

To activate/use the environment run:

```bash
source /path/to/environment/bin/activate
```

**You will need to activate this environment every time you work on your project.**

#### Using virtualenv

[Section titled “Using virtualenv”](#using-virtualenv)

[virtualenv](https://virtualenv.pypa.io/en/stable/) is an alternate option to `venv`. On later versions of Python there’s no real reason to use it, but if you’re familiar with it you can keep using it without any issues. First make sure [it’s installed](https://virtualenv.pypa.io/en/stable/installation.html) and then run the following command:

```bash
virtualenv -p python3.12 /path/to/environment
```

Like above, you should replace the `python3.12` variable with the version you want to use, and the `/path/to/environment` with wherever you want to set up the environment.

Like with `venv`, to activate the environment run:

```bash
source /path/to/environment/bin/activate
```

And, like `venv`, **you will need to activate this environment every time you work on your project.**

#### Using virtualenvwrapper

[Section titled “Using virtualenvwrapper”](#using-virtualenvwrapper)

[Virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) is an optional convenience tool that helps manage virtual environments. You can use it with either `venv` or `virtualenv` above.

If you choose to use `virtualenvwrapper` you can use the following command to create your environment. This can be run from anywhere since `virtualenvwrapper` manages the location of your envs for you (usually in `/home/<user>/.virtualenvs/`).

```bash
mkvirtualenv -p python3.12 {{ project_name }}
```

Then to activate the environment you use:

```bash
workon {{ project_name }}
```

Note: You can use `virtualenvwrapper` no matter how you created the environment. It provides a nice set of helper tools, but can be a bit finicky to set up.