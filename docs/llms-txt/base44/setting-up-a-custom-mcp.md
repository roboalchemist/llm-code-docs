# Source: https://docs.base44.com/documentation/account-and-billing/setting-up-a-custom-mcp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing MCP connections

> Connect and manage custom MCP servers that the AI chat can use while you build.

MCP connections let you connect custom MCP servers to your Base44 account so the AI chat can access external tools and data for context while you build. You configure MCP connections once per account, and they are then available in the AI chat for every app in every workspace that your account can access.

<Frame caption="Adding custom MCP connections to your Base44 account">
    <img src="https://mintcdn.com/base44/lUv6lmiPMIs6myQQ/images/MCPconnection.png?fit=max&auto=format&n=lUv6lmiPMIs6myQQ&q=85&s=2ff7b7a5fc6745c3de768689e2734e6a" alt="Adding custom MCP connections to your Base44 account" width="3194" height="924" data-path="images/MCPconnection.png" />
</Frame>

Base44’s AI treats MCP connections as tools it can call when your request requires external data or actions. It decides when to use them based on your prompt and the MCP’s description. You do not have to name an MCP explicitly, but it usually works best if you say what you want to use, such as “Use the GitHub MCP to list open issues.”

Each connection stores the server URL, authentication method, and any headers that need to be sent with every request.

<Warning>
  **Important:**

  * You need a Builder plan or higher to connect custom MCPs.
  * Using MCP connections can increase your credit usage, because the AI processes more information when it connects to external apps and data sources.
</Warning>

***

## Adding a custom MCP connection

Each account can connect up to 20 MCP servers. If you reach this limit, you must remove an existing server to add a new one.

**To add a custom MCP connection:**

1. Click your profile icon at the top-right of Base44.
2. Click **Settings**.
3. Under **Account**, click **MCP connections**.
4. Click **Add custom MCP**.
5. Enter the details for your MCP:
   * **Name:** Enter a clear name for your MCP server so collaborators can recognize it.
   * **URL:** Enter the MCP server URL, such as `https://mcp.deepwiki.com/sse`.
   * **Authentication:** Choose how Base44 should connect:
     * **Not required:** Select this option if the server does not require credentials.
     * **OAuth:** Select this option if the server uses OAuth. You complete the authorization in the next step after testing and adding the server.
   * **Custom headers** (optional): Add any headers that need to be sent with every request, such as API keys:
     1. Click **Add header**.
     2. Enter the **Header name**.
     3. Enter the **Header value**.

<Note>
  Add a header only if your MCP server requires one, such as an API key or bearer token. Check your MCP server or API documentation to see if a header is needed. If nothing is mentioned, leave this section empty and test the connection.
</Note>

6. Click **Test** to check that Base44 can reach the MCP server with the configuration you entered.
7. Click **Test & add** to test the connection and save the new MCP server to your account.

<Frame caption="Adding a custom MCP">
  <img src="https://mintcdn.com/base44/qVVHT2-sFHbNjxme/images/addmspserver-4.png?fit=max&auto=format&n=qVVHT2-sFHbNjxme&q=85&s=99103d420b0962c7bd8962f135ba4589" alt="Adding a custom MCP" title="Addmspserver 4" className="mx-auto" style={{ width:"72%" }} width="1198" height="1142" data-path="images/addmspserver-4.png" />
</Frame>

***

## Turning a custom MCP on or off

Turn an MCP connection on or off without removing its configuration.

**To turn a custom MCP connection on or off:**

1. Click your profile icon at the top-right of Base44.
2. Click **Settings**.
3. Under **Account**, click **MCP connections**.
4. Find the relevant MCP server in the list.
5. Click the toggle on the right to enable or disable that server for your account.

***

## Editing or removing a custom MCP

Make changes to an existing MCP connection or remove it completely from your account.

<Frame caption="Managing an MCP connection">
    <img src="https://mintcdn.com/base44/0rhIc2EaMZdkowWe/images/editmcp.png?fit=max&auto=format&n=0rhIc2EaMZdkowWe&q=85&s=5319be6a396901e4ecf3da9017fb27ac" alt="Managing an MCP connection" width="3168" height="912" data-path="images/editmcp.png" />
</Frame>

**To edit or remove a custom MCP connection:**

1. Click your profile icon at the top-right of Base44.
2. Click **Settings**.
3. Under **Account**, click **MCP connections**.
4. Next to the relevant MCP server, click the **More actions** icon.
5. Choose what you want to do:
   * **Edit Details:** Update the server name, URL, authentication, or custom headers, then save your changes.
   * **Remove MCP:** Permanently remove the MCP server from your account.

<Tip>
  Use clear, descriptive names for each MCP server so collaborators can quickly see which external tools or data sources the AI chat can use.
</Tip>

***

## FAQs

Click a question below to learn more about MCP connections.

<AccordionGroup>
  <Accordion title="Does my app call MCP servers directly?">
    No. MCP connections only control what the AI chat can access while you build. Your app code, APIs, and other integrations do not call MCP servers through this settings page.

    The AI chat uses an MCP server only when your prompt asks for something that requires that server. It does not call every connected MCP for each message.
  </Accordion>

  <Accordion title="How do I define shared AI rules for a workspace?">
    To define shared rules and best practices for how the AI builds apps in a workspace, use workspace skills.

    [Learn how to add skills](/documentation/using-your-workspaces/adding-workspace-skills).
  </Accordion>

  <Accordion title="Can I temporarily disable an MCP server without removing it?">
    Yes. Go to **Settings** → **MCP connections** and use the toggle next to the relevant MCP server to turn it off. When it is off, the AI chat no longer uses that server.

    You can turn the same server back on later without re-entering its configuration.
  </Accordion>

  <Accordion title="Who can use my MCP connections?">
    Any collaborator who can open the AI chat for an app you can access can benefit from your MCP connections in that chat. Because MCP connections are configured per account, they are available in all apps and all workspaces that your account has access to. The AI decides when to use each MCP based on the prompt and the MCP configuration.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).