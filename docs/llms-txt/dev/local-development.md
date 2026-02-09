# Source: https://dev.writer.com/agent-builder/local-development.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create and test agents locally

> Develop Agent Builder agents offline on your local machine with Writer Framework. Test agents locally before deploying to Writer Cloud.

This guide shows you how to create, edit, and test agents on your local machine before deploying them to the Writer Cloud. This uses [Writer Framework](https://github.com/writer/writer-framework) to work with Agent Builder agents locally with Python.

After completing these steps, you can develop Agent Builder agents offline locally and push them to the cloud when you're ready to share them with your team.

For more information about syncing agents between local and cloud and deploying to the Writer Cloud, see [Sync agents between local and cloud](/agent-builder/sync-agent).

## Prerequisites

Before getting started, ensure you have:

* Python 3.8 or later
* `pip` package manager
* A Writer API key. Learn how to [create and manage API keys](/api-reference/api-keys).

### Set your Writer API key as an environment variable

To pass your API key to Writer Framework, you need to set an environment variable called `WRITER_API_KEY`.

Create a new file called `.env` in the root of your project, for example, `my-agent/.env`, and add the following line:

```bash  theme={null}
export WRITER_API_KEY=[your_api_key]
```

Run the following command to activate the environment variable:

```bash  theme={null}
source .env
```

### Install the Writer Framework package

Install the Writer Framework package in a virtual environment. The Writer Framework package includes tools for creating, editing, and testing agents locally and deploying them to the Writer Cloud.

```bash  theme={null}
python3 -m venv venv  # Create a virtual environment
source venv/bin/activate  # Activate the virtual environment
pip install writer  # Install Writer Framework
```

<Tip>To make sure your local development environment matches the Writer Cloud environment, you should use the latest version of the Writer Framework package and check for updates regularly.</Tip>

## Create a new local project

Create a new Agent Builder project locally using the Writer Framework CLI:

```bash  theme={null}
writer create my-agent
cd my-agent
```

This creates a new project directory with the following structure:

```
my-agent/
├── .wf/                    # Project metadata and components. Don't edit this directory manually.
├── main.py                 # Main application code
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
└── static/                # Static assets
```

## Start developing

To run your agent in development mode with live reloading, run the following command:

```bash  theme={null}
writer edit . # Run in the current directory
```

This command displays the local URL in your terminal, which you can use to access your agent. The default URL is `http://127.0.0.1:4005` and you can specify a different port with the `--port` flag.

<Note>When you run the `writer edit` command, you might see the warning `Missing required environment variables for vault access`. This warning is expected because Vault is a secrets management feature that's only available in the Writer Cloud version of Agent Builder.</Note>

### Production mode

To run your agent in production-like mode, run the following command:

```bash  theme={null}
writer run .  # Run in the current directory
```

### Work with the included demo agent

When you create a new Agent Builder project, it automatically loads with a demo agent that demonstrates different components of an Agent Builder project. Learn how to navigate the demo agent in the [demo agent walkthrough](/agent-builder/demo-agent) or see how to [delete the demo agent in the Quickstart](/agent-builder/quickstart#clear-the-demo-agent).

### Control log output

You can enable verbose logging to see more detailed information about the agent's execution.

```bash  theme={null}
writer edit . --verbose
```

If you find the logs too verbose by default, you can control the log level using the `WRITER_LOG_LEVEL` environment variable:

```bash  theme={null}
# Show only errors
export WRITER_LOG_LEVEL=ERROR

# Reduce log output (only warnings and errors)
export WRITER_LOG_LEVEL=WARNING

# Show all logs (default)
export WRITER_LOG_LEVEL=INFO

# Show debug information (most verbose)
export WRITER_LOG_LEVEL=DEBUG
```

## Understand your project structure

Your local project contains several key components:

### Main application file (`main.py`)

The `main.py` file contains your agent's Python code and initial state:

```python  theme={null}
import writer as wf

# Initialize the agent's state
initial_state = wf.init_state({
    "user_count": 0,
    "messages": []
})

# Define your agent's logic here
def handle_user_message(state, payload):
    # Process user input
    user_message = payload.get("message", "")
    state["messages"].append(user_message)
    state["user_count"] += 1
    
    return {"response": f"Processed message: {user_message}"}
```

### Project metadata (`.wf/` directory)

The `.wf/` directory contains your agent's configuration, including:

* UI components and layout
* Blueprint definitions
* State schemas
* Component configurations

Do not manually edit the `.wf/` directory. Writer Framework automatically manages this directory.

### Static assets (`static/` directory)

Store your images, CSS files, and other static assets in the `static/` directory. The development server serves these files automatically, allowing you to reference them in your agent's UI.

## Follow the development workflow

### 1. Start local development

```bash  theme={null}
writer edit my-agent
```

The default URL to access your agent is `http://127.0.0.1:4005`. You can see the URL in the terminal after running the `writer edit` command.

### 2. Make changes

Edit your Python code, UI components, or blueprints either in code or in the local development web editor. The development server automatically detects changes and reloads your agent.

### 3. Test locally

Open your browser to the local development URL to test your agent's behavior.

### 4. Sync to cloud and deploy

When you're ready to make your agent live, sync it to the cloud and deploy it from there. See [Sync agents between local and cloud](/agent-builder/sync-agent) for complete instructions.

## Plan for cross-environment development

If you plan to do both local and cloud development or to deploy your agent to the Writer Cloud, review the following differences between the two environments.

### Python package compatibility

If you install Python packages locally that aren't listed in [Python libraries installed in Agent Builder](/agent-builder/python-libraries), your agent won't run in the cloud version of Agent Builder because those packages aren't available there.

### Local and cloud secrets support

The remote cloud version of Agent Builder uses [Vault](/agent-builder/secrets) to manage secrets. Vault is only available when you're working in the cloud editor. To access secrets and environment variables in local development, you should add them to your `.env` file.

<Warning>When you export your agent to a zip file, the exported file includes all files in your project including dot files. Do not include sensitive information in the exported file as it will be visible in the cloud editor. For example, you should delete your `.env` file when exporting your agent to a zip file and move your secrets to your cloud agent's Vault.</Warning>

If you plan to do both local and cloud development or to deploy your agent to the Writer Cloud, structure your code to check for both environment variables and Vault values. The code below shows how to get a secret from Vault if available, otherwise fall back to environment variables.

```python  theme={null}
import os

def get_secret(key, default=None):
    """Get a secret from Vault if available, otherwise from environment variables"""
    try:
        # Try to get from Vault first (cloud environment). The `vault` object is available in Python code blocks and in event handlers.
        return vault[key]
    except KeyError:
        # Fall back to environment variables (local development)
        return os.getenv(key, default)

# Usage example
api_key = get_secret("WRITER_API_KEY", "default_key")
database_url = get_secret("DATABASE_URL")
```

### Keep your local Writer Framework package up to date

When you sync your agent to the cloud, the cloud version of Agent Builder uses the latest version of the Writer Framework package. If you're using a different version of the Writer Framework package in your local project, you might encounter errors when you sync to the cloud. To avoid this, keep your local Writer Framework package up to date by running the following command:

```bash  theme={null}
pip install --upgrade writer
```

## Next steps

* Learn how to [sync your local agent with cloud agents](/agent-builder/sync-agent)
* Understand how to [deploy your agent](/agent-builder/sync-agent#deploy-your-agent) from the cloud
* Explore [custom Python code](/agent-builder/python-code) for advanced functionality

<feedback />
