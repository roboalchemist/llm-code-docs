# Source: https://docs.xano.com/xano-cli/get-started.md

# Source: https://docs.xano.com/developer-mcp/get-started.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Developer MCP

> Install and configure the Xano Developer MCP for AI-assisted XanoScript development

export const BrowserFrame = props => {
  const {url = "xano.run", maxWidth = 820, className = "", lightSrc, darkSrc, alt = "", children} = props || ({});
  const style = typeof maxWidth === "number" ? {
    maxWidth: `${maxWidth}px`,
    margin: "16px 0"
  } : {
    maxWidth,
    margin: "16px 0"
  };
  const hasSwapImages = Boolean(lightSrc && darkSrc);
  return <div className={`browser-frame ${className}`.trim()} style={style}>
      <div className="browser-frame__top">
        <div className="browser-frame__controls" aria-hidden="true">
          <span className="browser-frame__dot browser-frame__dot--red" />
          <span className="browser-frame__dot browser-frame__dot--yellow" />
          <span className="browser-frame__dot browser-frame__dot--green" />
        </div>
        <div className="browser-frame__address">{url}</div>
      </div>

      <div className="browser-frame__body">
        {hasSwapImages ? <>
            <img className="browser-frame__img--light" src={lightSrc} alt={alt} />
            <img className="browser-frame__img--dark" src={darkSrc} alt={alt} />
          </> : children}
      </div>
    </div>;
};

The Xano Developer MCP (`@xano/developer-mcp`) is an MCP server that gives AI assistants superpowers for developing on Xano. It provides XanoScript documentation, code validation, and workflow guides directly to your AI tools.

<Info>
  **What does it do?**

  The Developer MCP is designed for **building with Xano**, not managing your Xano instance. It helps AI assistants:

  * Access XanoScript language documentation and syntax references
  * Validate XanoScript code for syntax errors in real-time
  * Retrieve Meta API, Run API, and CLI documentation on demand
  * Provide context-aware docs based on the file you're editing

  Looking to **manage your Xano instance** (create tables, build APIs, manage data) via MCP? See the [Xano MCP Server](/building/build-with-ai/xano-mcp) instead.
</Info>

## Installation

The Developer MCP requires Node.js 18 or later. Choose the installation method that matches your MCP client.

### Claude Code

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  claude mcp add xano -- npx -y @xano/developer-mcp
  ```
</BrowserFrame>

### Claude Desktop

Add the following to your Claude Desktop configuration file.

<Tabs>
  <Tab title="macOS">
    Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:
  </Tab>

  <Tab title="Windows">
    Edit `%APPDATA%\Claude\claude_desktop_config.json`:
  </Tab>
</Tabs>

```json  theme={null}
{
  "mcpServers": {
    "xano": {
      "command": "npx",
      "args": ["-y", "@xano/developer-mcp"]
    }
  }
}
```

### VS Code

Create or edit `.vscode/mcp.json` in your project:

```json  theme={null}
{
  "servers": {
    "xano": {
      "command": "npx",
      "args": ["-y", "@xano/developer-mcp"]
    }
  }
}
```

### Cursor

Open Cursor Settings > Tools & Integrations > New MCP Server, and add:

```json  theme={null}
{
  "xano": {
    "command": "npx",
    "args": ["-y", "@xano/developer-mcp"]
  }
}
```

### Windsurf

Open Windsurf Settings > Cascade > Manage Plugins > View Raw Config, and add:

```json  theme={null}
{
  "xano": {
    "command": "npx",
    "args": ["-y", "@xano/developer-mcp"]
  }
}
```

### Global npm Install

If you prefer a global install instead of `npx`:

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  npm install -g @xano/developer-mcp
  ```
</BrowserFrame>

Then reference the command directly in your MCP client configuration:

```json  theme={null}
{
  "xano": {
    "command": "xano-developer-mcp"
  }
}
```

***

## No Authentication Required

The Developer MCP runs entirely locally and serves documentation and validation tools. It does **not** connect to your Xano instance and requires no access tokens or credentials.

<Note>
  The APIs documented by the `meta_api_docs` and `run_api_docs` tools do require authentication when you call them directly. The MCP server itself just provides the documentation.
</Note>

***

## Verify Your Setup

After installation, verify the server is working by asking your AI assistant:

> "What version of the Xano Developer MCP is installed?"

The assistant should call `mcp_version` and return the current version number.

You can also try:

> "Validate this XanoScript: `var $x { value = 1 }`"

The assistant should call `validate_xanoscript` and confirm the code is valid.

***

## What's Next

<CardGroup cols={2}>
  <Card title="Tools Reference" icon="wrench" href="/developer-mcp/tools">
    Explore all 6 tools available in the Developer MCP
  </Card>

  <Card title="Resources & Library" icon="book" href="/developer-mcp/resources">
    Access MCP resources and use the package as an npm library
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).