# Source: https://docs.helicone.ai/getting-started/integration-method/deepseek.md

# DeepSeek AI Integration

> Connect Helicone with DeepSeek AI, a platform that provides powerful language models including MoE and Code models for various AI applications.

<Warning>
  This integration method is maintained but no longer actively developed. For the best experience and latest features, use our new [AI Gateway](/gateway/overview) with unified API access to 100+ models.
</Warning>

You can follow their documentation here: [https://api-docs.deepseek.com/](https://api-docs.deepseek.com/)

# Gateway Integration

<Steps>
  <Step title="Create a Helicone account">
    Log into [helicone](https://www.helicone.ai) or create an account. Once you have an account, you
    can generate an [API key](https://helicone.ai/developer).
  </Step>

  <Step title="Create a DeepSeek AI account">
    Log into platform.deepseek.ai or create an account. Once you have an account, you
    can generate an API key from your dashboard.
  </Step>

  <Step title="Set HELICONE_API_KEY and DEEPSEEK_API_KEY as environment variable">
    ```javascript  theme={null}
    HELICONE_API_KEY=<your API key>
    DEEPSEEK_API_KEY=<your API key>
    ```
  </Step>

  <Step title="Modify the base URL and add Auth headers">
    Replace the following DeepSeek AI URL with the Helicone Gateway URL:

    `https://api.deepseek.ai/v1/chat/completions` -> `https://deepseek.helicone.ai/v1/chat/completions`

    and then add the following authentication headers:

    ```javascript  theme={null}
    Authorization: Bearer <your API key>
    ```
  </Step>
</Steps>

Now you can access all the models on DeepSeek AI with a simple fetch call:

## Example

```bash  theme={null}
curl --request POST \
      --url https://deepseek.helicone.ai/chat/completions \
      --header 'Content-Type: application/json' \
      --header "Authorization: Bearer $DEEPSEEK_API_KEY" \
      --header "Helicone-Auth: Bearer $HELICONE_API_KEY" \
      --data '{
          "model": "deepseek-chat",
          "messages": [
              {
                  "role": "system",
                  "content": "Say Hello!"
              }
          ],
          "temperature": 1,
          "max_tokens": 30
        }'
```

For more information on how to use headers, see [Helicone Headers](https://docs.helicone.ai/helicone-headers/header-directory#utilizing-headers) docs.
And for more information on how to use DeepSeek AI, see [DeepSeek AI Docs](https://platform.deepseek.ai/docs).
