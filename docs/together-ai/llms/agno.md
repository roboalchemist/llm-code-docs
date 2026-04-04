# Source: https://docs.together.ai/docs/agno.md

# Agno

> Using Agno with Together AI

Agno is an open-source library for creating multimodal agents. It supports interactions with text, images, audio, and video while remaining model-agnostic, allowing you to use any model in the Together AI library with our integration.

## Install Libraries

```bash  theme={null}
pip install -U agno duckduckgo-search
```

## Authentication

Set your `TOGETHER_API_KEY` environment variable.

<CodeGroup>
  ```shell Shell theme={null}
  export TOGETHER_API_KEY=***
  ```
</CodeGroup>

## Example

Below is a simple agent with access to web search.

<CodeGroup>
  ```python Python theme={null}
  from agno.agent import Agent
  from agno.models.together import Together
  from agno.tools.duckduckgo import DuckDuckGoTools

  agent = Agent(
      model=Together(id="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"),
      tools=[DuckDuckGoTools()],
      markdown=True,
  )
  agent.print_response("What's happening in New York?", stream=True)
  ```
</CodeGroup>

## Next Steps

<Info>
  ### Agno - Together AI Cookbook

  Explore our in-depth [Agno Cookbook](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/Agno/Agents_Agno.ipynb)
</Info>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt