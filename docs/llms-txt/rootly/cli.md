# Source: https://docs.rootly.com/integrations/cli.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# CLI

> Manage Rootly incidents, alerts, services, teams, and on-call schedules from your terminal.

<Warning>
  Early Preview

  The Rootly CLI is currently in **early preview**. Features may change and some functionality may be limited. We welcome feedback and bug reports on [GitHub](https://github.com/rootlyhq/rootly-cli/issues).
</Warning>

The Rootly CLI is a command-line interface for managing Rootly resources directly from your terminal. Built for engineers who prefer working in the terminal, it provides fast access to incidents, alerts, services, teams, and on-call schedules.

## Features

* **Incidents**: Full CRUD operations with filtering by status, severity, and more
* **Alerts**: Create, acknowledge, and resolve alerts with source tracking
* **Services & Teams**: Manage your service catalog and team structure
* **On-Call**: Query schedules, view shifts, and see who is on-call right now
* **Multiple Output Formats**: Table, JSON, YAML, and Markdown
* **TTY-Aware Output**: Table format in terminal, JSON when piped
* **Shell Completions**: Bash, Zsh, Fish, and PowerShell
* **Pagination & Filtering**: Server-side filtering with paginated results

## Installation

### Using Homebrew (macOS/Linux)

```bash  theme={null}
brew install rootlyhq/tap/rootly-cli
```

### Using Go

```bash  theme={null}
go install github.com/rootlyhq/rootly-cli/cmd/rootly@latest
```

### Download Binary

Download the latest release from [GitHub Releases](https://github.com/rootlyhq/rootly-cli/releases).

Available for Linux (amd64/arm64), macOS (Intel/Apple Silicon), and Windows (amd64).

## Quick Start

1. **Set your API key**:
   ```bash  theme={null}
   export ROOTLY_API_TOKEN="your-api-key"
   ```

2. **List your incidents**:
   ```bash  theme={null}
   rootly incidents list
   ```

3. **Get incident details**:
   ```bash  theme={null}
   rootly incidents get INC-123
   ```

## Configuration

Set your API token via environment variable or config file:

```bash  theme={null}
# Environment variable (recommended for CI/scripts)
export ROOTLY_API_TOKEN="your-api-key"
```

Or create a config file at `~/.rootly-cli/config.yaml`:

```yaml  theme={null}
api_token: "your-api-key"
endpoint: "api.rootly.com"  # Optional, defaults to api.rootly.com
```

### Getting an API Key

1. Log in to your Rootly account
2. Navigate to **Settings** > **API Keys**
3. Create a new API key with appropriate permissions

## Commands

### Incidents

```bash  theme={null}
# List incidents
rootly incidents list

# List with filters
rootly incidents list --status=started --severity=critical

# Get incident details
rootly incidents get INC-123

# Create a new incident
rootly incidents create --title="Database outage" --severity=critical

# Update an incident
rootly incidents update INC-123 --status=mitigated

# Delete an incident
rootly incidents delete INC-123
```

### Alerts

```bash  theme={null}
# List alerts
rootly alerts list

# Get alert details
rootly alerts get ALR-123

# Create a new alert
rootly alerts create --summary="High CPU usage" --source=datadog

# Acknowledge an alert
rootly alerts ack ALR-123

# Resolve an alert
rootly alerts resolve ALR-123 --message="Issue fixed"
```

### Services

```bash  theme={null}
# List services
rootly services list

# Get service details
rootly services get api-gateway

# Create a service
rootly services create --name="api-gateway"

# Update a service
rootly services update api-gateway --description="Main API gateway"

# Delete a service
rootly services delete api-gateway
```

### Teams

```bash  theme={null}
# List teams
rootly teams list

# Get team details
rootly teams get engineering

# Create a team
rootly teams create --name="Platform"

# Update a team
rootly teams update engineering --color="#FF5733"

# Delete a team
rootly teams delete engineering
```

### On-Call

```bash  theme={null}
# List on-call schedules
rootly oncall list

# View upcoming shifts (next 7 days)
rootly oncall shifts

# View shifts for next 14 days
rootly oncall shifts --days=14

# See who is on-call right now
rootly oncall who

# Filter shifts by schedule
rootly oncall shifts --schedule="Primary On-Call"
```

## Output Formats

The CLI supports multiple output formats via the `--format` flag:

| Format     | Description                                |
| ---------- | ------------------------------------------ |
| `table`    | Human-readable table (default in terminal) |
| `json`     | JSON output (default when piped)           |
| `yaml`     | YAML output                                |
| `markdown` | Markdown table                             |

```bash  theme={null}
# Table (default in terminal)
rootly incidents list

# JSON (default when piped, or explicit)
rootly incidents list --format=json

# Pipe JSON to jq for processing
rootly incidents list --format=json | jq '.[].title'

# YAML
rootly incidents get INC-123 --format=yaml

# Markdown
rootly incidents list --format=markdown
```

## Pagination & Filtering

```bash  theme={null}
# Pagination
rootly incidents list --limit=50 --page=2

# Filtering
rootly incidents list --status=started --severity=critical
rootly alerts list --source=datadog
rootly services list --name=api

# Sorting
rootly incidents list --sort=created_at --order=desc
```

## Global Flags

| Flag          | Description                                                           |
| ------------- | --------------------------------------------------------------------- |
| `--api-token` | Rootly API token (env: `ROOTLY_API_TOKEN`)                            |
| `--endpoint`  | Rootly API endpoint (default: `api.rootly.com`)                       |
| `--format`    | Output format: `table`, `json`, `yaml`, `markdown` (default: `table`) |
| `--no-color`  | Disable colored output                                                |
| `--help`      | Show help for any command                                             |

## Shell Completions

Generate shell completion scripts for tab-completion support:

```bash  theme={null}
# Bash
rootly completion bash > /etc/bash_completion.d/rootly

# Zsh
rootly completion zsh > "${fpath[1]}/_rootly"

# Fish
rootly completion fish > ~/.config/fish/completions/rootly.fish

# PowerShell
rootly completion powershell > rootly.ps1
```

## Feedback & Support

* **Issues**: [GitHub Issues](https://github.com/rootlyhq/rootly-cli/issues)
* **Source Code**: [GitHub Repository](https://github.com/rootlyhq/rootly-cli)


Built with [Mintlify](https://mintlify.com).