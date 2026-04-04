# Source: https://docs.xano.com/ai-tools/mcp-builder/connecting-clients.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Connecting Clients

export const McpJsonGenerator = () => {
  const [name, setName] = useState("");
  const [url, setUrl] = useState("");
  const [token, setToken] = useState("");
  const [showToken, setShowToken] = useState(false);
  const [copied, setCopied] = useState(false);
  const trimmedName = name.trim();
  const trimmedUrl = url.trim();
  const trimmedToken = token.trim();
  const serverKey = trimmedName || "xano";
  const serverConfig = {
    serverUrl: trimmedUrl || "<url>"
  };
  if (trimmedToken) {
    serverConfig.headers = {
      Authorization: "Bearer " + trimmedToken
    };
  }
  const config = {
    mcpServers: {
      [serverKey]: serverConfig
    }
  };
  const jsonString = JSON.stringify(config, null, 2);
  const handleCopy = () => {
    navigator.clipboard.writeText(jsonString);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };
  const inputClass = "w-full px-2 py-1.5 border rounded-md text-xs bg-white dark:bg-gray-700 dark:border-gray-600 dark:text-gray-100";
  return <div className="not-prose border rounded-lg bg-gray-50 dark:bg-gray-800 transition-colors overflow-hidden">
      <div className="p-5">
        <div className="flex items-center justify-between mb-4">
          <p className="text-xs font-semibold uppercase tracking-wider text-gray-400 dark:text-gray-500">
            Connection Details
          </p>
          {(trimmedName || trimmedUrl || trimmedToken) && <button onClick={() => {
    setName("");
    setUrl("");
    setToken("");
    setShowToken(false);
  }} className="text-xs text-gray-400 hover:text-gray-600 dark:hover:text-gray-300 transition-colors">
              Clear all
            </button>}
        </div>

        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium mb-1">Server name</label>
            <input type="text" placeholder="e.g. xano" value={name} onChange={e => setName(e.target.value)} className={inputClass} />
            <p className="mt-1 text-xs text-gray-400 dark:text-gray-500">
              The key used in your MCP config file.
            </p>
          </div>

          <div>
            <label className="block text-sm font-medium mb-1">Connection URL</label>
            <input type="text" placeholder="https://xxxx.n7d.xano.io/x2/mcp/meta/mcp/streaming" value={url} onChange={e => setUrl(e.target.value)} className={inputClass} />
          </div>

          <div>
            <label className="block text-sm font-medium mb-1">
              Auth token
              <span className="ml-1 font-normal text-gray-400 dark:text-gray-500">(optional)</span>
            </label>
            <div className="relative">
              <input type={showToken ? "text" : "password"} placeholder="eyJ..." value={token} onChange={e => setToken(e.target.value)} className={inputClass + " pr-16"} />
              {trimmedToken && <button onClick={() => setShowToken(!showToken)} className="absolute right-2.5 top-1/2 -translate-y-1/2 text-xs text-gray-400 hover:text-gray-600 dark:hover:text-gray-300 transition-colors">
                  {showToken ? "Hide" : "Show"}
                </button>}
            </div>
          </div>
        </div>
      </div>

      <div className="border-t border-gray-200 dark:border-gray-700" />

      <div className="p-5">
        <p className="text-xs font-semibold uppercase tracking-wider text-gray-400 dark:text-gray-500 mb-3">
          Generated JSON
        </p>
        <pre className="p-3 bg-gray-900 text-green-300 text-xs rounded-md overflow-auto whitespace-pre-wrap break-all">
          {jsonString}
        </pre>
        <button onClick={handleCopy} className="mt-2 px-3 py-1.5 border border-gray-300 dark:border-gray-600 text-xs text-gray-500 dark:text-gray-400 rounded-md hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors">
          {copied ? "Copied!" : "Copy JSON"}
        </button>
      </div>
    </div>;
};

export const CursorInstallLink = () => {
  const [name, setName] = useState("");
  const [url, setUrl] = useState("");
  const [token, setToken] = useState("");
  const [showToken, setShowToken] = useState(false);
  const [copied, setCopied] = useState(false);
  const [expanded, setExpanded] = useState(false);
  const trimmedUrl = url.trim();
  const trimmedToken = token.trim();
  const trimmedName = name.trim();
  const isUrlValid = trimmedUrl.length > 0 && trimmedUrl.startsWith("https://") && trimmedUrl.includes("x2/mcp");
  const hasSSE = trimmedUrl.replace(/\/+$/, "").endsWith("/sse");
  const isTokenValid = !trimmedToken || trimmedToken.startsWith("eyJ");
  const isNameProvided = trimmedName.length > 0;
  const hasAnyInput = trimmedName || trimmedUrl || trimmedToken;
  let mcpUrl = "";
  let webInstallUrl = "";
  let deepLinkUrl = "";
  if (isUrlValid) {
    let normalized = trimmedUrl.replace(/\/+$/, "");
    if (normalized.endsWith("/sse")) {
      normalized = normalized.slice(0, -4) + "/streaming";
    }
    if (!normalized.endsWith("/streaming")) {
      normalized = normalized + "/streaming";
    }
    if (trimmedToken) {
      const idx = normalized.lastIndexOf("/streaming");
      normalized = normalized.substring(0, idx) + "/" + trimmedToken + "/streaming";
    }
    mcpUrl = normalized;
    const config = JSON.stringify({
      url: mcpUrl
    });
    const base64Config = btoa(config);
    const encodedName = encodeURIComponent(trimmedName || "xano-mcp");
    webInstallUrl = `https://cursor.com/en/install-mcp?name=${encodedName}&config=${base64Config}`;
    deepLinkUrl = `cursor://anysphere.cursor-deeplink/mcp/install?name=${encodedName}&config=${base64Config}`;
  }
  const showOutput = isUrlValid && isTokenValid && isNameProvided && mcpUrl;
  const handleCopy = () => {
    navigator.clipboard.writeText(deepLinkUrl);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };
  const handleClear = () => {
    setName("");
    setUrl("");
    setToken("");
    setShowToken(false);
    setCopied(false);
    setExpanded(false);
  };
  const inputClass = "w-full px-2 py-1.5 border rounded-md text-xs bg-white dark:bg-gray-700 dark:border-gray-600 dark:text-gray-100";
  return <div className="not-prose border rounded-lg bg-gray-50 dark:bg-gray-800 transition-colors overflow-hidden">

      {}
      <div className="p-5">
        <div className="flex items-center justify-between mb-4">
          <p className="text-xs font-semibold uppercase tracking-wider text-gray-400 dark:text-gray-500">
            Connection Details
          </p>
          {hasAnyInput && <button onClick={handleClear} className="text-xs text-gray-400 hover:text-gray-600 dark:hover:text-gray-300 transition-colors">
              Clear all
            </button>}
        </div>

        <div className="space-y-4">
          {}
          <div>
            <label className="block text-sm font-medium mb-1">Server name</label>
            <input type="text" placeholder="e.g. xano-meta" value={name} onChange={e => setName(e.target.value)} className={inputClass} />
            <p className="mt-1 text-xs text-gray-400 dark:text-gray-500">
              Shows up in Cursor's MCP server list.
            </p>
          </div>

          {}
          <div>
            <label className="block text-sm font-medium mb-1">MCP server URL</label>
            <input type="text" placeholder="https://xxxx.n7d.xano.io/x2/mcp/meta/mcp/streaming" value={url} onChange={e => setUrl(e.target.value)} className={inputClass} />
            {trimmedUrl && !trimmedUrl.startsWith("https://") ? <p className="mt-1 text-xs text-red-500">URL must start with https://</p> : trimmedUrl && !trimmedUrl.includes("x2/mcp") ? <p className="mt-1 text-xs text-red-500">URL must contain x2/mcp</p> : hasSSE ? <p className="mt-1 text-xs text-amber-500">
                /sse will be replaced with /streaming for Cursor's streamable HTTP transport.
              </p> : <p className="mt-1 text-xs text-gray-400 dark:text-gray-500">
                The <code className="text-xs">/mcp/...</code> endpoint Cursor will connect to.
              </p>}
          </div>

          {}
          <div>
            <label className="block text-sm font-medium mb-1">
              Auth token
              <span className="ml-1 font-normal text-gray-400 dark:text-gray-500">(optional)</span>
            </label>
            <div className="relative">
              <input type={showToken ? "text" : "password"} placeholder="eyJ..." value={token} onChange={e => setToken(e.target.value)} className={inputClass + " pr-16"} />
              {trimmedToken && <button onClick={() => setShowToken(!showToken)} className="absolute right-2.5 top-1/2 -translate-y-1/2 text-xs text-gray-400 hover:text-gray-600 dark:hover:text-gray-300 transition-colors">
                  {showToken ? "Hide" : "Show"}
                </button>}
            </div>
            {trimmedToken && !isTokenValid ? <p className="mt-1 text-xs text-red-500">Token should be a valid JWE (starts with eyJ)</p> : trimmedToken && isTokenValid ? <p className="mt-1 text-xs text-green-500">Valid token format</p> : <p className="mt-1 text-xs text-gray-400 dark:text-gray-500">
                Embedded in the URL. Rotate if shared.
              </p>}
          </div>
        </div>
      </div>

      {}
      {showOutput && <>
          <div className="border-t border-gray-200 dark:border-gray-700" />

          {}
          <div className="p-5">
            <p className="text-xs font-semibold uppercase tracking-wider text-gray-400 dark:text-gray-500 mb-4">
              Install
            </p>

            <div className="flex items-center gap-3">
              {}
              <a href={webInstallUrl} target="_blank" rel="noopener noreferrer">
                <img src="https://cursor.com/deeplink/mcp-install-dark.svg" alt="Install MCP Server in Cursor" style={{
    height: "32px"
  }} />
              </a>

              {}
              <button onClick={handleCopy} className="px-3 py-1.5 border border-gray-300 dark:border-gray-600 text-xs text-gray-500 dark:text-gray-400 rounded-md hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors">
                {copied ? "Copied!" : "Copy install link"}
              </button>

              {}
              <button onClick={() => setExpanded(!expanded)} className="px-3 py-1.5 border border-gray-300 dark:border-gray-600 text-xs text-gray-500 dark:text-gray-400 rounded-md hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors">
                {expanded ? "Hide link preview" : "Show link preview"}
              </button>
            </div>

            <div>
              {expanded && <pre className="mt-2 p-3 bg-gray-900 text-green-300 text-xs rounded-md overflow-auto whitespace-pre-wrap break-all">
                  {deepLinkUrl}
                </pre>}
            </div>
          </div>
        </>}
    </div>;
};

## Before We Begin

Gather the following information, which you'll need regardless of client.

<Steps>
  <Step title="Name">
    This is just a name you want to give your MCP server. Make sure it is unique to other MCP servers you're using, and is human readable so you can easily keep track of what each server does.
  </Step>

  <Step title="URL">
    **For the Xano MCP Server**

    > Each instance has its own unique connection URL. The URL can be found inside of your Instance Settings panel from the instance selection screen by clicking the <span class="ui-bubble"><Icon icon="gear" /></span> icon next to the instance you want to connect to.

    > When creating a URL, you'll need to choose the scope of tools the URL provides. Each client will have its own limits on how many tools can be available at once, so make sure to consult your client's documentation for more information.

    **For an MCP Server you built in Xano**

    > Click the <span class="ui-bubble"><Icon icon="link-simple" /> Connection URL</span> button next to the MCP server you want in the <span class="ui-bubble"><Icon icon="sparkles" /> AI</span> > <span class="ui-bubble"><Icon icon="server" /> MCP Servers</span> screen.
  </Step>

  <Step title="Token">
    **For the Xano MCP Server**

    > The Xano MCP Server token can be found in the same place you retrieved your URL. See [Generating an Access Token](/xano-features/metadata-api#generate-an-access-token) for more information.

    **For an MCP Server you built in Xano**

    > The token for a custom MCP server is generated the same way your other auth tokens are generated, usually as part of your `signup` and `login` API logic.
  </Step>
</Steps>

***

<Columns cols={4}>
  <Card title="Claude Code" icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/claude-ai-icon.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=77edf5396d1a9fe79c2d882b4cfe942a" href="#claude-code" width="256" height="257" data-path="images/icons/claude-ai-icon.svg" />

  <Card title="Claude Desktop" icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/claude-ai-icon.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=77edf5396d1a9fe79c2d882b4cfe942a" href="#claude-desktop--web" width="256" height="257" data-path="images/icons/claude-ai-icon.svg" />

  <Card title="Cursor" icon="https://mintcdn.com/xano-997cb9ee/How4y2-NUVnTIPUm/images/icons/Cursor_light.svg?fit=max&auto=format&n=How4y2-NUVnTIPUm&q=85&s=d215b3668eb9d4c3ff535f9aca013588" href="#cursor" width="467" height="532" data-path="images/icons/Cursor_light.svg" />

  <Card title="Windsurf" icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/Windsurf_light.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=542d34e733783e40a26d359de9dca307" href="#windsurf" width="1024" height="1024" data-path="images/icons/Windsurf_light.svg" />

  <Card title="Antigravity" icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/antigravity.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=a56089bb77619e8d8d019d4aac5ffb80" href="#antigravity" width="16" height="15" data-path="images/icons/antigravity.svg" />

  <Card title="VS Code" icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/vscode.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=c9ca342a4c7cc10adcf78c89f822c596" href="#vs-code" width="100" height="100" data-path="images/icons/vscode.svg" />

  <Card title="Raycast" icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/raycast.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=ef9ce6614fc5e84fa07b6725efa64de5" href="#raycast" width="28" height="28" data-path="images/icons/raycast.svg" />

  <Card title="Warp" icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/warp.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=fdd7beb4d6ccf935e33e1c30511ca6d1" href="#warp" width="400" height="400" data-path="images/icons/warp.svg" />
</Columns>

***

## <Icon icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/claude-ai-icon.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=77edf5396d1a9fe79c2d882b4cfe942a" width="256" height="257" data-path="images/icons/claude-ai-icon.svg" /> Claude Code

Learn how to connect the Xano MCP Server to Clade

In your terminal, execute the following command:

```bash  theme={null}
claude mcp add --transport http <name> <url> --header "Authorization: Bearer <token>"
```

***

## <Icon icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/claude-ai-icon.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=77edf5396d1a9fe79c2d882b4cfe942a" width="256" height="257" data-path="images/icons/claude-ai-icon.svg" /> Claude Desktop / Web

<Note>
  Claude on the Web can not connect to the Xano Developer MCP because it runs locally. Use Claude Desktop or Claude Code (recommended).
</Note>

For the Xano MCP Server or a server you built that requires authentication, you'll need to embed the token in the server URL, as shown below.

```bash  theme={null}
<url>/<token>/streaming
```

**For Claude Team and Enterprise Plans**

> Make sure an Owner or Primary Owner have taken the correct preliminary steps outlined in [Anthropic's documentation](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp). Do not configure OAuth settings; Xano's MCP Servers do not support OAuth at this time.

1. Navigate to Settings > Connectors.
2. Locate the "Connectors" section.
3. Find the custom connector your Owner added in the list (it will have a "Custom" label).
4. Click "Connect" to authenticate and start using the connector with Claude.

**For Claude Pro and Max Plans**

1. Navigate to Settings > Connectors.
2. Locate the "Connectors" section.
3. Click "Add custom connector" at the bottom of the section.
4. Add your connector's remote MCP server URL.
5. Finish configuring your connector by clicking "Add."

***

## <Icon icon="https://mintcdn.com/xano-997cb9ee/How4y2-NUVnTIPUm/images/icons/Cursor_light.svg?fit=max&auto=format&n=How4y2-NUVnTIPUm&q=85&s=d215b3668eb9d4c3ff535f9aca013588" width="467" height="532" data-path="images/icons/Cursor_light.svg" /><Icon icon="https://mintcdn.com/xano-997cb9ee/How4y2-NUVnTIPUm/images/icons/Cursor_dark.svg?fit=max&auto=format&n=How4y2-NUVnTIPUm&q=85&s=280459277edcf35c871156a9c402bbb2" width="467" height="532" data-path="images/icons/Cursor_dark.svg" /> Cursor

Cursor supports one-click MCP server installation via install links. Use the generator below to create yours.

<CursorInstallLink />

***

## <Icon icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/Windsurf_light.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=542d34e733783e40a26d359de9dca307" width="1024" height="1024" data-path="images/icons/Windsurf_light.svg" /><Icon icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/Windsurf_dark.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=40947ecb9252732deb925a4e4fac0fa2" width="1024" height="1024" data-path="images/icons/Windsurf_dark.svg" /> Windsurf

<Steps>
  <Step title="Access your Windsurf settings">
    Head to Windsurf Settings > Cascade and click **MCP Marketplace**.

    Click the <Icon icon="gear" /> icon to access your `mcp_config.json` file directly.
  </Step>

  <Step title="Add an entry for your MCP server">
    Use the generator below to get the correct JSON.

    <McpJsonGenerator />
  </Step>
</Steps>

***

## <Icon icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/antigravity.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=a56089bb77619e8d8d019d4aac5ffb80" width="16" height="15" data-path="images/icons/antigravity.svg" /> Antigravity

<Steps>
  <Step title="Access your Antigravity MCP settings">
    1. Open the MCP store via the "..." dropdown at the top of the editor's agent panel.
    2. Click on "Manage MCP Servers"
    3. Click on "View raw config"
    4. Modify the mcp\_config.json with your custom MCP server configuration.
  </Step>

  <Step title="Add an entry for your MCP server">
    Use the generator below to get the correct JSON.

    <McpJsonGenerator />
  </Step>
</Steps>

***

## <Icon icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/vscode.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=c9ca342a4c7cc10adcf78c89f822c596" width="100" height="100" data-path="images/icons/vscode.svg" /> VS Code

These instructions may work for other VS Code-based IDEs, but we recommend consulting that client's official documentation for more specific instructions.

**Per-project**:
Create or open `.vscode/mcp.json` in your workspace and add the configuration generated below.

**Across multiple projects**:

1. Run the **MCP: Open User Configuration** command, which opens the `mcp.json` file for your user profile. Add the configuration generated below.

<McpJsonGenerator />

***

## <Icon icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/raycast.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=ef9ce6614fc5e84fa07b6725efa64de5" width="28" height="28" data-path="images/icons/raycast.svg" /> Raycast

1. Run the **Manage MCP Servers** command and use the **Open Servers Folder** action. Open the `mcp-config.json` file and add the configuration generated below.

<McpJsonGenerator />

***

## <Icon icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/warp.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=fdd7beb4d6ccf935e33e1c30511ca6d1" width="400" height="400" data-path="images/icons/warp.svg" /> Warp

1. Access **Warp Drive** and click **MCP Servers** in your Personal settings.
2. Click **+ Add** and add the configuration generated below.

<McpJsonGenerator />

***


Built with [Mintlify](https://mintlify.com).