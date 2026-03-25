# Source: https://plivo.com/docs/aiagent/aistudio/mcptools.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MCP Tools

> MCP Tools allows you to seamlessly integrate third-party applications into the Agent flow.

Plivo supports multiple external tools via MCP integrations. These integrations are available under the "External Tools" section in the primary navigation bar.

<Frame>
    <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/aiagent/images/tools1.jpg?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=b5c3ef70bc7f7688cf4706cf41fbb197" alt="" width="2880" height="1760" data-path="aiagent/images/tools1.jpg" />
</Frame>

The MCP Tools section enables you to connect third-party applications directly to your AI agents. You can integrate applications such as Slack, Shopify, Zendesk, and others with ease. However, please note that:

* You need to have an account for the application you wish to integrate. Plivo does not create accounts on your behalf.
* You will be required to authorize access to your account on the application.

<Info>
  Multiple accounts for each application can be linked if needed.
</Info>

**Configure Actions**

For each application, a set of supported actions will be available in the workflow builder. These actions can be used in your agent flows. Each action may require additional configuration details. Read more about setting up [App Actions](/aiagent/aistudio/nodereference/actions.mdx).

<Frame>
    <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/aiagent/images/tools2.jpg?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=85783b08e129e59465d2df074430077f" alt="" width="2880" height="1760" data-path="aiagent/images/tools2.jpg" />
</Frame>

#### Example of Action Configuration

After connecting your application, actions from the app can be used as nodes in the workflow builder. For example, with Slack integration, you could set up an action like send a message or create a channel directly from your agent's flow.

## Supported Applications

The following list includes a few applications that can be integrated via MCP Tools:

### 1. CRM & Sales:

* **Zoho** (OAuth 2.0)
* **HubSpot** (OAuth 2.0)
* **Salesforce** (OAuth 2.0)
* **Shopify** (OAuth 2.0)

### 2. Communication & Collaboration:

* **Zoho People** (OAuth 2.0)
* **Slack** (OAuth 2.0)

### 3. Customer Support & Service:

* **Intercom** (OAuth 2.0)
* **Zendesk** (OAuth 2.0)
* **Zoho Desk** (OAuth 2.0)
* **FreshDesk** (Basic)

### 4. File Storage:

* **Dropbox** (OAuth 2.0)
* **Google Drive** (OAuth 2.0)

### 5. Google Workspace:

* **Gmail** (OAuth 2.0)
* **Google Sheets** (OAuth 2.0)
* **Google Docs** (OAuth 2.0)

### 6. Productivity & Project Management:

* **Confluence** (OAuth 2.0)
* **Notion** (OAuth 2.0)
* **Linear** (OAuth 2.0)

### 7. Scheduling & Calendar:

* [**Cal.com**](http://Cal.com) (API Key)
* **Calendly** (OAuth 2.0)
* **Google Calendar** (OAuth 2.0)

### 8. Search & Information:

* **WeatherAPI** (API Key)
* **SearchApi** (API Key)
* **Google Search** (API Key)
* **Perplexity** (API Key)
* **SerpApi** (API Key)

### 9. Social Media & Content:

* [**TwitterAPI.io**](http://TwitterAPI.io) (API Key)
* **Reddit** (OAuth 2.0)
* **YouTube** (OAuth 2.0)
* **X** (OAuth 2.0)
