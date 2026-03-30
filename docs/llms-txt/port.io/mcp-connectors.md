# Source: https://docs.port.io/ai-interfaces/mcp-connectors.md

# MCP connectors

MCP Connectors turn Port into a unified MCP gateway, routing requests from developers and AI agents to external MCP servers while applying Port's governance, RBAC, and audit controls. Platform engineers configure which MCP servers are available and which tools are exposed. Developers and AI agents access everything through a single interface.

## Why MCP connectors?[â](#why-mcp-connectors "Direct link to Why MCP connectors?")

Organizations building AI agents need access to tools beyond Port's native integrations. For example, internal documentation, custom systems, third-party platforms. Without MCP Connectors, teams either run parallel MCP systems (creating confusion) or build their own gateway infrastructure (recreating governance from scratch).

MCP Connectors solve three critical challenges:

* **Unified developer experience**: Connect once to Port's MCP gateway instead of managing multiple separate integrations. Developers access Port's native tools and all approved external MCPs through one interface.

* **Governance and control**: Platform engineers choose which MCPs are approved, which tools are exposed, and who can access them. Complete audit trails and RBAC enforcement apply to all tool invocations.

* **Holistic data access**: Port AI uses the [Context Lake](/ai-interfaces/context-lake.md) for structured organizational data and MCP Connectors for ephemeral or time-series data that doesn't belong in your data model. Refer to the following [article](https://www.port.io/blog/why-ai-agents-need-a-context-lake) to learn more about why agents need both types of data.

## Setting up MCP connectors[â](#setting-up-mcp-connectors "Direct link to Setting up MCP connectors")

Admins configure which MCP connectors are available organization-wide and control which tools each connector exposes.

### Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* Admin role in Port.
* Account credentials for the external tool you want to connect.

### Add a connector[â](#add-a-connector "Direct link to Add a connector")

1. Go to the [data sources](https://app.getport.io/settings/data-sources) page of your portal.

2. Click on the `+ Data source` in the top-right corner.

3. Select the **MCP Servers** tab.

4. Choose from the available MCP servers (like Notion, Linear, Slack, GitLab, etc) or select **Custom Server** to add your own.

5. Fill in the connector details:

   <!-- -->

   * **Name** (required): A recognizable name for developers and AI agents.
   * **Description**: When this MCP should be used and for which use cases. This helps AI agents determine when to use this connector.
   * **URL** (required): The remote MCP server endpoint.
   * **Icon**: Select an icon to visually identify the connector.
   * **Team**: Assign ownership to a specific team.
   * **Headers**: Custom headers to include with requests (e.g., for API key authentication).

6. Click **Connect** and complete the authentication flow if required.

7. Under **Allowed Tools**, select which tools to expose to your organization using `+ Add Tool`. Only the tools you add will be visible to users. **Consider carefully before enabling write or delete capabilities** - users and AI agents will be able to perform these actions based on their permissions in the external tool.

8. Click `Publish` to make the connector available to users.

**Advanced OAuth settings**

For MCP servers that require manual OAuth configuration, you can expand the **Advanced OAuth Settings** section and provide:

* **OAuth Client ID** and **OAuth Client Secret**: From the OAuth application you created in the external service.
* **OAuth Scope**: The permissions to request during authentication.

MCP connectors can also be added from the MCP connector catalog page. When adding from the catalog, an additional property is available:

**Expose Port Connector**: Determines whether this entity is used as an active MCP connector. When enabled, the connector's tools are available to users through the AI assistant and Port MCP server. When disabled, the entity exists in the catalog but is not used as an MCP connector.

### Supported server types[â](#supported-server-types "Direct link to Supported server types")

Port supports several types of remote MCP servers. All require **Name** and **URL**. Additional configuration depends on the authentication method:

* **Dynamic client registration** (e.g., Notion, Slack): Servers that support [OAuth 2.0 Dynamic Client Registration](https://datatracker.ietf.org/doc/html/rfc7591). Port automatically registers as an OAuth client - no additional configuration required.

* **Manual client registration** (e.g., GitHub, GitLab): Servers that require you to create an OAuth application first. Configure **OAuth Client ID**, **OAuth Client Secret**, and optionally **OAuth Scope** under Advanced OAuth Settings.

* **API-based authentication**: Servers that use API keys or tokens. Add authentication credentials via **Headers** (e.g., `Authorization: Bearer <token>`).

* **No authentication** (e.g., GitMCP): Publicly accessible servers - no additional configuration required.

### Reference organization secrets[â](#reference-organization-secrets "Direct link to Reference organization secrets")

When configuring authentication (via headers or Advanced OAuth Settings), you can reference your organization's secrets using the following syntax:

```
{{ .secrets["YOUR_SECRET_KEY"] }}
```

**In headers:**

```
{ "Authorization": "{{ .secrets[\"YOUR_SECRET_KEY\"] }}" }
```

**In Advanced OAuth Settings inputs:**

Use the same syntax in the **OAuth Client ID** and **OAuth Client Secret** fields to reference stored secrets:

```
{{ .secrets["YOUR_SECRET_KEY"] }}
```

## Authenticate to connectors[â](#authenticate-to-connectors "Direct link to Authenticate to connectors")

Once your admin has configured MCP connectors, you need to authenticate your personal account to use them.

### From the MCP Servers menu[â](#from-the-mcp-servers-menu "Direct link to From the MCP Servers menu")

1. Click your **avatar** in the top-right corner of Port.
2. Select **MCP Servers**.
3. In the modal, select the **MCP External** tab.
4. You will see the MCP servers your admin has made available.
5. Click **Connect** on one and complete the OAuth authentication flow.
6. The MCP server is now available in all Port AI interfaces.

### From Port AI assistant[â](#from-port-ai-assistant "Direct link to From Port AI assistant")

1. Open the Port AI chat interface.
2. Click the **+** button to see available MCP servers.
3. Under **Need to Connect**, you will see servers that require authentication.
4. Click on one to initiate authentication.
5. Complete the OAuth flow.
6. After authenticating, the server appears under **Connectors** with the number of enabled tools (e.g., "9 of 10").

### Manage your tools[â](#manage-your-tools "Direct link to Manage your tools")

After authenticating, you can toggle which tools are active for your account:

1. In the Port AI chat, click the **+** button.
2. Under **Connectors**, click the arrow next to an authenticated server.
3. Toggle individual tools on or off based on your needs.

You can only toggle tools that your admin has enabled. Tools not added by the admin will not appear.

## Using MCP connectors[â](#using-mcp-connectors "Direct link to Using MCP connectors")

After authenticating, you can use natural language to interact with external tools through any Port AI interface.

**Example queries:**

* "Search Notion for our API authentication documentation"
* "Find the deployment runbook in Confluence"
* "Show me open Jira tickets for the payments service"
* "What alerts fired in the last hour?"

### IDE access[â](#ide-access "Direct link to IDE access")

If you've connected your IDE to [Port's MCP server](/ai-interfaces/port-mcp-server/overview-and-installation.md#installing-port-mcp), your authenticated MCP connectors are automatically available alongside Port's native tools.

## Security and permissions[â](#security-and-permissions "Direct link to Security and permissions")

* **Per-user authentication**: Each user authenticates with their own account. Data access respects individual permissions in the external tool.
* **RBAC enforcement**: Port's role-based access controls apply to all MCP connector access.
* **Audit logging**: All tool invocations are logged as part of [AI invocations](/ai-interfaces/port-ai/overview.md#ai-invocations).

For more details, see [AI Security and Data Controls](/ai-interfaces/port-ai/security-and-data-controls.md).

## Limitations[â](#limitations "Direct link to Limitations")

* **Self-hosted MCP servers**: Only remote MCP servers are supported. Self-hosted MCP servers cannot be connected as MCP connectors.
* **AI Agents**: MCP connector tools are not available for [AI Agents](/ai-interfaces/ai-agents/overview.md) automated workflows.

## FAQs[â](#faqs "Direct link to FAQs")

**Who can add MCP connectors?**

By default, only admins can add and configure MCP connectors. Organizations can change this by editing the MCP server blueprint permissions or by creating a [self-service action](/actions-and-automations/create-self-service-experiences/.md).

**Why don't I see any connectors available?**

Your organization admin needs to add connectors first. Contact your platform team to request the tools you need.

**What happens if my authentication expires?**

Port automatically refreshes OAuth tokens where supported. If refresh fails or isn't available, you will be prompted to re-authenticate.
