# Source: https://dev.writer.com/connectors/factset.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# FactSet connector

> Connect WRITER Agent to FactSet to access financial data, equity fundamentals, and market analytics

This guide shows you how to configure the [FactSet](https://www.factset.com/) connector for WRITER Agent. After setting up this connector, WRITER Agent can perform operations like accessing global equity fundamentals, earnings data, financial statements, estimates, and industry analytics.

## Set up the FactSet connector

Configure the FactSet connector in [AI Studio](https://app.writer.com/aistudio) under **Connectors & Tools**. The FactSet connector requires organization-managed OAuth authentication with private key JWT authentication method.

<Note>
  The FactSet connector only supports organization-managed OAuth. You must create your own FactSet OAuth application. WRITER-managed OAuth is not available for FactSet.
</Note>

### Create a FactSet OAuth application

Create an OAuth 2.0 application in FactSet:

1. Contact FactSet to enable OAuth 2.0 access for your account
2. Configure your OAuth application with FactSet and grant access to the [required OAuth scopes](#required-oauth-scopes)
3. Generate a private key for JWT authentication
4. Add the Writer redirect URI if required by FactSet
5. Note your client ID and authentication credentials

For detailed instructions, see [FactSet's OAuth 2.0 documentation](https://developer.factset.com/learn/authentication-oauth2).

#### Required OAuth scopes

* `api|content/eventsandtranscripts/v2` - Access events and transcripts
* `api|content/fundamentals` - Access fundamental financial data
* `api|content/estimates` - Access estimates and forecasts

<Note>
  OAuth scopes are fixed per connector and cannot be customized based on enabled tools. When users authorize the FactSet connector, they will grant all the scopes listed above, even if you disable certain tools in AI Studio.
</Note>

### Configure the connector in AI Studio

After creating your FactSet OAuth application:

1. Navigate to **Connectors & Tools** in [AI Studio](https://app.writer.com/aistudio)
2. Select the FactSet connector
3. Select who has access by default (all users or specific teams)
4. Select the connection level: User level (each user authenticates their own account) or org level (shared connection to a single account)
5. Select which tools to enable for your agents
6. Enter your OAuth client ID
7. Upload or configure your private key for JWT authentication
8. Complete the OAuth authorization flow

## Next steps

* [Set up connectors](https://support.writer.com/article/299-setting-up-connectors): Learn how to configure and enable connectors in AI Studio
* [Tool calling guide](/home/tool-calling): Understand how AI agents use tools in conversations
* [Action Agent guide](https://support.writer.com/article/293-how-to-use-action-agent): Learn how to use Action Agent with connected tools
* [MCP gateway overview](/home/mcp-gateway): Learn about Writer's MCP gateway architecture
