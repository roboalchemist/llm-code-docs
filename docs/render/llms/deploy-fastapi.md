# Source: https://render.com/docs/deploy-fastapi.md

# Deploy a FastAPI App

[FastAPI](https://fastapi.tiangolo.com/) is a modern, high-performance web framework for building APIs with Python 3.7+ based on standard Python type hints.

Here's how to deploy a basic FastAPI app on Render.

1. Create your own repository using the [render-examples/fastapi template](https://github.com/new?template_name=fastapi&template_owner=render-examples) on GitHub.
   - Alternatively, you can [clone the repo](https://github.com/render-examples/fastapi/) and push your clone to GitLab or Bitbucket.
2. Create a new *Web Service* on Render, and give Render permission to access your new repo.
3. Provide the following values during service creation:
   | Setting | Value |
   | ----------- | --------- |
   | *Language* | `Python 3` |
   | *Build Command* | `pip install -r requirements.txt` |
   | *Start Command* | `uvicorn main:app --host 0.0.0.0 --port $PORT` |

That's it! Your web service will be live at its `onrender.com` URL as soon as the deploy finishes.

See [Specifying a Python Version](python-version) if you need to customize the version of Python used for your app.