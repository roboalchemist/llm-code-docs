# Source: https://docs.upsun.com/languages/python.md

# Python


p:last-child]:mb-0 [&>h3]:mt-0 rounded-lg" >

### Note
You can now use composable image (BETA) to install runtimes and tools in your application container. To find out more, see the [dedicated documentation page](https://docs.upsun.com/create-apps/app-reference/composable-image.md).

Python is a general purpose scripting language often used in web development.
You can deploy Python apps on Upsun using a server or a project such as [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/).

## Supported versions

You can select the major and minor version.

Patch versions are applied periodically for bug fixes and the like. When you deploy your app, you always get the latest available patches.

   - 3.13

   - 3.12

   - 3.11

   - 3.10

   - 3.9

   - 3.8

### Specify the language

To use Python, specify ``python`` as your [app’s type](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#types):

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  <APP_NAME>:
    type: 'python:<VERSION_NUMBER>'
```

For example:

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'python:3.13'
```

### Deprecated versions

The following versions are [deprecated](https://docs.upsun.com/glossary.md#deprecated-versions).
They're available, but they don't receive security updates from upstream and aren't guaranteed to work.
They'll be removed in the future – consider migrating to a [supported version](#supported-versions).

   - 3.7

   - 3.6

   - 3.5

   - 2.7*

\* This version doesn't receive any updates at all.
You are strongly recommended to upgrade to a supported version.

## Usage example

### Run your own server

You can define any server to handle requests.
Once you have it configured, add the following configuration to get it running on Upsun:

1.  Specify one of the [supported versions](#supported-versions):

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'python:3.13'
```
2.  Install the requirements for your app.

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'python:3.13'
    dependencies:
      python3:
        pipenv: "2024.4.1"
    hooks:
      build: |
        set -eu
        pipenv install --system --deploy
```
3.  Define the command to start your web server:

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'python:3.13'
    web:
      # Start your app with the configuration you define
      # You can replace the file location with your location
      commands:
        start: python server.py
```
You can choose from many web servers such as Daphne, Gunicorn, Hypercorn, and Uvicorn.
See more about [running Python web servers](https://docs.upsun.com/languages/python/server.md).

### Use uWSGI

You can also use [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) to manage your server.
Follow these steps to get your server started.

1.  Specify one of the [supported versions](#supported-versions):

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'python:3.13'
```
2.  Define the conditions for your web server:

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'python:3.13'
    web:
      upstream:
        # Send requests to the app server through a unix socket
        # Its location is defined in the SOCKET environment variable
        socket_family: "unix"

      # Start your app with the configuration you define
      # You can replace the file location with your location
      commands:
        start: "uwsgi --ini conf/uwsgi.ini"

      locations:
        # The folder from which to serve static assets
        "/":
          root: "public"
          passthru: true
          expires: 1h
```
3.  Create configuration for uWSGI such as the following:

    ```ini  {location="config/uwsgi.ini"}
    [uwsgi]
    # Unix socket to use to talk with the web server
    # Uses the variable defined in the configuration in step 2
    socket = $(SOCKET)
    protocol = http

    # the entry point to your app
    wsgi-file = app.py
    ```

    Replace `app.py` with whatever your file is.

4.  Install the requirements for your app.

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'python:3.13'
    dependencies:
      python3:
        pipenv: "2024.4.1"
    hooks:
      build: |
        set -eu
        pipenv install --system --deploy
```
5.  Define the entry point in your app:

    ```python
    # You can name the function differently and pass the new name as a flag
    # start: "uwsgi --ini conf/uwsgi.ini --callable <NAME>"
    def application(env, start_response):

        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b"Hello world from Upsun"]
    ```

## Package management

Your app container comes with pip pre-installed.
For more about managing packages with pip, Pipenv, and Poetry,
see how to [manage dependencies](https://docs.upsun.com/languages/python/dependencies.md).

To add global dependencies (packages available as commands),
add them to the `dependencies` in your [app configuration](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#dependencies):

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'python:3.13'
    dependencies:
      python3:
        <PACKAGE_NAME>: <PACKAGE_VERSION>
```
For example, to use `pipenv` to manage requirements and a virtual environment, add the following:

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'python:3.13'
    dependencies:
      python3:
        pipenv: "2024.4.1"
    hooks:
      build: |
        set -eu
        pipenv install --system --deploy
```
## Connect to services

The following examples show how to access various [services](https://docs.upsun.com../../add-services.md) with Python.
For more information on configuring a given service, see the page for that service.

You can access service credentials to connect to [managed services](https://docs.upsun.com/add-services/) from environment variables present in the application container.
Consult each of the individual service documentation to see how to retrieve and surface credentials into your application.

- [Chroma](https://docs.upsun.com/add-services/chroma.md#3-use-the-relationship-in-your-application)

- [ClickHouse](https://docs.upsun.com/add-services/clickhouse.md#usage-example)

- [Elasticsearch](https://docs.upsun.com/add-services/elasticsearch.md#use-in-app)

- [Edgee (Edge Analytics)](https://docs.upsun.com/add-services/edgee.md#setup-edgee)

- [Gotenberg](https://docs.upsun.com/add-services/gotenberg.md#usage-example)

- [Headless Chrome](https://docs.upsun.com/add-services/headless-chrome.md#use-in-app)

- [InfluxDB](https://docs.upsun.com/add-services/influxdb.md#use-in-app)

- [Kafka](https://docs.upsun.com/add-services/kafka.md#use-in-app)

- [MariaDB/MySQL](https://docs.upsun.com/add-services/mysql.md#use-in-app)

- [Memcached](https://docs.upsun.com/add-services/memcached.md#use-in-app)

- [MongoDB](https://docs.upsun.com/add-services/mongodb.md#use-in-app)

- [Network Storage](https://docs.upsun.com/add-services/network-storage.md#usage-example)

- [OpenSearch](https://docs.upsun.com/add-services/opensearch.md#use-in-app)

- [PostgreSQL](https://docs.upsun.com/add-services/postgresql.md#use-in-app)

- [Qdrant](https://docs.upsun.com/add-services/qdrant.md#4-use-the-relationship-in-your-application)

- [RabbitMQ](https://docs.upsun.com/add-services/rabbitmq.md#use-in-app)

- [Redis](https://docs.upsun.com/add-services/redis.md#use-in-app)

- [Solr](https://docs.upsun.com/add-services/solr.md#use-in-app)

- [Valkey](https://docs.upsun.com/add-services/valkey.md#use-in-app)

- [Varnish](https://docs.upsun.com/add-services/varnish.md#usage-example)

- [Vault KMS](https://docs.upsun.com/add-services/vault.md#use-vault-kms)

## Sanitizing data

By default, data is inherited automatically by each child environment from its parent.
If you need to sanitize data in preview environments for compliance,
see how to [sanitize databases](https://docs.upsun.com../../development/sanitize-db.md).

## Frameworks

All major Python web frameworks can be deployed on Upsun.
See dedicated guides for deploying and working with them:

- [Django](https://docs.upsun.com/get-started/stacks/django.md)
- [Flask](https://docs.upsun.com/get-started/stacks/flask.md)

