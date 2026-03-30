# Source: https://ngrok.com/docs/using-ngrok-with/googleColab.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Using ngrok with Google Colab

> Learn how to use ngrok with Google Colab projects using the pyngrok library to expose local services.

This guide shows you how to use ngrok from a Google Colab notebook using the [pyngrok](https://pyngrok.readthedocs.io/en/latest/integrations.html#google-colaboratory) library.
It covers installing `pyngrok`, adding your ngrok authtoken, and starting a tunnel from Colab.

## What you'll need

* A Google Colab notebook.
* An [ngrok account](https://ngrok.com/signup).
* Your [ngrok authtoken](https://dashboard.ngrok.com/get-started/your-authtoken).

## 1. Install pyngrok in your notebook

In a Colab cell, install `pyngrok`:

```bash  theme={null}
!pip -q install pyngrok
```

## 2. Add your ngrok authtoken

In a new cell, add your ngrok authtoken:

```python  theme={null}
from pyngrok import ngrok

ngrok.set_auth_token("YOUR_AUTHTOKEN")
```

## 3. Start a tunnel

Start a tunnel to your local port (for example, `8080`):

```python  theme={null}
tunnel = ngrok.connect(8080)
print(tunnel.public_url)
```

Use the printed URL to access your service through ngrok.


Built with [Mintlify](https://mintlify.com).