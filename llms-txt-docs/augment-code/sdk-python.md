# Source: https://docs.augmentcode.com/cli/sdk-python.md

# Python SDK

> Build custom integrations and agents using the Auggie Python SDK.

## About

The Auggie Python SDK provides a programmatic interface to Auggie for building custom integrations and agents in Python applications.

## Installation

```sh  theme={null}
pip install auggie-sdk
```

## Usage

### Basic Initialization

```python  theme={null}
from auggie_sdk import Auggie

# Simple initialization
agent = Auggie(model="sonnet4.5")

# Run a task
result = agent.run("What is 2 + 2?", return_type=int)
print(result)  # 4
```

### Full Configuration

```python  theme={null}
from auggie_sdk import Auggie
from auggie_sdk.acp import AgentEventListener

# Optional: Create a custom event listener
class MyListener(AgentEventListener):
    def on_agent_message_chunk(self, text: str):
        print(text, end="", flush=True)

agent = Auggie(
    # Working directory for the agent (default: current directory)
    workspace_root="/path/to/workspace",

    # Model to use: "haiku4.5" | "sonnet4.5" | "sonnet4" | "gpt5"
    model="sonnet4.5",

    # Event listener for real-time updates (optional)
    listener=MyListener(),

    # Allow codebase indexing (default: True)
    allow_indexing=True,

    # Default timeout in seconds (default: 300)
    timeout=600,

    # API key for authentication (optional, sets AUGMENT_API_TOKEN)
    api_key="your-api-key",

    # API URL (optional, sets AUGMENT_API_URL)
    api_url="https://api.augmentcode.com",

    # Rule file paths (optional)
    rules=["/path/to/rules.md"]
)

# Use the agent
result = agent.run("Your question here", return_type=str)
print(result)
```

## Output Modes

The Python SDK supports multiple output modes to fit different use cases:

### Typed Returns

Specify the exact type you expect, and the SDK ensures the agent returns data in that format:

```python  theme={null}
from auggie_sdk import Auggie

agent = Auggie()

# Get an integer
result = agent.run("What is 15 + 27?", return_type=int)
print(result)  # 42

# Get a dictionary
weather = agent.run(
    "Get weather info for Tokyo",
    return_type=dict
)

# Get a list
files = agent.run(
    "List all Python files",
    return_type=list
)
```

### Automatic Type Inference

When no `return_type` is specified, the agent automatically infers the best type:

```python  theme={null}
result, inferred_type = agent.run("What is 15 + 27?")
print(f"Result: {result} (type: {inferred_type.__name__})")
# Result: 42 (type: int)
```

### Structured Data with Dataclasses

Return complex structured data using Python dataclasses:

```python  theme={null}
from dataclasses import dataclass
from typing import List

@dataclass
class Task:
    id: int
    description: str
    is_done: bool

# Get a single object
task = agent.run(
    "Create a sample task for 'Buy groceries'",
    return_type=Task
)

# Get a list of objects
tasks = agent.run(
    "Create 3 sample tasks for a weekend to-do list",
    return_type=List[Task]
)
```

### Streaming Mode

Listen to real-time updates using an event listener:

```python  theme={null}
from auggie_sdk import Auggie
from auggie_sdk.acp import AgentEventListener

class MyListener(AgentEventListener):
    def on_agent_message_chunk(self, text: str):
        """Called when agent sends response chunks (streaming)."""
        print(text, end="", flush=True)

    def on_tool_call(self, tool_call_id, title, kind=None, status=None):
        """Called when agent makes a tool call."""
        print(f"\n🔧 Using tool: {title}")

agent = Auggie(listener=MyListener())
result = agent.run("Your question here")
```

**Supported return types:** `int`, `float`, `str`, `bool`, `list`, `dict`, `List[T]`, `Dict[K, V]`, `dataclasses`, `Enum`

## Custom Functions

The Python SDK supports **custom function calling**, allowing you to provide Python functions that the agent can intelligently call during execution. This enables the agent to interact with external systems, perform calculations, fetch data, and more.

### Creating Custom Functions

Define Python functions with type hints and docstrings. The agent will automatically understand how to use them:

```python  theme={null}
from auggie_sdk import Auggie
import datetime


def get_current_weather(location: str, unit: str = "celsius") -> dict:
    """
    Gets the weather for a given location.

    Args:
        location: The city and state, e.g. San Francisco, CA
        unit: Temperature unit ('celsius' or 'fahrenheit')
    """
    # In a real app, you'd call a weather API here
    return {"temp": 72, "unit": unit, "forecast": "sunny"}


def get_time() -> str:
    """Returns the current time."""
    return datetime.datetime.now().strftime("%H:%M")


agent = Auggie()

# The agent will call the appropriate function(s) to answer the question
response = agent.run(
    "What's the weather like in NYC right now, and what time is it there?",
    functions=[get_current_weather, get_time],
)
print(response)
```

### Function Requirements

For functions to work properly with the agent:

1. **Type Hints Required**: All parameters must have type annotations
2. **Docstrings Required**: Function must have a docstring with:
   * Function description (first paragraph)
   * Parameter descriptions in the `Args:` section
3. **JSON-Serializable**: Arguments and return values must be JSON-serializable
4. **Keyword Arguments**: Functions must accept keyword arguments

### Example with Multiple Functions

```python  theme={null}
from auggie_sdk import Auggie


def add_numbers(a: int, b: int) -> int:
    """Add two numbers together.

    Args:
        a: First number
        b: Second number
    """
    return a + b


def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers together.

    Args:
        a: First number
        b: Second number
    """
    return a * b


agent = Auggie()

result = agent.run(
    "What is (15 + 27) multiplied by 3?",
    return_type=int,
    functions=[add_numbers, multiply_numbers],
)
print(result)  # 126
```

### How It Works

1. Function schemas are automatically generated from type hints and docstrings
2. The agent receives the instruction and available functions
3. The agent intelligently decides when to call functions
4. The SDK executes the functions and sends results back to the agent
5. The agent continues processing and can call more functions if needed
6. Final response is returned according to `return_type`

<Note>
  **Function Calling Limits**: Function calling is limited to 5 rounds to prevent infinite loops.
</Note>

## See Also

* [Python SDK on PyPI](https://pypi.org/project/auggie-sdk)
* [TypeScript SDK](/cli/sdk-typescript)
* [ACP Clients](/cli/acp/clients)
