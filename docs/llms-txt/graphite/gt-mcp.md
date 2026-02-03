# Source: https://graphite-58cc94ce.mintlify.dev/docs/gt-mcp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://graphite-58cc94ce.mintlify.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# GT MCP

> Use the Graphite CLI with AI agents through Model Context Protocol

<Note>
  GT MCP is currently in beta and some workflows may not be fully supported.
</Note>

## Overview

GT MCP allows AI agents to automatically create stacked PRs, breaking down large AI-generated changes into smaller, reviewable stacked pull requests.

* With large AI-generated diffs, stacking is more essential than ever. Just like reviewing large human PRs, reviewing massive AI-generated diffs can be overwhelming, and makes it hard to understand what changes your agent has made.
* Stacking breaks AI output into clear, sequential chunks, so you can understand what's changing and why—earlier, faster, and in order. It helps your agent reason through changes chronologically, validating each step as it goes.

## Installation

GT MCP is built into the Graphite CLI. Update your CLI version to 1.6.7 to get access:

**Homebrew**

```bash  theme={null}
brew update && brew upgrade withgraphite/tap/graphite
```

**npm**

```bash  theme={null}
npm install -g @withgraphite/graphite-cli@stable
```

## Setup

### Claude Code

```bash Terminal theme={null}
claude mcp add graphite gt mcp
```

### Cursor IDE

Open Cursor Settings > Tools & Integrations > Add Custom MCP

```json  theme={null}
{
  "mcpServers": {
    "graphite": {
      "command": "gt",
      "args": ["mcp"]
    }
  }
}
```
