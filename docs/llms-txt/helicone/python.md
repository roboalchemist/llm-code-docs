# Source: https://docs.helicone.ai/integrations/xai/python.md

# Source: https://docs.helicone.ai/integrations/openai/python.md

# Source: https://docs.helicone.ai/integrations/nvidia/python.md

# Source: https://docs.helicone.ai/integrations/llama/python.md

# Source: https://docs.helicone.ai/integrations/instructor/python.md

# Source: https://docs.helicone.ai/integrations/groq/python.md

# Source: https://docs.helicone.ai/integrations/gemini/vertex/python.md

# Source: https://docs.helicone.ai/integrations/gemini/api/python.md

# Source: https://docs.helicone.ai/integrations/bedrock/python.md

# Source: https://docs.helicone.ai/integrations/azure/python.md

# Source: https://docs.helicone.ai/integrations/anthropic/python.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Anthropic Python SDK Integration

> Use Anthropic's Python SDK to integrate with Helicone to log your Anthropic LLM usage.

<Warning>
  This integration method is maintained but no longer actively developed. For the best experience and latest features, use our new [AI Gateway](/gateway/overview) with unified API access to 100+ models.
</Warning>

## Proxy Integration

<Steps>
  <Step title="Create an account + Generate an API Key">
    Log into [helicone](https://www.helicone.ai) or create an account. Once you have an account, you
    can generate an [API key](https://helicone.ai/developer).
  </Step>

  <Step title="Set HELICONE_API_KEY as an environment variable">
    ```Python  theme={null}
    export HELICONE_API_KEY=<your API key>
    ```
  </Step>

  <Step title="Modify the base path and add a Helicone-Auth header">
    <CodeGroup>
      ```Python example.py theme={null}
      import anthropic
      import os

      client = anthropic.Anthropic(
        api_key=os.environ.get("ANTHROPIC_API_KEY"),
        base_url="https://anthropic.helicone.ai",
        default_headers={
          "Helicone-Auth": f"Bearer {os.environ.get("HELICONE_API_KEY")}",
        },
      )

      client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1024,
        messages=[
          {"role": "user", "content": "Hello, world"}
        ]
      )
      ```
    </CodeGroup>
  </Step>
</Steps>
