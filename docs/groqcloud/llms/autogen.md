# Source: https://console.groq.com/docs/autogen

---
description: Learn how to use AutoGen with Groq to build fast, collaborative multi-agent AI applications with tool integration and code execution.
title: AutoGen + Groq: Multi-Agent AI Applications - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

## [AutoGen + Groq: Building Multi-Agent AI Applications](#autogen--groq-building-multiagent-ai-applications)

[AutoGen](https://microsoft.github.io/autogen/) developed by [Microsoft Research](https://www.microsoft.com/research/) is an open-source framework for building multi-agent AI applications. By powering the AutoGen agentic framework with Groq's fast inference speed, you can create sophisticated AI agents that work together to solve complex tasks fast with features including:

* **Multi-Agent Orchestration:** Create and manage multiple agents that can collaborate in realtime
* **Tool Integration:** Easily connect agents with external tools and APIs
* **Flexible Workflows:** Support both autonomous and human-in-the-loop conversation patterns
* **Code Generation & Execution:** Enable agents to write, review, and execute code safely

### [Python Quick Start (3 minutes to hello world)](#python-quick-start-3-minutes-to-hello-world)

#### [1\. Install the required packages:](#1-install-the-required-packages)

curl

```
pip install autogen-agentchat~=0.2 groq
```

#### [2\. Configure your Groq API key:](#2-configure-your-groq-api-key)

curl

```
export GROQ_API_KEY="your-groq-api-key"
```

#### [3\. Create your first multi-agent application with Groq:](#3-create-your-first-multiagent-application-with-groq)

In AutoGen, **agents** are autonomous entities that can engage in conversations and perform tasks. The example below shows how to create a simple two-agent system with `llama-3.3-70b-versatile` where`UserProxyAgent` initiates the conversation with a question and `AssistantAgent` responds:

Python

```
import os
from autogen import AssistantAgent, UserProxyAgent

# Configure
config_list = [{
    "model": "llama-3.3-70b-versatile",
    "api_key": os.environ.get("GROQ_API_KEY"),
    "api_type": "groq"
}]

# Create an AI assistant
assistant = AssistantAgent(
    name="groq_assistant",
    system_message="You are a helpful AI assistant.",
    llm_config={"config_list": config_list}
)

# Create a user proxy agent (no code execution in this example)
user_proxy = UserProxyAgent(
    name="user_proxy",
    code_execution_config=False
)

# Start a conversation between the agents
user_proxy.initiate_chat(
    assistant,
    message="What are the key benefits of using Groq for AI apps?"
)
```

### [Advanced Features](#advanced-features)

#### [Code Generation and Execution](#code-generation-and-execution)

You can enable secure code execution by configuring the `UserProxyAgent` that allows your agents to write and execute Python code in a controlled environment:

Python

```
from pathlib import Path
from autogen.coding import LocalCommandLineCodeExecutor

# Create a directory to store code files
work_dir = Path("coding")
work_dir.mkdir(exist_ok=True)
code_executor = LocalCommandLineCodeExecutor(work_dir=work_dir)

# Configure the UserProxyAgent with code execution
user_proxy = UserProxyAgent(
    name="user_proxy",
    code_execution_config={"executor": code_executor}
)
```

#### [Tool Integration](#tool-integration)

You can add tools for your agents to use by creating a function and registering it with the assistant. Here's an example of a weather forecast tool:

Python

```
from typing import Annotated

def get_current_weather(location, unit="fahrenheit"):
    """Get the weather for some location"""
    weather_data = {
        "berlin": {"temperature": "13"},
        "istanbul": {"temperature": "40"},
        "san francisco": {"temperature": "55"}
    }
    
    location_lower = location.lower()
    if location_lower in weather_data:
        return json.dumps({
            "location": location.title(),
            "temperature": weather_data[location_lower]["temperature"],
            "unit": unit
        })
    return json.dumps({"location": location, "temperature": "unknown"})

# Register the tool with the assistant
@assistant.register_for_llm(description="Weather forecast for cities.")
def weather_forecast(
    location: Annotated[str, "City name"],
    unit: Annotated[str, "Temperature unit (fahrenheit/celsius)"] = "fahrenheit"
) -> str:
    weather_details = get_current_weather(location=location, unit=unit)
    weather = json.loads(weather_details)
    return f"{weather['location']} will be {weather['temperature']} degrees {weather['unit']}"
```

#### [Complete Code Example](#complete-code-example)

Here is our quick start agent code example combined with code execution and tool use that you can play with:

Python

```
import os
import json
from pathlib import Path
from typing import Annotated
from autogen import AssistantAgent, UserProxyAgent
from autogen.coding import LocalCommandLineCodeExecutor

# Configure Groq
config_list = [{
    "model": "llama-3.3-70b-versatile",
    "api_key": os.environ.get("GROQ_API_KEY"),
    "api_type": "groq"
}]

# Create a directory to store code files from code executor
work_dir = Path("coding")
work_dir.mkdir(exist_ok=True)
code_executor = LocalCommandLineCodeExecutor(work_dir=work_dir)

# Define weather tool
def get_current_weather(location, unit="fahrenheit"):
    """Get the weather for some location"""
    weather_data = {
        "berlin": {"temperature": "13"},
        "istanbul": {"temperature": "40"},
        "san francisco": {"temperature": "55"}
    }
    
    location_lower = location.lower()
    if location_lower in weather_data:
        return json.dumps({
            "location": location.title(),
            "temperature": weather_data[location_lower]["temperature"],
            "unit": unit
        })
    return json.dumps({"location": location, "temperature": "unknown"})

# Create an AI assistant that uses the weather tool
assistant = AssistantAgent(
    name="groq_assistant",
    system_message="""You are a helpful AI assistant who can:
    - Use weather information tools
    - Write Python code for data visualization
    - Analyze and explain results""",
    llm_config={"config_list": config_list}
)

# Register weather tool with the assistant
@assistant.register_for_llm(description="Weather forecast for cities.")
def weather_forecast(
    location: Annotated[str, "City name"],
    unit: Annotated[str, "Temperature unit (fahrenheit/celsius)"] = "fahrenheit"
) -> str:
    weather_details = get_current_weather(location=location, unit=unit)
    weather = json.loads(weather_details)
    return f"{weather['location']} will be {weather['temperature']} degrees {weather['unit']}"

# Create a user proxy agent that only handles code execution
user_proxy = UserProxyAgent(
    name="user_proxy",
    code_execution_config={"executor": code_executor}
)

# Start the conversation
user_proxy.initiate_chat(
    assistant,
    message="""Let's do two things:
    1. Get the weather for Berlin, Istanbul, and San Francisco
    2. Write a Python script to create a bar chart comparing their temperatures"""
)
```

**Challenge:** Add to the above example and create a multi-agent [GroupChat](https://microsoft.github.io/autogen/0.2/docs/topics/groupchat/customized%5Fspeaker%5Fselection) workflow!

For more detailed documentation and resources on building agentic applications with Groq and AutoGen, see:

* [AutoGen Documentation](https://microsoft.github.io/autogen/0.2/docs/topics/non-openai-models/cloud-groq/)
* [AutoGroq](https://github.com/jgravelle/AutoGroq)