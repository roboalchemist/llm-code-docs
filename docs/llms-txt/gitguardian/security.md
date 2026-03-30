# Source: https://docs.gitguardian.com/platform/agent/security.md

# Source: https://docs.gitguardian.com/ggmcp-docs/security.md

# Security

> Security model of the GitGuardian MCP server â read-only permissions, server-side scanning, and secret redaction.

# Security

:::warning[Beta]
The GitGuardian MCP Server is currently in **beta**. Features and behavior may change as we iterate based on user feedback.
:::

Most tools operate with **read-only permissions** by design, limiting the agent's capabilities to safe, non-destructive operations such as scanning, listing incidents, and browsing detectors. A few tools â such as honeytoken generation â perform write operations but remain scoped to low-risk actions.

Secret values are never sent to the AI model â scanning is performed server-side via the GitGuardian API.
