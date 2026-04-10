# Source: https://directus.io/docs/raw/guides/ai/mcp/installation.md

# Installation

> Set up the Directus MCP server and connect your AI tools in under 5 minutes.

Get AI assistants connected to your Directus instance in three simple steps. The MCP server is built into Directus with no additional setup required.

<callout color="info" icon="material-symbols:info">

**MCP requires Directus v11.12+**. For older versions, use the [Local MCP alternative](/guides/ai/mcp/local-mcp).

</callout>

## Quick Setup

The Directus MCP server is disabled by default and must be manually enabled. When enabled, it uses the same permissions as the user account you connect with. AI tools can only access what that user is allowed to see and do.

System administrators can completely disable MCP functionality through [configuration environment variables](/configuration/ai#model-context-protocol).

<steps level="3">

### Enable MCP in Directus

1. Log into your Directus admin as an administrator
2. Go to **Settings → AI → Model Context Protocol**
3. Click **Enabled** under **MCP Server** to activate the MCP server
![MCP Server Enabled](/img/mcp-settings-page-enable.png)
4. **Save the AI settings**

<callout color="primary">

Most users can keep the default settings. The MCP server is now ready at `https://your-directus-url.com/mcp`.

</callout>

### Generate Access Token

<tabs>
<tabs-item icon="material-symbols:person-add" label="Create New User">

1. Navigate to **User Directory**
2. Click **Create User** with these settings:

  - **Name**: `Your Name - MCP User` or similar
  - **Email**: Email is not required for MCP operations
  - **Role**: Create a new role or use existing role with appropriate [permissions](/guides/auth/access-control).
3. Generate an access token:

  - Open the user profile
  - Scroll to **Token** field → Generate new token
  - **Copy the token** (you'll need it next)
  - **Save the user**

</tabs-item>

<tabs-item icon="material-symbols:person" label="Use Existing User">
<callout color="warning" icon="material-symbols:warning">

**Not recommended**: It's best to use dedicated accounts for AI operations, instead of using your personal admin account.

</callout>

1. Navigate to **User Directory**
2. Find your existing user
3. Open the user profile
4. Generate an access token:

  - Scroll to **Token** field → Generate new token
  - **Copy the token** (you'll need it next)
  - **Save the user**

</tabs-item>
</tabs>

### Connect Your AI Client

You control the LLM integration. This tool connects to your own language model - either self-hosted or via a public service like OpenAI, Anthropic, or others.

Choose your AI tool and follow the setup:

<accordion type="single">
<accordion-item icon="i-simple-icons-openai" label="ChatGPT">

1. Log into [ChatGPT](https://chat.openai.com/) with Pro/Teams account
2. Go to **Settings → Apps & Connectors**
3. Click **Create** in the top-right corner
4. Configure:

  - **Name**: Directus MCP
  - **MCP Server URL**: `https://your-directus-url.com/mcp?access_token=your-generated-token`
  - **Authentication**: No authentication
5. Click **Create** to save the connector

</accordion-item>

<accordion-item icon="i-simple-icons-anthropic" label="Claude Desktop">

1. Download [Claude Desktop](https://claude.ai/download) and sign in with your Claude account
2. Open **Settings → Connectors**
3. Click **Add custom connector**
4. Configure the connector:

  - **Name**: Directus MCP
  - **Server URL**: `https://your-directus-url.com/mcp?access_token=your-generated-token`
5. Click **Add** to save the connector
6. Review and accept the permissions when prompted

</accordion-item>

<accordion-item icon="vscode-icons:file-type-cursorrules" label="Cursor">

[![Install MCP Server in Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en/install-mcp?name=directus&config=eyJ1cmwiOiJodHRwczovL3lvdXItZGlyZWN0dXMtdXJsLmNvbS9tY3AiLCJoZWFkZXJzIjp7IkF1dGhvcml6YXRpb24iOiJCZWFyZXIgRElSRUNUVVNfVE9LRU4ifX0%3D)

1. **One-click install**: Click the button above to automatically configure Directus MCP in Cursor
2. **Manual setup**: Alternatively, create `.cursor/mcp.json` in your project root:

```json
{
  "mcpServers": {
    "directus": {
      "url": "https://your-directus-url.com/mcp",
      "headers": {
        "Authorization": "Bearer your-generated-token"
      }
    }
  }
}
```

1. Replace `your-directus-url.com` and `your-generated-token` with your values

</accordion-item>

<accordion-item icon="i-simple-icons-anthropic" label="Claude Code">

1. Install [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code/quickstart)
2. Add Directus MCP server using the command line:

```bash
claude mcp add --transport http directus https://your-directus-url.com/mcp \
  --header "Authorization: Bearer your-generated-token"
```

1. Start Claude Code and verify the connection:

```bash
# Start Claude Code
claude

# Ask Claude to test the connection
> "Can you tell me about my Directus schema?"
```

</accordion-item>

<accordion-item icon="i-simple-icons-visualstudiocode" label="VS Code">

1. Install VS Code 1.102+ and the [GitHub Copilot extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat)
2. Create or edit `mcp.json` in your workspace `.vscode` folder or user settings
3. Add this configuration:

```json
{
  "servers": {
    "directus": {
      "type": "http",
      "url": "https://your-directus-url.com/mcp",
      "headers": {
        "Authorization": "Bearer ${input:directus-token}"
      }
    }
  },
  "inputs": [
    {
      "id": "directus-token",
      "type": "promptString",
      "description": "Directus Access Token",
      "password": true
    }
  ]
}
```

1. VS Code will prompt you for your Directus token when the server starts
2. Use MCP tools in Agent mode from the Chat view

</accordion-item>

<accordion-item icon="i-simple-icons-raycast" label="Raycast">

1. Download [Raycast](https://raycast.com/)
2. Open Raycast and search for "MCP Servers"
3. Configure Directus MCP server through the UI:

  - **Name**: Directus MCP
  - **URL**: `https://your-directus-url.com/mcp?access_token=your-generated-token`
4. Save the configuration
5. Use `@directus` to interact with your instance

</accordion-item>
</accordion>
</steps>

## Verify Connection

Once connected, test your setup with a simple question about your Directus instance:

<chat :messages="[{"role":"user","content":"Can you tell me about my Directus schema?"},{"role":"assistant","content":"I'll help you explore your Directus schema. Let me start by getting my role information and then examine your database structure.","toolInvocations":[{"toolCallId":"system-prompt","toolName":"system-prompt","state":"result"},{"toolCallId":"schema","toolName":"schema","state":"result"}]}]" chatId="verify-connection">



</chat>

## User Permissions

Configure your AI user's role based on what you want them to do:

**Content Editor Role** (recommended for most users):

- **Collections**: Read/Create/Update on your content collections
- **Files**: Read/Create/Update/Delete
- **Folders**: Read/Create/Update/Delete
- **System Collections**: Read only

**Developer Role** (required for schema management):

- All content permissions above, plus:
- **Collections**: Full CRUD access
- **Fields**: Full CRUD access
- **Relations**: Full CRUD access
- **Flows**: Full CRUD access

or add the administrator role to your MCP user.

<callout color="info" icon="material-symbols:info">

**Note**: The MCP server uses your existing permissions and access policy settings. AI tools can only access what you explicitly allow - just like any other Directus user. See [Access Control](/guides/auth/access-control) for more information.

</callout>

---

## MCP Server Settings

![MCP Server Settings](/img/mcp-settings-page.png)

Access advanced options in **Settings → AI → Model Context Protocol**:

<table>
<thead>
  <tr>
    <th>
      Setting
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Default
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <strong>
        MCP Server
      </strong>
    </td>
    
    <td>
      Toggle
    </td>
    
    <td>
      Disabled
    </td>
    
    <td>
      Connect AI/LLM tools to your Directus project via Model Context Protocol (MCP). This enables AI assistants to read and interact with your Directus data securely.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Allow Deletes
      </strong>
    </td>
    
    <td>
      Toggle
    </td>
    
    <td>
      Disabled
    </td>
    
    <td>
      Enable deletion of items, files, flows, fields, relations, and collections through MCP tools. <strong>
        WARNING: May cause data loss.
      </strong>
      
       Disabled by default for safety.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        AI Prompts Collection
      </strong>
    </td>
    
    <td>
      Select
    </td>
    
    <td>
      No collection selected
    </td>
    
    <td>
      Select a collection to enable reusable prompt templates. Select existing collection or click "Generate AI Prompts collection..." to create one automatically.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Use System Prompt
      </strong>
    </td>
    
    <td>
      Toggle
    </td>
    
    <td>
      Enabled
    </td>
    
    <td>
      Use the default system prompt to guide LLM behavior. Disable to remove or override with your own prompt below.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Custom System Prompt
      </strong>
    </td>
    
    <td>
      Rich Text
    </td>
    
    <td>
      Empty
    </td>
    
    <td>
      Custom system prompt to replace the default. Leave empty to use default (if enabled above).
    </td>
  </tr>
</tbody>
</table>

---

## Next Steps

Your MCP server is ready! Here's what to explore:

<card-group>
<card icon="material-symbols:bolt" title="See What's Possible" to="/guides/ai/mcp/use-cases">

Real examples of AI-powered content workflows that save hours of manual work.

</card>

<card icon="material-symbols:construction" title="Available Tools" to="/guides/ai/mcp/tools">

Complete reference of MCP tools and their capabilities.

</card>

<card icon="material-symbols:chat" title="Custom Prompts" to="/guides/ai/mcp/prompts">

Create reusable prompt templates for consistent AI interactions.

</card>

<card icon="material-symbols:security" title="Security Guide" to="/guides/ai/mcp/security">

Essential security practices for using MCP safely with your Directus data.

</card>

<card icon="material-symbols:help" title="Troubleshooting" to="/guides/ai/mcp/troubleshooting">

Common issues and solutions when setting up and using the Directus MCP server.

</card>
</card-group>
