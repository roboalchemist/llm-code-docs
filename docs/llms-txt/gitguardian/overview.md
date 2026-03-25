# Source: https://docs.gitguardian.com/public-monitoring/perimeter/overview.md

# Source: https://docs.gitguardian.com/public-monitoring/explore/overview.md

# Source: https://docs.gitguardian.com/public-monitoring/detect-public-secret-incidents/overview.md

# Source: https://docs.gitguardian.com/platform/analytics/overview.md

# Source: https://docs.gitguardian.com/platform/agent/overview.md

# Source: https://docs.gitguardian.com/internal-monitoring/remediate/remediation-scenarios/overview.md

# Source: https://docs.gitguardian.com/internal-monitoring/prevent/overview.md

# Source: https://docs.gitguardian.com/internal-monitoring/integrate-sources/secrets-managers-integrations/overview.md

# Source: https://docs.gitguardian.com/internal-monitoring/integrate-sources/overview.md

# Source: https://docs.gitguardian.com/ggshield-docs/integrations/overview.md

# Source: https://docs.gitguardian.com/ggmcp-docs/overview.md

# Overview

> Learn what the GitGuardian MCP Server is, what tools it provides, and how it fits into your AI-assisted development workflow.

# GitGuardian MCP Server

:::warning[Beta]
The GitGuardian MCP Server is currently in **beta**. Features and behavior may change as we iterate based on user feedback.
:::

The GitGuardian MCP Server brings secrets security directly into your AI coding assistant. Scan for leaked credentials, manage security incidents, and deploy honeytokens â all without leaving your IDE.

> For full documentation, source code, and installation guides, see the [GitHub repository](https://github.com/GitGuardian/gg-mcp).

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/IuDsDcrUqJk?controls=0&modestbranding=1" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowFullScreen></iframe>

## What is MCP?

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) is an open standard that lets AI assistants interact with external tools and data sources. The GitGuardian MCP server exposes security capabilities as tools your AI agent can call on your behalf.

## Server profile

The GitGuardian MCP Server is available as a **Developer** profile *(beta)*, designed for developers working in IDEs. It provides primarily read-focused tools for scanning, incident review, and guided remediation, with limited write capabilities such as honeytoken generation.

A **SecOps** profile tailored for security teams is being planned, with additional capabilities such as incident management, secret revocation, and automated code fixes.
