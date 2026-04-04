# Source: https://firebase.google.com/docs/studio/mcp-servers.md.txt

# Connect to Model Context Protocol (MCP) servers

MCP servers provide Gemini with additional tools and data
sources. For example, by adding the [Firebase MCP server](https://firebase.google.com/docs/cli/mcp-server),
you can use natural language to explore your Cloud Firestore data while
building or debugging your application.

> [!CAUTION]
> **Caution:** Adding an MCP server to your workspace gives it permission to run code and potentially modify your app. Only add MCP servers from trusted sources.

## Prerequisites

If required by the MCP server, ensure you have a working installation of Node.js
and npm.

## Choose a compatible MCP server

Firebase Studio has foundational support for MCP servers, but not all MCP
servers are compatible. When choosing an MCP server, keep the following
compatibility details in mind:

- **Supported:**

  - Standard input/output (stdio) or Server-Sent Events (SSE)/Streamable HTTP transport servers
  - API key authentication using HTTP headers or environment variables
  - Tools provided by MCP servers
- **Not supported:**

  - Servers that require a graphical user interface or a desktop session
  - Prompts, sampling, or other resources provided by MCP servers

> [!NOTE]
> **Note:** You can pass environment variables to MCP servers through the `.env` file.

## Add an MCP server

To add an MCP server, you need to create or edit its configuration file.

- **For your first server** : [Create the configuration file](https://firebase.google.com/docs/studio/mcp-servers#config).
- **To add or adjust servers** : [Edit the server configuration](https://firebase.google.com/docs/studio/mcp-servers#server).

### Step 1: Create the configuration file

Interactive chat and Gemini CLI can both connect to MCP
servers, but use different configuration files:

- Interactive chat uses `.idx/mcp.json`.
- Gemini CLI uses `.gemini/settings.json`.

Create one or both files using the following instructions.

#### Interactive chat

In Code view, create `.idx/mcp.json` using
one of these methods:

- **Command Palette** : Open the Command Palette (`Shift+Ctrl+P`), and use the **Firebase Studio: Add MCP Server** command.
- **Interactive chat** : Click ![Customize tools icon](https://firebase.google.com/static/docs/studio/images/icons/customize-tools.png) **Customize Tools** in interactive chat and select **Add MCP server**.
- **Explorer** : From Explorer `(Ctrl+Shift+E)`, right-click the `.idx` directory and select **New file** . Name the file `mcp.json`.

#### Gemini CLI

In Code view, create `.gemini/settings.json`:

1. In Explorer `(Ctrl+Shift+E)`, check if the `.gemini` directory exists. If not, right-click the Explorer pane and select **New folder** . Name the folder `.gemini`.
2. Right-click the `.gemini` directory and select **New file** . Name the file `settings.json`.

For details about using MCP servers with Gemini CLI, [review the full
documentation](https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/mcp-server.md#configuration-structure).

### Step 2: Edit the server configuration

1. Open the server configuration file.

   > [!TIP]
   > **Tip:** To quickly open `.idx/mcp.json`, click ![Customize tools icon](https://firebase.google.com/static/docs/studio/images/icons/customize-tools.png) **Customize Tools** in interactive chat and select **Edit
   > Config**.

2. Add the server configuration to the content of the file. For example, to add
   the Firebase MCP server, enter:

       {
         "mcpServers": {
          "firebase": {
            "command": "npx",
            "args": [
              "-y",
              "firebase-tools@latest",
              "mcp"
             ]
           }
         }
       }

   This configuration file instructs Gemini which MCP server
   you want it to use. This example shows a single server called
   `firebase` that will use the `npx` command to install and run
   `firebase-tools@latest`.

   If your MCP server requires API key authentication, you can configure it in
   one of the following ways:
   - For remote HTTP MCP servers that require an API key in request headers,
     use the `headers` field. For example, to configure GitHub's MCP server:

         {
           "mcpServers": {
             "github": {
               "url": "https://api.githubcopilot.com/mcp/",
               "headers": {
                 "Authorization": "Bearer <ACCESS_TOKEN>"
               }
             }
           }
         }

   - For local stdio MCP servers that require an API key in environment
     variables, use the `env` field. For example, to configure a local build
     of GitHub's MCP server:

         {
           "mcpServers": {
             "github": {
               "command": "/path/to/github-mcp-server",
               "args": ["stdio"],
               "env": {
                 "GITHUB_PERSONAL_ACCESS_TOKEN": "<ACCESS_TOKEN>"
               }
             }
           }
         }

   - To avoid hardcoding secrets in `mcp.json`, you can optionally use the
     `${env:VARIABLE_NAME}` syntax. This will substitute in values from
     environment variables defined in a `.env` or `.env.local` file in your
     workspace root. For example:

         {
           "mcpServers": {
             "github": {
               "url": "https://api.githubcopilot.com/mcp/",
               "headers": {
                 "Authorization": "Bearer ${env:GITHUB_ACCESS_TOKEN}"
               }
             }
           }
         }

3. In the terminal (`Shift+Ctrl+C`), run any necessary commands to complete
   installation. For example, to use the Firebase MCP server, enter the
   following command to sign in to your account:

       firebase login --no-localhost

   Follow the instructions in the terminal to authorize the session. Some
   tools require a connected Firebase project. You can use the
   Firebase MCP server to create a project, or you can
   run the following command to initialize a Firebase project:

       firebase init

   This creates a `firebase.json` file in your root directory.

## Use MCP tools

After installing the MCP server you want to use, the tools or data it provides
are available in:

- Gemini CLI
- Interactive chat when using Agent mode and Agent (Auto-run) modes
- the App Prototyping agent

For example, if you add the Firebase MCP server, you could ask
Gemini to fetch the SDK config for the current project,
retrieve data stored in Cloud Firestore and Realtime Database, help you set up
Firebase services, [and more](https://firebase.google.com/docs/cli/mcp-server).

In interactive chat, type `/` to see a list of available
[MCP prompts](https://modelcontextprotocol.io/specification/2025-06-18/server/prompts).

![List of available MCP prompts](https://firebase.google.com/static/docs/studio/images/mcp-prompts.png)

### Check or adjust tools

You can manage which tools are active in interactive chat:

1. Click ![Customize tools icon](https://firebase.google.com/static/docs/studio/images/icons/customize-tools.png) **Customize Tools** in interactive chat to see a list of all available tools from your configured MCP servers.
2. Use the checkboxes to enable or disable an entire server or individual tools.

![List of available MCP tools](https://firebase.google.com/static/docs/studio/images/mcp-tool-list.png)

## Troubleshoot MCP servers

If you encounter issues with an MCP server, use these steps to diagnose the
problem.

### Check the logs for errors

1. Open the Output panel (`Shift+Ctrl+U`).
2. In the drop-down menu, select **Gemini**.
3. Check for messages that begin with an `[MCPManager]` tag. These logs show which servers are configured, which tools were successfully added, and any error messages.

### Rebuild the environment

If an MCP server fails to install or connect, try rebuilding your workspace:

1. Open the Command Palette (`Shift+Ctrl+P`).
2. Run the **Firebase Studio: Rebuild Environment** command.
3. After the workspace rebuilds, check if the MCP server connects.

### If tools aren't being used

If the MCP server connects but Gemini doesn't use its tools:

- **Start a new chat session** : This ensures Gemini picks up the latest tool configuration. [Learn how to manage chat history](https://firebase.google.com/docs/studio/try-gemini#manage-chat-history).
- **Be specific in your prompt** : If Gemini can accomplish the task without using an MCP tool, it might attempt a different method. If you want to use a specific tool, try naming the tool. For example: "Use `firebase_get_sdk_config` to get the SDK config for the current project."
- **Join the Google Developer Program** : [Check if your account is enrolled](https://developers.google.com/profile/u/_/dashboard).

## Next steps

- [Learn more about the Firebase MCP server](https://firebase.google.com/docs/cli/mcp-server).
- [Complete the Firebase Studio MCP server codelab](https://firebase.google.com/codelabs/firebase-mcp-in-studio#0).