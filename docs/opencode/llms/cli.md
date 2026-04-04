# OpenCode CLI Reference

## Default Command

```bash
# Start TUI in current directory
opencode

# Start TUI in specific directory
opencode /path/to/project
```

## TUI Command

```bash
opencode [project]
```

### Flags

- `--continue`, `-c`: Continue last session
- `--session`, `-s`: Session ID to continue
- `--prompt`, `-p`: Prompt to use
- `--model`, `-m`: Model in format provider/model
- `--agent`: Agent to use
- `--port`: Port to listen on
- `--hostname`: Hostname to listen on

### Examples

```bash
# Continue last session
opencode -c

# Use specific model
opencode -m anthropic/claude-sonnet-4-5

# Start with prompt
opencode -p "Explain the codebase"
```

## Agent Commands

### Create Agent

```bash
opencode agent create
```

Interactive wizard to create new agent.

### List Agents

```bash
opencode agent list
```

## Auth Commands

### Login to Provider

```bash
opencode auth login
```

Configure API keys for providers. Stored in `~/.local/share/opencode/auth.json`.

### List Authenticated Providers

```bash
opencode auth list
# or
opencode auth ls
```

### Logout from Provider

```bash
opencode auth logout
```

## GitHub Commands

### Install GitHub Agent

```bash
opencode github install
```

Sets up GitHub Actions workflow for repository automation.

### Run GitHub Agent

```bash
opencode github run
```

Flags:
- `--event`: GitHub mock event
- `--token`: GitHub personal access token

## MCP Commands

### Add MCP Server

```bash
opencode mcp add
```

Interactive wizard for local or remote MCP servers.

### List MCP Servers

```bash
opencode mcp list
# or
opencode mcp ls
```

### Authenticate with OAuth MCP

```bash
# Interactive selection
opencode mcp auth

# Specific server
opencode mcp auth <name>

# List OAuth-capable servers
opencode mcp auth list
# or
opencode mcp auth ls
```

### Logout from MCP

```bash
opencode mcp logout <name>
```

### Debug MCP OAuth

```bash
opencode mcp debug <name>
```

## Models Commands

### List Available Models

```bash
# All models
opencode models

# Models from specific provider
opencode models anthropic

# Refresh cache from models.dev
opencode models --refresh

# Verbose output (includes costs)
opencode models --verbose
```

## Run Command

Non-interactive execution:

```bash
opencode run [message..]
```

### Flags

- `--command`: Command to run
- `--continue`, `-c`: Continue last session
- `--session`, `-s`: Session ID to continue
- `--share`: Share the session
- `--model`, `-m`: Model (provider/model format)
- `--agent`: Agent to use
- `--file`, `-f`: File(s) to attach
- `--format`: Output format (default or json)
- `--title`: Session title
- `--attach`: Attach to running server (e.g., http://localhost:4096)
- `--port`: Local server port

### Examples

```bash
# Quick question
opencode run "Explain async/await in JavaScript"

# With file attachment
opencode run -f config.json "Analyze this config"

# Attach to running server
opencode run --attach http://localhost:4096 "Explain closures"

# JSON output
opencode run --format json "List all functions"
```

## Serve Command

Start headless HTTP server:

```bash
opencode serve
```

Flags:
- `--port`, `-p`: Port to listen on
- `--hostname`: Hostname to listen on

Use with `opencode run --attach` to avoid MCP cold boot times.

## Session Commands

### List Sessions

```bash
opencode session list
```

Flags:
- `--max-count`, `-n`: Limit to N recent sessions
- `--format`: Output format (table or json)

## Stats Command

Show usage statistics:

```bash
opencode stats
```

Flags:
- `--days`: Last N days (default: all time)
- `--tools`: Number of tools to show (default: all)
- `--project`: Filter by project (default: all)

## Export Command

Export session as JSON:

```bash
# Interactive selection
opencode export

# Specific session
opencode export <sessionID>
```

## Import Command

Import session from JSON or share URL:

```bash
# From file
opencode import session.json

# From share URL
opencode import https://opncd.ai/s/abc123
```

## Web Command

Start web interface:

```bash
opencode web
```

Flags:
- `--port`, `-p`: Port to listen on
- `--hostname`: Hostname to listen on

## ACP Command

Start Agent Client Protocol server:

```bash
opencode acp
```

Flags:
- `--cwd`: Working directory
- `--port`: Port to listen on
- `--hostname`: Hostname to listen on

## Uninstall Command

Remove OpenCode and related files:

```bash
opencode uninstall
```

Flags:
- `--keep-config`, `-c`: Keep config files
- `--keep-data`, `-d`: Keep sessions and snapshots
- `--dry-run`: Show what would be removed
- `--force`, `-f`: Skip confirmation

## Upgrade Command

Update to latest or specific version:

```bash
# Latest version
opencode upgrade

# Specific version
opencode upgrade v0.1.48
```

Flags:
- `--method`, `-m`: Installation method (curl, npm, pnpm, bun, brew)

## Global Flags

Available for all commands:

- `--help`, `-h`: Display help
- `--version`, `-v`: Print version
- `--print-logs`: Print logs to stderr
- `--log-level`: Set log level (DEBUG, INFO, WARN, ERROR)

## Environment Variables

### General

- `OPENCODE_AUTO_SHARE`: Auto-share sessions (boolean)
- `OPENCODE_GIT_BASH_PATH`: Git Bash path on Windows
- `OPENCODE_CONFIG`: Config file path
- `OPENCODE_CONFIG_DIR`: Config directory path
- `OPENCODE_CONFIG_CONTENT`: Inline JSON config
- `OPENCODE_DISABLE_AUTOUPDATE`: Disable auto-updates
- `OPENCODE_DISABLE_PRUNE`: Disable old data pruning
- `OPENCODE_DISABLE_TERMINAL_TITLE`: Disable terminal title updates
- `OPENCODE_PERMISSION`: Inline permissions JSON
- `OPENCODE_DISABLE_DEFAULT_PLUGINS`: Disable default plugins
- `OPENCODE_DISABLE_LSP_DOWNLOAD`: Disable LSP auto-downloads
- `OPENCODE_ENABLE_EXPERIMENTAL_MODELS`: Enable experimental models
- `OPENCODE_DISABLE_AUTOCOMPACT`: Disable auto-compaction
- `OPENCODE_CLIENT`: Client identifier (default: "cli")
- `OPENCODE_ENABLE_EXA`: Enable Exa web search

### Experimental

- `OPENCODE_EXPERIMENTAL`: Enable all experimental features
- `OPENCODE_EXPERIMENTAL_ICON_DISCOVERY`: Icon discovery
- `OPENCODE_EXPERIMENTAL_DISABLE_COPY_ON_SELECT`: Disable copy on select
- `OPENCODE_EXPERIMENTAL_BASH_MAX_OUTPUT_LENGTH`: Max bash output length
- `OPENCODE_EXPERIMENTAL_BASH_DEFAULT_TIMEOUT_MS`: Bash timeout (ms)
- `OPENCODE_EXPERIMENTAL_OUTPUT_TOKEN_MAX`: Max output tokens
- `OPENCODE_EXPERIMENTAL_FILEWATCHER`: Enable file watcher
- `OPENCODE_EXPERIMENTAL_OXFMT`: Enable oxfmt formatter
- `OPENCODE_EXPERIMENTAL_LSP_TOOL`: Enable LSP tool

## Examples

```bash
# Complete workflow
opencode auth login               # Configure provider
cd /path/to/project              # Navigate to project
opencode                         # Start TUI
# In TUI: /init                  # Initialize project

# Quick tasks
opencode run "Add error handling to auth.ts"
opencode run -f package.json "Update dependencies"

# Server mode
opencode serve &                 # Start server
opencode run --attach http://localhost:4096 "Review code"

# Session management
opencode session list            # List sessions
opencode export abc123           # Export session
opencode import session.json     # Import session

# Statistics
opencode stats --days 7          # Last 7 days
opencode stats --project myapp   # Specific project
```
