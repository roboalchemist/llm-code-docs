# Source: https://docs.gitguardian.com/platform/agent/tools-reference.md

# Source: https://docs.gitguardian.com/ggmcp-docs/tools-reference.md

# Tools reference

> Full list of Developer tools available through the GitGuardian MCP server.

# Tools reference

:::warning[Beta]
The GitGuardian MCP Server is currently in **beta**. Features and behavior may change as we iterate based on user feedback.
:::

The following tools are available in the Developer profile *(beta)*:

| Tool | Description |
|------|-------------|
| **Scan secrets** | Detect leaked credentials in code before commit |
| **List incidents** | View security incidents filtered by severity, status, detector, and more |
| **Get incident** | Retrieve detailed incident information with occurrences |
| **List repo occurrences** | Locate secrets with exact file paths and line numbers |
| **Remediate incidents** | Get step-by-step remediation instructions for detected secrets |
| **Find current source** | Auto-detect the current repository's GitGuardian source ID |
| **List sources** | Browse repositories and integrations monitored by GitGuardian |
| **List detectors** | Explore 500+ available secret detectors |
| **Generate honeytoken** | Create AWS honeytokens with placement recommendations |
| **List honeytokens** | View existing honeytokens |
| **List users / Get member** | Look up workspace members |

## What's next

A **SecOps** profile for security teams is being planned. It will extend the Developer tools with additional capabilities such as incident assignment, status management, custom tags, secret revocation, and automated code fix requests.
