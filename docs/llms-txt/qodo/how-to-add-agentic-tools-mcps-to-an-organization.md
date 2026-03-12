# Source: https://docs.qodo.ai/qodo-documentation/on-prem/ide-plugin/how-to-add-agentic-tools-mcps-to-an-organization.md

# How to Add Agentic Tools (MCPs) to an Organization

Enterprise organizations can govern Agentic Tools (MCPs) usage in Qodo, by using a pre-defined **MCP allow-list**.

### How to use an MCP Allow List

1. Reach out to Qodo to **enable the MCP Allow List** mode.
2. Modify the Helm values file to include the necessary configurations:

```json
secrets:
  org-mcp-json:
    data:
      org_mcp.json: |
        {
          "mcpServers": {}
        }

volumes:
  org-mcp-json:
    secret:
      secretName: org-mcp-json
      useShortName: true

volumeMounts:
  org-mcp-json:
    mountPath: /copilot_proxy/settings/org_mcp.json
    subPath: org_mcp.json
```

**Note:** The JSON file `org_mcp.json` is any JSON file configuration for the MCP you want to add to your organization.

For example:

```json
{
  "mcpServers": {
      "memory": {
        "command": "npx",
        "args": [
          "-y",
          "@modelcontextprotocol/server-memory"
        ]
      }
    }
}
```

3. Run helm upgrade and wait until Qodo backend is up.
4. When the developers in your organization next log in to Qodo, they will be able to view the Organization's approved MCP list.

### Add built-in MCP to the entire organization

If you'd like to **enable the built-in MCP for your entire organization**, add the `approvedBuiltinMcps` section to the MCP JSON:

```json
{
  "mcpServers": {
      "memory": {
        "command": "npx",
        "args": [
          "-y",
          "@modelcontextprotocol/server-memory"
        ]
      }
    },
  "approvedBuiltinMcps": [{
    "name": "Terminal", "enabled": "true"
  }]
}
```
