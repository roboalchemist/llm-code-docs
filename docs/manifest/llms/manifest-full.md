# Manifest Documentation

Source: https://www.manifest.build/docs/llms-full.txt

---

# Cloud vs Local

Source: https://manifest.build/docs/cloud-vs-local

Choose the right mode for your workflow

Manifest runs in two modes: **Cloud** (hosted at app.manifest.build) and **Local** (embedded on your machine). Both share the same features — the difference is where data lives and how auth works.

## Comparison

|                        | Cloud                                             | Local                                              |
| ---------------------- | ------------------------------------------------- | -------------------------------------------------- |
| **Setup**              | Sign up + API key                                 | Zero config                                        |
| **Data storage**       | PostgreSQL (hosted)                               | SQLite on your machine                             |
| **Dashboard**          | app.manifest.build                                | [http://127.0.0.1:2099](http://127.0.0.1:2099)     |
| **Auth**               | Email/password or OAuth (Google, GitHub, Discord) | Auto-login (loopback trust)                        |
| **Multi-device**       | Yes — access from any browser                     | No — localhost only                                |
| **API key**            | Generated in dashboard (`mnfst_...`)              | Auto-generated (`mnfst_local_...`)                 |
| **Email alerts**       | Built-in (platform mail)                          | Requires provider config (Mailgun/Resend/SendGrid) |
| **Telemetry interval** | \~30 seconds                                      | \~10 seconds                                       |
| **Privacy**            | Metadata only (no message content)                | 100% on your machine                               |
| **Cost**               | Free                                              | Free                                               |

## When to use Cloud

* You work across multiple machines.
* You want email alerts without configuring a mail provider.
* You want a managed experience with no local server.

## When to use Local

* Privacy is paramount — no data leaves your machine.
* You don't need multi-device access.
* You prefer zero-config, offline-capable tooling.

## Switching modes

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Switch to cloud
openclaw config set plugins.entries.manifest.config.mode cloud
openclaw config set plugins.entries.manifest.config.apiKey "mnfst_YOUR_KEY"
openclaw gateway restart

# Switch to local
openclaw config set plugins.entries.manifest.config.mode local
openclaw gateway restart
```

<Warning>Switching modes does not migrate data. Cloud and local have separate databases.</Warning>

# Configuration

Source: https://manifest.build/docs/configuration

All settings reference for Manifest

## Plugin settings

Set these via `openclaw config set plugins.entries.manifest.config.<key> <value>`.

| Setting    | Type     | Default                           | Description                                                           |
| ---------- | -------- | --------------------------------- | --------------------------------------------------------------------- |
| `mode`     | `string` | `local`                           | `local`, `cloud`, or `dev`                                            |
| `apiKey`   | `string` | —                                 | OTLP key (`mnfst_...`). Required for cloud. Auto-generated for local. |
| `endpoint` | `string` | `https://app.manifest.build/otlp` | OTLP endpoint. Only used in cloud/dev.                                |
| `port`     | `number` | `2099`                            | Dashboard port (local only).                                          |
| `host`     | `string` | `127.0.0.1`                       | Bind address (local only).                                            |

## Environment variables

<Tabs>
  <Tab title="Cloud">
    For self-hosting the cloud backend:

    | Variable                | Description                                |
    | ----------------------- | ------------------------------------------ |
    | `BETTER_AUTH_SECRET`    | Auth secret for session signing            |
    | `DATABASE_URL`          | PostgreSQL connection string               |
    | `PORT`                  | Server port (default: 3001)                |
    | `BIND_ADDRESS`          | Bind address (default: 0.0.0.0)            |
    | `NODE_ENV`              | `production` or `development`              |
    | `CORS_ORIGIN`           | Allowed CORS origin                        |
    | `API_KEY`               | Internal API key                           |
    | `THROTTLE_TTL`          | Rate limit window in ms (default: 60000)   |
    | `THROTTLE_LIMIT`        | Max requests per window (default: 100)     |
    | `MAILGUN_API_KEY`       | Mailgun API key for email alerts           |
    | `MAILGUN_DOMAIN`        | Mailgun domain                             |
    | `MAILGUN_FROM`          | Sender address for alerts                  |
    | `GOOGLE_CLIENT_ID`      | Google OAuth client ID                     |
    | `GOOGLE_CLIENT_SECRET`  | Google OAuth client secret                 |
    | `GITHUB_CLIENT_ID`      | GitHub OAuth client ID                     |
    | `GITHUB_CLIENT_SECRET`  | GitHub OAuth client secret                 |
    | `DISCORD_CLIENT_ID`     | Discord OAuth client ID                    |
    | `DISCORD_CLIENT_SECRET` | Discord OAuth client secret                |
    | `SEED_DATA`             | Set to `true` to seed demo data on startup |
  </Tab>

  <Tab title="Local">
    No environment variables needed. Local mode runs with zero configuration.

    If self-hosting the backend in local mode, set `MANIFEST_MODE=local`.
  </Tab>
</Tabs>

## Config file locations

<Tabs>
  <Tab title="Cloud">
    All config is managed via environment variables or the dashboard UI. No local config files.
  </Tab>

  <Tab title="Local">
    | Path                               | Description                                 |
    | ---------------------------------- | ------------------------------------------- |
    | `~/.openclaw/manifest/config.json` | API key, auth secret, email provider config |
    | `~/.openclaw/manifest/manifest.db` | SQLite database                             |
    | `~/.openclaw/openclaw.json`        | OpenClaw master config (provider injection) |
  </Tab>
</Tabs>

## Opt-out of analytics

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
MANIFEST_TELEMETRY_OPTOUT=1
```

Or add `"telemetryOptOut": true` to `~/.openclaw/manifest/config.json`.

## Rate limiting

Default: 100 requests per 60-second window.

Configurable via `THROTTLE_TTL` (ms) and `THROTTLE_LIMIT` (count) environment variables (self-hosted only).

# Contributing

Source: https://manifest.build/docs/contributing

Get the development environment up and running

## Tech stack

| Layer    | Technology                          |
| -------- | ----------------------------------- |
| Frontend | SolidJS                             |
| Backend  | NestJS                              |
| Database | sql.js (local) / PostgreSQL (cloud) |
| Auth     | Better Auth                         |
| Build    | Turborepo                           |

## Prerequisites

* Node.js 22.x
* npm 10.x

## Dev setup

<Tabs>
  <Tab title="Cloud">
    <Steps>
      <Step title="Clone and install">
        ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
        git clone https://github.com/mnfst/manifest.git
        cd manifest
        npm install
        ```
      </Step>

      <Step title="Start PostgreSQL">
        ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
        docker run -d --name postgres_db \
          -e POSTGRES_USER=myuser \
          -e POSTGRES_PASSWORD=mypassword \
          -e POSTGRES_DB=mydatabase \
          -p 5432:5432 postgres:16
        ```
      </Step>

      <Step title="Configure environment">
        Copy `.env.example` to `.env` and fill in:

        * `BETTER_AUTH_SECRET` — any random string
        * `DATABASE_URL` — `postgres://myuser:mypassword@localhost:5432/mydatabase`
        * `SEED_DATA=true`
      </Step>

      <Step title="Start the backend">
        ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
        cd packages/backend
        NODE_OPTIONS='-r dotenv/config' npx nest start --watch
        ```
      </Step>

      <Step title="Start the frontend">
        ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
        cd packages/frontend
        npx vite
        ```
      </Step>

      <Step title="Login">
        Use `admin@manifest.build` / `manifest`.
      </Step>
    </Steps>
  </Tab>

  <Tab title="Local">
    <Steps>
      <Step title="Clone and install">
        ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
        git clone https://github.com/mnfst/manifest.git
        cd manifest
        npm install
        ```
      </Step>

      <Step title="Build">
        ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
        npm run build
        ```
      </Step>

      <Step title="Run">
        ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
        MANIFEST_MODE=local node packages/backend/dist/main.js
        ```
      </Step>

      <Step title="Open the dashboard">
        Open [http://127.0.0.1:3001](http://127.0.0.1:3001). No login needed.
      </Step>
    </Steps>
  </Tab>
</Tabs>

## Running tests

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Jest unit tests
npm test --workspace=packages/backend

# Jest e2e tests
npm run test:e2e --workspace=packages/backend

# Vitest frontend tests
npm test --workspace=packages/frontend
```

## Database migrations

Cloud mode only. Local mode uses `synchronize: true` — no migrations needed.

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
cd packages/backend
npm run migration:generate -- src/database/migrations/DescriptiveName
npm run migration:run
```

## Changesets

Every PR needs a changeset. Backend/frontend changes need a `manifest` changeset.

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Add a changeset
npx changeset

# For docs/CI-only changes
npx changeset add --empty
```

## Links

* [GitHub Issues](https://github.com/mnfst/manifest/issues)
* [Discord](https://discord.gg/FepAked3W7)
* [Code of Conduct](https://github.com/mnfst/manifest/blob/main/CODE_OF_CONDUCT.md)

# Install

Source: https://manifest.build/docs/install

Get Manifest running in under a minute

## Prerequisites

<Tabs>
  <Tab title="Cloud">
    * An OpenClaw installation.
    * A Manifest account at [app.manifest.build](https://app.manifest.build).
  </Tab>

  <Tab title="Local">
    * An OpenClaw installation.
    * Node.js >= 20.
    * No account needed.
  </Tab>
</Tabs>

## Install the plugin

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
openclaw plugins install manifest
```

## Configure mode

<Tabs>
  <Tab title="Cloud">
    <Steps>
      <Step title="Sign up">
        Create an account at [app.manifest.build](https://app.manifest.build).
      </Step>

      <Step title="Create an agent">
        Open the Workspace page and create a new agent.
      </Step>

      <Step title="Copy your API key">
        Copy the generated API key (`mnfst_...`).
      </Step>

      <Step title="Configure the plugin">
        ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
        openclaw config set plugins.entries.manifest.config.mode cloud
        openclaw config set plugins.entries.manifest.config.apiKey "mnfst_YOUR_KEY"
        ```
      </Step>
    </Steps>
  </Tab>

  <Tab title="Local">
    No configuration needed. Local mode is the default.

    Optionally change the dashboard port:

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    openclaw config set plugins.entries.manifest.config.port 3000
    ```
  </Tab>
</Tabs>

## Restart the gateway

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
openclaw gateway restart
```

## Verify

<Tabs>
  <Tab title="Cloud">
    Open [app.manifest.build](https://app.manifest.build). Send a message to any agent — it should appear in the dashboard within 30 seconds.
  </Tab>

  <Tab title="Local">
    Open [http://127.0.0.1:2099](http://127.0.0.1:2099). Send a message to any agent — it should appear in the dashboard within 10 seconds.
  </Tab>
</Tabs>

<Info>The gateway batches telemetry every 10–30 seconds. New messages may take a moment to appear.</Info>

# Manifest

Source: https://manifest.build/docs/introduction

Take control of your OpenClaw costs

Manifest is an open-source OpenClaw plugin that routes queries to the most cost-effective model and gives you a real-time dashboard to track tokens, costs, and usage.

## Why Manifest

<CardGroup>
  <Card title="Smart routing" icon="split">
    Scores each query across 23 dimensions and picks the cheapest model that can handle it. Saves up to 90%.
  </Card>

  <Card title="Real-time dashboard" icon="chart-no-axes-combined">
    Track tokens, costs, messages, and model usage at a glance.
  </Card>

  <Card title="Set limits" icon="shield-alert">
    Get notified or automatically block requests when spending exceeds a threshold.
  </Card>
</CardGroup>

## How it works

Manifest intercepts each OpenClaw request, runs a scoring algorithm in under 2 ms, assigns a tier (simple / standard / complex / reasoning), and forwards the query to the matching model. All telemetry is captured via OpenTelemetry and displayed in the dashboard.

## Manifest vs OpenRouter

|                         | Manifest                          | OpenRouter           |
| ----------------------- | --------------------------------- | -------------------- |
| **Open source**         | Yes                               | No                   |
| **Self-hostable**       | Yes                               | No                   |
| **Privacy**             | Metadata only (or 100% local)     | Full request proxied |
| **Routing logic**       | Transparent, 23-dimension scoring | Black box            |
| **Cost**                | Free                              | Per-token markup     |
| **Dashboard**           | Built-in                          | Separate             |
| **Works with OpenClaw** | Native plugin                     | Requires config      |

## Privacy

* **Local mode:** All data stays on your machine. Nothing is sent anywhere.
* **Cloud mode:** Only OpenTelemetry metadata (model name, token counts, latency) is sent — never message content.
* **Opt-out of analytics:** Set `MANIFEST_TELEMETRY_OPTOUT=1` to disable anonymous usage analytics.

## Next step

<Card title="Install Manifest" icon="arrow-down-to-line" href="/install">
  Get Manifest running in under a minute.
</Card>

# Routing

Source: https://manifest.build/docs/routing

How Manifest scores queries and routes them to the cheapest capable model

## What is routing?

Instead of sending every request to the same expensive model, Manifest scores each query and routes it to the cheapest model that can handle it.

* Four tiers: **simple**, **standard**, **complex**, **reasoning**.
* Scoring happens in under 2 ms with zero external calls.

## The four tiers

<CardGroup>
  <Card title="Simple" icon="zap">
    Greetings, definitions, short factual questions. Routed to the cheapest model.
  </Card>

  <Card title="Standard" icon="code">
    General coding help, moderate questions. Good quality at low cost.
  </Card>

  <Card title="Complex" icon="layers">
    Multi-step tasks, large context, code generation. Best quality models.
  </Card>

  <Card title="Reasoning" icon="brain">
    Formal logic, proofs, math, multi-constraint problems. Reasoning-capable models only.
  </Card>
</CardGroup>

## How scoring works

23 dimensions grouped into two categories:

**Keyword-based (13)** — Scans the prompt for patterns like "prove", "write function", "what is", etc.

**Structural (10)** — Analyzes token count, nesting depth, code-to-prose ratio, tool count, conversation depth, etc.

Each dimension has a weight. The weighted sum maps to a tier via threshold boundaries. A confidence score (0–1) indicates how clearly the request fits its tier.

## Session momentum

Manifest remembers the last 5 tier assignments (30-minute TTL).

Short follow-up messages ("yes", "do it") inherit momentum from the conversation, preventing unnecessary tier drops.

## Tier overrides

Certain signals force a minimum tier:

| Signal                      | Minimum tier  |
| --------------------------- | ------------- |
| Tools detected              | **standard**  |
| Large context (>50k tokens) | **complex**   |
| Formal logic keywords       | **reasoning** |

## Response headers

Every routed response includes:

| Header                  | Description                                |
| ----------------------- | ------------------------------------------ |
| `X-Manifest-Tier`       | Assigned tier                              |
| `X-Manifest-Model`      | Actual model used                          |
| `X-Manifest-Provider`   | Provider (anthropic, openai, google, etc.) |
| `X-Manifest-Confidence` | Scoring confidence (0–1)                   |

## Cloud vs Local

<Tabs>
  <Tab title="Cloud">
    Routing is performed server-side. Model mappings are managed by the Manifest team and updated regularly.
  </Tab>

  <Tab title="Local">
    Routing runs on your machine inside the embedded server. The model-to-tier mapping is seeded on first boot and can be customized in the dashboard.
  </Tab>
</Tabs>

# Set limits

Source: https://manifest.build/docs/set-limits

Configure alerts and hard limits to control spending

## What are limits?

Two types of rules you can set per agent:

* **Notify** — Sends an email alert when a threshold is reached.
* **Block** — Returns HTTP 429 and stops requests when the threshold is reached.

## Creating a rule

<Tabs>
  <Tab title="Cloud">
    <Steps>
      <Step title="Open agent settings">
        Open your agent's Settings page in the dashboard.
      </Step>

      <Step title="Add a rule">
        Under "Notification Rules", click **Add Rule**.
      </Step>

      <Step title="Configure the rule">
        Pick a metric (tokens or cost), period (hour / day / week / month), threshold, and action (notify or block).
      </Step>

      <Step title="Save">
        Save. The rule takes effect immediately.
      </Step>
    </Steps>
  </Tab>

  <Tab title="Local">
    <Steps>
      <Step title="Open the dashboard">
        Open [http://127.0.0.1:2099](http://127.0.0.1:2099) and navigate to your agent's settings.
      </Step>

      <Step title="Add a rule">
        Add a rule with metric, period, threshold, and action.
      </Step>

      <Step title="Save">
        Save. The rule takes effect immediately.
      </Step>
    </Steps>
  </Tab>
</Tabs>

## How blocking works

When a "block" rule triggers, the next ingest request returns `429 Too Many Requests` with a message:

```
Limit exceeded: cost usage ($X) exceeds $Y per day
```

The block resets at the start of the next period.

## Email notifications

<Tabs>
  <Tab title="Cloud">
    Emails are sent via the platform's mail provider. Make sure your account email is valid.
  </Tab>

  <Tab title="Local">
    Configure an email provider in `~/.openclaw/manifest/config.json`:

    ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
    {
      "email": {
        "provider": "mailgun",
        "apiKey": "key-...",
        "domain": "mg.example.com",
        "from": "alerts@example.com"
      }
    }
    ```

    Supported providers: Mailgun, Resend, SendGrid. If no provider is configured, email notifications are skipped (block rules still work).
  </Tab>
</Tabs>

## Checking rules

* Rules are evaluated hourly (cron) for notifications, and on every ingest for blocks.
* A notification is sent once per rule per period to avoid spam.

# Track usage

Source: https://manifest.build/docs/track-usage

Understand what data Manifest tracks and how costs are calculated

## Overview dashboard

The dashboard shows:

* **Total messages** — number of LLM calls.
* **Total tokens** — input, output, and cache read tokens.
* **Total cost** — calculated from model pricing and token counts.
* **Messages over time** — chart of LLM calls by period.
* **Cost over time** — chart of spend by period.
* **Model distribution** — breakdown of which models handled requests.

## Metrics captured

| Metric                | Description                              |
| --------------------- | ---------------------------------------- |
| **Messages**          | Number of LLM calls                      |
| **Input tokens**      | Prompt tokens sent                       |
| **Output tokens**     | Completion tokens received               |
| **Cache read tokens** | Tokens served from cache                 |
| **Cost (USD)**        | Calculated from model pricing × tokens   |
| **Duration (ms)**     | Round-trip latency                       |
| **Model**             | Which LLM handled the request            |
| **Routing tier**      | simple / standard / complex / reasoning  |
| **Agent name**        | The OpenClaw agent that sent the request |

## How cost is calculated

Manifest maintains a pricing table for 40+ models (Anthropic, OpenAI, Google, DeepSeek, and more).

```
Cost = input_tokens × input_price + output_tokens × output_price
```

Pricing is refreshed automatically in the background. In local mode, pricing syncs from OpenRouter.

## Message log

Every LLM call is recorded with full metadata. The message log provides:

* Paginated list of all requests.
* Filters by agent, model, and time range.

## Data storage

<Tabs>
  <Tab title="Cloud">
    PostgreSQL hosted at app.manifest.build. Data persists across devices and is accessible from any browser.
  </Tab>

  <Tab title="Local">
    SQLite file at `~/.openclaw/manifest/manifest.db`. Data stays on your machine. The dashboard is only accessible from localhost.
  </Tab>
</Tabs>
