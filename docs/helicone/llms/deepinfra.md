# Source: https://docs.helicone.ai/getting-started/integration-method/deepinfra.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Deepinfra Integration

> Connect Helicone with OpenAI-compatible models on Deepinfra. Simple setup process using a custom base_url for seamless integration with your Deepinfra-based AI applications.

<Warning>
  This integration method is maintained but no longer actively developed. For the best experience and latest features, use our new [AI Gateway](/gateway/overview) with unified API access to 100+ models.
</Warning>

The integration process closely mirrors the [proxy approach](/getting-started/integration-method/openai-proxy). The only distinction lies in the modification of the base\_url to point to the dedicated Deepinfra endpoint `https://deepinfra.helicone.ai/v1`.

<Steps>
  <Step title="Create an account + Generate an API Key">
    Log into [helicone](https://www.helicone.ai) or create an account. Once you have an account, you
    can generate an [API key](https://helicone.ai/developer).

    <Note>
      Make sure to generate a [write only API key](helicone-headers/helicone-auth).
    </Note>
  </Step>

  <Step title="Set base_url for whatever client you are using">
    For more information on how to set the base\_url for your client, please refer to the documentation of the client you are using.

    <CodeGroup>
      ```python example.py theme={null}
      base_url=f"https://deepinfra.helicone.ai/{HELICONE_API_KEY}/v1/openai"
      ```
    </CodeGroup>

    Please ensure that the base\_url is correctly set to ensure successful integration.
  </Step>
</Steps>
