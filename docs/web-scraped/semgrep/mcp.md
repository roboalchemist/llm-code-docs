# Semgrep MCP Server (beta)

Source: https://semgrep.dev/docs/mcp

- [](/docs/)- Set up and deploy scans- Integrations- MCP Server**On this page- [MCP](/docs/tags/mcp)- [Semgrep Code](/docs/tags/semgrep-code)Semgrep MCP Server (beta)
Semgrep&#x27;s open source [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server scans AI-generated code for security vulnerabilities using Semgrep Code, Supply Chain, and Secrets. The IDE re-generates code until Semgrep returns no findings or the user prompts the IDE to ignore Semgrep&#x27;s findings.

This article includes instructions for setting up the MCP server with Cursor and Claude Code, but it also works with any IDE-based MCP client.

## Prerequisites[​](#prerequisites)

- Python 3.10 or later
- Homebrew or Pip to install Semgrep
- A Semgrep account

## Installation[​](#installation)
- Cursor- Claude Code- Other IDEs
- 
Install Semgrep:

`# install through homebrewbrew install semgrep# install through pippython3 -m pip install semgrep`

- 
Verify that you&#x27;ve installed the [latest version](https://github.com/semgrep/semgrep/releases) of Semgrep by running the following:

`semgrep --version`

- 
Log in to Semgrep and install Semgrep Pro

`semgrep login &amp;&amp; semgrep install-semgrep-pro`

- 
[Add Semgrep to Cursor](cursor://anysphere.cursor-deeplink/mcp/install?name=semgrep&amp;config=eyJjb21tYW5kIjoic2VtZ3JlcCBtY3AifQ%3D%3D). Review the prefilled information and click **Install** to proceed.

- 
Create a `hooks.json` file in your project&#x27;s `.cursor` directory and paste the following configuration:

`{&quot;version&quot;: 1,&quot;hooks&quot;: {    &quot;stop&quot;: [    {        &quot;command&quot;: &quot;semgrep mcp -k stop-cli-scan -a cursor&quot;    }    ],    &quot;afterFileEdit&quot;: [    {        &quot;command&quot;: &quot;semgrep mcp -k record-file-edit -a cursor&quot;    }    ]}}`

- 
Install Semgrep:

`# install through homebrewbrew install semgrep# install through pippython3 -m pip install semgrep`

- 
Verify that you&#x27;ve installed the [latest version](https://github.com/semgrep/semgrep/releases) of Semgrep by running the following:

`semgrep --version`

- 
Sign in to your Semgrep account. Running this command launches a browser window, but you can also use the link that&#x27;s returned in the CLI to proceed:

`semgrep login`
In the **Semgrep CLI login**, click **Activate** to proceed.

- 
Return to the CLI, and install the Semgrep Pro engine:

`semgrep install-semgrep-pro`

- 
Add the Semgrep MCP Server to Claude:

`claude mcp add --scope user semgrep semgrep mcp`

- 
Install Semgrep:

`# install through homebrewbrew install semgrep# install through pippython3 -m pip install semgrep`

- 
Verify that you&#x27;ve installed the [latest version](https://github.com/semgrep/semgrep/releases) of Semgrep by running the following:

`semgrep --version`

- 
Sign in to your Semgrep account. Running this command launches a browser window, but you can also use the link that&#x27;s returned in the CLI to proceed:

`semgrep login`
In the **Semgrep CLI login**, click **Activate** to proceed.

- 
Return to the CLI, and install the Semgrep Pro engine:

`semgrep install-semgrep-pro`

- 
Add the Semgrep MCP Server to your IDE. Semgrep provides [sample configuration information](https://github.com/semgrep/semgrep/tree/develop/cli/src/semgrep/mcp#integrations) that you can use as a starting point for your configuration. Refer to your IDE’s documentation for specific details on where to add the MCP server configuration information.

## Scan your code[​](#scan-your-code)

- Open up your IDE&#x27;s AI chat window.
- Ensure that you&#x27;re in the correct context to use Semgrep.
- Prompt your IDE to scan with Semgrep.

By default, the MCP Server runs all three Semgrep products: Code, Supply Chain, and Secrets.

## Additional resources[​](#additional-resources)

- Semgrep&#x27;s `#mcp` [Slack community](https://go.semgrep.dev/slack)
- The [Semgrep MCP server repo on GitHub](https://github.com/semgrep/semgrep/tree/develop/cli/src/semgrep/mcp)
Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

Tags:**- [MCP](/docs/tags/mcp)- [Semgrep Code](/docs/tags/semgrep-code)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/mcp.md)Last updated on **Dec 22, 2025**