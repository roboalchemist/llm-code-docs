# Source: https://docs.linkup.so/pages/integrations/cerebras.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Cerebras

> Use Linkup as a real-time web search tool for models served on Cerebras' ultra-fast inference platform

Cerebras provides ultra-fast inference (3,000+ tokens/sec) for open-source models. With Linkup, you can ground these models in real-time web data, giving them the ability to retrieve current facts, news, and source-backed information beyond their training data.

This guide demonstrates the integration using GPT-OSS 120B, but the same approach works with any model available on Cerebras that supports function calling.

<Steps>
  <Step title="Get your API Keys">
    <CardGroup cols={2}>
      <Card title="Get your Linkup API key" icon="key" href="https://app.linkup.so/" horizontal="True">
        Create a Linkup account for free to get your API key.
      </Card>

      <Card title="Get your Cerebras API key" icon="key" href="https://cloud.cerebras.ai/" horizontal="True">
        Create a Cerebras account for free to get your API key.
      </Card>
    </CardGroup>
  </Step>

  <Step title="Install and Setup">
    Install the required packages:

    ```bash  theme={null}
    pip install linkup-sdk cerebras-cloud-sdk
    ```

    Set up your clients:

    ```python  theme={null}
    from cerebras.cloud.sdk import Cerebras
    from linkup import LinkupClient
    import json
    from datetime import datetime

    cerebras_client = Cerebras(api_key="your_cerebras_api_key")
    linkup_client = LinkupClient(api_key="your_linkup_api_key")
    ```
  </Step>

  <Step title="Define the Function Schema">
    Tell Cerebras about your search function:

    ```python  theme={null}
    tools = [{
        "type": "function",
        "function": {
            "name": "search_web",
            "description": "Search the web for current information. Returns comprehensive content from relevant sources.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query"
                    }
                },
                "required": ["query"]
            }
        }
    }]
    ```
  </Step>

  <Step title="Build the Chatbot">
    Put it all together in a conversational loop:

    ```python  theme={null}
    system_prompt = f"You are a helpful assistant. Today is {datetime.now().strftime('%B %d, %Y')}. Use web search when you need current information."
    messages = [{"role": "system", "content": system_prompt}]

    print("Chatbot ready! Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input or user_input.lower() == "quit":
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = cerebras_client.chat.completions.create(
                model="gpt-oss-120b",
                messages=messages,
                tools=tools
            )

            message = response.choices[0].message

            while message.tool_calls:
                messages.append(message)
                for tool_call in message.tool_calls:
                    args = json.loads(tool_call.function.arguments)
                    print(f"Searching with Linkup: {args['query']}...")
                    linkup_response = linkup_client.search(
                        query=args["query"],
                        depth="standard",
                        output_type="searchResults"
                    )
                    search_results = json.dumps(
                        [{"content": r.content} for r in linkup_response.results]
                    )
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": search_results
                    })

                response = cerebras_client.chat.completions.create(
                    model="gpt-oss-120b",
                    messages=messages,
                    tools=tools
                )
                message = response.choices[0].message

            print(f"\nAssistant: {message.content}\n")
            messages.append({"role": "assistant", "content": message.content})

        except Exception as e:
            print(f"Error: {e}\n")
            messages.pop()
    ```
  </Step>
</Steps>

For more information, visit:

* [Cerebras Inference Documentation](https://inference-docs.cerebras.ai/)

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


Built with [Mintlify](https://mintlify.com).