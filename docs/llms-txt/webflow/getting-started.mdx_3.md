# Source: https://developers.webflow.com/mcp/reference/getting-started.mdx

***

title: Getting started
description: Install and configure Webflow's MCP server and AI tools
--------------------------------------------------------------------

The Webflow MCP server connects your AI agent directly to your Webflow projects. In this guide, you'll install the remote MCP server, authorize your sites, and start building with natural language prompts.

## Setup overview

The installation process takes about 5 minutes and includes:

1. **Configure your AI tool** - Add the Webflow connector to Claude Desktop or add the MCP server to Claude Code, Cursor, or Windsurf
2. **Authorize sites** - Connect the MCP server to your Webflow account via OAuth
3. **Launch companion app** - Open the bridge app in the Webflow Designer for real-time syncing
4. **Start prompting** - Use natural language to interact with your sites

<Callout intent="info">
  **What you'll need**

  * **AI client**: We provide instructions for [Claude Code](https://github.com/anthropics/claude-code), [Claude Desktop](https://claude.ai/download), [Cursor](https://www.cursor.com/), or [Windsurf](https://codeium.com/windsurf)
  * **Node.js**: Version 22.3.0 or higher ([download here](https://nodejs.org/))
  * **Webflow account**: With at least one site you can access

  **Estimated time**: 5 minutes
</Callout>

<Note title="Companion app installation">
  The MCP companion app installs automatically during OAuth authorization. It's not available on the public Webflow app marketplace.
</Note>

For local installation options, see the [NPM package documentation](https://www.npmjs.com/package/webflow-mcp-server).

## Installation

Select your AI tool below to begin:

<Tabs>
  <Tab title="Claude Desktop">
    Webflow provides a connector that you can use in Claude Desktop.
    It provides direct access to the MCP server.

    <Steps>
      <Step title="Open the list of connectors">
        In the Claude chat window, click the `+` symbol and then click `Add connectors`.

        <Frame>
          <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/5978b53a9f117dedbd4c12981676274630a99bd5e30e333b1281a61094b1a825/products/assets/images/claude-add-connector.png" alt="Add connector option in the drop-down list" />
        </Frame>
      </Step>

      <Step title="Find the Webflow connector">
        Search for the Webflow connector by name.
        You may need to select **All** instead of **Featured** to see it.
      </Step>

      <Step title="Select the Webflow connector">
        Click the Webflow connector and then click `Connect` to install it.
      </Step>

      <Step title="Grant access">
        Grant Claude access to your Webflow account and log in to your Webflow account if you are prompted to do so.
      </Step>

      <Step title="Select sites or Workspaces">
        Select the Webflow sites and Workspaces to give Claude access to and then click `Authorize App`.

        <Frame>
          <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/6ccc744c3720df5b29b183b9cb55a4c9e56ea15429c0c1ad09755d6524fe36ef/products/assets/images/claude-connector-select-sites.png" alt="Add connector option in the drop-down list" />
        </Frame>
      </Step>

      <Step title="Write your first prompt">
        Start interacting with the MCP server in your AI agent's chat window. Try prompts like:

        ```
        List all my collections and show me their field structures
        ```

        ```
        Audit my site for broken links, missing alt text, and incomplete meta descriptions
        ```

        ```
        Create a responsive hero section with a headline, description, and CTA button
        ```
      </Step>
    </Steps>
  </Tab>

  <Tab title="Claude Code">
    <Steps>
      <Step title="Install Claude Code CLI">
        If you haven't installed Claude Code yet, follow the [installation guide](https://github.com/anthropics/claude-code#installation).

        Verify installation:

        ```bash
        claude --version
        ```
      </Step>

      <Step title="Add the Webflow MCP server">
        Use the CLI to add the Webflow MCP server:

        ```bash
        claude mcp add --transport http webflow https://mcp.webflow.com/mcp
        ```

        This will add the Webflow MCP server to your Claude Code configuration.
      </Step>

      <Step title="Authorize the MCP server and app">
        Start Claude Code:

        ```bash
        claude
        ```

        Once Claude Code is running, use the `/mcp` command to manage MCP servers:

        ```bash
        /mcp list
        ```

        Select the Webflow MCP server from the list. If you haven't authenticated yet, Claude Code will automatically open a browser window showing an OAuth login page where you can authorize the Webflow sites you want the MCP server to access and install the [companion app](/mcp/reference/how-it-works#designer-companion-app).
      </Step>

      <Step title="Open the Webflow Designer">
        Open your site in the Webflow Designer.

        Or, type this prompt in Claude Code:

        ```
        Give me a link to open <MY_SITE_NAME> in the Webflow Designer
        ```
      </Step>

      <Step title="Open the MCP Webflow App">
        1. In the designer, open the Apps panel by pressing the `E` key.
        2. Launch the "Webflow MCP Bridge App". This app was automatically installed during the OAuth authorization process.
        3. Wait for the companion app to connect to the MCP Server

        <Frame>
          <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/02ae17428a9bc1c3d5ed26bc14b44a66d935ef85970e30b85f6c2b0d64c15ddb/products/mcp/pages/assets/bridge-app.png" alt="Webflow MCP Bridge App" />
        </Frame>
      </Step>

      <Step title="Write your first prompt">
        Start interacting with the MCP server in Claude Code. Try prompts like:

        ```
        List all my collections and show me their field structures
        ```

        ```
        Audit my site for broken links, missing alt text, and incomplete meta descriptions
        ```

        ```
        Create a responsive hero section with a headline, description, and CTA button
        ```
      </Step>
    </Steps>
  </Tab>

  <Tab title="Cursor">
    Click the button to install, or follow the instructions below:

    <div>
      <span>
        [![Install MCP Server](https://cursor.com/deeplink/mcp-install-light.svg)](https://cursor.com/en-US/install-mcp?name=webflow\&config=eyJ1cmwiOiJodHRwczovL21jcC53ZWJmbG93LmNvbS9tY3AifQ%3D%3D)
      </span>

      <span>
        [![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en-US/install-mcp?name=webflow\&config=eyJ1cmwiOiJodHRwczovL21jcC53ZWJmbG93LmNvbS9tY3AifQ%3D%3D)
      </span>
    </div>

    <Steps>
      <Step title="Install the MCP server on Cursor">
        1. Go to `Settings → Cursor Settings → MCP & Integrations`
        2. Under MCP Tools, click `+ New MCP Server`/`Add Custom MCP`
        3. Paste the following configuration into `.cursor/mcp.json` (or add the `webflow` part to your existing configuration):

           <CodeBlock title=".cursor/mcp.json">
             ```json
             {
               "mcpServers": {
                 "webflow": {
                   "url": "https://mcp.webflow.com/mcp"
                 }
               }
             }
             ```
           </CodeBlock>

           <Tip title="Use project-specific MCP configuration to avoid repeated auth prompts">
             Configure `mcp.json` [per project](https://docs.cursor.com/en/context/mcp#configuration-locations) instead of using Cursor's global settings. This prevents repeated authentication prompts when opening multiple Cursor windows without being authenticated.
           </Tip>
        4. Save and close the file
      </Step>

      <Step title="Authorize the MCP server and app">
        1. Go to `Settings → Cursor Settings → MCP & Integrations`
        2. Authorize Webflow MCP by clicking the Connect button
        3. Cursor automatically opens an OAuth login page where you authorize the Webflow sites you want to access and install the [companion app](/mcp/reference/how-it-works#designer-companion-app).
        4. Once authorization is complete, the Webflow MCP indicator should turn green.

        <Tip title="Limit authorized sites">
          Limit the number of sites for security and performance. To reauthorize, simply click **Logout** by expanding Webflow MCP.
        </Tip>
      </Step>

      <Step title="Open the Webflow Designer">
        Open your site in the Webflow Designer.

        Or, type this prompt in your AI chat window:

        ```
        Give me a link to open <MY_SITE_NAME> in the Webflow Designer
        ```
      </Step>

      <Step title="Open the MCP Webflow App">
        1. In the designer, open the Apps panel by pressing the `E` key.
        2. Launch the "Webflow MCP Bridge App". This app was automatically installed during the OAuth authorization process.
        3. Wait for the companion app to connect to the MCP Server

        <Frame>
          <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/02ae17428a9bc1c3d5ed26bc14b44a66d935ef85970e30b85f6c2b0d64c15ddb/products/mcp/pages/assets/bridge-app.png" alt="Webflow MCP Bridge App" />
        </Frame>
      </Step>

      <Step title="Write your first prompt">
        Start interacting with the MCP server in your AI agent's chat window. Try prompts like:

        ```
        List all my collections and show me their field structures
        ```

        ```
        Audit my site for broken links, missing alt text, and incomplete meta descriptions
        ```

        ```
        Create a responsive hero section with a headline, description, and CTA button
        ```
      </Step>
    </Steps>

    <Tip title="Start with a fresh project for better MCP performance">
      MCP servers perform more efficiently with smaller codebases. In Cursor, create a new project when using the MCP server to reduce tool call overhead and improve response times.
    </Tip>
  </Tab>

  <Tab title="Windsurf">
    <Steps>
      <Step title="Add the MCP server to the configuration">
        1. Navigate to `Windsurf → Settings → Windsurf Settings`
        2. Scroll down to the `Cascade` section → `MCP Servers` → `Manage MCPs`
        3. Click the "View raw config" button
        4. Paste the following configuration (or add the `webflow` part to your existing configuration):

           ```json mcp_config.json
           {
             "mcpServers": {
               "webflow": {
                 "serverUrl": "https://mcp.webflow.com/mcp"
               }
             }
           }
           ```

           ```
           ```
        5. Save and close the file
      </Step>

      <Step title="Authorize the MCP server">
        1. Click the "Refresh" button in the settings page
        2. Windsurf will automatically open a new browser window showing an OAuth login page.
        3. Authorize the Webflow sites you want the MCP server to access. This will also automatically install the [companion app](/mcp/reference/how-it-works#designer-companion-app) to any sites you authorize.

        <Tip title="Limit authorized sites">
          Limit the number of sites for security and performance.
        </Tip>
      </Step>

      <Step title="Open the Webflow Designer">
        Open your site in the Webflow Designer.

        Or, type this prompt in your AI chat window:

        ```
        Give me a link to open <MY_SITE_NAME> in the Webflow Designer
        ```
      </Step>

      <Step title="Open the MCP Webflow App">
        1. In the designer, open the Apps panel by pressing the `E` key.
        2. Launch the "Webflow MCP Bridge App". This app was automatically installed during the OAuth authorization process.
        3. Wait for the companion app to connect to the MCP Server

        <Frame>
          <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/02ae17428a9bc1c3d5ed26bc14b44a66d935ef85970e30b85f6c2b0d64c15ddb/products/mcp/pages/assets/bridge-app.png" alt="Webflow MCP Bridge App" />
        </Frame>
      </Step>

      <Step title="Write your first prompt">
        Start interacting with the MCP server in your AI agent's chat window. Try prompts like:

        ```
        List all my collections and show me their field structures
        ```

        ```
        Audit my site for broken links, missing alt text, and incomplete meta descriptions
        ```

        ```
        Create a responsive hero section with a headline, description, and CTA button
        ```
      </Step>
    </Steps>
  </Tab>
</Tabs>

## Next steps

Now that you've installed the MCP server, explore what you can do:

<Cards>
  <Card
    title="Explore the prompt library"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Ai.svg" alt="" className="dark-icon" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Ai.svg" alt="" className="light-icon" />
    </>
  }
    iconSize={12}
    iconPosition="left"
    href="/mcp/examples"
  >
    Browse ready-to-use prompts for image optimization, SEO audits, style refactoring, and more.
  </Card>

  <Card
    title="Review available tools"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/ToolNut.svg" alt="" className="dark-icon" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/ToolNut.svg" alt="" className="light-icon" />
    </>
  }
    iconSize={12}
    iconPosition="left"
    href="/mcp/reference/how-it-works#available-tools"
  >
    See the complete list of Data API and Designer API tools you can use with your AI agent.
  </Card>

  <Card
    title="Learn how it works"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Resources.svg" alt="" className="dark-icon" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Resources.svg" alt="" className="light-icon" />
    </>
  }
    iconSize={12}
    iconPosition="left"
    href="/mcp/reference/how-it-works"
  >
    Understand the architecture, authentication, and how the MCP server connects to Webflow's APIs.
  </Card>
</Cards>
