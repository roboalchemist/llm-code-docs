# Source: https://ngrok.com/docs/using-ngrok-with/flask.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Using ngrok with Flask

> Learn how to use ngrok with Flask development servers to share your local application with others using the ngrok agent or Python SDK.

This guide shows you how to use ngrok with Flask development servers to share your local application with others.
You can use either the ngrok agent or the Python SDK to expose your Flask app.

## What you'll need

* Python and Flask installed.
* An [ngrok account](https://dashboard.ngrok.com/signup).
* Your [ngrok authtoken](https://dashboard.ngrok.com/get-started/your-authtoken).

## Option 1. Use the ngrok agent

To share a local Flask development server with someone else, run:

```bash  theme={null}
ngrok http 5000
```

You may need to update your `SERVER_NAME` and `APPLICATION_ROOT` in your Flask app configuration to the values provided by ngrok.
See the Flask configuration docs for more information.

<Note>
  For users on the latest MacOS, there is an issue where the default port 5000 (and 7000) is used by Apple AirPlay Receiver.
  You can use a different port for your Flask app or disable the Apple AirPlay receiver by disabling it in **System Settings > General > AirDrop & Handoff > AirPlay Receiver**.
</Note>

## Option 2. Use the Python SDK

You can use the [ngrok Python SDK](https://github.com/ngrok/ngrok-python) to start an endpoint to the Flask dev server via Python code, or using the [ngrok ASGI runner](https://github.com/ngrok/ngrok-python#asgi-runner---tunnels-to-uvicorn-gunicorn-django-and-more-with-no-code) with an ASGI wrapper.

## Further resources

* [ngrok SDK on PyPI](https://pypi.org/project/ngrok/)
* [ngrok SDK on GitHub](https://github.com/ngrok/ngrok-python)
* [ngrok Python SDK docs](https://ngrok.github.io/ngrok-python/)


Built with [Mintlify](https://mintlify.com).