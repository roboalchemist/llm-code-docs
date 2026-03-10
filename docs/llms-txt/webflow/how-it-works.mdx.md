# Source: https://developers.webflow.com/mcp/reference/how-it-works.mdx

***

title: How it works
description: Learn how Webflow's MCP server works
-------------------------------------------------

The Webflow MCP server implements [Anthropic's Model Context Protocol specification](https://docs.anthropic.com/en/docs/model-context-protocol-mcp) to standardize communication between AI agents and Webflow's APIs. This allows you to interact with your Webflow projects using natural language in any MCP-compatible AI tool.

## Architecture

The MCP server acts as a translation layer between AI agents and Webflow's APIs. When you prompt your AI agent, the server:

1. **Receives the request** from your AI tool (Claude Desktop, Cursor, etc.)
2. **Translates the intent** into specific Webflow API calls
3. **Executes operations** on your sites using OAuth-authenticated access
4. **Returns results** back to your AI agent in a structured format

<Callout intent="info">
  **Open source**

  The MCP server is built as an [open-source package](https://github.com/webflow/mcp-server) that wraps Webflow's REST and Designer APIs into a format any MCP-compatible AI agent can understand and execute.
</Callout>

## Remote deployment

The server runs remotely at `https://mcp.webflow.com/sse` to enable OAuth authentication. This approach provides several benefits:

* **No local credentials**: Authorize multiple Webflow sites without storing API keys on your machine
* **Secure access**: Token-based authentication with automatic refresh
* **Easy updates**: Server improvements deploy automatically without reinstalling

<Warning title="Remote authorization is experimental">
  Remote authorization relies on the [`mcp-remote` npm package](https://www.npmjs.com/package/mcp-remote), which is currently considered experimental by Anthropic.
</Warning>

## Available tools

The MCP server exposes Webflow's APIs as MCP tools that your AI agent can use. Tools are organized into two categories based on their purpose.

<Tabs>
  <Tab title="Data API tools">
    [**Data API**](/data/reference/rest-introduction) tools access your site's content and structure for bulk operations and content management. These tools work immediately after OAuth authorization.

    **What you can do:**

    * Manage CMS collections, fields, and items
    * Work with site pages and components
    * Handle custom code and scripts
    * Access site metadata and configuration

    **Available tools:**

    * [**Sites**](/mcp/reference/data/sites) - List and manage Webflow sites
    * [**Pages**](/mcp/reference/data/pages) - Get page content and metadata
    * [**Components**](/mcp/reference/data/components) - Work with reusable components
    * [**Collections**](/mcp/reference/data/cms/collections) - Manage CMS collections
    * [**Fields**](/mcp/reference/data/cms/fields) - Define and update collection fields
    * [**Items**](/mcp/reference/data/cms/items) - Create, read, update, and delete CMS items
    * [**Custom Code**](/mcp/reference/data/custom-code) - Manage site-wide custom code
  </Tab>

  <Tab title="Designer API tools">
    [**Designer API**](/designer/reference/introduction) tools enable real-time canvas manipulation. These tools require the companion app to be open in the Webflow Designer.

    **What you can do:**

    * Create and modify elements on the canvas
    * Apply styles, classes, and design tokens
    * Manage design variables and themes
    * Work with assets and media

    **Available tools:**

    * [**Elements**](/mcp/reference/designer/elements) - Create and manipulate DOM elements
    * [**Styles**](/mcp/reference/designer/styles) - Apply CSS styles and classes
    * [**Assets**](/mcp/reference/designer/assets) - Manage images and media files
    * [**Variables**](/mcp/reference/designer/variables) - Work with design variables and tokens

    ### Designer companion app

    Designer API calls are executed through a companion app that automatically installs to your authorized sites after OAuth authorization. **The companion app must remain open in the Webflow Designer** for Designer API tools to function. However, you can minimize it once connected.

    <div>
      <Frame>
        <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/02ae17428a9bc1c3d5ed26bc14b44a66d935ef85970e30b85f6c2b0d64c15ddb/products/mcp/pages/assets/bridge-app.png" alt="MCP Bridge App" />
      </Frame>
    </div>
  </Tab>
</Tabs>

<Tip>
  For detailed information about each tool's parameters and capabilities, visit the individual tool reference pages linked above.
</Tip>
