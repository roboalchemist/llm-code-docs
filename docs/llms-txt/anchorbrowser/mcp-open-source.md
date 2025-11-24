# Source: https://docs.anchorbrowser.io/advanced/mcp-open-source.md

# MCP - Open Source

> Self-host Anchor MCP server with customizable Playwright integration for your specific needs

# Anchor MCP Server (Open Source)

<img src="https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp_logo.png?fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=ec164cf1532c41350abe6f1dd8c52e73" alt="Model Context Protocol" style={{width: "200px", margin: "20px 0"}} data-og-width="485" width="485" data-og-height="514" height="514" data-path="images/mcp_logo.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp_logo.png?w=280&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=a7afe80fed92f76a00fce74df69f33de 280w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp_logo.png?w=560&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=a7a9af2ab0e76f6de65611ff785bd01a 560w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp_logo.png?w=840&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=f954470c4999efd6b83502c4b5463626 840w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp_logo.png?w=1100&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=f288405c55b1fcb1c6d51ce232b468c2 1100w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp_logo.png?w=1650&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=54292ecf2eab83c5e92a2c9a65028bfb 1650w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp_logo.png?w=2500&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=e9432402a01b3bcf1a46bbfffcc5d4f9 2500w" />

A Model Context Protocol (MCP) server that provides browser automation capabilities using [Anchor Browser](https://anchorbrowser.io)'s remote browser service with [Playwright](https://playwright.dev). This server enables LLMs to interact with web pages through Anchor's cloud-based browsers with built-in proxies, stealth features, and advanced capabilities.

This is based on the open source repository at [browsermcp-com/mcp](https://github.com/browsermcp-com/mcp), which extends Microsoft's Playwright MCP with Anchor Browser's cloud infrastructure.

<Info>
  Looking for our hosted MCP service? Check out [MCP - Hosted Version](/advanced/mcp) for zero-setup integration.
</Info>

## When to Use Open Source MCP

Choose the open source version when you need:

* **Custom tool modifications** - Modify browser automation tools for specific use cases
* **Advanced configuration** - Fine-tune browser settings and behaviors
* **Local development** - Test MCP integrations during development
* **Compliance requirements** - Run MCP server within your infrastructure
* **Integration with existing systems** - Connect MCP to your internal tools and workflows

## Key Features

* **Remote Browser Execution**: Uses Anchor Browser's cloud infrastructure instead of local browsers
* **Built-in Proxies**: Automatic residential proxy rotation and geo-targeting
* **Stealth & Anti-Detection**: Advanced browser fingerprinting and anti-bot detection
* **Fast and lightweight**: Uses Playwright's accessibility tree, not pixel-based input
* **LLM-friendly**: No vision models needed, operates purely on structured data
* **Deterministic tool application**: Avoids ambiguity common with screenshot-based approaches
* **Customizable**: Modify and extend tools for your specific needs

## Requirements

* Node.js 18 or newer
* **Anchor Browser API Key** ([Get one here](https://anchorbrowser.io))
* VS Code, Cursor, Windsurf, Claude Desktop, Goose or any other MCP client

## Getting Started

### 1. Clone and Build

Since this is a custom Anchor MCP server, you need to build it locally:

```bash  theme={null}
# Clone the repository
git clone https://github.com/browsermcp-com/mcp.git
cd mcp

# Install dependencies and build
npm install
npm run build
```

### 2. Get Your Anchor API Key

1. Sign up at [anchorbrowser.io](https://anchorbrowser.io)
2. Get your API key from the dashboard
3. Copy your API key (starts with `sk-`)

### 3. Configure MCP Client

#### Cursor

Add to your `~/.cursor/mcp.json`:

```json  theme={null}
{
  "mcpServers": {
    "anchor-browser": {
      "command": "node",
      "args": [
        "/path/to/mcp/cli.js"
      ],
      "env": {
        "ANCHOR_API_KEY": "sk-your-api-key-here"
      }
    }
  }
}
```

#### VS Code

Add to your MCP configuration:

```json  theme={null}
{
  "mcpServers": {
    "anchor-browser": {
      "command": "node",
      "args": [
        "/path/to/mcp/cli.js"
      ],
      "env": {
        "ANCHOR_API_KEY": "sk-your-api-key-here"
      }
    }
  }
}
```

#### Claude Desktop

Add to your `claude_desktop_config.json`:

```json  theme={null}
{
  "mcpServers": {
    "anchor-browser": {
      "command": "node",
      "args": [
        "/path/to/mcp/cli.js"
      ],
      "env": {
        "ANCHOR_API_KEY": "sk-your-api-key-here"
      }
    }
  }
}
```

### 4. Restart Your MCP Client

After updating the configuration, restart your MCP client (Cursor, VS Code, etc.) to load the new server.

## Configuration Options

The Anchor MCP server supports essential configuration options:

```bash  theme={null}
node cli.js --help
```

### Available Options:

* `--host <host>` - Host to bind server to (default: localhost, use 0.0.0.0 for all interfaces)
* `--port <port>` - Port to listen on for HTTP transport (Docker/server mode)

### Example with Options:

```json  theme={null}
{
  "mcpServers": {
    "anchor-browser": {
      "command": "node",
      "args": [
        "/path/to/mcp/cli.js"
      ],
      "env": {
        "ANCHOR_API_KEY": "sk-your-api-key-here"
      }
    }
  }
}
```

## How It Works

1. **Browser Session Creation**: When you use browser tools, the MCP server calls Anchor's API to create a remote browser session
2. **Remote Connection**: Connects to the remote browser via WebSocket using Chrome DevTools Protocol (CDP)
3. **Tool Execution**: All browser automation happens in Anchor's cloud infrastructure
4. **Proxy & Stealth**: Automatic residential proxy rotation and advanced anti-detection features
5. **Session Management**: Each session is isolated and can be viewed live via Anchor's dashboard

## Production & CI/CD Usage

### Self-Hosted in Production

The open source MCP server can be deployed in production environments:

* **Docker Containers** - Run in containerized environments
* **CI/CD Pipelines** - Integrate with Jenkins, GitHub Actions, GitLab CI
* **Serverless Functions** - Deploy as microservices or serverless functions
* **Kubernetes** - Scale horizontally in Kubernetes clusters

### CI/CD Integration Example

```yaml  theme={null}
# GitHub Actions with self-hosted MCP
name: E2E Testing
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    services:
      anchor-mcp:
        image: your-registry/anchor-mcp:latest
        env:
          ANCHOR_API_KEY: ${{ secrets.ANCHOR_API_KEY }}
        ports:
          - 8931:8931
    steps:
      - uses: actions/checkout@v3
      - name: Run AI tests against MCP server
        run: |
          python ai_test_runner.py --mcp-url http://localhost:8931/mcp
```

## Benefits Over Local Browsers

### 🌐 **Global Proxy Network**

* Automatic residential proxy rotation
* Geo-targeting for different regions
* No proxy configuration needed

### 🛡️ **Advanced Stealth**

* Browser fingerprinting protection
* Anti-bot detection bypass
* Real browser environments

### ☁️ **Cloud Infrastructure**

* No local browser dependencies
* Consistent browser versions
* Scalable execution

### 📊 **Monitoring & Debugging**

* Live view of browser sessions
* Session recordings and traces
* Network request logging
