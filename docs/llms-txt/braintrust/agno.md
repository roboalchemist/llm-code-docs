# Source: https://braintrust.dev/docs/integrations/sdk-integrations/agno.md

# Agno

[Agno](https://www.agno.com/) is a Python agent framework for building AI applications. Braintrust automatically traces Agno agents, capturing agent interactions, tool calls, and model responses (supports Agno v2 and higher).

## Setup

Install Braintrust alongside Agno:

<CodeGroup>
  ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  pip install braintrust agno
  ```
</CodeGroup>

To trace Agno agents with Braintrust using an OpenAI model, configure these environment variables:

```bash title=".env" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
BRAINTRUST_API_KEY=your-api-key
OPENAI_API_KEY=your-openai-key
```

## Trace with Agno

To enable automatic tracing, call `setup_agno()` before creating your agents.

This example creates a stock price agent with Yahoo Finance tools:

```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
pip install braintrust agno yfinance
```

```python title="agno_braintrust.py" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
from braintrust.wrappers.agno import setup_agno

# Enable Braintrust tracing
setup_agno(project_name="simple-agent-project")

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools

# Create and configure the agent
agent = Agent(
    name="Stock Price Agent",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[YFinanceTools()],
    instructions="You are a stock price agent. Answer questions in the style of a stock analyst.",
)

response = agent.run("What is the current price of AAPL?")
print(response.content)
```

## Resources

* [Agno documentation](https://www.agno.com/)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt