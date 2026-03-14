# Source: https://docs.anyscale.com/platform/workspaces/workspaces-notebooks.md

# Notebooks on workspaces

[View Markdown](/platform/workspaces/workspaces-notebooks.md)

# Notebooks on workspaces

This page provides an overview of working with Jupyter notebooks on Anyscale workspaces.

important

Auto-termination for Anyscale clusters only tracks Ray activity. Your workspace might shut down if you're only running Python or system commands on your workspace.

## Notebooks in VS Code[​](#notebooks-in-vs-code "Direct link to Notebooks in VS Code")

When working with notebooks, Anyscale recommends using the VS Code notebook viewer because it has a richer ecosystem around Anyscale's [distributed debugger](/platform/workspaces/workspaces-debugging.md), search capabilities, VS Code extensions, and notebook specific features such as truncated cell outputs. Access VS Code from the Overview dropdown.

You can also use JupyterLab to work with notebooks if you prefer.

## Preserve state using SSH[​](#preserve-state-using-ssh "Direct link to Preserve state using SSH")

Use one of the SSH options, such as open in VS Code Desktop or Cursor, as that preserves the notebook state even if you refresh any web pages. If you use the in-browser VS Code option, the state, meaning variables and loaded modules, of your notebooks refreshes.

note

This behavior is an on-going issue with Microsoft and VS Code, so feel free to drop a reaction and comment so it gets prioritized: <https://github.com/microsoft/vscode-jupyter/issues/3998>.

## `autoreload`[​](#autoreload "Direct link to autoreload")

When working with notebooks, use the [`autoreload` module](https://ipython.org/ipython-doc/3/config/extensions/autoreload.html) to ensure that the notebook automatically updates all your imports and changes to those imports:

```
%load_ext autoreload
%autoreload 2
```

## Environment variables[​](#environment-variables "Direct link to Environment variables")

If you want to use environment variables in notebooks, be sure to have them in the **Dependencies** tab. For example:

```
# In the Dependencies tab.
ENV foo=bar
```

Create a .env file and use `load_dotenv(overwrite=True)` to load the updated environment variables into the notebook kernel.

```
from dotenv import load_dotenv
import os

# Load environment variables from .env file.
load_dotenv(overwrite=True)

# Access an environment variable.
api_key = os.getenv("API_KEY")
print(f"API Key: {api_key}")
```

## Changing imported modules[​](#changing-imported-modules "Direct link to Changing imported modules")

If you import any modules from local scripts and you make changes to the code behind those modules, then you need to restart Ray so that all the [worker nodes](https://docs.ray.io/en/latest/cluster/key-concepts.html#worker-node) have the updated modules.

```
ray.shutdown()
ray.init()
```

If you are running a [Ray Serve](https://docs.ray.io/en/latest/serve/index.html) app, you need to shutdown the running service as well and then restart Ray:

```
serve.shutdown()
ray.shutdown()
ray.init()
```

note

If the code for your functions and classes are directly inside the notebook, you can change them and use them right away. You don't need to restart Ray.

## Running multiple notebooks[​](#running-multiple-notebooks "Direct link to Running multiple notebooks")

If you have a Workspace with multiple notebooks, be sure to terminate each one before you start the next one. You can either `Restart` the kernel manually or run the following code cell at the end of your notebooks. This is to avoid potential issues with multiple Ray versions conflicting.

```
import IPython
IPython.get_ipython().kernel.do_shutdown(restart=True)
```
