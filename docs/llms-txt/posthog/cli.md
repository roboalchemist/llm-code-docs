# Source: https://posthog.com/docs/error-tracking/upload-source-maps/cli.md

# Source: https://posthog.com/docs/endpoints/cli.md

# Managing Endpoints with the CLI - Docs

**Experimental**

The Endpoints CLI is experimental. Commands are prefixed with `exp` and may change in future releases.

The PostHog CLI provides commands to manage your Endpoints as code. You can version control your endpoint definitions, push changes from local YAML files, and pull existing endpoints for local editing.

## Installation

Terminal

PostHog AI

```bash
# Install the PostHog CLI
npm install -g @posthog/cli
# Authenticate
posthog-cli login
```

**API key scope required**

To manage Endpoints with the CLI, your personal API key needs the `endpoint:write` scope. If your endpoints use variables, you also need the `insight_variable:read` or `insight_variable:write` scope, depending on whether you intend to update endpoints using the CLI. You can create or update your API key in [Personal API Keys](https://us.posthog.com/settings/user-api-keys).

## Commands

### List endpoints

List all endpoints in your project:

Terminal

PostHog AI

```bash
posthog-cli exp endpoints list
```

### Get endpoint details

View details of a specific endpoint:

Terminal

PostHog AI

```bash
posthog-cli exp endpoints get <endpoint-name>
```

### Run an endpoint

Execute an endpoint and see the results:

Terminal

PostHog AI

```bash
# Run a remote endpoint
posthog-cli exp endpoints run <endpoint-name>
# Run from a local YAML file (without creating the endpoint)
posthog-cli exp endpoints run -f my-endpoint.yaml
# Pass variables
posthog-cli exp endpoints run <endpoint-name> --var customer_id=cust_123
# Output as JSON
posthog-cli exp endpoints run <endpoint-name> --json
```

### Open in browser

Open an endpoint in the PostHog UI:

Terminal

PostHog AI

```bash
posthog-cli exp endpoints open <endpoint-name>
```

## Endpoints as code

### Pull endpoints

Download endpoints from PostHog to local YAML files:

Terminal

PostHog AI

```bash
# Pull a specific endpoint
posthog-cli exp endpoints pull my-endpoint
# Pull all endpoints
posthog-cli exp endpoints pull --all
# Pull to a specific directory
posthog-cli exp endpoints pull --all -o ./endpoints/
```

### Push endpoints

Push local YAML files to PostHog:

Terminal

PostHog AI

```bash
# Push a single file
posthog-cli exp endpoints push my-endpoint.yaml
# Push all YAML files in a directory
posthog-cli exp endpoints push ./endpoints/
# Preview changes without applying
posthog-cli exp endpoints push ./endpoints/ --dry-run
```

### Diff endpoints

Compare local files with remote endpoints:

Terminal

PostHog AI

```bash
posthog-cli exp endpoints diff ./endpoints/
```

## YAML format

Endpoints are defined in YAML files:

YAML

PostHog AI

```yaml
name: daily_active_users
description: Count of unique users per day
# Simple HogQL query
query: |
  SELECT
    toDate(timestamp) as date,
    count(DISTINCT distinct_id) as users
  FROM events
  WHERE event = '$pageview'
  GROUP BY date
  ORDER BY date DESC
```

### With variables

YAML

PostHog AI

```yaml
name: events_by_customer
description: Events for a specific customer
query: |
  SELECT event, count() as count
  FROM events
  WHERE properties.customer_id = {variables.customer_id}
  GROUP BY event
variables:
  - name: customer_id
    type: string
    default: "default_customer"
```

### With materialization

YAML

PostHog AI

```yaml
name: hourly_metrics
description: Pre-computed hourly metrics
query: |
  SELECT count() FROM events
materialization:
  enabled: true
  schedule: "1hour"  # Options: 5min, 15min, 30min, 1hour, 2hour, 4hour, 6hour, 12hour, 24hour, 7day, 30day
```

### Complex queries (insights)

For insight-based endpoints, use `query_definition` instead of `query`:

YAML

PostHog AI

```yaml
name: signup_funnel
description: User signup funnel
query_definition:
  kind: FunnelsQuery
  funnelsFilter:
    funnelVizType: steps
  series:
    - kind: EventsNode
      event: "$pageview"
      name: "Page View"
    - kind: EventsNode
      event: "signed_up"
      name: "Signed Up"
```

## Workflow example

Terminal

PostHog AI

```bash
# 1. Pull existing endpoints
posthog-cli exp endpoints pull --all -o ./posthog/endpoints/
# 2. Edit locally, commit to git
git add posthog/endpoints/
git commit -m "feat: add new customer metrics endpoint"
# 3. Preview changes
posthog-cli exp endpoints diff ./posthog/endpoints/
# 4. Push to PostHog
posthog-cli exp endpoints push ./posthog/endpoints/
```

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better