# Source: https://docs.fiddler.ai/reference/settings/llm-gateway.md

# LLM Gateway

The **LLM Gateway** allows you to manage and securely configure credentials for multiple Large Language Model (LLM) providers, enabling you to use your own API keys for AI-powered features throughout the Fiddler platform.

## Overview

LLM Gateway provides centralized management of LLM provider credentials, giving you control over which models and API keys power Fiddler's AI features such as:

* **Custom Evaluators** - Use your preferred LLM to evaluate model outputs
* **LLM Enrichments** - Generate AI-powered insights on your monitoring data
* **Content Analysis** - Assess response quality, detect hallucinations, and monitor trust metrics

### Key Capabilities

* **Multiple Provider Support** - Configure credentials for OpenAI, Anthropic, Gemini, and Fiddler
* **Credential Redundancy** - Add multiple API keys per provider for failover and load balancing
* **Flexible Key Management** - Organize credentials by team, environment, or purpose
* **Secure Storage** - API keys are encrypted and stored securely

***

## Prerequisites

Before configuring LLM Gateway, ensure you have:

* **Admin Permissions** - Only administrators can access the LLM Gateway settings
* **Provider API Keys** - Valid API credentials from your chosen LLM providers (OpenAI, Anthropic, Gemini, or Fiddler)

{% hint style="info" %}
**Note:** Each provider requires a separate API key. Obtain keys from your provider's developer portal before proceeding.
{% endhint %}

***

## Configure LLM Providers

### Add a New Provider

Follow these steps to add an LLM provider to your Fiddler organization:

{% stepper %}
{% step %}
**Navigate to the LLM Gateway Settings**

From the top navigation bar, click the **Settings** icon (gear icon) and select the **LLM Gateway** tab.
{% endstep %}

{% step %}
**Add a Provider**

Click the **Add Provider** button to open the provider configuration dialog.
{% endstep %}

{% step %}
**Select the Provider Type**

Choose your LLM provider from the dropdown menu:

* **OpenAI** - GPT-4, GPT-3.5, and other OpenAI models
* **Anthropic** - Claude models (Sonnet, Opus, Haiku)
* **Gemini** - Google's Gemini models
* **Fiddler** - Fiddler-hosted LLM services
  {% endstep %}

{% step %}
**Add Your First Credential**

a. Click **Add Credential**

b. Enter a **Nickname** for the credential (for example, `Production Team Key` or `Test Environment`)

{% hint style="info" %}
**Tip:** Use clear, descriptive nicknames to differentiate between test and production keys or to identify which team owns the credential.
{% endhint %}

c. Paste your **API Key** into the credential field

d. The provider's available models will be automatically populated
{% endstep %}

{% step %}
**Save the Provider**

Click **Update Provider** to save your configuration, or **Cancel** to discard changes.

Your provider is now configured and ready to use with Fiddler's AI-powered features.
{% endstep %}
{% endstepper %}

***

### Add Multiple Credentials to a Provider

You can add multiple API keys to a single provider for redundancy, load balancing, or to separate keys by environment or team.

**Why Use Multiple Credentials?**

* **Redundancy** - Automatic failover if one key reaches rate limits or expires
* **Load Balancing** - Distribute API calls across multiple keys to improve throughput
* **Key Rotation** - Safely test new credentials before removing old ones
* **Environment Separation** - Use different keys for development, staging, and production

**To Add Additional Credentials:**

1. Navigate to **Settings → LLM Gateway**
2. Click the **edit** icon next to the provider you want to modify
3. In the Edit Provider dialog, click **Add Credential**
4. Enter a nickname and paste the new API key
5. Click **Update Provider** to save

All credentials for a provider will be available for use across Fiddler features. The platform handles credential selection and failover automatically.

***

### Edit an Existing Provider

You can modify provider configurations, update credentials, or rename existing keys.

**To Edit a Provider:**

1. Navigate to **Settings → LLM Gateway**
2. Locate the provider you want to edit
3. Click the **edit** icon next to the provider name
4. Make your changes:
   * **Update Credentials** - Click the edit icon next to a credential to modify the API key
   * **Rename Credentials** - Update the nickname to reflect the key's purpose
   * **Add More Credentials** - Click **Add Credential** to add another API key
   * **Remove Credentials** - Delete individual credentials that are no longer needed
5. Click **Update Provider** to save your changes

{% hint style="warning" %}
Removing a credential that is actively in use may impact running evaluations or enrichments. Ensure you have alternate credentials configured before removing a key.
{% endhint %}

***

## Supported Providers

The LLM Gateway supports the following providers:

### OpenAI

* **Models Available:** GPT-4, GPT-4 Turbo, GPT-3.5 Turbo, and other OpenAI models
* **API Key Location:** [OpenAI Platform - API Keys](https://platform.openai.com/api-keys)
* **Use Cases:** Custom evaluators, content generation, response quality assessment

### Anthropic

* **Models Available:** Claude 3 Opus, Claude 3 Sonnet, Claude 3 Haiku, and other Claude models
* **API Key Location:** [Anthropic Console](https://console.anthropic.com/)
* **Use Cases:** Advanced reasoning, content analysis, evaluation tasks

### Gemini

* **Models Available:** Gemini Pro, Gemini Ultra, and other Google AI models
* **API Key Location:** [Google AI Studio](https://makersuite.google.com/app/apikey)
* **Use Cases:** Multimodal analysis, content generation, embeddings

### Fiddler

* **Models Available:** Fiddler-managed LLM services
* **API Key Location:** Provided by Fiddler
* **Use Cases:** Pre-configured evaluators, platform-optimized features

***

## Best Practices

### Credential Management

* **Use Descriptive Nicknames** - Label credentials by team, environment, or purpose (for example, `ML Team - Production`, `Data Science - Test`)
* **Rotate Keys Regularly** - Add new credentials before removing old ones to avoid service interruption
* **Separate Environments** - Use different API keys for development, staging, and production
* **Monitor Usage** - Track API consumption through your provider's dashboard to avoid unexpected costs

### Security

* **Restrict Access** - Only grant Admin permissions to users who need to manage LLM credentials
* **Avoid Sharing Keys** - Each team should have their own credentials rather than sharing a single key
* **Revoke Compromised Keys** - If a key is exposed, immediately revoke it in your provider's console and remove it from Fiddler

### Performance Optimization

* **Add Multiple Credentials** - Configure 2-3 keys per provider for redundancy and better throughput
* **Test Before Production** - Validate new credentials in a test environment before using them in production
* **Monitor Rate Limits** - Be aware of your provider's rate limits and adjust your credential count accordingly

***

## Related Features

Once you've configured LLM providers in the Gateway, you can use them with these Fiddler features:

* **Custom Evaluators** - Create LLM-based evaluators to assess model outputs
* **LLM Enrichments** - Generate AI-powered metrics for your LLM applications
* **Content Safety** - Use LLM providers for advanced content analysis

***

## Troubleshooting

### Provider Not Appearing in Feature Selection

**Issue:** After adding a provider, it doesn't appear in evaluator or enrichment configuration.

**Solution:**

* Verify the provider was saved successfully (check the LLM Gateway tab)
* Ensure at least one credential was added to the provider
* Refresh your browser page
* Contact your Fiddler administrator to verify permissions

### Invalid API Key Error

**Issue:** Receiving authentication errors when using a configured provider.

**Solution:**

* Verify the API key is correct in your provider's console
* Check that the key hasn't expired or been revoked
* Ensure the key has the necessary permissions for the models you're using
* Update the credential in Settings → LLM Gateway

### Rate Limit Warnings

**Issue:** Receiving rate limit errors from a provider.

**Solution:**

* Add additional credentials to the provider for load balancing
* Check your provider's dashboard for current usage and limits
* Consider upgrading your provider plan for higher limits
* Temporarily reduce the number of concurrent evaluations or enrichments

***
