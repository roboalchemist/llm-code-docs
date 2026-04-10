# Source: https://dev.writer.com/connectors/gong.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Gong connector

> Connect WRITER Agent to Gong to access call transcripts, meeting summaries, and sales analytics

This guide shows you how to configure the [Gong](https://www.gong.io/) connector for WRITER Agent. After setting up this connector, WRITER Agent can perform operations like retrieving call transcripts, meeting summaries, performance scorecards, engagement metadata, and conversation analytics.

## Set up the Gong connector

Configure the Gong connector in [AI Studio](https://app.writer.com/aistudio) under **Connectors & Tools**. The Gong connector supports API key authentication or OAuth 2.0 authentication (contact Gong to enable OAuth).

### Obtain Gong API credentials

For API key authentication:

1. Log in to your Gong account
2. Navigate to Settings > API
3. Create a new API key
4. Copy the API key for use in AI Studio
5. Note your Gong tenant URL (for example: `https://yourcompany.api.gong.io`)

For detailed instructions, see [Gong's API authentication guide](https://www.gong.io/docs/api/getting-started/authentication).

### Configure the connector in AI Studio

After obtaining your Gong API credentials:

1. Navigate to **Connectors & Tools** in [AI Studio](https://app.writer.com/aistudio)
2. Select the Gong connector
3. Select who has access by default (all users or specific teams)
4. Select which tools to enable for your agents
5. Enter your API key credentials
6. Enter your Gong tenant URL (for example: `https://yourcompany.api.gong.io`)

## Next steps

* [Set up connectors](https://support.writer.com/article/299-setting-up-connectors): Learn how to configure and enable connectors in AI Studio
* [Tool calling guide](/home/tool-calling): Understand how AI agents use tools in conversations
* [Action Agent guide](https://support.writer.com/article/293-how-to-use-action-agent): Learn how to use Action Agent with connected tools
* [MCP gateway overview](/home/mcp-gateway): Learn about Writer's MCP gateway architecture
