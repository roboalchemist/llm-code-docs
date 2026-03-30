# Source: https://firebase.google.com/docs/crashlytics/ai-assistance-mcp.md.txt

> [!WARNING]
> **Experimental:** MCP features for Crashlytics are Experimental, which means they aren't subject to any SLA or deprecation policy and could change in backwards-incompatible ways.

<br />

With Firebase Crashlytics MCP tools and prompts, you can interact with your
Crashlytics data using your MCP-capable AI-powered development tools, like
Gemini CLI, Claude Code, or Cursor. These Crashlytics MCP tools and prompts
provide critical context to your AI tool to help you manage, prioritize, debug,
and fix issues.

**After you [set up the Firebase MCP server](https://firebase.google.com/docs/crashlytics/ai-assistance-mcp#set-up-firebase-mcp-server),
you can use the MCP features for Crashlytics:**

[Guided workflow to prioritize and fix issues](https://firebase.google.com/docs/crashlytics/ai-assistance-mcp#guided-workflow-prioritize-and-fix)

[Free-form conversational debugging](https://firebase.google.com/docs/crashlytics/ai-assistance-mcp#free-form-conversational-debugging)

> [!IMPORTANT]
> **Important:** The currently available Crashlytics MCP tools and prompts are for use with apps that already use Crashlytics.

<br />

**What is MCP?**
[Model Context Protocol (MCP)](https://modelcontextprotocol.io/about)
is a standardized way for AI tools to access external tools and data sources.

<br />

*** ** * ** ***

## Before you begin: Set up the Firebase MCP server

This section describes the basic setup of the
[Firebase MCP server](https://firebase.google.com/docs/ai-assistance/mcp-server) so that you can use
Crashlytics-specific MCP commands, prompts, and tools (which are all
described later on this page).

#### Prerequisites

Make sure your environment meets these requirements:

- A working installation of [Node.js](https://www.nodejs.org/) and
  npm. Installing Node.js automatically installs the npm command tools.

- Your AI-powered development tool supports MCP integrations.

If you're working with a Unity project, review the
[FAQ about loading Crashlytics MCP tools and prompts](https://firebase.google.com/docs/crashlytics/ai-assistance-mcp#faq-crashlytics-mcp-tools-and-prompts-not-loading).

#### Configure your AI tool to use the Firebase MCP server

### Antigravity

To configure Antigravity to use the Firebase MCP server:

1. In Antigravity, click the menu in the Agent pane \> **MCP Servers**.
2. Select **Firebase** \> **Install**.

This automatically updates your `mcp_config.json` file, which you can view by
clicking **Manage MCP Servers** at the top of the MCP Store pane \>
**View raw config**, with the following content:

    {
      "mcpServers": {
        "firebase-mcp-server": {
          "command": "npx",
          "args": ["-y", "firebase-tools@latest", "mcp"]
        }
      }
    }

### Gemini CLI

The recommended way to set up the Gemini CLI to use the
Firebase MCP server is to install the
[Firebase extension for Gemini CLI](https://firebase.google.com/docs/crashlytics/gcli-extension):

    gemini extensions install https://github.com/gemini-cli-extensions/firebase/

Installing the Firebase extension automatically configures the Firebase MCP
server and also comes with a context file that can improve Gemini's Firebase
app development performance.

Alternatively, you can configure Gemini CLI to use the
Firebase MCP server (but not the Firebase extension context file), by editing
or creating one of the configuration files:

- In your project: `.gemini/settings.json`
- In your home directory: `~/.gemini/settings.json`

If the file doesn't yet exist, create it by right-clicking the parent
directory and selecting **New file**. Add the following contents to the file:

    {
      "mcpServers": {
        "firebase": {
          "command": "npx",
          "args": ["-y", "firebase-tools@latest", "mcp"]
        }
      }
    }

### Gemini Code Assist

The recommended way to set up Gemini Code Assist to use the
Firebase MCP server is to install the
[Firebase extension for Gemini CLI](https://firebase.google.com/docs/crashlytics/gcli-extension):

    gemini extensions install https://github.com/gemini-cli-extensions/firebase/

Installing the Firebase extension automatically configures the Firebase MCP
server and also comes with a context file that can improve Gemini's Firebase
app development performance.

Alternatively, you can configure Gemini Code Assist to use the
Firebase MCP server (but not the Firebase extension context file), by editing
or creating one of the configuration files:

- In your project: `.gemini/settings.json`
- In your home directory: `~/.gemini/settings.json`

If the file doesn't yet exist, create it by right-clicking the parent
directory and selecting **New file**. Add the following contents to the file:

    {
      "mcpServers": {
        "firebase": {
          "command": "npx",
          "args": ["-y", "firebase-tools@latest", "mcp"]
        }
      }
    }

### Firebase Studio

To configure Firebase Studio to use the Firebase MCP server, edit or
create the configuration file: `.idx/mcp.json`.

If the file doesn't yet exist, create it by right-clicking the parent
directory and selecting **New file**. Add the following contents to the file:

    {
      "mcpServers": {
        "firebase": {
          "command": "npx",
          "args": ["-y", "firebase-tools@latest", "mcp"]
        }
      }
    }

### Claude

#### Claude Code

- **Option 1**: Install via plugin (Recommended)

  The easiest way to set up the Firebase MCP server in Claude Code is to
  install the official Firebase plugin:
  1. Add the Firebase marketplace for Claude plugins:

         claude plugin marketplace add firebase/firebase-tools

  2. Install the Claude plugin for Firebase:

         claude plugin install firebase@firebase

  3. Verify the installation:

         claude plugin marketplace list

- **Option 2**: Configure MCP server manually

  Alternatively, you can manually configure the Firebase MCP server:
  1. Run the following command under your app folder:

         claude mcp add firebase npx -- -y firebase-tools@latest mcp

  2. Verify the installation:

         claude mcp list

     It should show:

         firebase: npx -y firebase-tools@latest mcp - ✓ Connected

#### Claude Desktop

To configure Claude Desktop to use the Firebase MCP server, edit the
`claude_desktop_config.json` file. You can open or create this file from the
**Claude \> Settings** menu. Select the **Developer** tab, then click
**Edit Config**.

    {
      "mcpServers": {
        "firebase": {
          "command": "npx",
          "args": ["-y", "firebase-tools@latest", "mcp"]
        }
      }
    }

### Cline

To configure Cline to use the Firebase MCP server, edit the
`cline_mcp_settings.json` file. You can open or create this file by clicking
the MCP Servers icon at the top of the Cline pane, then clicking the
**Configure MCP Servers** button.

    {
      "mcpServers": {
        "firebase": {
          "command": "npx",
          "args": ["-y", "firebase-tools@latest", "mcp"],
          "disabled": false
        }
      }
    }

### Cursor

Click the following button to add the Firebase MCP server to your global
Cursor configuration.

[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en/install-mcp?name=firebase&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyIteSIsImZpcmViYXNlLXRvb2xzQGxhdGVzdCIsIm1jcCJdfQ%3D%3D)

If you prefer to add the configuration manually or want to configure it for a
specific project, you can edit your `mcp.json` file.

- **For a specific project** : Edit `.cursor/mcp.json`
- **For all projects (global)** : Edit `~/.cursor/mcp.json`

    "mcpServers": {
      "firebase": {
        "command": "npx",
        "args": ["-y", "firebase-tools@latest", "mcp"]
      }
    }

### VS Code Copilot

To configure a single project, edit the `.vscode/mcp.json` file in your
workspace:

    "servers": {
      "firebase": {
        "type": "stdio",
        "command": "npx",
        "args": ["-y", "firebase-tools@latest", "mcp"]
      }
    }

To make the server available in every project you open, edit your user
settings, for example:

    "mcp": {
      "servers": {
        "firebase": {
          "type": "stdio",
          "command": "npx",
          "args": ["-y", "firebase-tools@latest", "mcp"]
        }
      }
    }

### Windsurf

To configure Windsurf Editor, edit the file
`~/.codeium/windsurf/mcp_config.json`:

    "mcpServers": {
      "firebase": {
        "command": "npx",
        "args": ["-y", "firebase-tools@latest", "mcp"]
      }
    }

In addition to the basic configuration described above for each AI tool, you can
[specify optional parameters](https://firebase.google.com/docs/ai-assistance/mcp-server#options).

> [!NOTE]
> **Note:** When the Firebase MCP server makes MCP tool calls, it uses the same user credentials that authorize the Firebase CLI in the environment where it's running. Depending on the environment, this could be a logged-in user or [Application Default Credentials](https://cloud.google.com/docs/authentication/application-default-credentials).

<br />

*** ** * ** ***

## *(Recommended)* Guided workflow to prioritize and fix issues with `crashlytics:connect`

Crashlytics provides a guided workflow that's conversational and flexible
to help you prioritize and fix Crashlytics issues in your app. For example,
your AI tool can fetch issues, explain issues, identify potential fixes, and
even make the code changes for you.

This guided workflow is available via the `crashlytics:connect` MCP command.

> [!NOTE]
> **Note:** Not all AI tools support MCP commands like this, but you can still [debug issues using free-form conversation](https://firebase.google.com/docs/crashlytics/ai-assistance-mcp##free-form-conversational-debugging).

#### Access and use the command

![Gemini CLI using crashlytics:connect command](https://firebase.google.com/static/docs/crashlytics/images/crashlytics-connect-gemini-cli.png) Use an AI tool, like the Gemini CLI, with the `crashlytics:connect` guided workflow.

1. If you haven't already,
   [set up the Firebase MCP server](https://firebase.google.com/docs/crashlytics/ai-assistance-mcp#set-up-firebase-mcp-server), and then
   start your AI tool.

2. Run the `crashlytics:connect` MCP command.

   Most AI tools provide a way to conveniently access this workflow.
   For example, if you're using the Gemini CLI, run the slash command
   `/crashlytics:connect`
3. Use your AI tool to help prioritize and fix Crashlytics issues,
   for example:

   - View a list of prioritized issues.
   - Debug a specific issue by providing its ID or URL.
   - Request more information about a crash.
   - Ask the agent its reasoning for a suggested root cause.

<br />

*** ** * ** ***

## Free-form conversational debugging

While we recommend
[using `crashlytics:connect` for the best debugging experience](https://firebase.google.com/docs/crashlytics/ai-assistance-mcp#debug-with-crashlytics-connect),
you can also debug issues using a free-form conversation with an AI tool that
has access to the Crashlytics MCP tools. This is especially important for
AI tools that don't yet support MCP prompts (often referred to as slash commands
or custom commands).

After you've [set up the Firebase MCP server](https://firebase.google.com/docs/crashlytics/ai-assistance-mcp#set-up-firebase-mcp-server),
try some of the following examples.

### Fetch an issue and crash context

When your AI tool has access to Crashlytics MCP tools, it can fetch critical
Crashlytics issue data like user and event counts, stacktraces, metadata,
and app version information.

Here are some example prompts:

- `A customer reported an issue during login when using our latest release. What
  Crashlytics issues do I have that could be related to this login trouble?`

  - To answer this question, your AI tool will likely read your code to understand where login happens and use various Crashlytics MCP tools to retrieve issue data. Your AI tool will then try to determine whether an issue exists in the latest version that relates to the login flow.
- `The previous on-call engineer was investigating issue abc123 but wasn't able
  to resolve it. She said she left some notes -- let's pick up where she left
  off.`

  - To answer this question, your AI tool will use various Crashlytics MCP tools to retrieve issue context and any notes posted to the issue. It might also fetch example crashes to resume the investigation into the issue.

### Document a debugging investigation

When debugging an issue, it's often helpful to maintain records for yourself or
your team. Crashlytics offers this capability in the Firebase console,
and your AI tool equipped with Crashlytics MCP tools can also help ---
for example: summarize an investigation, add a note with helpful metadata
(like a link to a Jira or GitHub issue), or close an issue after it's fixed.

Here are some example prompts:

- `Add a note to issue abc123 summarizing this investigation and the proposed
  fix.`
- `We weren't able to get to the bottom of this issue today, summarize what we
  learned and attach it to issue abc123 to pick back up later.`
- `Close issue abc123 and leave a note including the link to the PR that fixed
  the issue.`

<br />

*** ** * ** ***

## Crashlytics MCP tool reference

The following tables list the Crashlytics MCP tools that are available via
the Firebase MCP server.

After you've [set up the Firebase MCP server](https://firebase.google.com/docs/crashlytics/ai-assistance-mcp#set-up-firebase-mcp-server), your
AI tool can use these MCP tools to help you understand, debug, and manage
issues. These MCP tools are used in both the `crashlytics:connect` guided
workflow and in free-form conversations with your AI tool.

For the majority of use cases, these MCP tools are for LLM-use only and not for
*direct* use by a human developer. The LLM decides when to use these MCP tools
based on your interaction with your AI tool.

> [!NOTE]
> **Note:** You can also see this information using the command: `npx firebase-tools@latest mcp --generate-tool-list`

### Manage Crashlytics issues

The following table describes the tools available
to manage your Crashlytics issues.

| Tool Name | Feature Group | Description |
|---|---|---|
| crashlytics_create_note | crashlytics | Add a note to an issue from crashlytics. |
| crashlytics_delete_note | crashlytics | Delete a note from a Crashlytics issue. |
| crashlytics_update_issue | crashlytics | Use this to update the state of Crashlytics issue. |

### Fetch Crashlytics data

The following table describes the tools available
to get Crashlytics-related information about your apps.

| Tool Name | Feature Group | Description |
|---|---|---|
| crashlytics_get_issue | crashlytics | Gets data for a Crashlytics issue, which can be used as a starting point for debugging. |
| crashlytics_list_events | crashlytics | Use this to list the most recent events matching the given filters. Can be used to fetch sample crashes and exceptions for an issue, which will include stack traces and other data useful for debugging. |
| crashlytics_batch_get_events | crashlytics | Gets specific events by resource name. Can be used to fetch sample crashes and exceptions for an issue, which will include stack traces and other data useful for debugging. |
| crashlytics_list_notes | crashlytics | Use this to list all notes for an issue in Crashlytics. |
| crashlytics_get_report | crashlytics | Use this to request numerical reports from Crashlytics. The result aggregates the sum of events and impacted users, grouped by a dimension appropriate for that report. |

<br />

*** ** * ** ***

## Additional information

### How your data is used

Data governance is determined by the AI-powered development tool that you use,
and is subject to the terms defined by that AI tool.

### Pricing

Firebase doesn't charge you to use Crashlytics MCP tools and prompts or to
fetch Crashlytics data from our public API.

Any cost is determined by the AI-powered development tool that you use, and
could be determined by the volume of Crashlytics data that's used by the
AI tool. Note that Firebase doesn't offer an explicit way to control how much
data is loaded into context, but we do include sensible default guidance for the
model.

## Troubleshooting and FAQ

<br />

#### Crashlytics MCP tools and prompts aren't loading

<br />

The Firebase MCP server attempts to recognize when a codebase is using
Crashlytics by inspecting installed dependencies. This capability isn't yet
supported for Unity projects and doesn't cover some non-standard dependency
management systems for other platforms.

If Crashlytics MCP tools and prompts aren't loading for you, then as a
workaround, you can install the Firebase MCP server manually and use the
`--only crashlytics` argument to load Crashlytics MCP tools and prompts.

<br />

<br />