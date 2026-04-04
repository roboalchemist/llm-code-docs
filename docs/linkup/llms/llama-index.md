# Source: https://docs.linkup.so/pages/integrations/llama-index.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# LlamaIndex

> How to use Linkup in LlamaIndex

## Overview

Linkup can be used with [LlamaIndex](https://www.llamaindex.ai/) to create advanced AI agents and workflows based on internal and web data.

## Getting Started with Linkup in LLamaIndex

<Steps>
  <Step title="Get your Linkup API Key">
    <Card title="Get your API key" icon="key" href="https://app.linkup.so" horizontal="True">
      Create a Linkup account for free to get your API key.
    </Card>
  </Step>

  <Step title="Install dependencies">
    ```shell  theme={null}
    pip install llama-index llama-index-tools-linkup-research
    ```
  </Step>

  <Step title="Create your agent">
    ```python  theme={null}
    from llama_index.core.agent import FunctionCallingAgent
    from llama_index.llms.openai import OpenAI
    from llama_index.tools.linkup_research.base import LinkupToolSpec

    # Tool initialization
    linkup_tool = LinkupToolSpec(
        api_key="<YOUR LINKUP API KEY>",
        depth="standard", # Options: "standard" or "deep"
        output_type="searchResults", # Options: "searchResults", "sourcedAnswer", or "structured"
    )
    ```

    <Info>
      <table>
        <thead>
          <tr>
            <th style={{ color: '#FFFFFF' }}>Parameter</th>
            <th style={{ color: '#FFFFFF' }}>Options</th>
            <th style={{ color: '#FFFFFF' }}>Description</th>
          </tr>
        </thead>

        <tbody>
          <tr>
            <td><code>depth</code></td>
            <td><code>standard</code>, <code>deep</code></td>
            <td>Controls search depth. <code>deep</code> performs more thorough research, <code>standard</code> is faster.</td>
          </tr>

          <tr>
            <td><code>output\_type</code></td>
            <td><code>searchResults</code>, <code>sourcedAnswer</code>, <code>structured</code></td>
            <td>Determines the format of returned information.</td>
          </tr>
        </tbody>
      </table>
    </Info>
  </Step>

  <Step title="Initialize and run your agent">
    ```python  theme={null}
    # Agent initialization
    agent = FunctionCallingAgent.from_tools(
        linkup_tool.to_tool_list(),
        llm=OpenAI(
          api_key="<YOUR OPENAI API KEY>",
          model="gpt-4o-mini"
        ),
    )

    # Agent invocation
    response = agent.chat("Can you tell me which women were awarded the Physics Nobel Prize")
    print(response)
    ```
  </Step>
</Steps>

## Example Response

```python  theme={null}
# Sample output
{
  "response": "Marie Curie (1903), Maria Goeppert Mayer (1963), Donna Strickland (2018), and Andrea Ghez (2020) have been awarded the Nobel Prize in Physics.",
  "sources": [
    # Source information would appear here
  ]
}
```

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


Built with [Mintlify](https://mintlify.com).