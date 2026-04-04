# or including support for crewai
poetry add copilotkit[crewai] fastapi uvicorn
```

**Dependencies:**

- **copilotkit**: The CopilotKit Python SDK.
- **fastapi**: A modern, fast (high-performance) web framework for building APIs with Python.
- **uvicorn**: A lightning-fast ASGI server for Python.

### [Set Up a FastAPI Server](https://docs.copilotkit.ai/guides/backend-actions/remote-backend-endpoint\#set-up-a-fastapi-server)

Create a new Python file `/my_copilotkit_remote_endpoint/server.py` and set up a FastAPI server:

/my\_copilotkit\_remote\_endpoint/server.py

```
from fastapi import FastAPI

app = FastAPI()
```

### [Define Your Backend Actions](https://docs.copilotkit.ai/guides/backend-actions/remote-backend-endpoint\#define-your-backend-actions)

Import the CopilotKit SDK and define your backend actions. For example:

/my\_copilotkit\_remote\_endpoint/server.py

```
from fastapi import FastAPI
from copilotkit.integrations.fastapi import add_fastapi_endpoint
from copilotkit import CopilotKitRemoteEndpoint, Action as CopilotAction

app = FastAPI()