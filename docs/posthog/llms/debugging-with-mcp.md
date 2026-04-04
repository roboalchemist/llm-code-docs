# Source: https://posthog.com/docs/logs/debugging-with-mcp.md

# Source: https://posthog.com/docs/error-tracking/debugging-with-mcp.md

# Debugging with MCP - Docs

The [PostHog MCP server](/docs/model-context-protocol.md) exposes function calling tools to any MCP client, enabling AI agents to interact with PostHog's API via the MCP protocol.

When combining our MCP server with error tracking, your AI agents can take actions based on PostHog data which unlocks powerful, autonomous debugging capabilities.

For example, with MCP, your agents can:

-   **Triage issues**: Fetching the latest issues with details like status, frequency, users affected, last seen, etc.
-   **Inspect error details**: Accessing full stack traces, error messages, and relevant metadata.
-   **Explain or reproduce errors**: Identifying failure points and performing root cause analysis using the captured stack trace context.
-   **Debug and create fixes**: Proposing or even generating code fixes based on the error details.
-   **Update issue status**: Marking issues as resolved, archived, suppressed, or pending release directly from your code editor.

All of this happens directly inside the MCP client, like Cursor, Windsurf, or Claude Code, so you can investigate and resolve product issues without ever leaving the code editor.

## See it in action

Use Claude Code to debug and fix errors with PostHog's MCP server

Try these example questions and directives with your MCP-enabled agent:

PostHog AI

```
- Show me my most common errors.
- What's the full stack trace for the most recent error?
- Create a fix and show me how to reproduce the error with the highest severity.
- Which error is causing the most crashes in production?
- Mark this issue as resolved.
- Set all high-severity errors from today to suppressed.
```

## Install the MCP server

To start debugging with PostHog MCP, install the MCP server in your preferred MCP client.

The easiest way is to use the [AI wizard](/docs/ai-engineering/ai-wizard.md), which supports setup for agents like Claude, Cursor, Windsurf, VS Code, and more. The wizard guides you through the installation step by step.

Terminal

PostHog AI

```bash
npx @posthog/wizard mcp add
```

You can also install the MCP server by [configuring it manually](/docs/model-context-protocol.md#manual-install).

Check out the [MCP server documentation](/docs/model-context-protocol.md) for more detailed instructions and information.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better