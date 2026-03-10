# Source: https://docs.inkeep.com/visual-builder/tools/mcp-servers

# Register MCP Servers in Visual Builder (/visual-builder/tools/mcp-servers)

Create MCP servers that agents can use to access external services.



MCP servers provide tools that your agents can use to interact with external APIs and services. Once created, these servers are automatically synced to discover available tools, which can then be added to your agents.

<>
  To use MCP servers with your agents, you can:

  * **Connect to Native MCP servers** from providers like Atlassian, Linear, Notion, and more
  * **Use Composio's platform** for access to 10,000+ out-of-box MCP servers
  * **Use Gram** to easily convert existing OpenAPI APIs into MCP Servers
  * **Build Custom MCP servers** for totally custom MCP servers

  See the [MCP Servers tutorial](/guides/mcp-servers/overview) for details on all recommended approaches.

  Once you have access to an MCP server, you can register it with your agents.
</>

## Register an MCP server

1. Go to the **MCP Servers** tab in the left sidebar, then select "New MCP server".

2. Fill in the required server details:

| Field            | Description                         |
| ---------------- | ----------------------------------- |
| `Name`           | Server name                         |
| `URL`            | Endpoint URL of a remote MCP server |
| `Transport Type` | Streamable HTTP or SSE protocol     |

3. Optionally, configure additional settings:

| Field           | Description                                                                                                                                                                                                                                            |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Image URL`     | Custom icon for the server (URL or base64 data URL)                                                                                                                                                                                                    |
| `Custom Prompt` | Additional instructions for agents on how to use tools from this server. This context is provided to agents alongside each tool from this server.                                                                                                      |
| `Credential`    | Authentication credential if the server requires it. Choose from existing credentials, or leave blank and add a credential later. For OAuth 2.1/PKCE flows, leave blank and use the `Click to Login` button in the server details page to authenticate |

4. Click "Create" to create the server.

## Viewing server details

After creating an MCP server, you can view its details:

1. Click on your created MCP server from the list
2. The server details page shows:
   * **Server information** - URL, transport type, creation date, etc.
   * **Status** - healthy, unhealthy, unknown, disabled, or shows a "Click to Login" button if OAuth 2.1/PKCE flow is detected
   * **Active tools** - Currently enabled tools for the server
   * **Available tools** - All tools discovered from the server with descriptions and parameters

<Image
  src="/images/mcp-server-healthy-status.png"
  alt="MCP server healthy status"
  style={{
  width: "60%",
  border: "1px solid #e1e5e9",
  display: "block",
  margin: "0 auto",
}}
/>

<Note>
  Tool discovery requires a successful connection to the MCP server. If the
  server shows "Click to Login" in the status, use the button to initiate the
  authentication process.
</Note>

## Editing server settings

To modify an existing MCP server:

1. From the server details page, click the **Edit** button
2. The edit form shows all the same fields as creation, plus the ability to update **Active Tools**. By default, all available tools are enabled. You can select specific tools to enable.
3. Click **Save** to apply changes

## Tool overrides

For each enabled tool, you can configure overrides to customize how the tool appears to agents:

1. In the **Active Tools** section of the edit form, click the **Override** badge next to any tool
2. Configure the following override options:

| Field          | Description                                                                                                        |
| -------------- | ------------------------------------------------------------------------------------------------------------------ |
| `Display Name` | Custom name for the tool that agents will see (overrides the original tool name)                                   |
| `Description`  | Custom description that explains what the tool does (overrides the original description)                           |
| `Schema`       | Simplified parameter schema using visual builder or JSON. Useful for hiding complex parameters or adding defaults. |

3. Click **Save Override** to apply the customizations

<Note>
  Tool overrides help simplify complex tools for agents by providing clearer names, better descriptions, and simplified parameter schemas. The original tool functionality remains unchanged.
</Note>

<Image
  src="/images/mcp-server-edit-form.png"
  alt="MCP server healthy status"
  style={{
  width: "60%",
  border: "1px solid #e1e5e9",
  display: "block",
  margin: "0 auto",
}}
/>

## Authentication setup

If your MCP server requires authentication, you have two options: either use the **"Click to Login"** button to authenticate or manually create a credential to use with the MCP server.

### OAuth 2.1/PKCE authentication

1. Create your MCP server without selecting a credential
2. Go to the server details page and click the **"Click to Login"** button
3. Complete the OAuth authentication flow in your browser
4. The credential will be automatically created and saved to your Nango Store (follow steps to [setup Nango](/typescript-sdk/credentials/nango)). If Nango is not set up, the framework will use the [Keychain Store](/typescript-sdk/credentials/keychain) if available.

<Image
  src="/images/mcp-server-click-to-login.png"
  alt="MCP server click to login"
  style={{
  width: "60%",
  border: "1px solid #e1e5e9",
  display: "block",
  margin: "0 auto",
}}
/>

#### 1-click Install MCP servers

<>
  Here's an example list of popular service-maintained MCP Servers that support **1-click** install via the OAuth 2.1/PKCE authentication flow.

  | Name                                                                                                             | URL                                                                  |
  | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
  | [Atlassian (SSE)](https://support.atlassian.com/rovo/docs/getting-started-with-the-atlassian-remote-mcp-server/) | [https://mcp.atlassian.com/v1/sse](https://mcp.atlassian.com/v1/sse) |
  | [Canva](https://www.canva.dev/docs/connect/canva-mcp-server-setup/)                                              | [https://mcp.canva.com/mcp](https://mcp.canva.com/mcp)               |
  | [Hugging Face](https://huggingface.co/mcp)                                                                       | [https://huggingface.co/mcp?login](https://huggingface.co/mcp?login) |
  | [Intercom](https://developers.intercom.com/docs/guides/mcp)                                                      | [https://mcp.intercom.com/mcp](https://mcp.intercom.com/mcp)         |
  | [Linear](https://linear.app/docs/mcp)                                                                            | [https://mcp.linear.app/mcp](https://mcp.linear.app/mcp)             |
  | [Neon](https://neon.com/docs/ai/neon-mcp-server)                                                                 | [https://mcp.neon.tech/mcp](https://mcp.neon.tech/mcp)               |
  | [Notion](https://developers.notion.com/docs/get-started-with-mcp)                                                | [https://mcp.notion.com/mcp](https://mcp.notion.com/mcp)             |
  | [Prisma](https://www.prisma.io/docs/postgres/integrations/mcp-server#remote-mcp-server)                          | [https://mcp.prisma.io/mcp](https://mcp.prisma.io/mcp)               |
  | [Sentry](https://docs.sentry.io/product/sentry-mcp/)                                                             | [https://mcp.sentry.dev/mcp](https://mcp.sentry.dev/mcp)             |
  | [Vercel](https://vercel.com/docs/mcp/vercel-mcp)                                                                 | [https://mcp.vercel.com](https://mcp.vercel.com)                     |

  To add them to your project:

  1. navigate to **MCP Servers** in the Inkeep Visual Builder.
  2. Click on **New MCP Server**
  3. Choose from the preset list under **Popular Services** or register any under **Custom Server**

  When you register the server, an authentication pop-up will appear and allow you to sign in. Your credentials will automatically be saved to your [Nango Store](/typescript-sdk/credentials/nango) or [Keychain](/typescript-sdk/credentials/keychain) credential store.
</>

### Manual credential setup

1. Create a credential in the [Credentials](/visual-builder/tools/credentials) section. The credential can be API Key, Bearer Token, Basic, OAuth 2.0, etc.
2. When creating or editing your MCP server, select the credential from the dropdown
3. The credential will be automatically used when connecting to the server

## Finding more remote MCP servers

For additional remote MCP servers you can connect to:

* **[Anthropic's Remote MCP Servers](https://docs.anthropic.com/en/docs/agents-and-tools/remote-mcp-servers)** - Official documentation with curated third-party remote servers
* **[Awesome Remote MCP Servers](https://github.com/jaw9c/awesome-remote-mcp-servers)** - Community-curated list of high-quality remote MCP servers

## Using stdio-based MCP servers

The Visual Builder requires **Streamable HTTP or SSE transport** to connect to MCP servers. If you have an MCP server that runs in **stdio mode** locally, you can use the following setup to connect to it.

### Setup outline

1. **Deploy your stdio -> Streamable HTTP/SSE bridge** (locally or cloud)
2. **Set environment variables** (API tokens, etc.)
3. **Verify it's running** (i.e. on port `4000`, `4001`, etc.)
4. **Add to Visual Builder**:
   * **URL**: `http://localhost:4000/mcp` (or your server URL)
   * **Transport Type**: `Streamable HTTP` or `SSE`

### Example using `mcp-proxy`

1. Get familiar with [mcp-proxy](https://github.com/sparfenyuk/mcp-proxy) - proxy for MCP servers that use stdio transport
2. [Supabase MCP server](https://github.com/supabase-community/supabase-mcp)
3. Run the server locally:

```bash
SUPABASE_ACCESS_TOKEN=YOUR_SUPABASE_ACCESS_TOKEN mcp-proxy --port 4444 --shell "npx -y @supabase/mcp-server-supabase@latest --read-only"
```

4. Add to Visual Builder with the following settings:
   * **URL**: `http://localhost:4444/mcp`
   * **Transport Type**: `Streamable HTTP`

## Adding servers to agents

Once you have created an MCP server, you can add it to your agents:

<Tip>
  For tools that can make destructive changes, require explicit user approval before execution. See
  [Tool approvals](/typescript-sdk/tools/tool-approvals).
</Tip>

1. Go to the [Sub Agents](/visual-builder/sub-agents) page
2. Drag and drop an MCP server into your agent
3. Connect the MCP server to a Sub Agent by dragging from the server's connector to the Sub Agent
4. Your Sub Agent can now use the tools provided by that MCP server

<Image
  src="/images/mcp-server-add-to-agent.png"
  alt="MCP server add to agent"
  style={{
  width: "60%",
  border: "1px solid #e1e5e9",
  display: "block",
  margin: "0 auto",
}}
/>

For detailed instructions on working with MCP servers in agents, see the [Sub Agents](/visual-builder/sub-agents#adding-tools) page.

## Tool Output Pipelines

MCP tool outputs can be passed directly as inputs to subsequent tools — including other MCP servers or function tools — without creating an artifact in between. Agents handle this automatically when tools are designed for sequential use. See [Function Tools — Tool Output Pipelines](/visual-builder/tools/function-tools#tool-output-pipelines) for more detail.
