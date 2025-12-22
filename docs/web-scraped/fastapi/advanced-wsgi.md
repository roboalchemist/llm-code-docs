# Source: https://fastapi.tiangolo.com/advanced/wsgi/

# Including WSGI - Flask, Django, others[&para;](#including-wsgi-flask-django-others)

You can mount WSGI applications as you saw with [Sub Applications - Mounts](../sub-applications/), [Behind a Proxy](../behind-a-proxy/).

For that, you can use the `WSGIMiddleware` and use it to wrap your WSGI application, for example, Flask, Django, etc.

## Using `WSGIMiddleware`[&para;](#using-wsgimiddleware)

You need to import `WSGIMiddleware`.

Then wrap the WSGI (e.g. Flask) app with the middleware.

And then mount that under a path.

Python 3.9+

## Check it[&para;](#check-it)

Now, every request under the path `/v1/` will be handled by the Flask application.

And the rest will be handled by **FastAPI**.

If you run it and go to [http://localhost:8000/v1/](http://localhost:8000/v1/) you will see the response from Flask:

`Hello, World from Flask!
`

And if you go to [http://localhost:8000/v2](http://localhost:8000/v2) you will see the response from FastAPI:

`{
    "message": "Hello World"
}
`