# Source: https://docs.socket.dev/docs/guide-to-socket-mcp.md

# Guide to Socket MCP

A Model Context Protocol (MCP) server for Socket integration, allowing AI assistants to efficiently check dependency vulnerability scores and security information.

## ✨ Features

* 🔍 **Dependency Security Scanning** - Get comprehensive security scores for npm, PyPI, and other package ecosystems
* 🌐 **Public Hosted Service** - Use our public server at `https://mcp.socket.dev/` with no setup required
* 🚀 **Multiple Deployment Options** - Run locally via stdio, HTTP, or use our service
* 🤖 **AI Assistant Integration** - Works seamlessly with Claude, VS Code Copilot, Cursor, and other MCP clients
* 📊 **Batch Processing** - Check multiple dependencies in a single request
* 🔒 **No Authentication Required** - Public server requires no API keys or registration

## Installation

You can use Socket MCP either by using our [remote endpoint](remote-socket-mcp) or by deploying it [locally](local-socket-mcp) on your machine.

## Tools exposed by the Socket MCP Server

### depscore

The `depscore` tool allows AI assistants to query the Socket API for dependency scoring information. It provides comprehensive security and quality metrics for packages across different ecosystems.

**Parameters:**

| Parameter              | Type   | Required | Default     | Description                                      |
| ---------------------- | ------ | -------- | ----------- | ------------------------------------------------ |
| `packages`             | Array  | ✅ Yes    | -           | Array of package objects to analyze              |
| `packages[].ecosystem` | String | No       | `"npm"`     | Package ecosystem (`npm`, `pypi`, `cargo`, etc.) |
| `packages[].depname`   | String | ✅ Yes    | -           | Name of the dependency/package                   |
| `packages[].version`   | String | No       | `"unknown"` | Version of the dependency                        |

**Example Usage:**

```json
{
  "packages": [
    {
      "ecosystem": "npm",
      "depname": "express",
      "version": "4.18.2"
    },
    {
      "ecosystem": "pypi",
      "depname": "fastapi",
      "version": "0.100.0"
    }
  ]
}
```

**Sample Response:**

```
pkg:npm/express@4.18.2: supply_chain: 1.0, quality: 0.9, maintenance: 1.0, vulnerability: 1.0, license: 1.0
pkg:pypi/fastapi@0.100.0: supply_chain: 1.0, quality: 0.95, maintenance: 0.98, vulnerability: 1.0, license: 1.0
```

<br />

### How to Use the Socket MCP Server

1. **Ask your AI assistant** to check dependencies:
   * "Check the security score for express version 4.18.2"
   * "Analyze the security of my package.json dependencies"
   * "What are the vulnerability scores for react, lodash, and axios?"

2. **Get comprehensive security insights** including supply chain, quality, maintenance, vulnerability, and license scores.

### Adjust tool usage with custom rules

You can further customize how the Socket MCP server interacts with your AI assistant by modifying your client rules. The rules are usually a markdown file and its location depends on the AI assistant you are using.

| MCP Client          | Rules File Location               |
| ------------------- | --------------------------------- |
| Claude Desktop/Code | `CLAUDE.md`                       |
| VSCode Copilot      | `.github/copilot-instructions.md` |
| Cursor              | `.cursor/rules`                   |

Rules that can be added to the client rules file include the following:

```md
Always check dependency scores with the depscore tool when you add a new dependency. If the score is low, consider using an alternative library or writing the code yourself. If you are unsure about the score, ask for a review from someone with more experience. When checking dependencies, make sure to also check the imports not just the pyproject.toml/package.json/dependency file.
```

You can adjust the rules to fit your needs. For example, you can add rules to include specific manifest files, or guide the AI assistant on how to handle low scores. The rules are flexible and can be tailored to your workflow.