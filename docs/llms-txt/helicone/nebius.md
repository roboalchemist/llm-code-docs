# Source: https://docs.helicone.ai/getting-started/integration-method/nebius.md

# Nebius Token Factory Integration

> Connect Helicone with Nebius Token Factory, a platform that provides powerful AI models including text and multimodal models, embeddings and guardrails, and text-to-image models.

<Warning>
  This integration method is maintained but no longer actively developed. For the best experience and latest features, use our new [AI Gateway](/gateway/overview) with unified API access to 100+ models.
</Warning>

You can follow their documentation here: [https://docs.tokenfactory.nebius.com/](https://docs.tokenfactory.nebius.com/)

# Gateway Integration

<Steps>
  <Step title="Create a Helicone account">
    Log into [helicone](https://www.helicone.ai) or create an account. Once you have an account, you
    can generate an [API key](https://helicone.ai/developer).
  </Step>

  <Step title="Create a Nebius Token Factory account">
    Log into [Nebius Token Factory](https://tokenfactory.nebius.com/) or create an account. Once you have an account, you
    can generate an API key from your dashboard.
  </Step>

  <Step title="Set HELICONE_API_KEY and NEBIUS_API_KEY as environment variable">
    ```javascript  theme={null}
    HELICONE_API_KEY=<your API key>
    NEBIUS_API_KEY=<your API key>
    ```
  </Step>

  <Step title="Modify the base URL and add Auth headers">
    Replace the following Nebius Token Factory URL with the Helicone Gateway URL:

    `https://api.tokenfactory.nebius.com` -> `https://nebius.helicone.ai`

    and then add the following authentication headers:

    ```javascript  theme={null}
    Authorization: Bearer <your API key>
    ```
  </Step>
</Steps>

Now you can access all the models on Nebius Token Factory with a simple fetch call:

## Example - Text Completion

```bash  theme={null}
curl \
  --header "Authorization: Bearer $NEBIUS_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "deepseek-ai/DeepSeek-R1",
    "messages": [
      {
        "role": "user",
        "content": "Explain quantum computing in simple terms"
      }
    ]
}' \
  --url https://nebius.helicone.ai/v1/chat/completions
```

## Example - Image Generation

```bash  theme={null}
curl \
  --header "Authorization: Bearer $NEBIUS_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "black-forest-labs/flux-schnell",
    "prompt": "A beautiful sunset over a mountain landscape"
}' \
  --url https://nebius.helicone.ai/v1/images/generations
```

For more information on how to use headers, see [Helicone Headers](https://docs.helicone.ai/helicone-headers/header-directory#utilizing-headers) docs.
And for more information on how to use Nebius Token Factory, see [Nebius Token Factory Docs](https://docs.tokenfactory.nebius.com/).
