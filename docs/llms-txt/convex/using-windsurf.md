# Source: https://docs.convex.dev/ai/using-windsurf.md

# Using Windsurf with Convex

[Windsurf](https://codeium.com/windsurf), the AI code editor, makes it easy to write and maintain apps built with Convex. Let's walk through how to setup Windsurf for the best possible results with Convex.

## Add Convex Rules[​](#add-convex-rules "Direct link to Add Convex Rules")

Add the following rules file to your project and refer to it directly when prompting for changes:

* [Convex Rules](https://convex.link/convex_rules.txt)

We're constantly working on improving the quality of these rules for Convex by using rigorous evals. You can help by [contributing to our evals repo](https://github.com/get-convex/convex-evals).

## Setup the Convex MCP Server[​](#setup-the-convex-mcp-server "Direct link to Setup the Convex MCP Server")

The Convex CLI comes with a [Convex Model Context Protocol](/ai/convex-mcp-server.md) (MCP) server built in. The Convex MCP server gives your AI coding agent access to the your Convex deployment to query and optimize your project.

To get started with Windsurf, open "Windsurf Settings > Cascade > Model Context Protocol (MCP) Servers", click on "Add Server", click "Add custom server", and add the following configuration for Convex.

```
{
  "mcpServers": {
    "convex": {
      "command": "npx",
      "args": ["-y", "convex@latest", "mcp", "start"]
    }
  }
}
```

After adding the server return to the "Windsurf Settings > Cascade > Model Context Protocol (MCP) Servers" screen an click "Refresh" button for Windsurf to pick up the new server.

Once this is done you should see the Convex tool listed in the servers:

![Chat UI](/assets/images/windsurf_convex_mcp-ed91858fc5df64ae0b900f95b69ae2ad.png)

Now start asking it questions like:

* Evaluate and convex schema and suggest improvements
* What are this app's public endpoints?
* Run the `my_convex_function` query
