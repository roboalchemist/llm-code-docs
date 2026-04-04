# Source: https://braintrust.dev/docs/admin/proxy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure the AI Proxy

> Manage AI provider access across your organization

The AI Proxy provides unified access to AI providers through a single interface. Configure provider API keys and custom endpoints at the organization or project level to enable access across playgrounds, experiments, and production deployments.

## Add AI providers

Configure AI provider API keys at the organization or project level. Organization-level providers are available across all projects. Project-level providers override organization-level keys for that specific project, allowing you to isolate API usage, manage separate billing, or use different credentials per project.

You can configure providers in settings or inline from playgrounds and prompt pages for faster setup.

See [Manage organizations](/admin/organizations#configure-ai-providers) for organization-level configuration or [Manage projects](/admin/projects#configure-ai-providers) for project-level configuration.

### Supported providers

Standard providers include:

* OpenAI (GPT-4o, GPT-4o-mini, o4-mini, etc.).
* Anthropic (Claude 4 Sonnet, Claude 3.5 Sonnet, etc.).
* Google (Gemini 2.5 Flash, Gemini 2.5 Pro, etc.).
* AWS Bedrock (Claude, Llama, Mistral models).
* Azure OpenAI Service.
* Third-party providers (Together AI, Fireworks, Groq, Replicate, etc.).

See the full list in [Use the AI Proxy](/deploy/ai-proxy).

## Add custom providers

Braintrust supports custom AI providers, allowing you to integrate any AI model or endpoint into your evaluation and tracing workflows. See [Custom providers](/integrations/ai-providers/custom) for details.

## Load balance across providers

Configure multiple API keys for the same model to automatically load balance requests:

1. Add your primary provider key (e.g., OpenAI).
2. Add Azure OpenAI as a custom provider for the same models.
3. The proxy automatically distributes requests across both.

Load balancing provides:

* Resilience if one provider is down.
* Higher effective rate limits.
* Geographic distribution.

## Set up for self-hosted

For self-hosted deployments, configure proxy URLs:

1. Go to <Icon icon="settings-2" /> **Settings**.
2. Under **Organization**, select **API URL**.
3. Enter your URLs:
   * **API URL**: Main API endpoint.
   * **Proxy URL**: AI Proxy endpoint (usually `<API_URL>/v1/proxy`).
   * **Realtime URL**: Realtime API endpoint.
4. Click **Save**.

Test connectivity with the provided commands.

## Access the proxy

Users and applications access the proxy through configured endpoints:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAI } from "openai";

  const client = new OpenAI({
    baseURL: "https://api.braintrust.dev/v1/proxy",
    apiKey: process.env.BRAINTRUST_API_KEY,
  });

  // Use any configured model
  const response = await client.chat.completions.create({
    model: "claude-sonnet-4-5-20250929",
    messages: [{ role: "user", content: "Hello!" }],
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os
  from openai import OpenAI

  client = OpenAI(
      base_url="https://api.braintrust.dev/v1/proxy",
      api_key=os.getenv("BRAINTRUST_API_KEY"),
  )

  # Use any configured model
  response = client.chat.completions.create(
      model="claude-sonnet-4-5-20250929",
      messages=[{"role": "user", "content": "Hello!"}],
  )
  ```
</CodeGroup>

The proxy automatically uses configured API keys (project-level keys take precedence over organization-level keys) and routes requests to the appropriate provider.

## Monitor proxy usage

Track proxy usage across your organization:

1. Create a project for proxy logs.
2. Enable logging by setting the `x-bt-parent` header when calling the proxy.
3. View logs in the **Logs** page.
4. Create dashboards to track usage, costs, and errors.

See [Use the AI Proxy](/deploy/ai-proxy) for detailed logging configuration.

## Next steps

* [Use the AI Proxy](/deploy/ai-proxy) for detailed usage instructions
* [Manage organizations](/admin/organizations) to configure AI providers
* [Deploy prompts](/deploy/prompts) that use the proxy
* [Monitor deployments](/deploy/monitor) to track proxy usage
