# Source: https://docs.linkup.so/pages/integrations/baseten/baseten.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Baseten

> Use Linkup as a real-time web search tool for models served on Baseten's serverless inference platform

Baseten provides serverless GPU inference for open-source models with no infrastructure to manage. With Linkup, you can ground these models in real-time web data, giving them the ability to retrieve current facts, news, and source-backed information beyond their training data.

This guide demonstrates the integration using GPT-OSS 120B, but the same approach works with any model available on Baseten that supports function calling.

<Steps>
  <Step title="Get your API Keys">
    <CardGroup cols={2}>
      <Card title="Get your Linkup API key" icon="key" href="https://app.linkup.so/" horizontal="True">
        Create a Linkup account for free to get your API key.
      </Card>

      <Card title="Get your Baseten API key" icon="key" href="https://app.baseten.co/settings/api-keys" horizontal="True">
        Navigate to your Baseten settings, select API Keys, click Create API key, and copy the generated key.
      </Card>
    </CardGroup>
  </Step>

  <Step title="Set Up Your Environment">
    Initialize your project and create a virtual environment:

    ```bash  theme={null}
    mkdir baseten-linkup
    cd baseten-linkup
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

    Install dependencies:

    ```bash  theme={null}
    pip install openai linkup-sdk
    ```

    Configure your API keys as environment variables:

    <CodeGroup>
      ```bash Mac / Linux theme={null}
      export BASETEN_API_KEY=paste_your_baseten_key_here
      export LINKUP_API_KEY=paste_your_linkup_key_here
      ```

      ```bash Windows theme={null}
      set BASETEN_API_KEY=paste_your_baseten_key_here
      set LINKUP_API_KEY=paste_your_linkup_key_here
      ```
    </CodeGroup>
  </Step>

  <Step title="Build the Agent">
    Create a file named `agent.py` and add the following code:

    ```python agent.py theme={null}
    import os
    import json
    from datetime import datetime
    from openai import OpenAI
    from linkup import LinkupClient

    client = OpenAI(
        api_key=os.environ.get("BASETEN_API_KEY"),
        base_url="https://inference.baseten.co/v1"
    )
    linkup_client = LinkupClient(api_key=os.environ.get("LINKUP_API_KEY"))

    tools = [{
        "type": "function",
        "function": {
            "name": "search_web",
            "description": "Search the web in real time. Use this tool whenever the user needs trusted facts, news, or source-backed information. Returns comprehensive content from the most relevant sources.",
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

    def main():
        print("--- GPT-OSS 120B + Linkup ---")
        print("Type 'quit' to exit.\n")

        today_str = datetime.now().strftime("%B %d, %Y")
        system_prompt = (
            f"You are a helpful assistant. Today is {today_str}. "
            f"Use web search when you need current information. "
            f"Prefer searching over relying on your training data for anything that could be outdated."
        )

        history = [{"role": "system", "content": system_prompt}]

        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() in ["quit", "exit"]:
                    print("Goodbye!")
                    break

                history.append({"role": "user", "content": user_input})

                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=history,
                    tools=tools,
                    tool_choice="auto"
                )
                message = response.choices[0].message

                while message.tool_calls:
                    history.append(message)
                    for tc in message.tool_calls:
                        q = json.loads(tc.function.arguments)["query"]
                        print(f"Searching using Linkup: {q}...")
                        try:
                            result = linkup_client.search(
                                query=q,
                                depth="standard",
                                output_type="searchResults"
                            )
                            content = "\n\n".join(
                                f"{r.name}\n{r.url}\n{r.content}"
                                for r in result.results
                            )
                        except Exception as e:
                            content = f"Search error: {e}"
                        history.append({
                            "role": "tool",
                            "tool_call_id": tc.id,
                            "content": content
                        })

                    response = client.chat.completions.create(
                        model="openai/gpt-oss-120b",
                        messages=history,
                        tools=tools,
                        tool_choice="auto"
                    )
                    message = response.choices[0].message

                print(f"Agent: {message.content}\n")
                history.append(message)

            except Exception as e:
                print(f"Error: {e}")

    if __name__ == "__main__":
        main()
    ```
  </Step>

  <Step title="Run the Agent">
    ```bash  theme={null}
    python agent.py
    ```
  </Step>

  <Step title="Try Different Scenarios">
    **Internal knowledge (no tool call):**

    ```
    You: What is the definition of philosophy?
    Agent: Philosophy is the study of fundamental questions about existence,
           knowledge, values, reason, mind, and language...
    ```

    **Tool-augmented reasoning:**

    ```
    You: What are the latest books published on logic?
    Searching using Linkup: latest logic books 2025...
    Agent: Synthesizes a response citing recent publications found via Linkup.
    ```
  </Step>
</Steps>

For more information, visit:

* [Baseten Documentation](https://docs.baseten.co/)

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


Built with [Mintlify](https://mintlify.com).