# Source: https://docs.helicone.ai/integrations/xai/javascript.md

# Source: https://docs.helicone.ai/integrations/openai/javascript.md

# Source: https://docs.helicone.ai/integrations/ollama/javascript.md

# Source: https://docs.helicone.ai/integrations/nvidia/javascript.md

# Source: https://docs.helicone.ai/integrations/llama/javascript.md

# Source: https://docs.helicone.ai/integrations/instructor/javascript.md

# Source: https://docs.helicone.ai/integrations/groq/javascript.md

# Source: https://docs.helicone.ai/integrations/gemini/vertex/javascript.md

# Source: https://docs.helicone.ai/integrations/gemini/api/javascript.md

# Source: https://docs.helicone.ai/integrations/bedrock/javascript.md

# Source: https://docs.helicone.ai/integrations/azure/javascript.md

# Source: https://docs.helicone.ai/integrations/anthropic/javascript.md

# Source: https://docs.helicone.ai/integrations/xai/javascript.md

# Source: https://docs.helicone.ai/integrations/openai/javascript.md

# Source: https://docs.helicone.ai/integrations/ollama/javascript.md

# Source: https://docs.helicone.ai/integrations/nvidia/javascript.md

# Source: https://docs.helicone.ai/integrations/llama/javascript.md

# Source: https://docs.helicone.ai/integrations/instructor/javascript.md

# Source: https://docs.helicone.ai/integrations/groq/javascript.md

# Source: https://docs.helicone.ai/integrations/gemini/vertex/javascript.md

# Source: https://docs.helicone.ai/integrations/gemini/api/javascript.md

# Source: https://docs.helicone.ai/integrations/bedrock/javascript.md

# Source: https://docs.helicone.ai/integrations/azure/javascript.md

# Source: https://docs.helicone.ai/integrations/anthropic/javascript.md

# Source: https://docs.helicone.ai/integrations/xai/javascript.md

# Source: https://docs.helicone.ai/integrations/openai/javascript.md

# Source: https://docs.helicone.ai/integrations/ollama/javascript.md

# Source: https://docs.helicone.ai/integrations/nvidia/javascript.md

# Source: https://docs.helicone.ai/integrations/llama/javascript.md

# Source: https://docs.helicone.ai/integrations/instructor/javascript.md

# Source: https://docs.helicone.ai/integrations/groq/javascript.md

# Source: https://docs.helicone.ai/integrations/gemini/vertex/javascript.md

# Source: https://docs.helicone.ai/integrations/gemini/api/javascript.md

# Source: https://docs.helicone.ai/integrations/bedrock/javascript.md

# Source: https://docs.helicone.ai/integrations/azure/javascript.md

# Source: https://docs.helicone.ai/integrations/anthropic/javascript.md

# Source: https://docs.helicone.ai/integrations/xai/javascript.md

# Source: https://docs.helicone.ai/integrations/openai/javascript.md

# Source: https://docs.helicone.ai/integrations/ollama/javascript.md

# Source: https://docs.helicone.ai/integrations/nvidia/javascript.md

# Source: https://docs.helicone.ai/integrations/llama/javascript.md

# Source: https://docs.helicone.ai/integrations/instructor/javascript.md

# Source: https://docs.helicone.ai/integrations/groq/javascript.md

# Source: https://docs.helicone.ai/integrations/gemini/vertex/javascript.md

# Source: https://docs.helicone.ai/integrations/gemini/api/javascript.md

# Source: https://docs.helicone.ai/integrations/bedrock/javascript.md

# Source: https://docs.helicone.ai/integrations/azure/javascript.md

# Source: https://docs.helicone.ai/integrations/anthropic/javascript.md

# Anthropic JavaScript SDK Integration

> Use Anthropic's JavaScript SDK to integrate with Helicone to log your Anthropic LLM usage.

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
    ```javascript  theme={null}
    HELICONE_API_KEY=<your API key>
    ```
  </Step>

  <Step title="Modify the base path and add a Helicone-Auth header">
    <CodeGroup>
      ```javascript example.js theme={null}
      import Anthropic from "@anthropic-ai/sdk";

      const anthropic = new Anthropic({
        baseURL: "https://anthropic.helicone.ai",
        apiKey: process.env.ANTHROPIC_API_KEY,
        defaultHeaders: {
          "Helicone-Auth": `Bearer ${process.env.HELICONE_API_KEY}`,
        },
      });

      await anthropic.messages.create({
        model: "claude-3-opus-20240229",
        max_tokens: 1024,
        messages: [{ role: "user", content: "Hello, world" }],
      });
      ```
    </CodeGroup>
  </Step>
</Steps>
