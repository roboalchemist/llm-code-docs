# Remote Endpoint (Python)

Connect your CopilotKit application to a remote backend endpoint, allowing integration with Python-based services or other non-Node.js backends.

## [Stand up a FastAPI server using the CopilotKit Python SDK](https://docs.copilotkit.ai/guides/backend-actions/remote-backend-endpoint\#stand-up-a-fastapi-server-using-the-copilotkit-python-sdk)

### [Install CopilotKit Python SDK and Dependencies](https://docs.copilotkit.ai/guides/backend-actions/remote-backend-endpoint\#install-copilotkit-python-sdk-and-dependencies)

To integrate a Python backend with your CopilotKit application, set up your project and install the necessary dependencies by choosing your dependency management solution below.

Poetrypipconda

#### [Initialize a New Poetry Project](https://docs.copilotkit.ai/guides/backend-actions/remote-backend-endpoint\#initialize-a-new-poetry-project)

Run the following command to create and initialize a new Poetry project:

```
poetry new My-CopilotKit-Remote-Endpoint
```

Follow the prompts to set up your `pyproject.toml`.

#### [Install Dependencies](https://docs.copilotkit.ai/guides/backend-actions/remote-backend-endpoint\#install-dependencies)

After initializing the project, install the dependencies:

```
poetry add copilotkit fastapi uvicorn