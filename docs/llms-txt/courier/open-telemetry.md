# Source: https://www.courier.com/docs/external-integrations/observability/open-telemetry.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenTelemetry

> Export Courier logs and metrics to any OpenTelemetry-compatible observability platform.

Export Courier logs and metrics to any OpenTelemetry-compatible (OTel) observability platform by configuring the OpenTelemetry integration in the Courier dashboard. Courier supports both **Basic auth** and **Bearer Token** authorization, so you can connect directly to most providers without an OTel Collector or proxy.

## Setup

<Steps>
  <Step title="Open the OpenTelemetry integration">
    In Courier, go to **Channels** (or **Integrations**) and open the **OpenTelemetry** integration.
  </Step>

  <Step title="Enable the integration">
    Turn the **Enabled** toggle on.
  </Step>

  <Step title="Choose authorization">
    Set **Authorization type** to match your provider:

    * **Basic** — enter your username and password. Used by providers like Grafana Cloud.
    * **Bearer Token** — enter your API key or token. Used by providers that accept bearer tokens.
  </Step>

  <Step title="Set your OTLP endpoint">
    Enter your provider's OTLP endpoint URL in **OTLP endpoint**. For example:

    * Grafana Cloud: `https://otlp-gateway-<region>.grafana.net/otlp`
    * Self-hosted collector: `https://otel-collector.example.com:4318`
  </Step>

  <Step title="Optional: Set paths for metrics and logs">
    If your endpoint uses custom paths, fill in **Metrics path** and **Logs path**. Common defaults are `/v1/metrics` and `/v1/logs`. Leave blank to use the endpoint defaults.
  </Step>

  <Step title="Save">
    Click **Complete**. Courier will begin exporting logs and metrics to your platform.
  </Step>
</Steps>

## Configuration reference

| Field                  | Required          | Description                                               |
| ---------------------- | ----------------- | --------------------------------------------------------- |
| **Enabled**            | —                 | Toggle the integration on or off.                         |
| **Authorization type** | Yes               | **Basic** or **Bearer Token**.                            |
| **Username**           | When using Basic  | Username for Basic auth (e.g. Grafana Cloud Instance ID). |
| **Password**           | When using Basic  | Password for Basic auth (e.g. Grafana Cloud API token).   |
| **Bearer token**       | When using Bearer | API key or token for Bearer auth.                         |
| **OTLP endpoint**      | Yes               | Your provider's OTLP endpoint URL.                        |
| **Metrics path**       | No                | Custom path for metrics (e.g. `/v1/metrics`).             |
| **Logs path**          | No                | Custom path for logs (e.g. `/v1/logs`).                   |

<Tip>
  Use HTTPS and dedicated credentials for the Courier integration so you can rotate or revoke them without affecting other services.
</Tip>

## What gets exported

Courier sends **logs** and **metrics** over the [OTLP](https://opentelemetry.io/docs/specs/otlp/) protocol. For the full list of available metrics (message delivery, automations, account events, etc.), see [Observability](/external-integrations/observability/intro-to-observability#metrics).

***

## Grafana Cloud OTel setup guide

Courier connects directly to Grafana Cloud using Basic auth. No OTel Collector or proxy is required.

### Step 1: Get your credentials

1. Sign in to the [Grafana Cloud Portal](https://grafana.com/auth/sign-in/).
2. Select your stack and click **Configure** on the **OpenTelemetry** tile.
3. Note your **Instance ID** (a numeric value) and your **OTLP endpoint URL** (e.g. `https://otlp-gateway-prod-us-east-0.grafana.net/otlp`).
4. Generate a **Cloud API token** with `metrics:write` and `logs:write` scopes.

### Step 2: Configure Courier

In the Courier dashboard, open the OpenTelemetry integration and enter:

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| **Enabled**            | On                                               |
| **Authorization type** | Basic                                            |
| **Username**           | Your Instance ID                                 |
| **Password**           | Your Cloud API token                             |
| **OTLP endpoint**      | `https://otlp-gateway-<region>.grafana.net/otlp` |
| **Metrics path**       | *(leave blank)*                                  |
| **Logs path**          | *(leave blank)*                                  |

Click **Complete** to save.

### Step 3: Verify

1. In Grafana Cloud, go to **Explore**.
2. Select your **Mimir** data source and filter for `{service_name="courier"}`.
3. Switch to **Loki** to confirm logs are arriving.

Data should appear within a few minutes of enabling the integration.
