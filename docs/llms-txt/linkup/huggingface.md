# Source: https://docs.linkup.so/pages/integrations/huggingface.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Huggingface

> How to use Linkup with Huggingface

## Overview

Linkup can be used with [Huggingface](https://huggingface.co/docs/smolagents/en/index) (smolagents) to create advanced AI agents and workflows based on internal and web data.

## Getting Started with Linkup in Huggingface

<Steps>
  <Step title="Get your Linkup API Key">
    <Card title="Get your API key" icon="key" href="https://app.linkup.so" horizontal="True">
      Create a Linkup account for free to get your API key.
    </Card>
  </Step>

  <Step title="Install dependencies">
    ```shell  theme={null}
    pip install linkup-sdk smolagents openai
    ```
  </Step>

  <Step title="Create your agent">
    ```python  theme={null}
    from smolagents import CodeAgent, load_tool
    from smolagents.models import OpenAIServerModel

    linkup_tool = load_tool("Linkup-Platform/linkup-search-tool", trust_remote_code=True)
    ```
  </Step>

  <Step title="Initialize and run your agent">
    ```python  theme={null}
    # Agent initialization
    agent = CodeAgent(
        tools=[linkup_tool],
        model=OpenAIServerModel(
          model="gpt-4o-mini",
          api_key="your_openai_api_key"
        ),
    )
    # Agent invocation
    response = agent.run("What was Microsoft's revenue last quarter and was it well perceived by the market?")
    print(response)
    ```
  </Step>
</Steps>

## Example Response

```
Microsoft's revenue last quarter (3Q2024) was approximately $65.59 billion. The market's perception is mixed; while many analysts are optimistic about growth fueled by AI and cloud services, 
there are concerns regarding a lack of guidance in their report, leading to a cautious reaction from some investors.
```

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


Built with [Mintlify](https://mintlify.com).