# Source: https://docs.port.io/ai-interfaces/port-ai/llm-providers-management/setup-and-configuration.md

# Setup & Configuration

This guide covers all technical details for setting up and configuring LLM providers, including permissions, changing defaults, validation flow, and troubleshooting common issues.

## Permissions & Access Control[â](#permissions--access-control "Direct link to Permissions & Access Control")

Admin access required

Managing LLM provider settings requires organization administrator permissions. Only admins can modify default providers or add new provider configurations.

* Admin Users
* Organization Members

**Administrators** can perform all LLM provider management operations:

**Configuration Operations**

* [Get default LLM provider and model](/api-reference/get-default-llm-provider-and-model.md) - View current default provider settings
* [Change default LLM provider and model](/api-reference/change-default-llm-provider-and-model.md) - Update organization default providers
* [Create or connect an LLM provider](/api-reference/create-or-connect-an-llm-provider.md) - Create and configure new LLM provider connections
* [Get a specific provider configuration](/api-reference/get-a-specific-provider-configuration.md) - View existing provider configurations
* [Delete a specific provider configuration](/api-reference/delete-a-specific-provider-configuration.md) - Delete provider configurations

**Management Capabilities**

* Set organization-wide default providers and models
* Configure provider-specific settings and credentials
* Manage provider access and permissions
* Test provider connections with validation

**Organization members** have read-only access to LLM provider information:

**Read-Only Operations**

* [Get default LLM provider and model](/api-reference/get-default-llm-provider-and-model.md) - View current default provider settings
* [Get configured LLM providers](/api-reference/get-configured-llm-providers.md) - View available providers and their status
* See which models are currently configured as defaults

**No Management Access**

* Cannot modify provider configurations
* Cannot change default settings
* Cannot add or remove providers

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

Before configuring LLM providers, ensure you have:

1. **Access to Port AI**: Your organization has access to the Port AI features.
2. **Provider Accounts**: Active accounts with the LLM providers you want to use
3. **Admin Permissions**: Organization administrator role in Port

Some providers require additional setup before you can configure them in Port. See [Step 1: Configure provider policies and settings](#step-1-configure-provider-policies-and-settings-optional) for provider-specific configuration instructions.

## Step 1: Configure provider policies and settings (optional)[â](#step-1-configure-provider-policies-and-settings-optional "Direct link to Step 1: Configure provider policies and settings (optional)")

Some providers require additional policies and settings to be configured before you can use them. This step is only needed if you're configuring AWS Bedrock.

If you're using other providers (OpenAI, Anthropic, Azure OpenAI, or Azure Anthropic), you can skip this step and proceed to [Step 2: Store API Keys in Secrets](#step-2-store-api-keys-in-secrets).

**AWS Bedrock configuration (click to expand)**

**Step 1.1: Configure IAM policy**

Set up an IAM policy to grant permissions for invoking Bedrock models. The configuration varies by provider.

Serverless models are automatically available, but you control access through IAM policies. Anthropic models require additional setup (see [Anthropic models requirements](#anthropic-models-requirements) below).

**Option 1: Allow specific models**

Restrict access to specific models (recommended). Example for Anthropic models in Europe:

**View IAM policy example (click to expand)**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowBedrockInference",
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream"
      ],
      "Resource": [
        "arn:aws:bedrock:*:*:inference-profile/eu.anthropic.claude-sonnet-4-20250514-v1:0",
        "arn:aws:bedrock:*::foundation-model/anthropic.claude-sonnet-4-20250514-v1:0",
        "arn:aws:bedrock:*:*:inference-profile/eu.anthropic.claude-haiku-4-5-20251001-v1:0",
        "arn:aws:bedrock:*::foundation-model/anthropic.claude-haiku-4-5-20251001-v1:0",
        "arn:aws:bedrock:*:*:inference-profile/eu.anthropic.claude-sonnet-4-5-20250929-v1:0",
        "arn:aws:bedrock:*::foundation-model/anthropic.claude-sonnet-4-5-20250929-v1:0"
      ]
    }
  ]
}
```

Each model requires two ARN entries: `inference-profile` and `foundation-model`. Adjust the region and model as needed.

**Option 2: Allow all models**

Use a wildcard policy to allow all models. You can still disable specific models using the [Create or connect an LLM provider](/api-reference/create-or-connect-an-llm-provider.md) API.

**View IAM policy example (click to expand)**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowBedrockInference",
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream"
      ],
      "Resource": [
        "arn:aws:bedrock:*:*:inference-profile/*",
        "arn:aws:bedrock:*::foundation-model/*"
      ]
    }
  ]
}
```

**Using guardrails**

If you want to use guardrails with your Bedrock models, add the `bedrock:ApplyGuardrail` action to your IAM policy:

**View IAM policy example with guardrails (click to expand)**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowBedrockInference",
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream",
        "bedrock:ApplyGuardrail"
      ],
      "Resource": [
        "arn:aws:bedrock:*:*:inference-profile/*",
        "arn:aws:bedrock:*::foundation-model/*"
      ]
    }
  ]
}
```

**Anthropic models setup requirements (click to expand)**

**One-time usage form**

* Submit a one-time usage form through the Amazon Bedrock playground or `PutUserCaseForModelAccess` API.
* For AWS Organizations, complete at the management account level; approval extends to child accounts.

**AWS Marketplace subscription**

* Some Anthropic models require an AWS Marketplace subscription.
* Subscriptions auto-create on first invocation if IAM includes `aws-marketplace:Subscribe`, or an admin can enable models first via console/API.

For details, see the [AWS Security Blog post](https://aws.amazon.com/blogs/security/simplified-amazon-bedrock-model-access/).

**Step 1.2: Choose authentication method**

After configuring the IAM policy, choose how Port will authenticate with AWS Bedrock. You have two authentication options:

* **Option A: Assume role** (recommended) - Configure an IAM role that Port's LLM gateway can assume. This provides enhanced security by eliminating the need to store long-lived credentials. Configure this below.
* **Option B: Access keys** - Store AWS access key ID and secret access key in Port secrets. You'll configure this in [Step 2: Store API Keys in Secrets](#step-2-store-api-keys-in-secrets).

**Option A: Using assume role (recommended)**

Configure an IAM role that Port's LLM gateway can assume. This provides enhanced security by eliminating the need to store long-lived credentials.

**Trust relationship configuration**

Create a trust relationship policy on your IAM role that allows Port's LLM gateway roles to assume it:

**View trust relationship policy example (click to expand)**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::185657066287:role/port-ai-bring-your-own-llm-eu-west-1",
                    "arn:aws:iam::185657066287:role/port-ai-bring-your-own-llm-us-east-1"
                ]
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "sts:ExternalId": "<OPTIONAL_EXTERNAL_ID>"
                }
            }
        }
    ]
}
```

The `sts:ExternalId` condition is optional but recommended for additional security. If you use an external ID, you must create it as a secret in Port before configuring the provider. See [Step 2: Store API Keys in Secrets](#step-2-store-api-keys-in-secrets) for instructions on creating secrets.

**Option B: Using access keys**

If you prefer to use access keys instead of assume role, store your AWS access key ID and secret access key in Port secrets. See [Step 2: Store API Keys in Secrets](#step-2-store-api-keys-in-secrets) for instructions on creating these secrets.

### Anthropic models requirements

## Step 2: Store API Keys in Secrets[â](#step-2-store-api-keys-in-secrets "Direct link to Step 2: Store API Keys in Secrets")

Before configuring providers, store your API keys in Port's secrets system. The secret names you choose are flexible - you'll reference them in your provider configuration.

1. Click on the `...` button in the top right corner of your Port application
2. Click on **Credentials**
3. Click on the `Secrets` tab
4. Click on `+ Secret` and add the required secrets for your chosen provider(s):

* OpenAI
* Anthropic
* Azure OpenAI
* Azure Anthropic
* AWS Bedrock

**Required Secret:**

* API Key secret (e.g., `openai-api-key`) - Your OpenAI API key

**Required Secret:**

* API Key secret (e.g., `anthropic-api-key`) - Your Anthropic API key

**Required Secret:**

* API Key secret (e.g., `azure-openai-api-key`) - Your Azure OpenAI API key

**Required Secret:**

* API Key secret (e.g., `azure-anthropic-api-key`) - Your Azure Anthropic API key

**Option 1: Using access keys (required if not using assume role)**

* Access Key ID secret (e.g., `aws-bedrock-access-key-id`) - Your AWS access key ID
* Secret Access Key secret (e.g., `aws-bedrock-secret-access-key`) - Your AWS secret access key

**Option 2: Using assume role (alternative to access keys)**

* External ID secret (e.g., `BEDROCK_ROLE_EXTERNAL_ID`) - Optional external ID for the trust relationship

See the [AWS Bedrock configuration](#step-1-configure-provider-policies-and-settings-optional) section in Step 1 for configuration details.

Secret naming flexibility

You can choose any names for your secrets. The examples above are suggestions - use names that make sense for your organization. You'll reference these exact names in your provider configuration.

One-time view

After creating a secret, you will be able to view its value only once. Afterwards, you will be able to delete the secret or edit its value, but not to view it.

For more details on managing secrets, see the [Port Secrets documentation](/sso-rbac/port-secrets/.md).

## Step 3: Configure LLM Providers[â](#step-3-configure-llm-providers "Direct link to Step 3: Configure LLM Providers")

Use the [Create or connect an LLM provider](/api-reference/create-or-connect-an-llm-provider.md) API to configure your providers. The interactive API reference provides detailed examples and allows you to test the configuration for each provider type (OpenAI, Anthropic, Azure OpenAI, Azure Anthropic, AWS Bedrock).

After configuration

Once providers are configured, you can view and select default providers and models through the UI (**Builder** â **Organization Settings** â **AI** tab) or continue using the API for all operations.

## Step 4: Validate Configuration[â](#step-4-validate-configuration "Direct link to Step 4: Validate Configuration")

Test your provider configuration with connection validation using the [Create or connect an LLM provider](/api-reference/create-or-connect-an-llm-provider.md) API with the `validate_connection=true` parameter. The interactive API reference shows how to test your configuration before saving it.

## Getting Your Current Configuration[â](#getting-your-current-configuration "Direct link to Getting Your Current Configuration")

You can view your organization's current LLM provider defaults through the UI or API:

**Using the UI:**

1. Go to **Builder** â **Organization Settings** â **AI** tab.
2. View all configured providers and models.
3. See which provider and model are currently set as defaults.

**Using the API:** Retrieve your organization's current LLM provider defaults using the [Get default LLM provider and model](/api-reference/get-default-llm-provider-and-model.md) API. The interactive API reference shows the response format and allows you to test the endpoint.

### System Defaults[â](#system-defaults "Direct link to System Defaults")

When no organization-specific defaults are configured, Port uses these system defaults:

* **Default Provider**: `port`
* **Default Model**: `claude-sonnet-4-5-20250929`

## Changing Default Providers[â](#changing-default-providers "Direct link to Changing Default Providers")

You can change your organization's default LLM provider and model through the UI or API:

**Using the UI:**

1. Go to **Builder** â **Organization Settings** â **AI** tab.
2. Select your preferred **Default LLM provider** from the dropdown.
3. Select your preferred **Default model** from the dropdown.
4. Click **Save** to apply your changes.

Adding new providers

To add a new custom LLM provider, you still need to use the [Create or connect an LLM provider](/api-reference/create-or-connect-an-llm-provider.md) API. Once a provider is configured, it will appear in the UI dropdown for selection.

**Using the API:** Update your organization's default LLM provider and model using the [Change default LLM provider and model](/api-reference/change-default-llm-provider-and-model.md) API. The interactive API reference provides the request format and response examples.

## Validation Flow[â](#validation-flow "Direct link to Validation Flow")

The system validates provider configurations to ensure they work correctly before saving. This includes checking credentials, testing connections, and verifying model availability.

For detailed information about how validation works during API requests, see [Selecting LLM Provider](/ai-interfaces/port-ai/llm-providers-management/selecting-llm-provider.md#provider-validation).

## Configuration Hierarchy[â](#configuration-hierarchy "Direct link to Configuration Hierarchy")

LLM provider settings follow a hierarchy from organization defaults to system defaults.

For detailed information about how defaults are selected during API requests, see [Selecting LLM Provider](/ai-interfaces/port-ai/llm-providers-management/selecting-llm-provider.md#default-provider-selection).

## Frequently Asked Questions[â](#frequently-asked-questions "Direct link to Frequently Asked Questions")

I'm getting "LLM provider not found" - what should I do?

This error occurs when trying to use a provider that hasn't been configured:

```
{
  "ok": false,
  "error": {
    "name": "LLMProviderNotFoundError",
    "message": "LLM provider 'openai' not found for organization"
  }
}
```

**Solution**: Create the provider configuration first using the steps above, or contact your organization administrator.

Why is my connection test failing?

Connection test failures usually indicate credential or configuration issues:

```
{
  "ok": false,
  "error": {
    "name": "LLMProviderModelTestError",
    "message": "Connection test failed for provider 'openai'",
    "details": {
      "testedModels": {
        "gpt-5": { "isValid": false, "message": "Invalid API key" }
      }
    }
  }
}
```

**Solution**:

* Verify your API key is correct and stored properly in secrets
* Ensure the API key has the required permissions for your provider
* Check if your provider account has sufficient quota/credits

I'm getting "apiKeySecretName is required" error

This indicates missing required configuration parameters:

```
{
  "ok": false,
  "error": {
    "name": "LLMProviderInvalidConfigError", 
    "message": "apiKeySecretName is required"
  }
}
```

**Solution**: Check the provider-specific configuration requirements in the setup steps above and ensure all required fields are provided.

I don't have permission to manage LLM providers

```
{
  "name": "llm_provider_manage_forbidden",
  "message": "You do not have permission to manage LLM providers"
}
```

**Solution**: Only organization administrators can manage LLM providers. Contact your admin to get the necessary permissions or ask them to configure the providers for you.

How can I debug provider configuration issues?

Here are useful debugging tips:

* **Check Logs**: Monitor AI invocation logs for detailed error messages
* **Validate Secrets**: Ensure API keys are stored correctly in Port's secrets system
* **Test Connection**: Use `validate_connection=true` parameter when creating providers
* **Verify Permissions**: Ensure your provider API keys have the required permissions
* **Check Quotas**: Monitor usage limits and billing status for external providers
* **Provider Status**: Check if your external provider service is experiencing outages

What should I do if a model isn't enabled for my provider?

```
{
  "ok": false,
  "error": {
    "name": "LLMProviderModelNotEnabledError",
    "message": "Model 'gpt-5' is not enabled for provider 'openai'"
  }
}
```

**Solution**: This usually means the model needs to be enabled in your provider configuration. Contact your organization administrator to enable the specific model for your provider.
