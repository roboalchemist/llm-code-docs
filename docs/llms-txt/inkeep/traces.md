# Source: https://docs.inkeep.com/get-started/traces

# Live Debugger, Traces, and OTEL Telemetry (/get-started/traces)

Set up SigNoz to enable full observability with traces and live debugging capabilities for your agents.



## Overview

The Inkeep Agent Framework provides powerful **traces** and **live debugging** capabilities powered by SigNoz. Setting up SigNoz gives you:

* **Real-time trace visualization** - See exactly how your agents execute step-by-step
* **Live debugging** - Debug agent conversations as they happen
* **Export traces as JSON** - Copy complete traces for offline analysis and debugging
* **Full observability** - Complete OpenTelemetry instrumentation for monitoring
* **Performance insights** - Identify bottlenecks and optimize agent performance

<Image src="/images/live-traces.png" alt="Live traces interface showing real-time agent execution" />

## Setup Options

You can set up SigNoz in two ways:

1. **Cloud Setup**: Use SigNoz Cloud
2. **Local Setup**: Run SigNoz locally using Docker

## Option 1: SigNoz Cloud Setup

<Video src="https://www.youtube.com/watch?v=F8n6427hjUE&t=3s" title="SigNoz Cloud Setup steps" />

### Step 1: Create a SigNoz Cloud Project

1. Sign up at [SigNoz](https://signoz.io/teams/)
2. Create a new project or use an existing one

### Step 2: Save Your SigNoz Credentials

You'll need to collect three pieces of information from your SigNoz dashboard:

1. **API Key**:

   * Navigate to Settings → Workspace Settings → API Keys → New Key
   * Choose any role (Admin, Editor, or Viewer) - Viewer is sufficient for observability
   * Set the expiration field to "No Expiry" to prevent the key from expiring
   * Copy the generated API key

2. **Ingestion Key**:

   * Navigate to Settings → Workspace Settings → Ingestion
   * Set the expiration field to "No Expiry" to prevent the key from expiring
   * Copy the ingestion key

3. **SigNoz URL**:
   * Copy the URL from your browser's address bar
   * It will look like: `https://<your-organization>.signoz.cloud`

<Note>
  By default, the retention period for conversation data and traces is set to **15 days**. To set a longer retention period, navigate to the **General** tab on the **Settings** page in SigNoz.
</Note>

### Step 3: Configure Your Root `.env` File

```bash
# SigNoz
SIGNOZ_URL=https://<your-organization>.signoz.cloud
SIGNOZ_API_KEY=<your-api-key>

OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=https://ingest.us.signoz.cloud:443/v1/traces
OTEL_EXPORTER_OTLP_TRACES_HEADERS="signoz-ingestion-key=<your-ingestion-key>"
```

### Step 4: Verify Cloud Setup

1. Restart your development environment:

   ```bash
   pnpm dev
   ```

2. Generate some traces by interacting with your agents

3. Open your SigNoz cloud dashboard and navigate to "Traces" to see your agent traces

## Option 2: Local SigNoz Setup

### Automated Setup (Recommended)

<Note>
  Run `pnpm setup-dev` first to set up core databases and migrations. `setup-dev:optional` only starts optional services.
</Note>

Run the following from your project root:

```bash
pnpm setup-dev:optional
```

This:

* Clones [`agents-optional-local-dev`](https://github.com/inkeep/agents-optional-local-dev) into `.optional-services/` if not already present
* Starts SigNoz, OTEL Collector, Jaeger, and [Nango](/typescript-sdk/credentials/nango) via Docker Compose
* Registers a SigNoz admin account and creates an API key
* Writes all required env vars to your `.env`

Restart your dev server after setup completes:

```bash
pnpm dev
```

Open SigNoz at `http://localhost:3080` to view traces. Jaeger is available at `http://localhost:16686`.

Use `pnpm optional:status` to check service health, `pnpm optional:stop` to stop optional services, or `pnpm optional:reset` to start fresh.

### Manual Setup

<Video src="https://www.youtube.com/watch?v=DWuL4AeRzAA&t=3s" title="Local SigNoz Setup steps" />

If you prefer manual setup:

#### Prerequisites

* Docker installed on your machine

#### Step 1: Clone the Optional Services Repository

Clone the Inkeep optional local development services repository:

```bash
git clone https://github.com/inkeep/agents-optional-local-dev .optional-services
cd .optional-services
```

#### Step 2: Start SigNoz Services

Run the following command to start SigNoz and related services:

```bash
docker compose --profile signoz up -d
```

This will start:

* SigNoz frontend (accessible at `http://localhost:3080`)
* SigNoz query service
* SigNoz OTEL collector
* ClickHouse database

When you visit `http://localhost:3080`, you can sign up with your desired credentials.

#### Step 3: Configure Environment Variables

In your **root project directory** (e.g., `my-agents`), update your `.env` file:

```bash
# SigNoz Configuration
SIGNOZ_URL=http://localhost:3080
SIGNOZ_API_KEY=your-signoz-api-key

# Local SigNoz OTEL endpoint (port 4318 — the SigNoz collector)
OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=http://localhost:4318/v1/traces
OTEL_SERVICE_NAME=inkeep-agents
```

To get your SigNoz API key:

1. Open SigNoz at `http://localhost:3080`
2. Navigate to Settings → Account Settings → API Keys → New Key
3. Create a new API key or copy an existing one.
   * Choose any role (Admin, Editor, or Viewer) - Viewer is sufficient for observability
   * Set the expiration field to "No Expiry" to prevent the key from expiring

<Note>
  By default, the retention period for conversation data and traces is set to **15 days**. To set a longer retention period, navigate to the **General** tab on the **Settings** page in SigNoz.
</Note>

#### Step 4: Verify Setup

1. Restart your Inkeep agents:

   ```bash
   pnpm dev
   ```

2. Make some requests to your agents to generate traces

3. Open SigNoz at `http://localhost:3080` and navigate to the "Traces" section to see your agent traces

## Viewing Traces and Using the Live Debugger

Once SigNoz is set up, you can access traces and live debugging in two ways:

### 1. Visual Builder Traces Interface

If you're using the Visual Builder:

1. Open your agent project in the Visual Builder
2. Navigate to the **Traces** section
3. You'll see real-time traces of your agent executions
4. Click on any trace to see detailed execution flow and timing

The traces overview shows conversation metrics and recent activity:

<Image src="/images/trace-overview.png" alt="Traces overview dashboard showing conversation metrics and recent activity" />

Click on any conversation to see detailed execution flow:

<Image src="/images/trace-detail.png" alt="Detailed conversation trace showing step-by-step execution and timing" />

<>
  ### Copy Trace for Debugging

  The `Copy Trace` button in the timeline view allows you to export the entire conversation trace as JSON. This is particularly useful for offline analysis and debugging complex flows.

  <Image src="/images/copy-trace.png" alt="Copy Trace button in the timeline view for exporting conversation traces" />

  #### What's Included in the Trace Export

  When you click `Copy Trace`, the system exports a JSON object containing:

  ```json
  {
    "metadata": {
      "conversationId": "unique-conversation-id",
      "traceId": "distributed-trace-id",
      "agentId": "agent-identifier",
      "agentName": "Agent Name",
      "exportedAt": "2025-10-14T12:00:00.000Z"
    },
    "timing": {
      "startTime": "2025-10-14T11:59:00.000Z",
      "endTime": "2025-10-14T12:00:00.000Z",
      "durationMs": 60000
    },
    "timeline": [
      // Array of all activities with complete details:
      // - Agent messages and responses
      // - Tool calls and results
      // - Agent transfers
      // - Artifact information
      // - Execution context
    ]
  }
  ```

  #### How to Use Copy Trace

  1. Navigate to the **Traces** section in the management UI
  2. Open the conversation you want to debug
  3. Click the **Copy Trace** button at the top of the timeline
  4. The complete trace JSON is copied to your clipboard
  5. Paste it into your preferred tool for analysis

  This exported trace contains all the activities shown in the timeline, making it easy to share complete execution context with team members or support.
</>

### 2. SigNoz Dashboard

For detailed analysis and further debugging:

1. Open your SigNoz dashboard (cloud or local)
2. Navigate to **Traces** to see all agent executions
3. Use filters to find specific conversations or agents
4. Click on traces to see:
   * Step-by-step execution details
   * Performance metrics
   * Error information
   * Agent-to-agent communication flows

For more detailed information on using traces, see the [SigNoz Usage guide](/guides/observability/signoz-usage).

## Additional Observability and Evals

👉 For additional observability or a dedicated Evals platform, you can connect to any OTEL-based provider. For example, check out the [Langfuse Usage guide](/guides/observability/langfuse-usage) for end-to-end instructions.

## Next steps

Next, we recommend setting up the Nango credential store for production-ready credential management. See [Credentials](/typescript-sdk/credentials/overview) to get started.
