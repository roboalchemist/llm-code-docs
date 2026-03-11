# Source: https://docs.linkup.so/pages/integrations/agno/agno.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Agno

> How to use Linkup with Agno

## Overview

Linkup can be integrate with [Agno](https://www.agno.com) as a tool to provide real-time web search capabilities to your Agno AI agents.

## Installation

<Steps>
  <Step title="Set Up API Key">
    1. Get your Linkup API Key:
       <Card title="Get your API key" icon="key" href="https://app.linkup.so" horizontal="True">
         Create a Linkup account for free to get your API key.
       </Card>

    2. Set the API key in your environment:
       ```shell  theme={null}
       export LINKUP_API_KEY=your_api_key_here
       ```
  </Step>

  <Step title="Install Linkup SDK">
    1. Install the Linkup SDK using pip:
       ```shell  theme={null}
       pip install linkup-sdk
       ```
  </Step>

  <Step title="Install Agno">
    1. Install Agno using pip:
       ```shell  theme={null}
       pip install agno
       ```
  </Step>
</Steps>

## Example Usage

The following agent will search the web for the latest news in French politics and print the response.

```python python theme={null}
    from agno.agent import Agent
    from agno.tools.linkup import LinkupTools

    agent = Agent(tools=[LinkupTools()], show_tool_calls=True)
    agent.print_response("What's the latest news in French politics?", markdown=True)
```

## Toolkit Functions

| Function                 | Description                                                                                                                                         |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `web_search_with_linkup` | Searches the web for a query using Linkup API. Takes a query string and optional depth/output\_type parameters. Returns search results as a string. |

## Toolkit Parameters

| Parameter     | Type                                        | Default           | Description                                                                                                                                                                                                       |
| ------------- | ------------------------------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api_key`     | `Optional[str]`                             | `None`            | API key for authentication. If not provided, will check LINKUP\_API\_KEY environment variable.                                                                                                                    |
| `depth`       | `Literal["standard", "deep"]`               | `"standard"`      | Depth of the search. Use 'standard' for fast and affordable web search or 'deep' for comprehensive, in-depth web search.                                                                                          |
| `output_type` | `Literal["sourcedAnswer", "searchResults"]` | `"searchResults"` | Type of output. 'sourcedAnswer' provides a comprehensive natural language answer to the query along with citations to the source material. 'searchResults' returns the raw search context data without synthesis. |

You are now ready to use Linkup in Agno as a tool for your agents !

<Tip>
  You can check the [Agno documention](https://docs.agno.com/introduction/agents) for more information about agents and tools.
</Tip>

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


Built with [Mintlify](https://mintlify.com).