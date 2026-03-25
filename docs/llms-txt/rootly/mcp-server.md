# Source: https://docs.rootly.com/integrations/mcp-server.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# MCP Server

> Enable incident management within IDE environments like Cursor, Windsurf, and Claude using the Rootly MCP (Model Context Protocol) Server.

## Overview

The Rootly MCP Server enables you to resolve production incidents in under a minute without leaving your IDE. It integrates seamlessly with MCP-compatible editors like Cursor, Windsurf, and Claude, dynamically generating MCP resources from Rootly's OpenAPI specification.

## Features

* **Dynamic Tool Generation**: Automatically creates MCP resources from Rootly's OpenAPI (Swagger) specification
* **Smart Pagination**: Defaults to 10 items per request for incident endpoints to prevent context window overflow
* **API Filtering**: Limits exposed API endpoints for security and performance
* **Intelligent Incident Analysis**: Smart tools that analyze historical incident data
  * **`find_related_incidents`**: Uses TF-IDF similarity analysis to find historically similar incidents
  * **`suggest_solutions`**: Mines past incident resolutions to recommend actionable solutions
* **MCP Resources**: Exposes incident and team data as structured resources for easy AI reference
* **Intelligent Pattern Recognition**: Automatically identifies services, error types, and resolution patterns
* **On-Call Health Integration**: Detects workload health risk in scheduled responders

## Prerequisites

* Python 3.12 or higher (for local installation only)
* `uv` package manager (for local installation only)
* [Rootly API token](https://docs.rootly.com/api-reference/overview#how-to-generate-an-api-key%3F) with appropriate permissions

### API Token Permissions

The MCP server requires a Rootly API token. Choose the appropriate token type based on your needs:

* **Global API Key** (Recommended): Full access to all entities across your Rootly instance. Required for organization-wide visibility across teams, schedules, and incidents.
* **Team API Key**: Team Admin permissions with full read/edit access to entities owned by that team. Suitable for team-specific workflows.
* **Personal API Key**: Inherits the permissions of the user who created it. Works for individual use cases but may have limited visibility.

For full functionality of tools like `get_oncall_handoff_summary`, `get_oncall_shift_metrics`, and organization-wide incident search, a **Global API Key** is recommended.

Generate a token in **Account** > **Manage API keys** > **Generate New API Key**.

## Quick Start

The fastest way to get started is to connect to Rootly's hosted MCP server — no installation required.

### Hosted (Streamable HTTP, recommended)

```json  theme={null}
{
  "mcpServers": {
    "rootly": {
      "url": "https://mcp.rootly.com/mcp",
      "headers": {
        "Authorization": "Bearer <YOUR_ROOTLY_API_TOKEN>"
      }
    }
  }
}
```

### Hosted (SSE, backward compatible)

```json  theme={null}
{
  "mcpServers": {
    "rootly": {
      "url": "https://mcp.rootly.com/sse",
      "headers": {
        "Authorization": "Bearer <YOUR_ROOTLY_API_TOKEN>"
      }
    }
  }
}
```

The hosted option provides:

* Zero installation and maintenance overhead
* Always up-to-date with the latest features
* Managed infrastructure and reliability
* Immediate access without local setup

### Claude Code

For Claude Code, run:

```bash  theme={null}
claude mcp add rootly --transport streamable-http https://mcp.rootly.com/mcp \
  --header "Authorization: Bearer YOUR_ROOTLY_API_TOKEN"

# SSE fallback
claude mcp add rootly-sse --transport sse https://mcp.rootly.com/sse \
  --header "Authorization: Bearer YOUR_ROOTLY_API_TOKEN"
```

### Gemini CLI

Install the extension:

```bash  theme={null}
gemini extensions install https://github.com/Rootly-AI-Labs/Rootly-MCP-server
```

Or configure manually in `~/.gemini/settings.json`:

```json  theme={null}
{
  "mcpServers": {
    "rootly": {
      "command": "uvx",
      "args": ["--from", "rootly-mcp-server", "rootly-mcp-server"],
      "env": {
        "ROOTLY_API_TOKEN": "<YOUR_ROOTLY_API_TOKEN>"
      }
    }
  }
}
```

## Local Installation

If you prefer to run the MCP server locally, configure your editor with one of the options below. The package will be automatically downloaded and installed when you first open your editor.

### With uv

```json  theme={null}
{
  "mcpServers": {
    "rootly": {
      "command": "uv",
      "args": [
        "tool",
        "run",
        "--from",
        "rootly-mcp-server",
        "rootly-mcp-server"
      ],
      "env": {
        "ROOTLY_API_TOKEN": "<YOUR_ROOTLY_API_TOKEN>"
      }
    }
  }
}
```

### With uvx

```json  theme={null}
{
  "mcpServers": {
    "rootly": {
      "command": "uvx",
      "args": [
        "--from",
        "rootly-mcp-server",
        "rootly-mcp-server"
      ],
      "env": {
        "ROOTLY_API_TOKEN": "<YOUR_ROOTLY_API_TOKEN>"
      }
    }
  }
}
```

## Self-Hosted Deployment

For organizations requiring full control over their deployment:

```bash  theme={null}
git clone https://github.com/Rootly-AI-Labs/Rootly-MCP-server
cd Rootly-MCP-server
uv pip install .
```

### Transport Options

Choose one transport per server process:

* **Streamable HTTP** endpoint path: `/mcp`
* **SSE** endpoint path: `/sse`

Example Docker run (Streamable HTTP):

```bash  theme={null}
docker run -p 8000:8000 \
  -e ROOTLY_TRANSPORT=streamable-http \
  -e ROOTLY_API_TOKEN=<YOUR_ROOTLY_API_TOKEN> \
  rootly-mcp-server
```

Example Docker run (SSE):

```bash  theme={null}
docker run -p 8000:8000 \
  -e ROOTLY_TRANSPORT=sse \
  -e ROOTLY_API_TOKEN=<YOUR_ROOTLY_API_TOKEN> \
  rootly-mcp-server
```

This option allows you to:

* Host the MCP server on your own infrastructure
* Customize the server configuration and endpoints
* Ensure compliance with internal security policies
* Control data flow and API access patterns

## On-Call Health Integration

Rootly MCP integrates with [On-Call Health](https://oncallhealth.ai) to detect workload health risk in scheduled responders.

### Setup

Set the `ONCALLHEALTH_API_KEY` environment variable:

```json  theme={null}
{
  "mcpServers": {
    "rootly": {
      "command": "uvx",
      "args": ["rootly-mcp-server"],
      "env": {
        "ROOTLY_API_TOKEN": "your_rootly_token",
        "ONCALLHEALTH_API_KEY": "och_live_your_key"
      }
    }
  }
}
```

### Usage

```
check_oncall_health_risk(
    start_date="2026-02-09",
    end_date="2026-02-15"
)
```

Returns at-risk users who are scheduled, recommended safe replacements, and action summaries.

## Example Tools

### On-Call Shift Metrics

Get on-call shift metrics for any time period, grouped by user, team, or schedule. Includes primary/secondary role tracking, shift counts, hours, and days on-call.

```
get_oncall_shift_metrics(
    start_date="2025-10-01",
    end_date="2025-10-31",
    group_by="user"
)
```

### On-Call Handoff Summary

Complete handoff: current/next on-call plus incidents during shifts.

```python  theme={null}
# All on-call (any timezone)
get_oncall_handoff_summary(
    team_ids="team-1,team-2",
    timezone="America/Los_Angeles"
)

# Regional filter - only show APAC on-call during APAC business hours
get_oncall_handoff_summary(
    timezone="Asia/Tokyo",
    filter_by_region=True
)
```

Regional filtering shows only people on-call during business hours (9am-5pm) in the specified timezone.

### Shift Incidents

Incidents during a time period, with filtering by severity/status/tags.

```python  theme={null}
get_shift_incidents(
    start_time="2025-10-20T09:00:00Z",
    end_time="2025-10-20T17:00:00Z",
    severity="critical",  # optional
    status="resolved",    # optional
    tags="database,api"   # optional
)
```

Returns incidents list plus summary with counts, average resolution time, and grouping.

## Related Documentation

* [API Reference](https://rootly.com/api)
* [API Integration](/integrations/api)
* [Rootly MCP Server on GitHub](https://github.com/Rootly-AI-Labs/Rootly-MCP-server)


Built with [Mintlify](https://mintlify.com).