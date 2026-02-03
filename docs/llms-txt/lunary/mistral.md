# Source: https://docs.lunary.ai/docs/integrations/mistral.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Mistral integration

Our Python SDK includes automatic integration with Mistral via OpenAI's package.

<Steps>
  <Step n="1" title="Setup the SDK">
    <CardGroup cols={1}>
      <Card title="Python" icon="python" href="/docs/integrations/python/installation">
        Learn how to set up the Python SDK.
      </Card>
    </CardGroup>
  </Step>

  <Step n="2" title="Monitor your client">
    With our SDKs, tracking Mistral calls is super simple.

    ```py  theme={null}
    import os
    from openai import OpenAI
    import lunary

    MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY")

    client = OpenAI(api_key=MISTRAL_API_KEY, base_url="https://api.mistral.ai/v1/")

    lunary.monitor(client)  # This line sets up monitoring for all calls made through the 'openai' module

    chat_completion = client.chat.completions.create(
      model="mistral-small-latest",
      messages=[{"role": "user", "content": "Hello world"}]
    )
    ```
  </Step>
</Steps>
