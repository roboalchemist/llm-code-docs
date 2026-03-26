# Source: https://docs.tabnine.com/main/administering-tabnine/managing-your-team/settings/agent-settings.md

# Source: https://docs.tabnine.com/main/getting-started/tabnine-agent/agent-settings.md

# In-IDE Agent Settings

## Tool Permissions

You can define which tools in Tabnine require user approval by using the **⚙︎** Settings → Tool Permissions → Native Tools panel.

To save time with Tabnine Agent, you can turn on **Auto-approve ▾** from a dropdown menu in Settings.

Navigate to the hamburger menu symbol (the three lines ≡), then:

* Go to **⛯ Settings**.
* Scroll down to and click **Tool Permissions ▾.**
* Finally, select **Native tools ▾**.

Here are the Native tools that will be available, complete with examples:

| Native Tool            | What It Does                                                                          | Example Usage                                         |
| ---------------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| Read Project Files     | Lets the Agent view code or documentation files to understand context.                | “Explain what this function does.”                    |
| Create Project Files   | Generates new files or directories with content.                                      | “Create a new `README.md` for my project.”            |
| Apply Code             | Writes or edits existing files based on your request.                                 | “Add input validation to the `login.js.` file”        |
| Read Terminal          | Reads command output to understand your environment.                                  | “What version of Node am I using?”                    |
| Run Command            | Executes terminal commands in your workspace.                                         | “Run npm install.” or “Run pytest.”                   |
| List Directory         | Lists files in a given folder for context.                                            | “Show me what’s inside /src/components.”              |
| Get Diagnostics        | Gathers environment or dependency info to debug issues.                               | “Run diagnostics. Check for missing Python packages.” |
| Local Workspace Search | Searches your workspace for code or text patterns.                                    | “Find all functions named fetchData.”                 |
| Search File Content    | Local code‑aware search that  Agent uses when answering queries or generating changes | "Search for API endpoints like /api/v1 or /api/v2"    |

For each tool, you can pick from the following options:

* <mark style="color:green;">**Auto-approve**</mark>
* <mark style="color:yellow;">**Ask first**</mark>
* <mark style="color:$info;">**Disable**</mark>

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-0c6aacae892e3a7b9fccf03cadcd6df1eb190426%2FTool%20Permissions.gif?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
It is recommended to require user approval for sensitive operations.

However, options like `Run Command` and `Apply Code` will frequently come up as options in Tabnine Agent. Depending on your needs, you might elect to auto-approve these prompts for quicker results.
{% endhint %}

###

### **Context Engine Tools**

In [5.26.0](https://docs.tabnine.com/main/administering-tabnine/release-notes#v5.26.0), we added the **Directory & Symbol Index**.&#x20;

This index includes new (or updated) search tools for navigating and finding resources in remote codebases (repositories, source code, folders, files, classes, functions, variables, etc.):

* `remote_repositories_list` - Lists all remote repositories available to your team
* `remote_symbols_search` - Searches for code symbols (functions, classes, variables) in remote repos by prefix
* `remote_symbol_content` - Gets complete source code content of symbols from remote repos
* `remote_repository_folder_tree` - Gets folder structure of a remote repo
* `remote_files_search` - Searches for files by path/name in remote repos
* `remote_file_content` - Fetches full content of specific files from remote repos
* `remote_semantic_and_textual_search` - \[previously called *`remote_codebase_search`*] Performs semantic RAG and lexical search across remote repos.&#x20;

### Add New MCP Servers

(Introduced [**5.26.0**](https://docs.tabnine.com/main/administering-tabnine/release-notes#v5.26.0))

Within the Tabnine IDE plugin, users can manage their MCP servers by adding new ones and configuring their permissions.&#x20;

To do this, navigate to the three-line menu symbol ☰, then select ⛭ Settings.&#x20;

Once there, select Tools and **MCPs ∨**, then select **MCP servers ∨**.&#x20;

Select the option **+ Add MCP server** and input the server’s information. This will open (and create if needed) the \``.tabnine\mcp_servers.json`\` file where you can configure the MCP servers.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FsmOIqv8jdOnf46PD7alC%2Funknown.png?alt=media&#x26;token=6d734080-cc91-4a87-9de6-cb55ad2189ab" alt=""><figcaption></figcaption></figure>

Once added, you will be able to select one of three options for handling results from each MCP server that is available:

* <mark style="color:green;">**Auto-approve**</mark>
* <mark style="color:yellow;">**Ask first**</mark>
* <mark style="color:$info;">**Disable**</mark>
