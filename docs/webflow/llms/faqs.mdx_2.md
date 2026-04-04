# Source: https://developers.webflow.com/mcp/faqs.mdx

***

title: FAQs
description: Frequently asked questions and troubleshooting for Webflow's MCP server
slug: faqs
----------

Common questions and solutions for installing, configuring, and using the Webflow MCP server.

## Installation and setup

<Accordion title="Why is my MCP server not appearing in my AI client?">
  After installing the MCP server, you may need to restart your AI client to see the new server. Additionally, check that your client (Claude Desktop, Cursor, or Windsurf) is updated to the latest version.

  **Troubleshooting steps:**

  1. Restart your AI client completely
  2. Check for updates to your AI client
  3. Verify the MCP server configuration is correct in your config file
  4. Review the [getting started guide](/mcp/reference/getting-started) for platform-specific instructions
</Accordion>

<Accordion title="How can I authenticate a different Webflow site?">
  To authenticate a different Webflow site, remove the existing authentication token and restart your AI client:

  ```bash
  rm -rf ~/.mcp-auth
  ```

  After executing this command, restart your AI client. A new authentication screen will appear, allowing you to select different sites to authorize.

  <Tip>
    Limit the number of authorized sites for better security and performance.
  </Tip>
</Accordion>

<Accordion title="The sites I want to authorize are greyed out">
  Only site owners and admins can authorize the MCP server and companion app. If you're not a site owner or admin, you won't be able to authorize those sites.

  **To resolve this:**

  * Request owner or admin access from your site administrator
  * Or, have a site owner/admin authorize the MCP server for the site
</Accordion>

<Accordion title="I'm getting a 500 error when loading the remote MCP server">
  A 500 error usually indicates an authentication or Node.js version issue.

  **Solution 1: Refresh OAuth token**

  Remove your authentication token and restart your AI client:

  ```bash
  rm -rf ~/.mcp-auth
  ```

  **Solution 2: Verify Node.js version**

  Check your Node.js version is **22.3.0 or higher**:

  ```bash
  node --version
  ```

  If your version is too old, see the [Node.js compatibility](#nodejs-compatibility) section below.
</Accordion>

## Using the MCP server

<Accordion title="The MCP server can't connect to the Webflow Designer">
  To use Designer API tools, you must open the MCP Bridge App in the Webflow Designer:

  **Steps:**

  1. Open your site in the Webflow Designer
  2. Press the `E` key to open the Apps panel
  3. Launch the "Webflow MCP Bridge App"
  4. Wait for the app to connect to the MCP server

  <Warning>
    The companion app must remain open in the Webflow Designer for Designer API tools to work. You can minimize it after it connects.
  </Warning>
</Accordion>

<Accordion title="The MCP server is timing out in the Designer">
  If the MCP server times out or disconnects while using the Designer, your browser may be putting inactive tabs to sleep. Configure your browser to keep the Designer tab active:

  **Chrome:**

  1. Go to `chrome://settings/performance`
  2. Scroll to "Always keep these sites active"
  3. Click "Add" and enter `webflow.com`

  **Firefox:**

  1. Type `about:config` in the address bar
  2. Search for `browser.tabs.unloadOnLowMemory`
  3. Set to `false`
  4. Or keep the Designer tab pinned to prevent unloading

  **Safari:**

  1. Safari doesn't have a built-in setting for this
  2. Keep the Designer tab active and pinned
  3. Or use Chrome/Firefox for better MCP server stability

  <Tip>
    Pinning the Webflow Designer tab in any browser can also help prevent timeout issues.
  </Tip>
</Accordion>

<Accordion title="What tools are available?">
  The MCP server exposes Webflow's Data and Designer APIs as tools your AI agent can use. Tools are organized into two categories:

  **Data API tools** - Work with site content and structure:

  * [Sites](/mcp/reference/data/sites) - List and manage Webflow sites
  * [Pages](/mcp/reference/data/pages) - Get page content and metadata
  * [Components](/mcp/reference/data/components) - Work with reusable components
  * [Collections](/mcp/reference/data/cms/collections) - Manage CMS collections
  * [Fields](/mcp/reference/data/cms/fields) - Define and update collection fields
  * [Items](/mcp/reference/data/cms/items) - Create, read, update, and delete CMS items
  * [Custom Code](/mcp/reference/data/custom-code) - Manage site-wide custom code

  **Designer API tools** - Manipulate the canvas in real-time:

  * [Elements](/mcp/reference/designer/elements) - Create and modify DOM elements
  * [Styles](/mcp/reference/designer/styles) - Apply CSS styles and classes
  * [Assets](/mcp/reference/designer/assets) - Manage images and media files
  * [Variables](/mcp/reference/designer/variables) - Work with design variables and tokens

  For detailed documentation on each tool, visit the [How it works](/mcp/reference/how-it-works#available-tools) page.
</Accordion>

<Accordion title="Can I use all available API endpoints with the MCP server?">
  The MCP server currently supports a focused set of Data and Designer API tools. Not all Webflow API endpoints are available through the MCP server.

  **Request new tools:**

  * [Open an issue on GitHub](https://github.com/webflow/mcp-server/issues) with your use case
  * Or contact the Developer Relations team at [developers@webflow.com](mailto:developers@webflow.com)
</Accordion>

<Accordion title="Does Webflow need to be open to use the MCP server?">
  It depends on which tools you're using:

  **Data API tools:** No, Webflow doesn't need to be open. You can manage content, collections, and site data from your AI client.

  **Designer API tools:** Yes, you must have:

  * The Webflow Designer open in your browser
  * The [companion app](/mcp/reference/how-it-works#designer-companion-app) launched and connected
</Accordion>

<Accordion title="Can I localize content with the MCP server?">
  The MCP server has partial support for localization:

  **Supported:**

  * Read and update static page/component content in secondary locales
  * Read and update default component properties in secondary locales
  * Read and update existing CMS items in secondary locales

  **Not supported:**

  * Creating new localized CMS items

  If you need additional localization features, please [open an issue](https://github.com/webflow/mcp-server/issues) or contact [developers@webflow.com](mailto:developers@webflow.com).
</Accordion>

## Node.js compatibility

The MCP server requires **Node.js version 22.3.0 or higher**. If you can't use this version as your default, use a version manager to switch Node.js versions per project.

### Using Node Version Manager (nvm)

**Install nvm:**

macOS/Linux:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
```

Windows: Download and install [nvm-windows](https://github.com/coreybutler/nvm-windows/releases)

**Install and use Node.js 22.3.0 or higher:**

```bash
nvm install 22.3.0
nvm use 22.3.0
nvm alias default 22.3.0
```

**Verify your Node.js version:**

```bash
node --version
```

<Tip>
  After changing Node.js versions, restart your AI client for the changes to take effect.
</Tip>

### Troubleshooting Node.js and NPM

<Accordion title="NPM and NPX issues">
  **Verify Node.js and NPM are installed:**

  ```bash
  node -v
  npm -v
  ```

  **Clear NPM cache if `npx` has issues:**

  ```bash
  npm cache clean --force
  ```

  **Fix NPM global package permissions:**

  If `npm -v` only works with `sudo`, you may have permission issues. See the [official NPM documentation](https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally) for solutions.

  <Note>
    If you make changes to your shell configuration (`.bashrc`, `.zshrc`, etc.), restart your terminal for changes to take effect.
  </Note>
</Accordion>

<Accordion title="Node.js version conflicts">
  If you have multiple Node.js versions installed and experience conflicts:

  **Option 1: Use nvm (recommended)**

  Install nvm and use it to manage Node.js versions as shown above.

  **Option 2: Set Node.js version per project**

  Create a `.nvmrc` file in your project directory:

  ```
  22.3.0
  ```

  Then run `nvm use` in that directory to automatically switch to the correct version.

  **Option 3: Uninstall conflicting versions**

  Remove old Node.js installations and install only version 22.3.0 or higher.
</Accordion>
