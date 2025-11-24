# Source: https://docs.augmentcode.com/setup-augment/mcp.md

# Source: https://docs.augmentcode.com/jetbrains/setup-augment/mcp.md

# Setup Model Context Protocol servers

> Use Model Context Protocol (MCP) servers with Augment to expand Augment's capabilities with external tools and data sources.

export const Command = ({text}) => <span className="font-bold">{text}</span>;

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

## About Model Context Protocol servers

Augment Agent can utilize external integrations through Model Context Protocol (MCP) to access external systems for information and integrate tools to take actions. MCP is an open protocol that provides a standardized way to connect AI models to different data sources and tools. MCP servers can be used to access local or remote databases, run automated browser testing, send messages to Slack or even play music on Spotify.

## Easy MCP: One-Click Integrations

> **New:** Easy MCP launched on July 30, 2025, making it easier than ever to connect popular developer tools to Augment Code.

Easy MCP is a new feature in the Augment Code extension that transforms complex MCP server setup into a single click. Instead of manually configuring servers, hunting for GitHub repos, or editing JSON files, you can now connect popular developer tools with just an API token or OAuth approval.

### Available Easy MCP Integrations

Easy MCP provides one-click access to these popular developer tools:

#### CircleCI

* **Context:** Build logs, test insights, flaky-test detection
* **Sample prompt:** "Find the latest failed pipeline on my branch and surface the failing tests."
* **Setup:** Click "+", paste your CircleCI API token, and you're connected.

#### MongoDB

* **Context:** Data exploration, database management, and context-aware code generation
* **Sample prompt:** "Analyze my user collection schema and suggest optimizations for our new search feature."
* **Setup:** One-click OAuth connection to your MongoDB instance.

#### Redis

* **Context:** Keyspace introspection, TTL audits, and migration helpers
* **Sample prompt:** "Generate a migration script to move expiring session keys to the new namespace."
* **Setup:** Connect with your Redis credentials in seconds.

### Getting Started with Easy MCP

1. Open the Augment Code extension in your JetBrains IDE
2. Navigate to the Easy MCP pane in the settings
3. Click the "+" button next to your desired integration
4. Paste an API token or approve OAuth
5. Start using the integration immediately in your Agent conversations

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/EasyMCP.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=c02010664a36e319631e3f5367f5f00e" className="rounded-xl" data-og-width="1078" width="1078" data-og-height="646" height="646" data-path="images/EasyMCP.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/EasyMCP.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=b26a28d983527d327bc35e249eabf1a8 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/EasyMCP.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7e06026e10eefc855da6579dac1dea47 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/EasyMCP.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=3c6df59927adaa82ba7427ad8f0defa2 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/EasyMCP.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=849c567deb9a052d933a4aa31f492dec 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/EasyMCP.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=3e66c48df372bb4e699350f8073ff0c6 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/EasyMCP.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=cda0cb53a2619c7cb2adffe3a12c3c38 2500w" />

From that moment on, Augment Code streams your tool's live context into every suggestion and autonomous Agent run.

## Advanced Configuration: Settings Panel

For developers who need custom MCP server configurations or want to use servers not available through Easy MCP, you can configure MCP servers manually using the Augment Settings Panel.

To access the settings panel, select the gear icon in the upper right of the Augment panel. Once the settings panel is open, you will see a section for MCP servers.

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=f34e3682127f6e6ba2dfc5a4ae7fd8a5" className="rounded-xl" data-og-width="1296" width="1296" data-og-height="556" height="556" data-path="images/settings-panel-mcp.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=a6dff18658e5c7454fa009cc484467db 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=dbc7a07976708c4fc72a662b98c06c60 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=e382a538a495053c3ca1a3c01d5e85ba 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=2efdfd04627b5a659795e5b74e672b4d 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=d0f3ce6ce06c668a2f3160a35c0586e5 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=e4b1e413786735c373fb6ec386cd676e 2500w" />

Fill in the `name` and `command` fields. The `name` field must be a unique name for the server. The `command` field is the command to run the server. Environment variables have their own section and no longer need to be specified in the command.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/mcp-env.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=20d9ffa2c683194ec1d66afe390f6f9d" className="rounded-xl" data-og-width="1090" width="1090" data-og-height="586" height="586" data-path="images/mcp-env.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/mcp-env.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=e9c87679180a6db78e05d7cce22845ff 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/mcp-env.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=e7e5805c874eb5e006c27ee3f52360fa 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/mcp-env.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=8930b7ececcdd06705dcc9d9ed86ef12 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/mcp-env.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=8e9b4f557196621ab4d45dd52defbda7 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/mcp-env.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=bd0ff7868ab46ea8325a6b9ed1856294 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/mcp-env.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=4cba9d7e59969d4a48aa630ab14932a7 2500w" />

To add additional servers, click the `+` button next to the `MCP` header.
To edit a configuration or to delete a server, click the `...` button next to the server name.

### Add a Remote MCP server

If your MCP server runs remotely (for example, a hosted service), click the "+ Add remote MCP" button in the MCP section. Remote MCP connections support both HTTP and SSE (Server‑Sent Events).

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp-remote.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=21086d1c640c6e20975aa7207532be78" className="rounded-xl" data-og-width="1036" width="1036" data-og-height="676" height="676" data-path="images/settings-panel-mcp-remote.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp-remote.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=3ac00d4975d2791c378a0e24b7fd1457 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp-remote.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=4d92460a09146279b73693c6af5be240 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp-remote.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=2a9dfd961063e277d0dee794b71b0b47 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp-remote.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=cdbad5fac2856fe1fb9bc272cb22622d 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp-remote.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=d99df8defa992c69589501c7db0e0204 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp-remote.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=7f5c7e96f585a368523586154bfd696e 2500w" />

* Connection Type: choose HTTP or SSE
* Name: a unique display name for the server
* URL: the base URL to your MCP server (e.g., [https://api.example.com](https://api.example.com))

Remote MCP servers appear alongside your local MCP servers in the list. You can edit or remove them using the "..." menu next to the server name.

## Server compatibility

Not all MCP servers are compatible with Augment's models. The MCP standard, implementation of specific servers, and Augment's MCP support are frequently being updated, so check compatibility frequently.
