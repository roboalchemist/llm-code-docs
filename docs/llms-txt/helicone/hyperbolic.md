# Source: https://docs.helicone.ai/getting-started/integration-method/hyperbolic.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Hyperbolic Integration

> Integrate Helicone with Hyperbolic, a platform for running open-source LLMs. Monitor and analyze interactions with any Hyperbolic-deployed model using a simple base_url configuration.

<Warning>
  This integration method is maintained but no longer actively developed. For the best experience and latest features, use our new [AI Gateway](/gateway/overview) with unified API access to 100+ models.
</Warning>

You can seamlessly integrate Helicone with the OpenAI compatible models that are deployed on Hyperbolic.

The integration process closely mirrors the [proxy approach](/integrations/openai/javascript). The only distinction lies in the modification of the base\_url to point to the dedicated Hyperbolic endpoint `https://hyperbolic.helicone.ai/v1`.

```bash  theme={null}
base_url="https://hyperbolic.helicone.ai/v1"
```

Please ensure that the base\_url is correctly set to ensure successful integration.

## Proxy Example

<Note>
  The integration process closely mirrors the [proxy
  approach](/integrations/openai/javascript). More docs available there.
</Note>

<Steps>
  <Step title="Create Helicone account + Generate an API Key">
    Log into [helicone](https://www.helicone.ai) or create an account. Once you have an account, you
    can generate an [API key](https://helicone.ai/developer).
  </Step>

  <Step title="Create Hyperbolic account + Retrieve an API Key">
    Log into [app.hyperbolic.xyz](https://app.hyperbolic.xyz/) or create an account. Once you have an account, you
    can retrieve your [API key](https://app.hyperbolic.xyz/settings).
  </Step>

  <Step title="Set HELICONE_WRITE_API_KEY as an environment variable">
    <Note>Helicone write only API keys are only required if passing auth in URL path [read more here.](/faq/secret-vs-public-key)
    Alternatively, pass auth in as header.</Note>

    ```javascript  theme={null}
    HELICONE_WRITE_API_KEY=<your API key>
    HYPERBOLIC_API_KEY=<your API key>
    ```
  </Step>

  <Step title="Modify the base path and add a Helicone Auth">
    <CodeGroup>
      ```javascript OpenAI V4+ theme={null}
      import OpenAI from "openai";

      const openai = new OpenAI({
        apiKey: process.env.HYPERBOLIC_API_KEY,
        basePath:
          "https://hyperbolic.helicone.ai/v1/${process.env.HELICONE_WRITE_API_KEY}",
      });

      async function main() {
        const response = await client.chat.completions.create({
          messages: [
            {
              role: "system",
              content: "You are an expert travel guide.",
            },
            {
              role: "user",
              content: "Tell me fun things to do in San Francisco.",
            },
          ],
          model: "meta-llama/Meta-Llama-3-70B-Instruct",
        });

        const output = response.choices[0].message.content;
        console.log(output);
      }

      main();
      ```

      ```bash cURL theme={null}
      curl --request POST \
          --url "https://hyperbolic.helicone.ai/v1/$HELICONE_WRITE_API_KEY/chat/completions" \
          --header "Authorization: Bearer $HYPERBOLIC_API_KEY" \
          --header "Helicone-Auth: Bearer $HELICONE_API_KEY" \
          --header "Content-Type: application/json" \
          --data '{
              "messages": [
                  {
                      "role": "system",
              	    "content": "You are a helpful and polite assistant."
                  },
                  {
                      "role": "user",
                      "content": "What is Chinese hotpot?"
                  }
              ],
              "model": "meta-llama/Meta-Llama-3-70B-Instruct",
              "presence_penalty": 0,
              "temperature": 0.1,
              "top_p": 0.9,
              "stream": false
          }'
      ```
    </CodeGroup>
  </Step>
</Steps>
