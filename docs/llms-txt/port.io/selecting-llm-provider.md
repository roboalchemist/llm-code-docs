# Source: https://docs.port.io/ai-interfaces/port-ai/llm-providers-management/selecting-llm-provider.md

# Selecting LLM Provider

When interacting with [Port AI](/ai-interfaces/port-ai/api-interaction.md) through the API, you can select which provider and model to use for specific requests. This gives you fine-grained control over AI processing on a per-request basis.

## Port AI Integration[â](#port-ai-integration "Direct link to Port AI Integration")

LLM providers integrate seamlessly with Port AI. You can specify the provider and model when making API requests, overriding the organization's default settings for specific use cases.

### Port AI API with Custom Provider[â](#port-ai-api-with-custom-provider "Direct link to Port AI API with Custom Provider")

Specify a custom provider and model when making Port AI API requests. See the [Selecting Model](/ai-interfaces/port-ai/api-interaction.md#selecting-model) section for detailed examples of how to include provider and model parameters in your requests.

## Default Provider Selection[â](#default-provider-selection "Direct link to Default Provider Selection")

If no provider is specified in your API request, the system uses default values:

1. **Organization Defaults**: If your organization has configured custom defaults

2. **System Defaults**: Port's fallback settings:

   <!-- -->

   * **Default Provider**: `port`
   * **Default Model**: `claude-sonnet-4-5-20250929`

## Provider Validation[â](#provider-validation "Direct link to Provider Validation")

When you specify a provider and model in your API request, the system validates that:

1. **Provider exists**: The specified provider is configured for your organization
2. **Provider is enabled**: The provider configuration is active
3. **Model is available**: The requested model is enabled for that provider
4. **Permissions**: You have access to use the specified provider

## Use Cases for Custom Provider Selection[â](#use-cases-for-custom-provider-selection "Direct link to Use Cases for Custom Provider Selection")

* **Cost Optimization**: Choose different providers based on request complexity or your existing contracts
* **Compliance Requirements**: Use specific providers for sensitive data that must stay within certain infrastructure
* **Performance Optimization**: Select providers based on response time needs or model capabilities
* **Regional Requirements**: Use providers that meet data residency or regional compliance needs

## Frequently Asked Questions[â](#frequently-asked-questions "Direct link to Frequently Asked Questions")

What happens if I specify a provider that doesn't exist?

If you specify a provider that isn't configured for your organization, you'll receive an error:

```
{
  "ok": false,
  "error": {
    "name": "LLMProviderNotFoundError",
    "message": "LLM provider 'openai' not found for organization"
  }
}
```

**Solution**: Make sure the provider is properly configured in your organization settings, or contact your admin.

Why am I getting a "Model not enabled" error?

This error occurs when the model isn't available for the specified provider:

```
{
  "ok": false,
  "error": {
    "name": "LLMProviderModelNotEnabledError",
    "message": "Model 'gpt-5' is not enabled for provider 'anthropic'"
  }
}
```

**Solution**: Check which models are available for your provider, or contact your admin to enable the model.

What happens if I don't specify a provider in my request?

The system will automatically use your organization's default provider and model. If no organization defaults are set, it falls back to Port's system defaults (`port` provider with `claude-sonnet-4-5-20250929` model).

Can I use different providers for different types of requests?

Yes! You can specify different providers and models for each API request. This allows you to optimize for cost, performance, compliance, or other requirements on a per-request basis.

How do I know which providers and models are available to me?

Use the [Get configured LLM providers](/api-reference/get-configured-llm-providers.md) API to see all configured providers for your organization, or check with your organization administrator about available options.

Does specifying a custom provider affect streaming?

No, all responses are streamed by default regardless of which provider you specify. You can use any configured provider with streaming enabled.

Will my request fail if the specified provider is temporarily unavailable?

If a provider connection fails, the system will return an error with details about the issue. The system does not automatically fall back to other providers to ensure predictable behavior.

Can I use provider selection with Port AI API?

Yes! You can specify custom providers and models when making Port AI API requests. This allows you to choose the best model for specific tasks. Learn more about [Port AI API interactions](/ai-interfaces/port-ai/api-interaction.md).
