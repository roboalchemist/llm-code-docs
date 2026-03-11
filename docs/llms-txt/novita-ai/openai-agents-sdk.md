# Source: https://novita.ai/docs/guides/openai-agents-sdk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAI Agents SDK

> Seamlessly integrate Novita AI with OpenAI Agents SDK for building multi-agent workflows.

The [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) is a lightweight yet powerful framework for building multi-agent workflows. And the SDK is compatible with any model providers that support the OpenAI Chat Completions API format.

This guide will walk you through how to use Novita LLM API with OpenAI Agents SDK.

## Get Started

1. Set up your Python environment and install the Agents SDK.

```bash  theme={"system"}
python -m venv env
source env/bin/activate
pip install openai-agents==0.0.7
```

2. Set up your Novita API key.

Go to [Key Management](https://novita.ai/settings/key-management?utm_source=getstarted) and create a new API key.

## Hello world example

<Warning>
  If running this, ensure you set the NOVITA\_API\_KEY and MODEL\_NAME environment variables.
</Warning>

```python  theme={"system"}
import os
from openai import AsyncOpenAI
from agents import (
    Agent,
    Runner,
    set_default_openai_api,
    set_default_openai_client,
    set_tracing_disabled,
)

BASE_URL = "https://api.novita.ai/openai"
API_KEY = os.getenv("NOVITA_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

# Because Novita not support the responses API so we use the chat completions API instead.
set_default_openai_api("chat_completions")
set_default_openai_client(AsyncOpenAI(base_url=BASE_URL, api_key=API_KEY))
# Disable tracing for this example
# Refer to https://openai.github.io/openai-agents-python/tracing/#external-tracing-processors-list to use the custom spans.
set_tracing_disabled(disabled=True)

agent = Agent(name="Assistant",
              instructions="You are a helpful assistant", model=MODEL_NAME)

result = Runner.run_sync(
    agent, "Write a haiku about recursion in programming.")
print(result.final_output)

# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.
```

## Handoffs example

<Warning>
  If running this, ensure you set the NOVITA\_API\_KEY and MODEL\_NAME environment variables.
</Warning>

```python  theme={"system"}
import os
import asyncio
from openai import AsyncOpenAI
from agents import (
    Agent,
    Runner,
    set_default_openai_api,
    set_default_openai_client,
    set_tracing_disabled,
)

BASE_URL = "https://api.novita.ai/openai"
API_KEY = os.getenv("NOVITA_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

# Because Novita not support the responses API so we use the chat completions API instead.
set_default_openai_api("chat_completions")
set_default_openai_client(AsyncOpenAI(base_url=BASE_URL, api_key=API_KEY))
# Disable tracing for this example
# Refer to https://openai.github.io/openai-agents-python/tracing/#external-tracing-processors-list to use the custom spans.
set_tracing_disabled(disabled=True)

spanish_agent = Agent(
    name="Spanish agent",
    instructions="You only speak Spanish.",
    model=MODEL_NAME,
)

english_agent = Agent(
    name="English agent",
    instructions="You only speak English",
    model=MODEL_NAME,
)

triage_agent = Agent(
    name="Triage agent",
    instructions="Handoff to the appropriate agent based on the language of the request.",
    handoffs=[spanish_agent, english_agent],
    model=MODEL_NAME,
)


async def main():
    result = await Runner.run(triage_agent, input="Hola, ¿cómo estás?")
    print(result.final_output)
    # ¡Hola! Estoy bien, gracias por preguntar. ¿Y tú, cómo estás?


if __name__ == "__main__":
    asyncio.run(main())
```

## Functions example

<Warning>
  If running this, ensure you set the NOVITA\_API\_KEY and MODEL\_NAME environment variables.
</Warning>

```python  theme={"system"}
import os
import asyncio
from openai import AsyncOpenAI
from agents import (
    Agent,
    Runner,
    set_default_openai_api,
    set_default_openai_client,
    set_tracing_disabled,
    function_tool,
)

BASE_URL = "https://api.novita.ai/openai"
API_KEY = os.getenv("NOVITA_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

# Because Novita not support the responses API so we use the chat completions API instead.
set_default_openai_api("chat_completions")
set_default_openai_client(AsyncOpenAI(base_url=BASE_URL, api_key=API_KEY))
# Disable tracing for this example
# Refer to https://openai.github.io/openai-agents-python/tracing/#external-tracing-processors-list to use the custom spans.
set_tracing_disabled(disabled=True)

@function_tool
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny."

agent = Agent(
    name="Hello world",
    instructions="You are a helpful agent.",
    tools=[get_weather],
    model=MODEL_NAME,
)

async def main():
    result = await Runner.run(agent, input="What's the weather in Tokyo?")
    print(result.final_output)
    # The weather in Tokyo is sunny.

if __name__ == "__main__":
    asyncio.run(main())
```


Built with [Mintlify](https://mintlify.com).