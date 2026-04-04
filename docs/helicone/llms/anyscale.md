# Source: https://docs.helicone.ai/getting-started/integration-method/anyscale.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Anyscale Integration

> Connect Helicone with any LLM deployed on Anyscale, including Llama, Mistral, Gemma, and GPT.

<Warning>
  This integration method is maintained but no longer actively developed. For the best experience and latest features, use our new [AI Gateway](/gateway/overview) with unified API access to 100+ models.
</Warning>

You can use Helicone with your OpenAI compatible models that are deployed on Anyscale.

Follow the Helicone integration as normal in the [proxy approach](/getting-started/integration-method/openai-proxy) but add the following header.

```bash  theme={null}
Helicone-OpenAI-API-Base: https://api.endpoints.anyscale.com/v1
```

This will route traffic through Helicone to your Anyscale deployment.
