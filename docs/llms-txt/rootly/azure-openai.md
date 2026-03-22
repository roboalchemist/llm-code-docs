# Source: https://docs.rootly.com/integrations/azure-openai.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Azure OpenAI

> Connect Rootly with your Azure OpenAI account to leverage Rootly AI features using your organization's Azure-hosted OpenAI deployments and data retention policies.

## Why

Connect Rootly with your Azure OpenAI account to leverage Rootly AI using your organization's Azure-hosted OpenAI deployments. Organizations using Azure OpenAI may have specific agreements pertaining to data residency, compliance requirements, and data retention policies that differ from the standard OpenAI offering.

Azure OpenAI provides enterprise-grade security, regional availability, and responsible AI content filtering through Microsoft's Azure infrastructure.

## Installation

Rootly requires three parameters to integrate with your Azure OpenAI account:

1. **API Key** - Your Azure OpenAI API key
2. **Resource Name** - Your Azure OpenAI resource name
3. **Deployment Name** - The name of your deployed model

### Finding Your Azure OpenAI Configuration

#### API Key

1. Navigate to the [Azure Portal](https://portal.azure.com)
2. Go to your Azure OpenAI resource
3. Select **Keys and Endpoint** from the left menu
4. Copy either **KEY 1** or **KEY 2**

#### Resource Name

The resource name is part of your Azure OpenAI endpoint URL. For example, if your endpoint is:

```
https://my-company-openai.openai.azure.com/
```

Your resource name is `my-company-openai`

#### Deployment Name

1. In the Azure Portal, go to your Azure OpenAI resource
2. Select **Model deployments** or **Deployments** from the left menu
3. Copy the deployment name of the model you want to use (e.g., `gpt-4`, `gpt-35-turbo`)

### Add Your Configuration

Once you have these three values, [add them to Rootly here](https://rootly.com/account/integrations/azure_open_ai_accounts).

## Supported Models

Azure OpenAI supports various GPT models through deployments. The deployment name you configure will be used as the model identifier in Rootly. Common deployments include:

* GPT-4 and GPT-4 Turbo variants
* GPT-3.5 Turbo variants
* Text embedding models

## API Version

Rootly uses Azure OpenAI API version `2024-02-01` for compatibility and stability.

## Additional Resources

* [Azure OpenAI Service Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
* [Azure OpenAI Quickstart](https://learn.microsoft.com/en-us/azure/ai-services/openai/quickstart)
* [Data, privacy, and security for Azure OpenAI](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/data-privacy)


Built with [Mintlify](https://mintlify.com).