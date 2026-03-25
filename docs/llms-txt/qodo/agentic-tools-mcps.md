# Source: https://docs.qodo.ai/qodo-documentation/qodo-gen/tools-mcps/agentic-tools-mcps.md

# Agentic Tools (MCPs)

Agentic Tools (MCPs) allow you to integrate external tools and services into Qodo IDE plugin. This enables Qodo to access and use custom tools when needed.

<figure><img src="https://782320861-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FhllduvO2nHKZ2vKzfcEn%2Fuploads%2F6hWXLwaOHmmci5Wt8HoH%2FScreenshot%202025-05-21%20at%2014.53.04.png?alt=media&#x26;token=c0c2c34f-028f-45b7-b7af-3c5cef17e9f8" alt="" width="563"><figcaption></figcaption></figure>

***

## Requirements

You will need [Node.js](https://nodejs.org/) installed in order to run tools properly.

To verify you have Node installed, open the command line on your computer.

* On macOS, open the Terminal from your Applications folder
* On Windows, press Windows + R, type “cmd”, and press Enter

Once in the command line, verify you have Node installed by entering in the following command:

```bash
node --version
```

If you get an error saying “command not found” or “node is not recognized”, download Node from [nodejs.org](https://nodejs.org/).

Learn more on why Node.js is required in [Anthropic's official MCP documentation](https://modelcontextprotocol.io/quickstart/user#2-add-the-filesystem-mcp-server).

***

## Agentic Tools Configuration

{% hint style="info" %}
**Note:** If you're an Enterprise user, you may be unable to add new Agentic Tools if your system administrator has restricted additions in the **Agentic Tools Allow List**.
{% endhint %}

In order to create a tool and add it to Qodo, you need the applicable MCP server configuration.

**Qodo supports two types of MCPs:**

1. **Local MCPs**\
   These run directly in your environment and don’t require network calls. Ideal for internal tools or logic that doesn’t rely on external APIs.
2. **Remote MCPs (SSE MCPs)**\
   These are hosted externally and communicate via HTTP. When setting up a Remote MCP, you'll provide a URL, and optionally, you can add custom HTTP headers (e.g., for authentication).

### 1. Local MCPs

The configuration for a local MCP is usually in JSON form. For example, the [GitHub MCP server configuration](https://github.com/modelcontextprotocol/servers) is:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-github"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "<YOUR_TOKEN>"
      }
    }
  }
}
```

You can find many MCP tools and setup options in the [MCP GitHub](https://github.com/modelcontextprotocol/servers/blob/main/README.md).

### 2. Remote (SSE) MCPs

We recommend using SSE MCPs, especially in Enterprise environments. They are easier to manage, more secure and ideal for external services like Jira. Also, if you're setting up an **Allow List** in your Enterprise environment, we recommend enabling SSE-based MCPs for a smoother and more secure user experience.

The SSE MCPs configuration relies on a URL.

To configure this type of tool, add the following as to the Agentic Tools configuration text box:

```json
{
    "semgrep": {
        "url": "https://mcp.semgrep.ai/sse"
    }
}
```

***

## Create a new Agentic Tool

Once you've got your [required MCP configuration](#agentic-tools-configuration), you can create a new Agentic Tool for Qodo's Agent to use:

1. **Open Qodo chat**\
   [Learn more about Agentic Mode and what it does.](https://docs.qodo.ai/qodo-documentation/qodo-gen/tools-mcps/broken-reference)
2. **Go to the Tools Management page**

   Click on **Add new tools.**

<figure><img src="https://782320861-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FhllduvO2nHKZ2vKzfcEn%2Fuploads%2FgO5U70TybraBa014E3w5%2FScreenshot%202025-07-14%20at%2017.26.13.png?alt=media&#x26;token=96bea660-c700-49a2-aedd-055a2e8f382e" alt="" width="375"><figcaption></figcaption></figure>

3. **Create a New Tool**\
   Click **Add new MCP** button at the top left of the tools management page.

<figure><img src="https://782320861-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FhllduvO2nHKZ2vKzfcEn%2Fuploads%2F9nziL2RtriQpxPfMYo90%2FScreenshot%202025-04-28%20at%2010.34.19.png?alt=media&#x26;token=d10d0938-d8d6-44ab-a1e5-7c0a6b2c475f" alt="" width="375"><figcaption></figcaption></figure>

4. **Enter Tool Configuration Details**\
   Paste a JSON configuration script to configure your new tool. [Learn more about tools configuration](#agentic-tools-configuration).

<figure><img src="https://782320861-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FhllduvO2nHKZ2vKzfcEn%2Fuploads%2FP5dn9UbVBUVXfjMSXWhN%2FScreenshot%202025-04-23%20at%2013.02.44.png?alt=media&#x26;token=1dddca6f-5bbd-467b-9d4c-af014e5b1f7f" alt="" width="300"><figcaption></figcaption></figure>

5. **Save and Test**\
   Save your configuration.

* &#x20;**A green dot** will indicate a successful connection.
  * A list of sub-tools will appear under the tool, indicating all the services this tool is capable of. You can toggle all sub-tools on or off.
  * Clicking on **Auto approve** will let you set if the use of the sub-tool will be automatically approved for every use in-chat.
  * You can turn sub-tools on or off by pressing the toggle button.

<figure><img src="https://782320861-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FhllduvO2nHKZ2vKzfcEn%2Fuploads%2FyvTvL5kFjUka86iroppJ%2FScreenshot%202025-04-28%20at%2010.36.04.png?alt=media&#x26;token=35cd8d7d-7cd9-4f94-9939-a51d42d9b37e" alt="" width="375"><figcaption></figcaption></figure>

* **A yellow dot** indicates a problem with your connection. Try checking your configuration and API keys and make sure you've set them all correctly.

<figure><img src="https://782320861-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FhllduvO2nHKZ2vKzfcEn%2Fuploads%2FzoSguRV9qxxl5gRqChWP%2Fimage.png?alt=media&#x26;token=38ad0b7a-ddec-4a87-b3a3-54a44b326db0" alt="" width="375"><figcaption></figcaption></figure>

6. **Modify or Delete:**\
   You can edit or remove a tool as needed. **Some of the built-in tools, like Code Navigation, cannot be edited.**

<figure><img src="https://782320861-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FhllduvO2nHKZ2vKzfcEn%2Fuploads%2FRFjURO8PdJ9iECplcHfL%2FScreenshot%202025-04-28%20at%2010.37.54.png?alt=media&#x26;token=6454f3a7-01f0-49aa-ab17-d634a8255d3a" alt="" width="375"><figcaption></figcaption></figure>

## Remove or Manage Tools

You can scroll through all connected tools in the tools management page.

<figure><img src="https://782320861-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FhllduvO2nHKZ2vKzfcEn%2Fuploads%2FzVp8btXVfOJEnYuUwyN7%2FScreenshot%202025-07-14%20at%2017.26.13.png?alt=media&#x26;token=036b6ffe-ffec-455b-9bd1-1e3161f9eba0" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="https://782320861-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FhllduvO2nHKZ2vKzfcEn%2Fuploads%2F6hWXLwaOHmmci5Wt8HoH%2FScreenshot%202025-05-21%20at%2014.53.04.png?alt=media&#x26;token=c0c2c34f-028f-45b7-b7af-3c5cef17e9f8" alt="" width="375"><figcaption></figcaption></figure>

You can enable, disable, or modify the configuration of tools at any time. Click the **pen and note symbol** next to a custom tool's toggle button to modify a tool's configuration.

<figure><img src="https://782320861-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FhllduvO2nHKZ2vKzfcEn%2Fuploads%2FjDgcBMDwZFdxVrevQ7V6%2FScreenshot%202025-04-28%20at%2010.40.41.png?alt=media&#x26;token=48c5338b-3b44-48b2-96d0-b81171734baf" alt="" width="375"><figcaption></figcaption></figure>

Toggling a tool off will disable Qodo from using it.

<figure><img src="https://782320861-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FhllduvO2nHKZ2vKzfcEn%2Fuploads%2FsLyiO6kl9doHDl1lg96D%2FScreenshot%202025-04-28%20at%2010.41.36.png?alt=media&#x26;token=d86d7b4f-88d7-4d8e-afb8-0ed7daea4a48" alt="" width="375"><figcaption></figcaption></figure>

See the number of available tools any time at the bottom of Qodo Chat, under the chatbox. Clicking on it displays a list of available tools.

<figure><img src="https://782320861-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FhllduvO2nHKZ2vKzfcEn%2Fuploads%2Fc79hRc42yX7BCEWY9kpt%2FScreenshot%202025-05-21%20at%2015.02.50.png?alt=media&#x26;token=7ba176f0-e788-420c-8700-e0ab44d0b444" alt="" width="375"><figcaption></figcaption></figure>

### Manage sub-tools

Click the small arrow next to a tool's name to open a list of sub-tools, indicating all the services this tool is capable of.

You can toggle all sub-tools on or off, and set whether your approval is needed for their use.

<figure><img src="https://782320861-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FhllduvO2nHKZ2vKzfcEn%2Fuploads%2FUavrbHm1iLfPmzi4nVPi%2FScreenshot%202025-04-28%20at%2010.42.16.png?alt=media&#x26;token=c7c748e3-aa5f-4b2a-a160-f80522be866c" alt="" width="375"><figcaption></figcaption></figure>

## Troubleshooting

**A yellow dot** near the tool's name indicates a problem with your connection.

Try checking your configuration and API keys and make sure you've set them all correctly. Also, ensure your internet connection is stable.

<figure><img src="https://782320861-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FhllduvO2nHKZ2vKzfcEn%2Fuploads%2Fc0ZezAQjJRcl48s0B52Z%2FScreenshot%202025-03-27%20at%2011.16.28.png?alt=media&#x26;token=5b1d8e57-c336-44df-b3ff-518947d04aaa" alt="" width="375"><figcaption></figcaption></figure>

***

## Agentic Tools Allow List

{% hint style="info" %}
This feature is only available for Enterprise users.
{% endhint %}

The **Agentic Tools Allow List** feature enables enterprise organizations to enforce stricter governance over Agentic Tools usage in Qodo.

When enabled, this mode restricts developers to using only a predefined set of tools defined at the organization level.

This feature is ideal for organizations requiring tight control over configuration parameters to comply with internal policies, reduce misconfigurations, and standardize environments across teams.

### Activation Flow

1. **Request Enablement**\
   An organization admin submits a request to Qodo Support to enable Agentic Tools Allow List mode.
2. **Allow List Configuration**\
   The Qodo DevOps team configures the organization's MCP allow list manually.

### Developer Behavior

Once MCP Allow List mode is active:

* ✅ **View Access:** Developers can view the organization-defined tools list upon their next login to Qodo.
* ✅ **Overrides Allowed:** Developers may override values for existing environment variables listed in the allow list.
* ❌ **No Custom Agentic Tools:** Developers **cannot** add new or custom tools outside the allow list.

<figure><img src="https://782320861-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FhllduvO2nHKZ2vKzfcEn%2Fuploads%2FWewHkHTNSe2Lzk0CzuTh%2FScreenshot%202025-06-16%20at%2010.55.11.png?alt=media&#x26;token=7eb641f4-a4dc-407e-beec-8cf93b1b51e2" alt="" width="375"><figcaption></figcaption></figure>
