# Source: https://docs.inkeep.com/guides/mcp-servers/native-mcp-servers

# Connect to Native MCP Servers (/guides/mcp-servers/native-mcp-servers)

Connect to Native MCP servers provided by SaaS vendors



The fastest way to get started is by connecting to existing MCP servers provided directly by SaaS providers that offer them.

### MCPs with OAuth 2.1/PKCE support

These servers often implement OAuth 2.1 with PKCE for secure authentication that allow for `1-click` authentication without the need for API keys.

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

<>
  ### Next steps

  Once you have your server, you can register it in one of:

  <Cards>
    <Card title="The TypeScript SDK" icon="LuCode" href="/typescript-sdk/tools/mcp-tools#step-2-register-the-mcp-server-as-a-tool-in-your-agent">
      Add your MCP server as a tool for your agents in the TypeScript SDK
    </Card>

    <Card title="The Visual Builder" icon="LuPalette" href="/visual-builder/tools/mcp-servers#register-an-mcp-server">
      Add your MCP server as a tool for your agents in the Visual Builder
    </Card>
  </Cards>
</>
