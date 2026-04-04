# Source: https://docs.helicone.ai/getting-started/integration-method/perplexity.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Perplexity AI Integration

> Connect Helicone with Perplexity AI, a platform that provides powerful language models including Sonar and Sonar Pro for various AI applications.

<Warning>
  This integration method is maintained but no longer actively developed. For the best experience and latest features, use our new [AI Gateway](/gateway/overview) with unified API access to 100+ models.
</Warning>

You can follow their documentation here: [https://docs.perplexity.ai/](https://docs.perplexity.ai/)

# Gateway Integration

<Steps>
  <Step title="Create a Helicone account">
    Log into [helicone](https://www.helicone.ai) or create an account. Once you have an account, you
    can generate an [API key](https://helicone.ai/developer).
  </Step>

  <Step title="Create a Perplexity AI account">
    Log into [Perplexity AI](https://www.perplexity.ai) or create an account. Once you have an account, you
    can generate an API key from your dashboard.
  </Step>

  <Step title="Set HELICONE_API_KEY and PERPLEXITY_API_KEY as environment variable">
    ```javascript  theme={null}
    HELICONE_API_KEY=<your API key>
    PERPLEXITY_API_KEY=<your API key>
    ```
  </Step>

  <Step title="Modify the base URL and add Auth headers">
    Replace the following Perplexity AI URL with the Helicone Gateway URL:

    `https://api.perplexity.ai/chat/completions` -> `https://perplexity.helicone.ai/chat/completions`

    and then add the following authentication headers:

    ```javascript  theme={null}
    Authorization: Bearer <your API key>
    ```
  </Step>
</Steps>

Now you can access all the models on Perplexity AI with a simple fetch call:

## Example

```bash  theme={null}
curl --request POST \
  --url https://perplexity.helicone.ai/chat/completions \
  --header "Authorization: Bearer $PERPLEXITY_API_KEY" \
  --header "Helicone-Auth: Bearer $HELICONE_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "sonar-pro",
    "messages": [{"role": "user", "content": "Say this is a test"}]
}'
```

For more information on how to use headers, see [Helicone Headers](https://docs.helicone.ai/helicone-headers/header-directory#utilizing-headers) docs.
And for more information on how to use Perplexity AI, see [Perplexity AI Docs](https://docs.perplexity.ai/).
