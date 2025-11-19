# Source: https://polar.sh/docs/integrate/mcp.md

# Polar over Model Context Protocol (MCP)

> Extend the capabilities of your AI agents with Polar's MCP Server

<img src="https://mintcdn.com/polar/0Af3hN6-oIM4IHT3/assets/integrate/mcp/mcp.png?fit=max&auto=format&n=0Af3hN6-oIM4IHT3&q=85&s=a6b10fbceef95c6f4a2c9793c9ee60fa" data-og-width="2676" width="2676" data-og-height="1592" height="1592" data-path="assets/integrate/mcp/mcp.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/polar/0Af3hN6-oIM4IHT3/assets/integrate/mcp/mcp.png?w=280&fit=max&auto=format&n=0Af3hN6-oIM4IHT3&q=85&s=abc2ede6a851f182767300a280c00411 280w, https://mintcdn.com/polar/0Af3hN6-oIM4IHT3/assets/integrate/mcp/mcp.png?w=560&fit=max&auto=format&n=0Af3hN6-oIM4IHT3&q=85&s=ef8336debe0ab28deeef4d7d7669368c 560w, https://mintcdn.com/polar/0Af3hN6-oIM4IHT3/assets/integrate/mcp/mcp.png?w=840&fit=max&auto=format&n=0Af3hN6-oIM4IHT3&q=85&s=ad707972479f7eb54511bc2f713bf8c5 840w, https://mintcdn.com/polar/0Af3hN6-oIM4IHT3/assets/integrate/mcp/mcp.png?w=1100&fit=max&auto=format&n=0Af3hN6-oIM4IHT3&q=85&s=6920ec776075a3506ef44e29c12403c7 1100w, https://mintcdn.com/polar/0Af3hN6-oIM4IHT3/assets/integrate/mcp/mcp.png?w=1650&fit=max&auto=format&n=0Af3hN6-oIM4IHT3&q=85&s=12a956db103ce1c7851ee28f1ebb40e1 1650w, https://mintcdn.com/polar/0Af3hN6-oIM4IHT3/assets/integrate/mcp/mcp.png?w=2500&fit=max&auto=format&n=0Af3hN6-oIM4IHT3&q=85&s=2b4774ac779c3531d71c628fbb564d69 2500w" />

Supercharge your AI agents with Polar as a Model Context Protocol (MCP) server.

## What is MCP?

MCP is a protocol for integrating tools with AI agents. It can greatly enhance the capabilities of your AI agents by providing them with real-time data and context.

Polar offers a remote MCP server that you can connect to from most AI clients.

## How does it work?

You need a MCP-capable agent environment to use Polar over MCP. A few of them are Claude Desktop and Cursor.

## Connecting to Polar MCP

When you can specify a MCP URL, use `https://mcp.polar.sh/mcp/polar-mcp`.

If you have to specify a command, use:

```json  theme={null}
{
  "mcpServers": {
    "Polar": {
      "command": "npx",
      "args": ["mcp-remote", "https://mcp.polar.sh/mcp/polar-mcp"]
    }
  }
}
```

### Cursor

In `.cursor/mcp.json`, add:

```
{
  "mcpServers": {
    "Polar": {
      "url": "https://mcp.polar.sh/mcp/polar-mcp"
    }
  }
}
```

### Windsurf

In `mcp_config.json`, add:

```json  theme={null}
{
  "mcpServers": {
    "Polar": {
      "command": "npx",
      "args": ["mcp-remote", "https://mcp.polar.sh/mcp/polar-mcp"]
    }
  }
}
```

### Codex

Add the following to your `~/.codex/config.toml`:

```sh  theme={null}
[mcp_servers.polar]
command = "npx"
args = ["-y", "mcp-remote", "https://mcp.polar.sh/mcp/polar-mcp"]
```

### Claude Code

Run the following command:

```
claude mcp add --transport http "Polar" "https://mcp.polar.sh/mcp/polar-mcp"
```

### ChatGPT

MCP is only available for paid users in beta on ChatGPT web, by enabling Developer Mode.

Once Developer Mode is enabled, go to *Settings* → *Connectors* and add the MCP server using `https://mcp.polar.sh/mcp/polar-mcp`.

### Claude Desktop

Go to *Settings* → *Connectors* and click *Add custom connector*.

Name it "Polar" and add `https://mcp.polar.sh/mcp/polar-mcp` as the server URL.

Save, and click *Connect* to connect to your Polar organization.
