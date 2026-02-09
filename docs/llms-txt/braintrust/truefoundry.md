# Source: https://braintrust.dev/docs/integrations/sdk-integrations/truefoundry.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# TrueFoundry

> Export LLM traces from TrueFoundry AI Gateway to Braintrust

[TrueFoundry](https://www.truefoundry.com/) is an AI Gateway that provides a unified interface for accessing multiple AI providers with observability, caching, and rate limiting. TrueFoundry can export LLM traces to Braintrust using OpenTelemetry, providing comprehensive observability for all your AI Gateway interactions.

The integration captures:

* LLM calls (chat completions, agent responses, embeddings)
* Token usage and cost metrics
* Request and response data
* Latency and performance data
* Hierarchical trace trees showing relationships between calls

## Prerequisites

Before configuring the integration, ensure you have:

1. A TrueFoundry account (sign up at [truefoundry.com](https://www.truefoundry.com/))
2. A Braintrust account (sign up at [braintrust.dev](https://www.braintrust.dev/))
3. Your Braintrust API key from [Settings → API Keys](https://www.braintrust.dev/app/settings?page=api-keys)
4. Your Braintrust project ID from your project's configuration page

## Trace with TrueFoundry

TrueFoundry exports traces to Braintrust using OpenTelemetry. Configure the integration through the TrueFoundry dashboard:

<Steps>
  <Step title="Enable OpenTelemetry export">
    In the TrueFoundry dashboard, navigate to **AI Gateway → Controls → OTEL Config** and enable the "Otel Traces Exporter Configuration" toggle.
  </Step>

  <Step title="Configure the Braintrust endpoint">
    Select the **HTTP Configuration** tab and configure these settings:

    * **Traces endpoint**: `https://api.braintrust.dev/otel/v1/traces`
    * **Encoding**: `Proto`
  </Step>

  <Step title="Add authentication headers">
    Add two HTTP headers to authenticate and route traces to your Braintrust project:

    ```
    Authorization: Bearer <YOUR_BRAINTRUST_API_KEY>
    x-bt-parent: project_id:<YOUR_PROJECT_ID>
    ```

    Replace `<YOUR_BRAINTRUST_API_KEY>` with your API key from Braintrust settings, and `<YOUR_PROJECT_ID>` with your project ID.

    <Note>
      The `x-bt-parent` header supports multiple prefixes for organizing traces: `project_id:`, `project_name:`, or `experiment_id:`.
    </Note>
  </Step>

  <Step title="Save the configuration">
    Click **Save** to apply the settings. TrueFoundry will automatically export all subsequent LLM traces to Braintrust.
  </Step>
</Steps>

## View traces in Braintrust

After configuration, all LLM interactions through TrueFoundry AI Gateway appear in the <Icon icon="activity" /> **Logs** page of your Braintrust project. Each trace includes:

* Request parameters and prompts
* Response data and completions
* Token usage and estimated costs
* Latency measurements
* Hierarchical span relationships

## Self-hosted Braintrust

For self-hosted Braintrust deployments, replace the standard endpoint with your custom Braintrust URL:

```
https://your-braintrust-instance.example.com/otel/v1/traces
```

Keep the encoding as `Proto` and use the same authentication headers with your self-hosted instance's API key.

## Resources

* [TrueFoundry documentation](https://truefoundry.com/docs)
* [TrueFoundry AI Gateway](https://truefoundry.com/docs/ai-gateway)
* [OpenTelemetry integration guide](/integrations/sdk-integrations/opentelemetry)
