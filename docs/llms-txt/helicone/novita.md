# Source: https://docs.helicone.ai/getting-started/integration-method/novita.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Novita AI Integration

> Connect Helicone with Novita AI, a platform that provides powerful LLM models including DeepSeek, Llama, Mistral, and more.

<Warning>
  This integration method is maintained but no longer actively developed. For the best experience and latest features, use our new [AI Gateway](/gateway/overview) with unified API access to 100+ models.
</Warning>

You can follow their documentation here: [https://novita.ai/docs](https://novita.ai/docs)

# Gateway Integration

<Steps>
  <Step title="Create a Helicone account">
    Log into [helicone](https://www.helicone.ai) or create an account. Once you have an account, you
    can generate an [API key](https://helicone.ai/developer).
  </Step>

  <Step title="Create a Novita AI account">
    Log into [Novita AI](https://novita.ai) or create an account. Once you have an account, you
    can generate an API key from your dashboard.
  </Step>

  <Step title="Set HELICONE_API_KEY and NOVITA_API_KEY as environment variable">
    ```javascript  theme={null}
    HELICONE_API_KEY=<your API key>
    NOVITA_API_KEY=<your API key>
    ```
  </Step>

  <Step title="Modify the base URL and add Auth headers">
    Replace the following Novita AI URL with the Helicone Gateway URL:

    `https://api.novita.ai` -> `https://novita.helicone.ai`

    and then add the following authentication headers:

    ```javascript  theme={null}
    Authorization: Bearer <your API key>
    ```
  </Step>
</Steps>

Now you can access all the models on Novita AI with a simple fetch call:

## Example

```bash  theme={null}
curl \
  --header "Authorization: Bearer $NOVITA_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "deepseek/deepseek-r1",
    "messages": [
      {
        "role": "user",
        "content": "What is the capital of France?"
      }
    ]
}' \
  --url https://novita.helicone.ai/v3/chat/completions
```

## Referral Program

Novita AI offers a referral program that provides \$20 in credits for both you and your referrals when using the DeepSeek R1 & V3 APIs. Share your referral link with others to earn credits and help them get started with Novita. Learn more about the program at [Novita's blog](https://blogs.novita.ai/earn-up-to-500-in-deepseek-api-credits-supercharge-your-ai-projects-today/).

For more information on how to use headers, see [Helicone Headers](https://docs.helicone.ai/helicone-headers/header-directory#utilizing-headers) docs.
And for more information on how to use Novita AI, see [Novita AI Docs](https://novita.ai/docs).
