# Source: https://docs.linkup.so/pages/integrations/linkup-openai.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Linkup + OpenAI

> Use OpenAI's function calling capabilities to integrate with Linkup

<Card title="Looking for OpenAI SDK?" icon="link" href="https://docs.linkup.so/pages/sdk/open-ai/open-ai" cta="Read our guide here">
  We have a dedicated guide for using the OpenAI SDK with Linkup.
</Card>

This tutorial shows you how to use OpenAI's function calling with Linkup to build a chatbot with real-time web search capabilities.

<Steps>
  <Step title="Get your API Keys">
    <CardGroup cols={2}>
      <Card title="Get your Linkup API key" icon="key" href="https://app.linkup.so/" horizontal="True">
        Create a Linkup account for free to get your API key.
      </Card>

      <Card title="Get your OpenAI API key" icon="key" href="https://platform.openai.com/api-keys" horizontal="True">
        Create an OpenAI account for free to get your API key.
      </Card>
    </CardGroup>
  </Step>

  <Step title="Install and Setup">
    Install the required packages:

    ```bash  theme={null}
    pip install linkup-sdk openai
    ```

    Set up your clients:

    ```python  theme={null}
    from openai import OpenAI
    from linkup import LinkupClient
    import json
    from datetime import datetime

    openai_client = OpenAI(api_key="your_openai_api_key")
    linkup_client = LinkupClient(api_key="your_linkup_api_key")
    ```
  </Step>

  <Step title="Define the Function Schema">
    Tell OpenAI about your search function using the Responses API format:

    ```python  theme={null}
    tools = [{
        "type": "function",
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
    }]
    ```
  </Step>

  <Step title="Build the Chatbot">
    Put it all together in a conversational loop using the Responses API:

    ```python  theme={null}
    system_prompt = f"You are a helpful assistant. Today is {datetime.now().strftime('%B %d, %Y')}. Use web search when you need current information."
    input_list = [{"role": "system", "content": system_prompt}]

    print("Chatbot ready! Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input or user_input.lower() == "quit":
            break

        input_list.append({"role": "user", "content": user_input})

        try:
            response = openai_client.responses.create(
                model="gpt-5",
                tools=tools,
                input=input_list,
            )

            while any(item.type == "function_call" for item in response.output):
                input_list += response.output

                for item in response.output:
                    if item.type == "function_call":
                        args = json.loads(item.arguments)
                        print(f"Searching with Linkup: {args['query']}...")
                        linkup_response = linkup_client.search(
                            query=args["query"],
                            depth="standard",
                            output_type="searchResults"
                        )
                        search_results_json = json.dumps(
                            linkup_response.model_dump(), indent=2
                        )
                        input_list.append({
                            "type": "function_call_output",
                            "call_id": item.call_id,
                            "output": search_results_json
                        })

                response = openai_client.responses.create(
                    model="gpt-5",
                    tools=tools,
                    input=input_list,
                )

            input_list += response.output

            print(f"\nAssistant: {response.output_text}\n")

        except Exception as e:
            print(f"Error: {e}\n")
            input_list.pop()
    ```
  </Step>
</Steps>

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


Built with [Mintlify](https://mintlify.com).