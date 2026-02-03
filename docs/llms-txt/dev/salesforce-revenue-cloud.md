# Source: https://dev.writer.com/connectors/salesforce-revenue-cloud.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Salesforce Revenue Cloud connector

> Connect WRITER Agent to Salesforce Revenue Cloud to manage quotes, orders, and asset lifecycle

This guide shows you how to configure the [Salesforce Revenue Cloud](https://www.salesforce.com/sales/revenue-lifecycle-management/) connector for WRITER Agent. After setting up this connector, WRITER Agent can perform operations like managing quotes and orders through Revenue Lifecycle Management (RLM), configuring product nodes and instances, and handling asset lifecycle actions including renewals, amendments, and cancellations.

<Warning>
  Writer restricts access to the Salesforce Revenue Cloud connector. Contact your assigned Writer Customer Success Manager (CSM) to request access.
</Warning>

<Warning>
  Salesforce MCP connectors are only available for Salesforce Sandbox or Developer Edition accounts.
</Warning>

## Set up the Salesforce Revenue Cloud connector

Configure the Salesforce Revenue Cloud connector in [AI Studio](https://app.writer.com/aistudio) under **Connectors & Tools**. The Salesforce Revenue Cloud connector requires organization-managed OAuth authentication.

<Note>
  The Salesforce Revenue Cloud connector only supports organization-managed OAuth. You must create your own Salesforce External Client App. WRITER-managed OAuth is not available for Salesforce.
</Note>

### Create a Salesforce OAuth external client app

Create an OAuth 2.0 application in Salesforce:

1. From **Salesforce Setup**, navigate to **External Client App Manager**
2. Select **New External Client App**
3. Enter the basic information (app name, API name, contact email)
4. Expand **API (Enable OAuth Settings)** and select **Enable OAuth Settings**
5. Add the Writer redirect URI to **Callback URL**:
   ```
   https://app.writer.com/mcp/oauth/callback
   ```
6. Under **OAuth Scopes**, add the [required scopes](#oauth-scopes)
7. Under **Flow Enablement**, check **Enable Authorization Code and Credentials Flow**
8. Under **Security**, check the following options:
   * Require secret for Web Server Flow
   * Require secret for Refresh Token Flow
   * Require Proof Key for Code Exchange (PKCE) extension for Supported Authorization Flows
   * Issue JSON Web Token (JWT)-based access tokens for named users
9. Select **Create** to save the External Client App
10. [Update Salesforce User Interface settings](#enable-the-mcp-service) to enable the MCP service
11. [Retrieve your consumer key and secret](#retrieve-your-consumer-key-and-secret) for use in [AI Studio](#configure-the-connector-in-ai-studio)

For detailed instructions, see Salesforce documentation on [External Client Apps](https://help.salesforce.com/s/articleView?id=sf.external_client_apps.htm\&type=5).

#### OAuth scopes

##### **Required**

* `api` (Manage user data via APIs) - Salesforce REST API access for Revenue Cloud operations
* `sfap_api` (Access the Salesforce API Platform) - Grants access to Salesforce-hosted platform APIs for Revenue Lifecycle Management
* `refresh_token, offline_access` (Perform requests at any time) - Allows the connector to refresh expired access tokens

##### **Recommended**

* `full` (Full access) - Recommended for Sandbox environments

#### Enable the MCP service

Enable the MCP service in Salesforce to allow MCP connector access:

1. From **Salesforce Setup**, navigate to **User Interface**
2. Under **Setup**, check **Enable MCP Service (Beta)**
3. Select **Save**

#### Retrieve your consumer key and secret

Retrieve the credentials for AI Studio:

1. In **Salesforce Setup**, navigate to **External Client App Manager**
2. Select the External Client App [you created](#create-a-salesforce-oauth-external-client-app)
3. Go to the **Settings** tab and expand **OAuth Settings**
4. Copy the **Consumer Key** (client ID) and **Consumer Secret** (client secret)

### Configure the connector in AI Studio

After creating your Salesforce External Client App and enabling the MCP service:

1. Navigate to **Connectors & Tools** in [AI Studio](https://app.writer.com/aistudio)
2. Select the **Salesforce Revenue Cloud** connector
3. Select who has access by default (all users or specific teams)
4. Select which tools to enable for your agents
5. Enter your **Salesforce org URL** (tenant URL), **Consumer Key** (client ID), and **Consumer Secret** (client secret)
6. Complete the OAuth authorization flow

## Next steps

* [Set up connectors](https://support.writer.com/article/299-setting-up-connectors): Learn how to configure and enable connectors in AI Studio
* [Tool calling guide](/home/tool-calling): Understand how AI agents use tools in conversations
* [WRITER Agent guide](https://support.writer.com/article/293-how-to-use-action-agent): Learn how to use WRITER Agent with connected tools
* [MCP gateway overview](/home/mcp-gateway): Learn about Writer's MCP gateway architecture
