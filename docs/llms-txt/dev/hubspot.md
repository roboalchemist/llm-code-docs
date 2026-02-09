# Source: https://dev.writer.com/connectors/hubspot.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# HubSpot connector

> Connect WRITER Agent to HubSpot to access CRM data, contacts, deals, and pipeline insights

This guide shows you how to configure the [HubSpot](https://www.hubspot.com/) connector for WRITER Agent. After setting up this connector, WRITER Agent can perform operations like retrieving and searching CRM records including contacts, companies, deals, tickets, engagements, and notes.

<Note>
  The HubSpot connector provides read-only access to CRM data. It does not support creating or updating records.
</Note>

## Set up the HubSpot connector

Configure the HubSpot connector in [AI Studio](https://app.writer.com/aistudio) under **Connectors & Tools**. The HubSpot connector requires organization-managed OAuth authentication.

<Note>
  The HubSpot connector only supports organization-managed OAuth. You must create your own HubSpot OAuth application. WRITER-managed OAuth is not available for HubSpot.
</Note>

### Create a HubSpot OAuth application

Create an OAuth 2.0 application in HubSpot:

1. Navigate to your [HubSpot developer account](https://developers.hubspot.com/)
2. Create a new app or select an existing app
3. Configure OAuth settings with the [required scopes](#required-oauth-scopes)
4. Add the Writer redirect URI to Redirect URLs:
   ```
   https://app.writer.com/mcp/oauth/callback
   ```
5. Copy the client ID and client secret

For detailed instructions, see [HubSpot's OAuth documentation](https://developers.hubspot.com/docs/api/oauth).

#### Required OAuth scopes

* `oauth` - Base OAuth access
* `crm.objects.tickets.read` - Read ticket data
* `crm.objects.users.read` - Read user information
* `crm.objects.products.read` - Read product catalog
* `crm.objects.line_items.read` - Read line item details
* `crm.objects.carts.read` - Read shopping cart data
* `crm.objects.subscriptions.read` - Read subscription information
* `crm.objects.owners.read` - Read object ownership data
* `crm.objects.orders.read` - Read order information
* `crm.objects.invoices.read` - Read invoice data
* `crm.objects.quotes.read` - Read quote information

<Note>
  OAuth scopes are fixed per connector and cannot be customized based on enabled tools. When users authorize the HubSpot connector, they will grant all the scopes listed above, even if you disable certain tools in AI Studio.
</Note>

### Configure the connector in AI Studio

After creating your HubSpot OAuth application:

1. Navigate to **Connectors & Tools** in [AI Studio](https://app.writer.com/aistudio)
2. Select the HubSpot connector
3. Select who has access by default (all users or specific teams)
4. Select the connection level: User level (each user authenticates their own account) or org level (shared connection to a single account)
5. Select which tools to enable for your agents
6. Enter your OAuth client ID and client secret
7. Complete the OAuth authorization flow

## Next steps

* [Set up connectors](https://support.writer.com/article/299-setting-up-connectors): Learn how to configure and enable connectors in AI Studio
* [Tool calling guide](/home/tool-calling): Understand how AI agents use tools in conversations
* [Action Agent guide](https://support.writer.com/article/293-how-to-use-action-agent): Learn how to use Action Agent with connected tools
* [MCP gateway overview](/home/mcp-gateway): Learn about Writer's MCP gateway architecture
