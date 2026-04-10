# Source: https://directus.io/docs/raw/guides/ai/assistant/setup.md

# Setup

> Configure AI Assistant by adding your AI provider API keys and customizing assistant behavior.

AI Assistant requires an API key from a supported AI provider. This page covers the administrator setup process.

## Requirements

- Administrator access to your Directus instance
- API key from at least one supported provider: OpenAI, Anthropic, or Google (see below)
- Users must have **App access** - Public (non-authenticated) or API-only users cannot use AI Assistant
- AI Assistant can be [disabled at the infrastructure level](/configuration/ai) using the `AI_ENABLED` environment variable

Alternatively, you can use an [OpenAI-compatible provider](#openai-compatible-providers) like Ollama or LM Studio for self-hosted models.

<callout color="info" icon="material-symbols:info">

Note that all users of AI Assistant will share a single API key from your configured provider. Usage limits and costs will be shared across all users. See your provider's dashboard for monitoring usage details and costs.

</callout>

## Get an API Key

You'll need an API key from at least one provider. Choose based on which models you want to use.

<accordion type="single">
<accordion-item icon="i-simple-icons-openai" label="OpenAI">

OpenAI provides GPT-5 models (Nano, Mini, Standard).

1. Go to [platform.openai.com](https://platform.openai.com/) and sign in or create an account
2. Navigate to **API Keys** in the left sidebar (or go directly to [platform.openai.com/api-keys](https://platform.openai.com/api-keys))
3. Click **Create new secret key**
4. Give it a name like "Directus AI Assistant"
5. Copy the key immediately - you won't be able to see it again

<callout color="info" icon="material-symbols:info">

OpenAI requires a payment method and has usage-based pricing. Set spending limits in **Settings → Limits** to control costs.

</callout>
</accordion-item>

<accordion-item icon="i-simple-icons-anthropic" label="Anthropic">

Anthropic provides Claude models (Haiku 4.5, Sonnet 4.5, Opus 4.5).

1. Go to [console.anthropic.com](https://console.anthropic.com/) and sign in or create an account
2. Navigate to **API Keys** in the settings
3. Click **Create Key**
4. Give it a name like "Directus AI Assistant"
5. Copy the key immediately

<callout color="info" icon="material-symbols:info">

Anthropic requires a payment method and has usage-based pricing. Monitor usage in the Console dashboard.

</callout>
</accordion-item>

<accordion-item icon="i-simple-icons-googlegemini" label="Google AI">

Google provides Gemini models (2.5 Flash, 2.5 Pro, 3 Flash Preview, 3 Pro Preview).

1. Go to [aistudio.google.com](https://aistudio.google.com/) and sign in with your Google account
2. Click **Get API Key** in the left sidebar
3. Click **Create API Key**
4. Select or create a Google Cloud project
5. Copy the generated API key

<callout color="info" icon="material-symbols:info">

Google AI Studio offers a free tier with rate limits. For production use, consider enabling billing in Google Cloud Console to increase quotas.

</callout>
</accordion-item>
</accordion>

## Configure Providers in Directus

<steps level="3">

### Navigate to AI Settings

Go to **Settings → AI** in the Directus admin panel.

![AI Settings page in Directus](/img/ai-settings-ai-chat.png)

### Enter Your API Keys

Add your API key for one or more providers:

- **OpenAI API Key** - Enables GPT-4 and GPT-5 models
- **Anthropic API Key** - Enables Claude models
- **Google API Key** - Enables Gemini models

<callout color="info" icon="material-symbols:security">

API keys are encrypted at rest in the database and masked in the UI.

</callout>

### Configure Allowed Models

For each provider, you can restrict which models are available to users. Use the **Allowed Models** dropdown next to each API key field to select the models users can choose from.

- If no models are selected, no models from that provider will be available
- You can add custom model IDs by typing them and pressing Enter (useful when new models are released)

This is useful for:

- Controlling costs by limiting access to expensive models
- Ensuring compliance by only allowing approved models
- Simplifying the user experience by reducing model choices

### Save Settings

Click **Save** to apply your changes. AI Assistant is now available to all users with [App access](/guides/auth/access-control#studio-users).

</steps>

## OpenAI-Compatible Providers

In addition to the built-in providers, Directus supports any OpenAI-compatible API endpoint. This allows you to use self-hosted models, alternative providers, or private deployments.

<callout color="warning" icon="material-symbols:warning">

**For best results, use built-in cloud providers.** Local models vary significantly in their tool-calling capabilities and may produce inconsistent results. If using OpenAI-compatible providers, we recommend cloud-hosted frontier models over locally-run models on personal hardware.

</callout>

<callout color="info" icon="material-symbols:info">

**File attachments are not supported with OpenAI-compatible providers.** [File uploads](/guides/ai/assistant/usage#files) require a built-in provider (OpenAI, Anthropic, or Google). The file attachment buttons are hidden when an OpenAI-compatible model is selected.

</callout>

![OpenAI Compatible Provider Settings](/img/ai-settings-openai-compat.png)

### Configuration

In **Settings → AI**, scroll to the **OpenAI-Compatible** section and configure:

<table>
<thead>
  <tr>
    <th>
      Field
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <strong>
        Provider Name
      </strong>
    </td>
    
    <td>
      Display name shown in the model selector (e.g., "Ollama", "LM Studio")
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Base URL
      </strong>
    </td>
    
    <td>
      The API endpoint URL (required). Must be OpenAI-compatible.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        API Key
      </strong>
    </td>
    
    <td>
      Authentication key if required by your provider
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Custom Headers
      </strong>
    </td>
    
    <td>
      Additional HTTP headers for authentication or configuration
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Models
      </strong>
    </td>
    
    <td>
      List of models available from this provider
    </td>
  </tr>
</tbody>
</table>

### Model Configuration

For each model, you can specify:

<table>
<thead>
  <tr>
    <th>
      Field
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <strong>
        Model ID
      </strong>
    </td>
    
    <td>
      The model identifier used in API requests
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Display Name
      </strong>
    </td>
    
    <td>
      Human-readable name shown in the UI
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Context Window
      </strong>
    </td>
    
    <td>
      Maximum input tokens (default: 128,000)
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Max Output
      </strong>
    </td>
    
    <td>
      Maximum output tokens (default: 16,000)
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Supports Attachments
      </strong>
    </td>
    
    <td>
      Whether the model can process images/files
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Supports Reasoning
      </strong>
    </td>
    
    <td>
      Whether the model has chain-of-thought capabilities
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Provider Options
      </strong>
    </td>
    
    <td>
      JSON object for model-specific parameters
    </td>
  </tr>
</tbody>
</table>

<callout color="info" icon="material-symbols:info">

The **Provider Options** field allows you to pass provider-specific parameters to the AI SDK. This is useful for enabling features like extended thinking or custom sampling parameters. See the [Vercel AI SDK documentation](https://sdk.vercel.ai/providers/openai-compatible) for details.

</callout>

### Example Configurations

<accordion type="single">
<accordion-item icon="i-simple-icons-ollama" label="Ollama">

[Ollama](https://ollama.ai/) lets you run open-source models locally.

1. Install Ollama and pull a model: `ollama pull gpt-oss:20b`
2. Ollama runs on `http://localhost:11434` by default

**Directus Configuration:**

- **Provider Name**: `Ollama`
- **Base URL**: `http://localhost:11434/v1`
- **API Key**: `ollama` (required by the OpenAI SDK but ignored by Ollama)
- **Models**: Add your pulled models (e.g., `gpt-oss:20b`, `gpt-oss:120b`, `qwen3:8b`)

<callout color="info" icon="material-symbols:info">

You can copy an existing model to an OpenAI-compatible name if needed: `ollama cp gpt-oss:20b gpt-4`

</callout>

See [Ollama OpenAI compatibility docs](https://docs.ollama.com/api/openai-compatibility) for supported endpoints and features.

</accordion-item>

<accordion-item icon="i-simple-icons-microsoftazure" label="Azure OpenAI">

[Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service) provides OpenAI models through Microsoft Azure.

1. Create an Azure OpenAI resource in the Azure portal
2. Deploy a model (e.g., GPT-4, GPT-4o)
3. Get your endpoint and API key from the Develop tab in your resource

**Directus Configuration:**

- **Provider Name**: `Azure OpenAI`
- **Base URL**: `https://YOUR-RESOURCE.openai.azure.com/openai/v1`
- **API Key**: Your Azure OpenAI API key
- **Models**: Add your deployed model names

<callout color="info" icon="material-symbols:info">

The v1 API (August 2025+) no longer requires an `api-version` header. If using an older API version, add `api-version` as a custom header (e.g., `2024-10-21`).

</callout>

See [Azure OpenAI documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/) for setup details.

</accordion-item>

<accordion-item icon="simple-icons:mistralai" label="Mistral AI">

[Mistral AI](https://mistral.ai/) provides high-performance open and commercial models.

1. Create an account at [console.mistral.ai](https://console.mistral.ai/)
2. Generate an API key

**Directus Configuration:**

- **Provider Name**: `Mistral`
- **Base URL**: `https://api.mistral.ai/v1`
- **API Key**: Your Mistral API key
- **Models**: Add models like `mistral-large-latest`, `mistral-small-latest`, `codestral-latest`

See [Mistral AI documentation](https://docs.mistral.ai/) for available models and pricing.

</accordion-item>
</accordion>

## Custom System Prompt

Optionally customize how the AI assistant behaves in **Settings → AI → Custom System Prompt**.

The [default system prompt](https://github.com/directus/directus/blob/main/api/src/ai/assistant/constants/system-prompt.ts) provides the AI with helpful instructions on how to interact with Directus and is tuned to provide good results.

If you choose to customize the system prompt, it's recommended to use the following template as a starting point:

<accordion type="single">
<accordion-item icon="material-symbols:code" label="View Default System Prompt">

```xml
<behavior_instructions>
You are **Directus Assistant**, a Directus CMS expert with access to a Directus instance through specialized tools

## Communication Style

- **Be concise**: Users prefer short, direct responses. One-line confirmations: "Created collection 'products'"
- **Match the audience**: Technical for developers, plain language for content editors
- **NEVER guess**: If not at least 99% about field values or user intent, ask for clarification

## Tool Usage Patterns

### Discovery First

1. Understand the user's task and what they need to achieve.
2. Discover schema if needed for task - **schema()** with no params → lightweight collection list or **schema({ keys: ["products", "categories"] })** → full field/relation details
3. Use other tools as needed to achieve the user's task.

### Content Items

- Use `fields` whenever possible to fetch only the exact fields you need
- Use `filter` and `limit` to control the number of fetched items unless you absolutely need larger datasets
- When presenting repeated structured data with 4+ items, use markdown tables for better readability

### Schema & Data Changes

- **Confirm before modifying any schema**: Collections, fields, relations always need approval from the user.
- **Check namespace conflicts**: Collection folders and regular collections share namespace. Collection folders are distinct from file folders.

### Safety Rules

- **Deletions require confirmation**: ALWAYS ask before deleting anything
- **Warn on bulk operations**: Alert when affecting many items ("This updates 500 items")
- **Avoid duplicates**: Never create duplicates if you can't modify existing items
- **Use semantic HTML**: No classes, IDs, or inline styles in content fields (unless explicitly asked for by the user)
- **Permission errors**: Report immediately, don't retry

### Behavior Rules

- Call tools immediately without explanatory text
- Use parallel tool calls when possible
- If you don't have access to a certain tool, ask the user to grant you access to the tool from the chat settings.
- If there are unused tools in context but task is simple, suggest disabling unused tools (once per conversation)

## Error Handling

- Auto-retry once for clear errors ("field X required")
- Stop after 2 failures, consult user
- If tool unavailable, suggest enabling in chat settings
</behavior_instructions>
```

</accordion-item>
</accordion>

Leave blank to use the default behavior.

## Prompts Collection

Enable reusable prompts in AI Assistant by configuring a prompts collection:

1. Go to **Settings → AI → Model Context Protocol**
2. Find **AI Prompts Collection**
3. Either generate a new collection or select an existing one

<callout color="info" icon="material-symbols:info">

This is the same collection used by the [MCP Server](/guides/ai/mcp/prompts). Prompts created here are available in both AI Assistant and external MCP clients. This also requires MCP to be enabled.

</callout>

For details on creating prompts with variables, see [MCP Prompts](/guides/ai/mcp/prompts).

## Managing Costs

<callout color="warning" icon="material-symbols:warning">

**AI Assistant uses your own AI provider API keys.** Every message and tool call costs money. Be mindful of usage, especially with larger models. You are responsible for the costs of your usage.

</callout>

**Tips for controlling costs:**

- Use faster, cheaper models (GPT-5 Nano, Claude Haiku 4.5, Gemini 2.5 Flash) for simple tasks
- Use [Allowed Models](#configure-allowed-models) to restrict access to expensive models
- Disable unused tools - disabled tools are not loaded into context, reducing token usage
- Set spending limits in your provider dashboard:

  - [OpenAI](https://platform.openai.com/settings/organization/limits)
  - [Anthropic](https://console.anthropic.com/)
  - [Google AI](https://aistudio.google.com/)
- Consider self-hosted models via [OpenAI-compatible providers](#openai-compatible-providers) for cost control

## Next Steps

<card-group>
<card icon="material-symbols:chat" title="User Guide" to="/guides/ai/assistant/usage">

Learn how users interact with AI Assistant.

</card>

<card icon="material-symbols:construction" title="Available Tools" to="/guides/ai/assistant/tools">

See what actions the AI can perform.

</card>

<card icon="material-symbols:lightbulb" title="Tips & Best Practices" to="/guides/ai/assistant/tips">

Get the most out of AI Assistant.

</card>

<card icon="material-symbols:security" title="Security" to="/guides/ai/assistant/security">

Access control and data protection.

</card>
</card-group>
