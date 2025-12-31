# Source: https://docs.augmentcode.com/cli/integrations.md

# Integrations and MCP

> Expand Augment's capabilities with external tools and data sources through native integrations and Model Context Protocol (MCP) servers.

export const Command = ({text}) => <span className="font-bold">{text}</span>;

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

<Note>Auggie runs commands and tools automatically. Only use integrations and MCP servers from trusted sources, and be aware of the risks of combining multiple tools with external data sources or production systems.</Note>

## About Integrations and MCP

Auggie can utilize external integrations through native integrations like GitHub, Linear, and Notion and Model Context Protocol (MCP) to access external systems for information and integrate tools to take actions. MCP is an open protocol that provides a standardized way to connect AI models to different data sources and tools.

## Native Integrations

You'll need to configure the integration in Augment for VS Code or JetBrains IDEs. Once configured, the integration will be available for use with Auggie automatically. See a full list and examples for [native agent integrations](/setup-augment/agent-integrations).

### 1. Setup in Augment extension

* **Visual Studio Code**: Click the settings icon in the top right of Augment's chat window or press <Keyboard shortcut="Cmd/Ctrl Shift P" /> and select <Command text="Show Settings Panel" />
* **JetBrains IDEs**: Click the Augment icon in the bottom right of your JetBrains IDE and select <Command text="Tool Settings" />

### 2. Connect the integration

Click "Connect" for the integration you want to set up

<img className="block rounded-xl" src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/integration-settings.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=8e1cb7e476ff72baf79853e1a396061a" alt="Set up integrations in the settings page" data-og-width="1096" width="1096" data-og-height="598" height="598" data-path="images/integration-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/integration-settings.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=6b58b42005ec712d925971f18e71f0df 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/integration-settings.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=b0347aaa6924edd4a61a6ed59e70f84c 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/integration-settings.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=50b67616fb88ab7b1620628cf09c5c40 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/integration-settings.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=66664659b4ca1d32c356fbf0e72b2778 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/integration-settings.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=ccfd90b3fe548564b1c3482f5d4d0e95 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/integration-settings.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=f78ecdd094cea06ca826da1580683efc 2500w" />

You'll be redirected to authorize the integration with the appropriate service. After authorization, the integration will be available for use with Augment Agent.

## MCP Integrations

In addition to native integrations, Auggie can also access external systems through Model Context Protocol (MCP) servers. MCP servers enable Auggie to interact with external tools and services through a standardized protocol, such as accessing databases, running browser automation, sending messages to Slack, or integrating with APIs.

### Configure MCP via settings.json

You can persist MCP servers in the Augment settings file `~/.augment/settings.json`, which will initialize on startup and can be checked with `/mcp-status`.

```json  theme={null}
{
  "mcpServers": {
    "context7": {
      "type": "http",
      "url": "https://mcp.context7.com/mcp",
      "headers": {
        "CONTEXT7_API_KEY": "YOUR_API_KEY"
      }
    },
    "weather": {
      "type": "sse",
      "url": "https://weather-mcp.example.com/v1",
      "headers": {
        "X-API-Key": "your_weather_api_key",
        "Content-Type": "application/json"
      }
    },
    "renderMCP": {
      "type": "http",
      "url": "https://mcp.render.com/mcp",
      "headers": {
        "Authorization": "Bearer <YOUR_API_KEY>"
      }
    },
    "local-tool": {
      "command": "/usr/local/bin/custom-mcp",
      "args": ["--serve", "--port", "3000"],
      "env": { "DEBUG": "true" }
    }
  }
}
```

#### HTTP Transport with Headers

MCP servers using HTTP transport can include a `headers` object for authentication or custom headers:

```json  theme={null}
{
  "mcpServers": {
    "renderMCP": {
      "type": "http",
      "url": "https://mcp.render.com/mcp",
      "headers": {
        "Authorization": "Bearer <YOUR_API_KEY>",
        "X-Custom-Header": "custom-value"
      }
    }
  }
}
```

The `headers` field accepts any valid HTTP headers as key-value pairs.

**Common uses**

* **Authentication** - `Authorization` headers with bearer tokens or API keys
* **Custom parameters** - Server-specific information that doesn't fit into standard request parameters
* **Session management** - `Mcp-Session-Id` header for managing sessions in Streamable HTTP transport

**Considerations**

* **Transport type** - Headers are relevant for HTTP and SSE transports only. Stdio transport uses standard input/output and does not use HTTP headers
* **Server requirements** - Required headers depend on the MCP server implementation
* **Security** - Avoid including sensitive information like API keys directly in configuration files. Consider secure credential management methods

### Manage MCP servers with the Auggie CLI

You can add and inspect MCP servers is via Auggie subcommands, which will persist the configuration to your `~/.augment/settings.json` file:

#### Usage

**Add MCP server:**

```bash  theme={null}
auggie mcp add <name> [options]
```

Writes the server entry to your settings.json with interactive prompts for overwriting existing configurations.

Options:

* `--command <path>` - Executable path (for stdio transport)
* `--args <args>` - Arguments string for command
* `-e, --env <KEY=VAL>` - Environment variable (repeatable)
* `-t, --transport <transport>` - stdio|sse|http (default: "stdio")
* `-u, --url <url>` - URL (required for --transport sse or http)
* `-h, --header <KEY:VAL>` - HTTP header (repeatable, for http transport)
* `-r, --replace` - Overwrite existing entry without prompt
* `--json` - Output JSON

**Add MCP server from JSON:**

```bash  theme={null}
auggie mcp add-json <name> <json>
```

Import an MCP server configuration directly from a JSON string. This is useful when you have a complete server configuration in JSON format and want to add it quickly without specifying individual options.

The JSON string should match the structure used in `settings.json` for MCP server configurations. This command uses the same mechanism as `--mcp-config` but provides a convenient way to add servers directly from the command line.

**List MCP servers:**

```bash  theme={null}
auggie mcp list [options]
```

Lists configured MCP servers (from settings and any active overrides).

Options:

* `--json` - Output JSON format

**Remove MCP server:**

```bash  theme={null}
auggie mcp remove <name> [options]
```

Cleanly removes the named server configuration from settings.json.

Examples:

```bash  theme={null}
# Add a stdio-based MCP server (executable with args and environment)
auggie mcp add context7 \
  --command npx \
  --args "-y @upstash/context7-mcp@latest" \
  --env CONTEXT7_API_KEY=your_key

# Compressed syntax 
auggie mcp add context7 -- npx -y @upstash/context7-mcp

# Add an SSE-based MCP server (Server-Sent Events with URL)
auggie mcp add weather-api \
  --transport sse \
  --url https://weather-mcp.example.com/sse

# Compressed syntax
auggie mcp add weather-api --transport sse https://weather-mcp.example.com/sse

# Add an HTTP-based MCP server with authentication headers
auggie mcp add renderMCP \
  --transport http \
  --url https://mcp.render.com/mcp \
  --header "Authorization:Bearer YOUR_API_TOKEN"

# Add HTTP server with multiple headers
auggie mcp add api-service \
  --transport http \
  --url https://api.example.com/mcp \
  --header "Authorization:Bearer YOUR_TOKEN" \
  --header "X-Custom-Header:custom-value"

# List all configured servers (tabular display with status)
auggie mcp list

# List servers in JSON format for programmatic access
auggie mcp list --json

# Remove a server configuration
auggie mcp remove context7

# Replace existing server without interactive prompt
auggie mcp add context7 --command npx --args "..." --replace

# Add MCP server from JSON configuration (stdio transport)
auggie mcp add-json weather-api '{"type":"stdio","command":"/path/to/weather-cli","args":["--api-key","abc123"],"env":{"CACHE_DIR":"/tmp"}}'

# Add MCP server from JSON configuration (SSE transport)
auggie mcp add-json remote-api '{"type":"sse","url":"https://api.example.com/sse"}'

# Add MCP server from JSON configuration (HTTP transport with headers)
auggie mcp add-json renderMCP '{"type":"http","url":"https://mcp.render.com/mcp","headers":{"Authorization":"Bearer ABC_XYZ_123"}}'
```

### MCP overrides

You can define servers by passing ad‑hoc overrides with `--mcp-config`. The structure is the same as `settings.json`:

```json  theme={null}
// After npm install gitlab-mr-mcp
{
  "mcpServers": {
    "gitlab-mr-mcp": {
      "command": "node",
      "args": ["/path/to/gitlab-mr-mcp/index.js"],
      "env": {
        "MR_MCP_GITLAB_TOKEN": "your_gitlab_token",
        "MR_MCP_GITLAB_HOST": "your_gitlab_host"
      }
    }
  }
}
```
