# Source: https://firebase.google.com/docs/cli/mcp-server.md.txt

<br />

You can use the [Firebase MCP server](https://github.com/firebase/firebase-tools/tree/master/src/mcp) to give AI-powered development tools the
ability to work with your Firebase projects. The Firebase MCP server works with
any tool that can act as an MCP client, including Claude Desktop, Cline, Cursor,
Visual Studio Code Copilot, Windsurf Editor, and more.

An editor configured to use the Firebase MCP server can use its AI capabilities
to help you:

- Create and manage Firebase projects
- Manage your Firebase Authentication users
- Work with data in Cloud Firestore and Firebase Data Connect
- Retrieve Firebase Data Connect schemas
- Understand your security rules for Firestore and Cloud Storage for Firebase
- Send messages with Firebase Cloud Messaging

Some of the tools use Gemini in Firebase to help you:

- Generate Firebase Data Connect schema and operations
- Consult Gemini about Firebase products

| **Important:** Gemini in Firebase can generate output that seems plausible but is factually incorrect. It may respond with inaccurate information that doesn't represent Google's views. Validate all output from Gemini before you use it and don't use untested generated code in production. Don't enter personally-identifiable information (PII) or user data into the chat. For more information, see [Gemini in Google Cloud and responsible AI](https://cloud.google.com/gemini/docs/discover/responsible-ai).   
|
| Learn more about [Gemini in Firebase and how it uses your data](https://firebase.google.com/docs/gemini-in-firebase#how-gemini-in-firebase-uses-your-data).

These are only partial lists; see the [server capabilities](https://firebase.google.com/docs/cli/mcp-server#capabilities)
section for a complete list of tools available to your editor.

When the Firebase MCP server makes tool calls, it uses the same user
credentials that authorize the Firebase CLI in the environment where it's
running. This could be a logged-in user or
[Application Default Credentials](https://cloud.google.com/docs/authentication/application-default-credentials)
, depending on the environment.

## Before you begin

Make sure you have a working installation of Node.js and npm.

## Set up your MCP client

The Firebase MCP server can work with any MCP client that supports standard I/O
(stdio) as the transport medium.

### Basic configuration

In this section, you can find specific instructions for some popular
AI-assistive tools:

- [Firebase Studio](https://firebase.google.com/docs/cli/mcp-server#firebase-studio)
- [Gemini CLI and Gemini Code Assist](https://firebase.google.com/docs/cli/mcp-server#gemini-cli)
- [Claude Code](https://firebase.google.com/docs/cli/mcp-server#claude-code)
- [Claude Desktop](https://firebase.google.com/docs/cli/mcp-server#claude-desktop)
- [Cline](https://firebase.google.com/docs/cli/mcp-server#cline)
- [Cursor](https://firebase.google.com/docs/cli/mcp-server#cursor)
- [Visual Studio Code Copilot](https://firebase.google.com/docs/cli/mcp-server#vs-code-copilot)
- [Windsurf Editor](https://firebase.google.com/docs/cli/mcp-server#windsurf)

#### Firebase Studio

To configure Firebase Studio to use the Firebase MCP server, edit or
create the configuration file: `.idx/mcp.json`.

If the file doesn't yet exist, create it by right-clicking the parent
directory and selecting **New file**. Add the following contents to the file:  

    {
      "mcpServers": {
        "firebase": {
          "command": "npx",
          "args": ["-y", "firebase-tools@latest", "experimental:mcp"]
        }
      }
    }

#### Gemini CLI and Gemini Code Assist

To configure Gemini CLI or Gemini Code Assist to use the Firebase MCP server, edit or
create the configuration file(s):

- In your project: `.gemini/settings.json`
- In your home directory: `~/.gemini/settings.json`

If the file doesn't yet exist, create it by right-clicking the parent
directory and selecting **New file**. Add the following contents to the file:  

    {
      "mcpServers": {
        "firebase": {
          "command": "npx",
          "args": ["-y", "firebase-tools@latest", "experimental:mcp"]
        }
      }
    }

#### Claude Code

To configure Claude Code to use the Firebase MCP server, run the following
command under your app folder:  

    claude mcp add firebase npx -- -y firebase-tools@latest experimental:mcp

You can verify the installation by running:  

    claude mcp list

It should show:  

    firebase: npx -y firebase-tools@latest experimental:mcp - â Connected

#### Claude Desktop

To configure Claude Desktop to use the Firebase MCP server, edit the
`claude_desktop_config.json` file. You can open or create this file from the
**Claude \> Settings** menu. Select the **Developer** tab, then click
**Edit Config**.  

    {
      "mcpServers": {
        "firebase": {
          "command": "npx",
          "args": ["-y", "firebase-tools@latest", "experimental:mcp"]
        }
      }
    }

#### Cline

To configure Cline to use the Firebase MCP server, edit the
`cline_mcp_settings.json` file. You can open or create this file by clicking the
MCP Servers icon at the top of the Cline pane, then clicking the
**Configure MCP Servers** button.  

    {
      "mcpServers": {
        "firebase": {
          "command": "npx",
          "args": ["-y", "firebase-tools@latest", "experimental:mcp"],
          "disabled": false
        }
      }
    }

#### Cursor

To configure Cursor to use the Firebase MCP server, edit either the file
`.cursor/mcp.json` (to configure only a specific project) or the file
`~/.cursor/mcp.json` (to make the MCP server available in all projects):  

    "mcpServers": {
      "firebase": {
        "command": "npx",
        "args": ["-y", "firebase-tools@latest", "experimental:mcp"]
       }
    }

#### Visual Studio Code Copilot

To configure a single project, edit the `.vscode/mcp.json` file in your
workspace:  

    "servers": {
      "firebase": {
        "type": "stdio",
        "command": "npx",
        "args": ["-y", "firebase-tools@latest", "experimental:mcp"]
      }
    }

To make the server available in every project you open, edit your [user
settings](https://code.visualstudio.com/docs/getstarted/personalize-vscode):  

    "mcp": {
      "servers": {
        "firebase": {
          "type": "stdio",
          "command": "npx",
          "args": ["-y", "firebase-tools@latest", "experimental:mcp"]
        }
      }
    }

#### Windsurf Editor

To configure Windsurf Editor, edit the file
`~/.codeium/windsurf/mcp_config.json`:  

    "mcpServers": {
      "firebase": {
        "command": "npx",
        "args": ["-y", "firebase-tools@latest", "experimental:mcp"]
      }
    }

### Optional configuration

In addition to the basic configuration for each client, shown earlier, there are
two optional parameters you can specify:

- `--dir `<var translate="no">ABSOLUTE_DIR_PATH</var>: The absolute path of a
  directory containing `firebase.json`, to set a project context for the MCP
  server. If unspecified, the `get_project_directory` and
  `set_project_directory` tools become available and the default directory will
  be the working directory where the MCP server was started.

- `--only `<var translate="no">FEATURE_1</var>`,`<var translate="no">FEATURE_2<var translate="no"></var></var>: A
  comma-separated list of feature groups to activate. Use this to limit the
  tools exposed to only features you are actively using. Note that the core
  tools are always available

For example:  

    "firebase": {
      "command": "npx",
      "args": [
        "-y",
        "firebase-tools@latest", "experimental:mcp",
        "--dir", "/Users/turing/my-project",
        "--only", "auth,firestore,storage"
      ]
    }

## MCP server capabilities

The following table lists the tools the MCP server makes available. You can also
see this information using the command:  

    npx firebase-tools@latest experimental:mcp --generate-tool-list

|               Tool Name                | Feature Group |                                                                                                                                                                                                                                                                                                                                                                                            Description                                                                                                                                                                                                                                                                                                                                                                                            |
|----------------------------------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| firebase_login                         | core          | Logs the user into the Firebase CLI and MCP server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| firebase_logout                        | core          | Log the CLI out of Firebase                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| firebase_get_project                   | core          | Retrieves information about the currently active Firebase project.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| firebase_list_apps                     | core          | Retrieves apps registered in the current Firebase project.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| firebase_get_admin_sdk_config          | core          | Gets the Admin SDK config for the current project.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| firebase_list_projects                 | core          | Retrieves a list of Firebase projects up to the specified total count.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| firebase_get_sdk_config                | core          | Retrieves the Firebase SDK configuration information for the specified platform. You must specify either a platform or an app_id.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| firebase_create_project                | core          | Creates a new Firebase project.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| firebase_create_app                    | core          | Creates a new app in your Firebase project for Web, iOS, or Android.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| firebase_create_android_sha            | core          | Adds a SHA certificate hash to an existing Android app.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| firebase_consult_assistant             | core          | Access an AI assistant specialized in all aspects of **Firebase** . Use this tool to get **detailed information** , **best practices** , **troubleshooting steps** , **code examples** , and **contextual help** regarding Firebase services, features, and project configuration. This includes questions about Firestore, Authentication, Cloud Functions, Hosting, Storage, Analytics, and more. It can also provide insights based on the **current Firebase project context**.                                                                                                                                                                                                                                                                                                               |
| firebase_get_environment               | core          | Retrieves information about the current Firebase environment including current authenticated user, project directory, active project, and more.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| firebase_update_environment            | core          | Updates Firebase environment config such as project directory, active project, active user account, and more. Use `firebase_get_environment` to see the currently configured environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| firebase_init                          | core          | Initializes selected Firebase features in the workspace (Firestore, Data Connect, Realtime Database). All features are optional; provide only the products you wish to set up. You can initialize new features into an existing project directory, but re-initializing an existing feature may overwrite configuration. To deploy the initialized features, run the `firebase deploy` command after `firebase_init` tool.                                                                                                                                                                                                                                                                                                                                                                         |
| firestore_delete_document              | firestore     | Deletes a Firestore documents from a database in the current project by full document paths. Use this if you know the exact path of a document.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| firestore_get_documents                | firestore     | Retrieves one or more Firestore documents from a database in the current project by full document paths. Use this if you know the exact path of a document.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| firestore_list_collections             | firestore     | Retrieves a list of collections from a Firestore database in the current project.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| firestore_query_collection             | firestore     | Retrieves one or more Firestore documents from a collection is a database in the current project by a collection with a full document path. Use this if you know the exact path of a collection and the filtering clause you would like for the document.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| firestore_get_rules                    | firestore     | Retrieves the active Firestore security rules for the current project.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| firestore_validate_rules               | firestore     | Checks the provided Firestore Rules source for syntax and validation errors. Provide EITHER the source code to validate OR a path to a source file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| auth_get_user                          | auth          | Retrieves a user based on an email address, phone number, or UID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| auth_disable_user                      | auth          | Disables or enables a user based on a UID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| auth_list_users                        | auth          | Retrieves all users in the project up to the specified limit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| auth_set_claim                         | auth          | Sets a custom claim on a specific user's account. Use to create trusted values associated with a user e.g. marking them as an admin. Claims are limited in size and should be succinct in name and value. Specify ONLY ONE OF `value` or `json_value` parameters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| auth_set_sms_region_policy             | auth          | Sets an SMS Region Policy for Firebase Auth to restrict the regions which can receive text messages based on an ALLOW or DENY list of country codes. This policy will override any existing policies when set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| dataconnect_build                      | dataconnect   | Use this to compile Firebase Data Connect schema, operations, and/or connectors and check for build errors.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| dataconnect_generate_schema            | dataconnect   | Generates a Firebase Data Connect Schema based on the users description of an app.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| dataconnect_generate_operation         | dataconnect   | Generates a single Firebase Data Connect query or mutation based on the currently deployed schema and the provided prompt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| dataconnect_list_services              | dataconnect   | List existing local and backend Firebase Data Connect services                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| dataconnect_execute                    | dataconnect   | Executes a GraphQL operation against a Data Connect service or its emulator.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| storage_get_rules                      | storage       | Retrieves the active Storage security rules for the current project.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| storage_validate_rules                 | storage       | Checks the provided Storage Rules source for syntax and validation errors. Provide EITHER the source code to validate OR a path to a source file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| storage_get_object_download_url        | storage       | Retrieves the download URL for an object in Firebase Storage.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| messaging_send_message                 | messaging     | Sends a message to a Firebase Cloud Messaging registration token or topic. ONLY ONE of `registration_token` or `topic` may be supplied in a specific call.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| remoteconfig_get_template              | remoteconfig  | Retrieves a remote config template for the project                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| remoteconfig_publish_template          | remoteconfig  | Publishes a new remote config template for the project                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| remoteconfig_rollback_template         | remoteconfig  | Rollback to a specific version of Remote Config template for a project                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| crashlytics_add_note                   | crashlytics   | Add a note to an issue from crashlytics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| crashlytics_delete_note                | crashlytics   | Delete a note from an issue in Crashlytics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| crashlytics_get_issue_details          | crashlytics   | Gets the details about a specific crashlytics issue.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| crashlytics_get_sample_crash_for_issue | crashlytics   | Gets the sample crash for an issue.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| crashlytics_list_notes                 | crashlytics   | List all notes for an issue in Crashlytics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| crashlytics_list_top_devices           | crashlytics   | List the top devices from Crashlytics for an application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| crashlytics_list_top_issues            | crashlytics   | List the top crashes from crashlytics happening in the application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| crashlytics_list_top_operating_systems | crashlytics   | List the top operating systems from Crashlytics for an application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| crashlytics_list_top_versions          | crashlytics   | List the top versions from Crashlytics for an application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| crashlytics_update_issue               | crashlytics   | Update the state of an issue in Crashlytics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| apphosting_fetch_logs                  | apphosting    | Fetches the most recent logs for a specified App Hosting backend. If `buildLogs` is specified, the logs from the build process for the latest build are returned. The most recent logs are listed first.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| apphosting_list_backends               | apphosting    | Retrieves a list of App Hosting backends in the current project. An empty list means that there are no backends. The `uri` is the public URL of the backend. A working backend will have a `managed_resources` array that will contain a `run_service` entry. That `run_service.service` is the resource name of the Cloud Run service serving the App Hosting backend. The last segment of that name is the service ID. `domains` is the list of domains that are associated with the backend. They either have type `CUSTOM` or `DEFAULT`. Every backend should have a `DEFAULT` domain. The actual domain that a user would use to conenct to the backend is the last parameter of the domain resource name. If a custom domain is correctly set up, it will have statuses ending in `ACTIVE`. |
| database_get_data                      | database      | Returns RTDB data from the specified location                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| database_set_data                      | database      | Writes RTDB data to the specified location                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| database_get_rules                     | database      | Get an RTDB database's rules                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| database_validate_rules                | database      | Validates an RTDB database's rules                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |