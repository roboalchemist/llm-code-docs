# Source: https://docs.linkup.so/pages/integrations/linkup-claude.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Linkup + Claude

> Use Claude's function calling capabilities to integrate with Linkup

This tutorial shows you how to use Claude's function calling with Linkup to build a chatbot with real-time web search capabilities.

<Steps>
  <Step title="Get your API Keys">
    <CardGroup cols={2}>
      <Card title="Get your Linkup API key" icon="key" href="https://app.linkup.so/" horizontal="True">
        Create a Linkup account for free to get your API key.
      </Card>

      <Card title="Get your Anthropic API key" icon="key" href="https://console.anthropic.com/settings/keys" horizontal="True">
        Create an Anthropic account for free to get your API key.
      </Card>
    </CardGroup>
  </Step>

  <Step title="Install and Setup">
    Install the required packages:

    ```bash  theme={null}
    pip install linkup-sdk anthropic
    ```

    Set up your clients:

    ```python  theme={null}
    import anthropic
    from linkup import LinkupClient
    import json
    from datetime import datetime

    claude_client = anthropic.Anthropic(api_key="your_anthropic_api_key")
    linkup_client = LinkupClient(api_key="your_linkup_api_key")
    ```
  </Step>

  <Step title="Define the Function Schema">
    Tell Claude about your search function:

    ```python  theme={null}
    tools = [{
        "name": "search_web",
        "description": "Search the web in real time. Use this tool whenever the user needs trusted facts, news, or source-backed information. Returns comprehensive content from the most relevant sources.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query"
                }
            },
            "required": ["query"]
        }
    }]
    ```
  </Step>

  <Step title="Build the Chatbot">
    Put it all together in a conversational loop that supports multiple and chained tool calls:

    ```python  theme={null}
    system_prompt = (
        f"You are a helpful assistant. Today is {datetime.now().strftime('%B %d, %Y')}. "
        f"Use web search when you need current information."
    )
    messages = []

    print("Chatbot ready! Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input or user_input.lower() == "quit":
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = claude_client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=1000,
                system=system_prompt,
                messages=messages,
                tools=tools
            )

            while response.stop_reason == "tool_use":
                tool_calls = [block for block in response.content if block.type == "tool_use"]

                tool_results = []
                for tool_use in tool_calls:
                    print(f"Searching with Linkup: {tool_use.input['query']}...")
                    linkup_response = linkup_client.search(
                        query=tool_use.input["query"],
                        depth="standard",
                        output_type="searchResults"
                    )
                    search_results = json.dumps(
                        [{"content": r.content} for r in linkup_response.results]
                    )
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": tool_use.id,
                        "content": search_results
                    })

                messages.append({"role": "assistant", "content": response.content})
                messages.append({"role": "user", "content": tool_results})

                response = claude_client.messages.create(
                    model="claude-sonnet-4-6",
                    max_tokens=1000,
                    system=system_prompt,
                    messages=messages,
                    tools=tools
                )

            text = next(
                (block.text for block in response.content if hasattr(block, "text")),
                None
            )
            if text:
                print(f"\nAssistant: {text}\n")

            messages.append({"role": "assistant", "content": response.content})

        except Exception as e:
            print(f"Error: {e}\n")
            messages.pop()
    ```
  </Step>
</Steps>

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


Built with [Mintlify](https://mintlify.com).