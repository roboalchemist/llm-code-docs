# Source: https://firebase.google.com/docs/ai-assistance/mcp-server.md.txt

<br />

[Video](https://www.youtube.com/watch?v=kgf4yLoYNrE)

You can use the
[Firebase MCP server](https://github.com/firebase/firebase-tools/tree/master/src/mcp)
to give AI-powered development tools the ability to work with your
Firebase projects and your app's codebase.

The Firebase MCP server works with
any tool that can act as an MCP client, including:
Antigravity,
Gemini CLI and Gemini Code Assist,
Firebase Studio,
Claude Code and Claude Desktop,
Cline,
Cursor,
VS Code Copilot,
Windsurf, and more!

[Jump to setup instructions](https://firebase.google.com/docs/ai-assistance/mcp-server#setup)

## Benefits of the MCP server

An editor configured to use the Firebase MCP server can use its AI capabilities
to help you:

- Create and manage Firebase projects
- Manage your Firebase Authentication users
- Work with data in Cloud Firestore and Firebase Data Connect
- Retrieve Firebase Data Connect schemas
- Understand your security rules for Firestore and Cloud Storage for Firebase
- Send messages with Firebase Cloud Messaging

These are only partial lists; see the [server capabilities](https://firebase.google.com/docs/ai-assistance/mcp-server#capabilities)
section for a complete list of tools available to your editor.

> [!TIP]
> **Tip:** Consider using [Firebase agent skills](https://firebase.google.com/docs/ai-assistance/agent-skills) alongside the MCP server to help your AI assistant understand Firebase best practices and execute complex tasks with higher accuracy and lower cost. For example, for tasks like setting up services like Authentication, Cloud Firestore, or Firebase AI Logic, or deploying web apps to Firebase Hosting or App Hosting, agent skills can provide a more guided and efficient experience than prompts like `/firebase:init` or `/firebase:deploy`. When you have both the Firebase MCP server and Firebase agent skills installed, skills can teach models how to use the MCP tools to accomplish complex tasks efficiently.

## Set up your MCP client

The Firebase MCP server can work with any MCP client that supports standard I/O
(stdio) as the transport medium.

When the Firebase MCP server makes tool calls, it uses the same user
credentials that authorize the Firebase CLI in the environment where it's
running. This could be a logged-in user or
[Application Default Credentials](https://cloud.google.com/docs/authentication/application-default-credentials),
depending on the environment.

### Before you begin

Make sure you have a working installation of Node.js and npm.

### Basic configuration

Here are basic configuration instructions for using the Firebase MCP server with
some popular AI-assistive tools:

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
[Firebase extension for Gemini CLI](https://firebase.google.com/docs/ai-assistance/gcli-extension):

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
[Firebase extension for Gemini CLI](https://firebase.google.com/docs/ai-assistance/gcli-extension):

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

### Optional configuration

In addition to the basic configuration for each client, shown earlier, there are
two optional parameters you can specify:

- `--dir ABSOLUTE_DIR_PATH`: The absolute path of a
  directory containing `firebase.json`, to set a project context for the MCP
  server. If unspecified, the `get_project_directory` and
  `set_project_directory` tools become available and the default directory will
  be the working directory where the MCP server was started.

- `--only FEATURE_1,FEATURE_2`: A
  comma-separated list of feature groups to activate. Use this to limit the
  tools exposed to only features you are actively using. Note that the core
  tools are always available

For example:

    "firebase": {
      "command": "npx",
      "args": [
        "-y",
        "firebase-tools@latest", "mcp",
        "--dir", "/Users/turing/my-project",
        "--only", "auth,firestore,storage"
      ]
    }

## MCP server capabilities

The Firebase MCP server provides three different categories of MCP features:

- [**Prompts**](https://firebase.google.com/docs/ai-assistance/mcp-server#prompts): A library of pre-written prompts that you can run;
  they're optimized for developing and running an app with Firebase

- [**Tools**](https://firebase.google.com/docs/ai-assistance/mcp-server#tools): A set of tools intended for use by LLMs that help them
  work directly with your Firebase project (with your approval!)

- [**Resources**](https://firebase.google.com/docs/ai-assistance/mcp-server#resources): Documentation files intended for use by LLMs to
  give them more guidance and context to complete a task or goal

### Prompts

The Firebase MCP server comes with a library of pre-written prompts optimized
for developing and running an app with Firebase. You can use these prompts to
complete various common tasks or goals with your agentic AI assistants.

The following table describes the prompts the MCP server makes available.

Most development tools that support MCP provide a convenient way to run these
prompts. For example, Gemini CLI makes these prompts available as
slash commands:

    /firebase:init

In the Gemini CLI, start typing `/firebase:` to see a list of available
commands.

> [!NOTE]
> **Note:** You can also see this information using the command:   
> `npx firebase-tools@latest mcp --generate-prompt-list`

| Prompt Name | Feature Group | Description |
|---|---|---|
| firebase:deploy | core | Use this command to deploy resources to Firebase. Arguments: \<prompt\> (optional): any specific instructions you wish to provide about deploying |
| firebase:init | core | Use this command to set up Firebase services, like backend and AI features. |
| crashlytics:connect | crashlytics | Use this command to access a Firebase application's Crashlytics data. |

### Tools

The Firebase MCP server also provides a number of tools intended for use by LLMs
that help them work directly with your Firebase project (with your approval!).
Unlike with prompts, you don't call these tools directly; rather, models that
support tool calling (such as Gemini, Claude, and GPT) can automatically call
these tools to perform development tasks when needed.

The following table describes the tools the MCP server makes available.

> [!NOTE]
> **Note:** You can also see this information using the command:   
> `npx firebase-tools@latest mcp --generate-tool-list`

| Tool Name | Feature Group | Description |
|---|---|---|
| firebase_login | core | Use this to sign the user into the Firebase CLI and Firebase MCP server. This requires a Google Account, and sign in is required to create and work with Firebase Projects. |
| firebase_logout | core | Use this to sign the user out of the Firebase CLI and Firebase MCP server. |
| firebase_validate_security_rules | core | Use this to check Firebase Security Rules for Firestore, Storage, or Realtime Database for syntax and validation errors. |
| firebase_get_project | core | Use this to retrieve information about the currently active Firebase Project. |
| firebase_list_apps | core | Use this to retrieve a list of the Firebase Apps registered in the currently active Firebase project. Firebase Apps can be iOS, Android, or Web. |
| firebase_list_projects | core | Use this to retrieve a list of Firebase Projects that the signed-in user has access to. |
| firebase_get_sdk_config | core | Use this to retrieve the Firebase configuration information for a Firebase App. You must specify EITHER a platform OR the Firebase App ID for a Firebase App registered in the currently active Firebase Project. |
| firebase_create_project | core | Use this to create a new Firebase Project. |
| firebase_create_app | core | Use this to create a new Firebase App in the currently active Firebase Project. Firebase Apps can be iOS, Android, or Web. |
| firebase_create_android_sha | core | Use this to add the specified SHA certificate hash to the specified Firebase Android App. |
| firebase_get_environment | core | Use this to retrieve the current Firebase **environment** configuration for the Firebase CLI and Firebase MCP server, including current authenticated user, project directory, active Firebase Project, and more. |
| firebase_update_environment | core | Use this to update environment config for the Firebase CLI and Firebase MCP server, such as project directory, active project, active user account, accept terms of service, and more. Use `firebase_get_environment` to see the currently configured environment. |
| firebase_init | core | Use this to initialize selected Firebase services in the workspace (Cloud Firestore database, Firebase Data Connect, Firebase Realtime Database, Firebase AI Logic). All services are optional; specify only the products you want to set up. You can initialize new features into an existing project directory, but re-initializing an existing feature may overwrite configuration. To deploy the initialized features, run the `firebase deploy` command after `firebase_init` tool. |
| firebase_get_security_rules | core | Use this to retrieve the security rules for a specified Firebase service. If there are multiple instances of that service in the product, the rules for the defualt instance are returned. |
| firebase_read_resources | core | Use this to read the contents of `firebase://` resources or list available resources |
| firestore_delete_document | firestore | Use this to delete a Firestore documents from a database in the current project by full document paths. Use this if you know the exact path of a document. |
| firestore_get_documents | firestore | Use this to retrieve one or more Firestore documents from a database in the current project by full document paths. Use this if you know the exact path of a document. |
| firestore_list_collections | firestore | Use this to retrieve a list of collections from a Firestore database in the current project. |
| firestore_query_collection | firestore | Use this to retrieve one or more Firestore documents from a collection is a database in the current project by a collection with a full document path. Use this if you know the exact path of a collection and the filtering clause you would like for the document. |
| auth_get_users | auth | Use this to retrieve one or more Firebase Auth users based on a list of UIDs or a list of emails. |
| auth_update_user | auth | Use this to disable, enable, or set a custom claim on a specific user's account. |
| auth_set_sms_region_policy | auth | Use this to set an SMS region policy for Firebase Authentication to restrict the regions which can receive text messages based on an ALLOW or DENY list of country codes. This policy will override any existing policies when set. |
| dataconnect_build | dataconnect | Use this to compile Firebase Data Connect schema, operations, and/or connectors and check for build errors. |
| dataconnect_list_services | dataconnect | Use this to list existing local and backend Firebase Data Connect services |
| dataconnect_execute | dataconnect | Use this to execute a GraphQL operation against a Data Connect service or its emulator. |
| storage_get_object_download_url | storage | Use this to retrieve the download URL for an object in a Cloud Storage for Firebase bucket. |
| messaging_send_message | messaging | Use this to send a message to a Firebase Cloud Messaging registration token or topic. ONLY ONE of `registration_token` or `topic` may be supplied in a specific call. |
| functions_get_logs | functions | Use this to retrieve a page of Cloud Functions log entries using Google Cloud Logging advanced filters. |
| remoteconfig_get_template | remoteconfig | Use this to retrieve the specified Firebase Remote Config template from the currently active Firebase Project. |
| remoteconfig_update_template | remoteconfig | Use this to publish a new remote config template or roll back to a specific version for the project |
| crashlytics_create_note | crashlytics | Add a note to an issue from crashlytics. |
| crashlytics_delete_note | crashlytics | Delete a note from a Crashlytics issue. |
| crashlytics_get_issue | crashlytics | Gets data for a Crashlytics issue, which can be used as a starting point for debugging. |
| crashlytics_list_events | crashlytics | Use this to list the most recent events matching the given filters. Can be used to fetch sample crashes and exceptions for an issue, which will include stack traces and other data useful for debugging. |
| crashlytics_batch_get_events | crashlytics | Gets specific events by resource name. Can be used to fetch sample crashes and exceptions for an issue, which will include stack traces and other data useful for debugging. |
| crashlytics_list_notes | crashlytics | Use this to list all notes for an issue in Crashlytics. |
| crashlytics_get_report | crashlytics | Use this to request numerical reports from Crashlytics. The result aggregates the sum of events and impacted users, grouped by a dimension appropriate for that report. |
| crashlytics_update_issue | crashlytics | Use this to update the state of Crashlytics issue. |
| apphosting_fetch_logs | apphosting | Use this to fetch the most recent logs for a specified App Hosting backend. If `buildLogs` is specified, the logs from the build process for the latest build are returned. The most recent logs are listed first. |
| apphosting_list_backends | apphosting | Use this to retrieve a list of App Hosting backends in the current project. An empty list means that there are no backends. The `uri` is the public URL of the backend. A working backend will have a `managed_resources` array that will contain a `run_service` entry. That `run_service.service` is the resource name of the Cloud Run service serving the App Hosting backend. The last segment of that name is the service ID. `domains` is the list of domains that are associated with the backend. They either have type `CUSTOM` or `DEFAULT`. Every backend should have a `DEFAULT` domain. The actual domain that a user would use to conenct to the backend is the last parameter of the domain resource name. If a custom domain is correctly set up, it will have statuses ending in `ACTIVE`. |
| realtimedatabase_get_data | realtimedatabase | Use this to retrieve data from the specified location in a Firebase Realtime Database. |
| realtimedatabase_set_data | realtimedatabase | Use this to write data to the specified location in a Firebase Realtime Database. |

### Resources

The MCP server provides resources, which are documentation files intended for
use by LLMs. Models that support using resources will automatically include
relevant resources in the session context.

The following table describes the resources the MCP server makes available.

> [!NOTE]
> **Note:** You can also see this information using the command:   
> `npx firebase-tools@latest mcp --generate-resource-list`

| Resource Name | Description |
|---|---|
| app_id_guide | Firebase App Id Guide: guides the coding agent through choosing a Firebase App ID in the current project |
| crashlytics_investigations_guide | Firebase Crashlytics Investigations Guide: Guides the coding agent when investigating bugs reported in Crashlytics issues, including procedures for diagnosing and fixing crashes. |
| crashlytics_issues_guide | Firebase Crashlytics Issues Guide: Guides the coding agent when working with Crashlytics issues, including prioritization rules and procedures for diagnosing and fixing crashes. |
| crashlytics_reports_guide | Firebase Crashlytics Reports Guide: Guides the coding agent through requesting Crashlytics reports, including setting appropriate filters and how to understand the metrics. The agent should read this guide before requesting any report. |
| backend_init_guide | Firebase Backend Init Guide: guides the coding agent through configuring Firebase backend services in the current project |
| ai_init_guide | Firebase GenAI Init Guide: guides the coding agent through configuring GenAI capabilities in the current project utilizing Firebase |
| data_connect_init_guide | Firebase Data Connect Init Guide: guides the coding agent through configuring Data Connect for PostgreSQL access in the current project |
| firestore_init_guide | Firestore Init Guide: guides the coding agent through configuring Firestore in the current project |
| firestore_rules_init_guide | Firestore Rules Init Guide: guides the coding agent through setting up Firestore security rules in the project |
| rtdb_init_guide | Firebase Realtime Database Init Guide: guides the coding agent through configuring Realtime Database in the current project |
| auth_init_guide | Firebase Authentication Init Guide: guides the coding agent through configuring Firebase Authentication in the current project |
| hosting_init_guide | Firebase Hosting Deployment Guide: guides the coding agent through deploying to Firebase Hosting in the current project |
| docs | Firebase Docs: loads plain text content from Firebase documentation, e.g. `https://firebase.google.com/docs/functions` becomes `firebase://docs/functions` |