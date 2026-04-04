# Source: https://docs.bito.ai/other-bito-ai-tools/bito-cli/available-commands.md

# Source: https://docs.bito.ai/ai-code-reviews-in-cli/available-commands.md

# Source: https://docs.bito.ai/ai-code-reviews-in-git/available-commands.md

# Source: https://docs.bito.ai/ai-architect/available-commands.md

# Available commands

Quick reference for CLI commands used to install, configure, and manage [**Bito's AI Architect**](https://docs.bito.ai/ai-architect/overview).

* [**Setup script commands:**](#setup-script-commands) Use these commands to **install AI Architect** and manage its initial service setup and lifecycle.
* [**AI Architect management commands (`bitoarch`):**](#ai-architect-management-commands) Use these commands **after installation** to manage repositories, indexing, configuration, health checks, and MCP operations.

## Setup script commands

Commands used to install AI Architect and manage its initial service setup.

| Command                      | Description                                                                                      |
| ---------------------------- | ------------------------------------------------------------------------------------------------ |
| `./setup.sh`                 | Run interactive setup wizard                                                                     |
| `./setup.sh --help` or `-h`  | Show help message with all available options                                                     |
| `./setup.sh --status`        | Check if services are running                                                                    |
| `./setup.sh --logs`          | View service logs for debugging                                                                  |
| `./setup.sh --stop`          | Stop all services (preserves containers)                                                         |
| `./setup.sh --restart`       | Restart all services without config changes                                                      |
| `./setup.sh --force-restart` | Restart all services and reapply environment variables. Use after updating `.env-bitoarch` file. |
| `./setup.sh --update`        | Force pull latest images based on service-versions.json and restart services                     |
| `./setup.sh --clean`         | Remove all data and services                                                                     |

## AI Architect management commands

Use these `bitoarch` commands to manage AI Architect.

{% hint style="info" %}
**Note:** After [installation of AI Architect](https://docs.bito.ai/ai-architect/install-ai-architect-self-hosted), the `bitoarch` command is available globally.
{% endhint %}

### Core operations

| Command                    | Description                           | Example                                    |
| -------------------------- | ------------------------------------- | ------------------------------------------ |
| `bitoarch index-repos`     | Trigger workspace repository indexing | Simple index without parameters            |
| `bitoarch index-status`    | Check indexing status                 | View progress and state                    |
| `bitoarch pause-indexing`  | Pause ongoing indexing process        | `bitoarch pause-indexing`                  |
| `bitoarch resume-indexing` | Resume paused indexing process        | `bitoarch resume-indexing`                 |
| `bitoarch stop-indexing`   | Stop indexing completely              | `bitoarch stop-indexing`                   |
| `bitoarch index-repo-list` | List all repositories                 | `bitoarch index-repo-list --status active` |
| `bitoarch show-config`     | Show current configuration            | `bitoarch show-config --raw`               |

**Examples:**

```shellscript
# Trigger repository indexing
bitoarch index-repos

# Check indexing status (default summary)
bitoarch index-status

# Full API response for debugging
bitoarch index-status --raw

# Machine-readable filtered JSON
bitoarch index-status --output json

# List all repositories
bitoarch index-repo-list
```

***

### Repository management

| Command                            | Description                    | Example                                       |
| ---------------------------------- | ------------------------------ | --------------------------------------------- |
| `bitoarch add-repo <namespace>`    | Add single repository          | `bitoarch add-repo myorg/myrepo`              |
| `bitoarch remove-repo <namespace>` | Remove repository              | `bitoarch remove-repo myorg/myrepo`           |
| `bitoarch add-repos <file>`        | Load configuration from YAML   | `bitoarch add-repos .bitoarch-config.yaml`    |
| `bitoarch update-repos <file>`     | Update configuration from YAML | `bitoarch update-repos .bitoarch-config.yaml` |
| `bitoarch repo-info <name>`        | Get detailed repository info   | `bitoarch repo-info myrepo --dependencies`    |

**Examples:**

```shellscript
# Add a single repository
bitoarch add-repo myorg/myrepo

# Remove a repository
bitoarch remove-repo myorg/myrepo

# Load multiple repositories from YAML
bitoarch add-repos .bitoarch-config.yaml

# Update configuration
bitoarch update-repos .bitoarch-config.yaml

# Get repository details
bitoarch repo-info myrepo
```

***

### Service operations

| Command           | Description                  | Example                     |
| ----------------- | ---------------------------- | --------------------------- |
| `bitoarch status` | View all services status     | Docker ps-like output       |
| `bitoarch health` | Check health of all services | `bitoarch health --verbose` |
| `bitoarch info`   | Get platform information     | Version, ports, resources   |

**Examples:**

```shellscript
# Check service status (docker ps-like)
bitoarch status

# Health check
bitoarch health

# Detailed health information
bitoarch health --verbose

# Platform information
bitoarch info
```

***

### Configuration

| Command                     | Description                     | Example                                 |
| --------------------------- | ------------------------------- | --------------------------------------- |
| `bitoarch update-api-key`   | Update Bito API key             | Interactive or with `--api-key` flag    |
| `bitoarch update-git-creds` | Update Git provider credentials | Interactive or with flags               |
| `bitoarch rotate-mcp-token` | Rotate MCP access token         | `bitoarch rotate-mcp-token <new-token>` |

**Examples:**

```shellscript
# Update API key (interactive)
bitoarch update-api-key

# Update API key with flag
bitoarch update-api-key --api-key <key> --restart

# Update Git credentials (interactive)
bitoarch update-git-creds

# Update Git credentials with flags
bitoarch update-git-creds --provider github --token <token> --restart

# Rotate MCP token
bitoarch rotate-mcp-token <new-token>
```

***

### MCP operations

| Command                     | Description                  | Example                                        |
| --------------------------- | ---------------------------- | ---------------------------------------------- |
| `bitoarch mcp-test`         | Test MCP connection          | Verify server connectivity                     |
| `bitoarch mcp-tools`        | List available MCP tools     | `bitoarch mcp-tools --details`                 |
| `bitoarch mcp-capabilities` | Show MCP server capabilities | `bitoarch mcp-capabilities --output caps.json` |
| `bitoarch mcp-resources`    | List MCP resources           | View available data sources                    |
| `bitoarch mcp-info`         | Show MCP configuration       | Display URL and token info                     |

**Examples:**

```shellscript
# Test MCP connection
bitoarch mcp-test

# List MCP tools
bitoarch mcp-tools

# Show detailed tool information
bitoarch mcp-tools --details

# Get server capabilities
bitoarch mcp-capabilities

# Save capabilities to file
bitoarch mcp-capabilities --output capabilities.json

# List resources
bitoarch mcp-resources

# Show MCP configuration
bitoarch mcp-info
```

***

### Output options

Add these flags to any command:

| Flag            | Purpose                | Example                |
| --------------- | ---------------------- | ---------------------- |
| `--format json` | JSON output            | For automation/scripts |
| `--raw`         | Show full API response | For debugging          |
| `--output json` | Filtered JSON output   | For `index-status`     |
| `--help`        | Show command help      | Get usage information  |

***

### Common workflows

#### Initial setup

```shellscript
# 1. Check services are running
bitoarch status

# 2. Add repositories
bitoarch add-repos .bitoarch-config.yaml

# 3. Trigger indexing
bitoarch index-repos

# 4. Monitor progress
bitoarch index-status
```

#### Daily operations

```shellscript
# Check health
bitoarch health

# View repositories
bitoarch index-repo-list

# Check index status
bitoarch index-status
```

#### Adding new repositories

```shellscript
# Single repository
bitoarch add-repo myorg/newrepo

# Multiple repositories from file
bitoarch add-repos new-repos.yaml

# Trigger re-indexing
bitoarch index-repos
```

#### Troubleshooting

```shellscript
# Check all services
bitoarch status
bitoarch health --verbose

# View full configuration
bitoarch show-config --raw

# Test MCP connection
bitoarch mcp-test

# Check indexing status with details
bitoarch index-status --raw
```

***

### Getting help

| Command                     | Shows                       |
| --------------------------- | --------------------------- |
| `bitoarch --help`           | Main menu with all commands |
| `bitoarch <command> --help` | Command-specific help       |

**Examples:**

```shellscript
# Main help
bitoarch --help

# Command help
bitoarch index-repos --help
bitoarch add-repo --help
bitoarch mcp-tools --help
```

***

### Environment

Configuration is loaded from `.env-bitoarch` file. Key variables:

* `BITO_API_KEY` - API key for authentication
* `GIT_PROVIDER` - Git provider (github, gitlab, bitbucket)
* `GIT_ACCESS_TOKEN` - Git access token
* `BITO_MCP_ACCESS_TOKEN` - MCP server access token
* `CIS_*_EXTERNAL_PORT` - Service external ports

***

### Version

Check CLI version:

```shellscript
bitoarch --version
```
