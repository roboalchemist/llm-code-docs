# Source: https://docs.upsun.com/languages/python/server.md

# Web servers


p:last-child]:mb-0 [&>h3]:mt-0 rounded-lg" >

### Note
You can now use composable image to install runtimes and tools in your application container. To find out more, see the [Composable image](https://docs.upsun.com/create-apps/app-reference/composable-image.md) topic.

The Python ecosystem offers a number of web servers that can be used to deploy to Upsun.
The following examples deploy a Django project named `myapp`.
They assume a `myapp/wsgi.py` or `myapp/asgi.py` file  with a callable `application`.
Adjust the examples to fit your framework and app.

## Gunicorn

[Gunicorn](https://docs.gunicorn.org/) is a Python WSGI HTTP Server for Unix
that operates on a pre-fork worker model.
The Gunicorn server is broadly compatible with various web frameworks, light on server resource usage, and fast.

To deploy with Gunicorn on Upsun ,
use one of the following examples to update your [app configuration](https://docs.upsun.com../../create-apps.md).

The examples vary based on both your package manager (Pip, Pipenv, or Poetry)
and whether your app listens on a TCP (default) or Unix (for running behind a proxy server) socket.
For more information on upstream sockets and protocols, see the [application reference](https://docs.upsun.com/create-apps/image-properties/web.md#upstream).

The snippets below assume that Gunicorn has been added as a dependency to your `requirements.txt`, `Pipfile.lock`, or `poetry.lock`.

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'python:3.14'
    web:
      commands:
        start: "gunicorn -w 4 -b localhost:$PORT app.wsgi:application"
      locations:
        "/":
          passthru: true
        "/static":
          root: "static"
          expires: 1h
          allow: true
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'python:3.14'
    web:
      upstream:
        socket_family: unix
      commands:
        start: "gunicorn -w 4 -b unix:$SOCKET app.wsgi:application"
      locations:
        "/":
          passthru: true
        "/static":
          root: "static"
          expires: 1h
          allow: true
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'python:3.14'
    web:
      commands:
        start: "pipenv run gunicorn -w 4 -b localhost:$PORT app.wsgi:application"
      locations:
        "/":
          passthru: true
        "/static":
          root: "static"
          expires: 1h
          allow: true
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'python:3.14'
    web:
      upstream:
        socket_family: unix
      commands:
        start: "pipenv run gunicorn -w 4 -b unix:$SOCKET app.wsgi:application"
      locations:
        "/":
          passthru: true
        "/static":
          root: "static"
          expires: 1h
          allow: true
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'python:3.14'
    web:
      commands:
        start: "poetry run gunicorn -w 4 -b localhost:$PORT app.wsgi:application"
      locations:
        "/":
          passthru: true
        "/static":
          root: "static"
          expires: 1h
          allow: true
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'python:3.14'
    web:
      upstream:
        socket_family: unix
      commands:
        start: "poetry run gunicorn -w 4 -b unix:$SOCKET app.wsgi:application"
      locations:
        "/":
          passthru: true
        "/static":
          root: "static"
          expires: 1h
          allow: true
```

### Gunicorn workers

These examples define four worker processes with `-w 4`.
For more details on what you can configure, see the [Gunicorn documentation](https://docs.gunicorn.org/en/stable/faq.md#worker-processes).

Workers can also be defined with a custom [worker class](https://docs.gunicorn.org/en/latest/settings.md#worker-class),
such as [Uvicorn](https://www.uvicorn.org/#running-with-gunicorn), [gevent](https://www.gevent.org/),
or [Tornado](https://www.tornadoweb.org/).

For example, to add a Uvicorn worker class to the pip example for Unix,
adjust the start command to the following:

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'python:3.14'
    web:
      upstream:
        socket_family: unix
      commands:
        start: "gunicorn -w 4 -k uvicorn.workers.UvicornWorker -b unix:$SOCKET app.wsgi:application"
```
## Daphne

[Daphne](https://github.com/django/daphne) is a HTTP, HTTP2 ,and WebSocket protocol server for ASGI and ASGI-HTTP,
developed to power Django Channels.

To deploy with Daphne on Upsun ,
use one of the following examples to update your [app configuration](https://docs.upsun.com../../create-apps.md).

The examples vary based on both your package manager (Pip, Pipenv, or Poetry)
and whether your app listens on a TCP (default) or Unix (for running behind a proxy server) socket.
For more information on upstream sockets and protocols, see the [application reference](https://docs.upsun.com/create-apps/image-properties/web.md#upstream).

The snippets below assume that Daphne has been added as a dependency to your `requirements.txt`, `Pipfile.lock`, or `poetry.lock`.

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'python:3.14'
    web:
      commands:
        start: "daphne -p $PORT app.asgi:application"
      locations:
        "/":
          passthru: true
        "/static":
          root: "static"
          expires: 1h
          allow: true
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'python:3.14'
    web:
      upstream:
        socket_family: unix
      commands:
        start: "daphne -u $SOCKET app.asgi:application"
      locations:
        "/":
          passthru: true
        "/static":
          root: "static"
          expires: 1h
          allow: true
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'python:3.14'
    web:
      commands:
        start: "pipenv run daphne -p $PORT app.asgi:application"
      locations:
        "/":
          passthru: true
        "/static":
          root: "static"
          expires: 1h
          allow: true
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'python:3.14'
    web:
      upstream:
        socket_family: unix
      commands:
        start: "pipenv run daphne -u $SOCKET app.asgi:application"
      locations:
        "/":
          passthru: true
        "/static":
          root: "static"
          expires: 1h
          allow: true
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'python:3.14'
    web:
      commands:
        start: "poetry run daphne -p $PORT app.asgi:application"
      locations:
        "/":
          passthru: true
        "/static":
          root: "static"
          expires: 1h
          allow: true
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'python:3.14'
    web:
      upstream:
        socket_family: unix
      commands:
        start: "poetry run -u $SOCKET app.asgi:application"
      locations:
        "/":
          passthru: true
        "/static":
          root: "static"
          expires: 1h
          allow: true
```

## Uvicorn

[Uvicorn](https://www.uvicorn.org/) is an ASGI web server implementation for Python.

To deploy with Uvicorn on Upsun ,
use one of the following examples to update your [app configuration](https://docs.upsun.com../../create-apps.md).

The examples vary based on both your package manager (Pip, Pipenv, or Poetry)
and whether your app listens on a TCP (default) or Unix (for running behind a proxy server) socket.
For more information on upstream sockets and protocols, see the [application reference](https://docs.upsun.com/create-apps/image-properties/web.md#upstream).

The snippets below assume that Uvicorn has been added as a dependency to your `requirements.txt`, `Pipfile.lock`, or `poetry.lock`.

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'python:3.14'
    web:
      commands:
        start: "uvicorn app.asgi:application --port $PORT --workers 4"
      locations:
        "/":
          passthru: true
        "/static":
          root: "static"
          expires: 1h
          allow: true
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'python:3.14'
    web:
      upstream:
        socket_family: unix
      commands:
        start: "uvicorn app.asgi:application --uds $SOCKET --workers 4"
      locations:
        "/":
          passthru: true
        "/static":
          root: "static"
          expires: 1h
          allow: true
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'python:3.14'
    web:
      commands:
        start: "pipenv run uvicorn app.asgi:application --port $PORT --workers 4"
      locations:
        "/":
          passthru: true
        "/static":
          root: "static"
          expires: 1h
          allow: true
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'python:3.14'
    web:
      upstream:
        socket_family: unix
      commands:
        start: "pipenv run uvicorn app.asgi:application --uds $SOCKET --workers 4"
      locations:
        "/":
          passthru: true
        "/static":
          root: "static"
          expires: 1h
          allow: true
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'python:3.14'
    web:
      commands:
        start: "poetry run uvicorn app.asgi:application --port $PORT --workers 4"
      locations:
          "/":
            passthru: true
          "/static":
            root: "static"
            expires: 1h
            allow: true
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'python:3.14'
    web:
      upstream:
        socket_family: unix
      commands:
        start: "poetry run uvicorn app.asgi:application --uds $SOCKET --workers 4"
      locations:
        "/":
          passthru: true
        "/static":
          root: "static"
          expires: 1h
          allow: true
```

### Uvicorn workers

These examples define four worker processes with `-w 4`.
For more recommendations on this and other settings, see the [Uvicorn documentation](https://www.uvicorn.org/settings/#timeouts).

Instead of the `-w` flag, you can also use the `WEB_CONCURRENCY` variable.
See how to [set variables](https://docs.upsun.com../../development/variables/set-variables.md).

## Hypercorn

[Hypercorn](https://hypercorn.readthedocs.io/) is an ASGI and WSGI web server inspired by Gunicorn.

To deploy with Hypercorn on Upsun ,
use one of the following examples to update your [app configuration](https://docs.upsun.com../../create-apps.md).

The examples vary based on both your package manager (Pip, Pipenv, or Poetry)
and whether your app listens on a TCP (default) or Unix (for running behind a proxy server) socket.
For more information on upstream sockets and protocols, see the [application reference](https://docs.upsun.com/create-apps/image-properties/web.md#upstream).

The snippets below assume that Hypercorn has been added as a dependency to your `requirements.txt`, `Pipfile.lock`, or `poetry.lock`.

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'python:3.14'
    web:
      commands:
        start: "hypercorn app.asgi:application -b localhost:$PORT -w 4"
      locations:
        "/":
          passthru: true
        "/static":
          root: "static"
          expires: 1h
          allow: true
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'python:3.14'
    web:
      upstream:
        socket_family: unix
      commands:
        start: "hypercorn app.asgi:application -b unix:$SOCKET -w 4"
      locations:
        "/":
          passthru: true
        "/static":
          root: "static"
          expires: 1h
          allow: true
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'python:3.14'
    web:
      commands:
        start: "pipenv run hypercorn app.asgi:application -b localhost:$PORT -w 4"
      locations:
        "/":
          passthru: true
        "/static":
          root: "static"
          expires: 1h
          allow: true
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'python:3.14'
    web:
      upstream:
        socket_family: unix
      commands:
        start: "pipenv run hypercorn app.asgi:application -b unix:$SOCKET -w 4"
      locations:
        "/":
          passthru: true
        "/static":
          root: "static"
          expires: 1h
          allow: true
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'python:3.14'
    web:
      commands:
        start: "poetry run hypercorn app.asgi:application -b localhost:$PORT -w 4"
      locations:
        "/":
          passthru: true
        "/static":
          root: "static"
          expires: 1h
          allow: true
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'python:3.14'
    web:
      upstream:
        socket_family: unix
      commands:
        start: "poetry run hypercorn app.asgi:application -b unix:$SOCKET -w 4"
      locations:
        "/":
          passthru: true
        "/static":
          root: "static"
          expires: 1h
          allow: true
```

### Hypercorn workers

These examples define four worker processes with `-w 4`.
For more details on what you can configure, see the [Hypercorn documentation](https://hypercorn.readthedocs.io/en/latest/how_to_guides/configuring.md).

Workers can also be defined with a custom [worker class](https://hypercorn.readthedocs.io/en/latest/how_to_guides/configuring.md#configuration-options),
such as Asyncio, Uvloop, or Trio.

For example, to add a Asyncio worker class to the pip example for Unix,
adjust the start command to the following:

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'python:3.14'
    web:
      upstream:
        socket_family: unix
      commands:
        start: "hypercorn app.asgi:application -b unix:$SOCKET -w 4 -k asyncio"
```

