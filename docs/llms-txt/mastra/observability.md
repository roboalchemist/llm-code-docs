# Source: https://mastra.ai/docs/mastra-cloud/observability

# Observability

Cloud provides observability for production applications, giving you insight into how your agents and workflows behave. Observability works whether your application is deployed to Mastra Cloud, running locally, or hosted on your own infrastructure. Any Mastra project can send traces and logs to the platform regardless of where it's running.

For details on configuring observability, see the [Cloud Exporter](https://mastra.ai/docs/observability/tracing/exporters/cloud) docs.

## Traces

Traces are available for both agents and workflows by enabling [observability](https://mastra.ai/docs/observability/tracing/overview) using one of the [supported providers](https://mastra.ai/docs/observability/tracing/overview).

### Agents

With observability enabled, you can view detailed outputs from your agents in the **Traces** section in [Studio](https://mastra.ai/docs/mastra-cloud/studio).

![observability agents](/assets/images/mastra-cloud-observability-agents-a51e3bcac8589ba42fc5bd958a627187.jpg)

Agent traces break a run into clear steps: model calls, tool calls, and intermediate chunks. Each includes timing, inputs, outputs, and errors. Drill into any span to inspect prompts, token usage, and results.

### Workflows

With observability enabled, you can view detailed outputs from your workflows in the **Traces** section in [Studio](https://mastra.ai/docs/mastra-cloud/studio).

![observability workflows](/assets/images/mastra-cloud-observability-workflows-47baf49146575e665e3aad9f1fd65e5f.jpg)

Workflow traces capture each step in the run, including transitions, branching, timing, and any tool calls. Inspect inputs, outputs, and errors for every step to debug long-running or multi-step processes.

## Logs

The **Logs** page in the [project dashboard](https://mastra.ai/docs/mastra-cloud/deployment) displays detailed information for debugging and monitoring your application's behavior.

![Dashboard logs](/assets/images/mastra-cloud-dashboard-logs-85576fde4dda03bba2892bb6134a6ebf.jpg)

Each log entry includes its severity level and a detailed message showing agent, workflow, or storage activity.

## Next steps

- [Logging](https://mastra.ai/docs/observability/logging)
- [Tracing](https://mastra.ai/docs/observability/tracing/overview)