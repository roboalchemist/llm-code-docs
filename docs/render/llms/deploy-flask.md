# Source: https://render.com/docs/deploy-flask.md

# Deploy a Flask App on Render

You can deploy a [Flask](https://github.com/pallets/flask) Python app on Render in just a few clicks.

This quickstart uses a simple example app. You're welcome to use your own Flask app instead.

1. Fork [render-examples/flask-hello-world](https://github.com/render-examples/flask-hello-world) on GitHub.

   Here's the `app.py` file from that repo, which is borrowed from the [official Flask docs](https://flask.palletsprojects.com/quickstart/#a-minimal-application):

   ```python
   from flask import Flask
   app = Flask(__name__)

   @app.route('/')
   def hello_world():
       return 'Hello, World!'
   ```

> A demo instance of this app is hosted at [flask.onrender.com](https://flask.onrender.com). It uses [Gunicorn](https://gunicorn.org) to serve the app in a production setting.

2. In the [Render Dashboard](https://dashboard.render.com), click *New > Web Service* and connect your new repo.
3. Provide the following values during creation:

| Setting | Value |
| --- | --- |
| *Language* | `Python 3` |
| *Build Command* | `pip install -r requirements.txt` |
| *Start Command* | `gunicorn app:app` (*Using your own app?* Instead provide whatever command Render should use to start it.) |

That's it! Your web service will be live at its `onrender.com` URL as soon as the build finishes.

Going forward, every push to your linked branch automatically builds and deploys your app. If a build fails, Render cancels the deploy, and your app's existing version continues running until the next successful deploy. [Learn more about deploys.](/deploys)

If you need to use a specific version of Python for your app, see [Setting Your Python Version](python-version).