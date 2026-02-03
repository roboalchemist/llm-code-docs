# Source: https://docs.sonarsource.com/sonarqube-for-vs-code/ai-capabilities/ides/cursor.md

# SonarQube for VS Code in Cursor

### Installation

The SonarQube for VS Code extension can easily be installed in Cursor from either the [Open VSX registry](https://open-vsx.org/extension/SonarSource/sonarlint-vscode) or by using Cursor’s [VS Code Migration](https://cursor.com/docs/configuration/migrations/vscode) tools.

To install the SonarQube for VS Code extension in Cursor:

1. Open the **Extensions** view by pressing `Ctrl + Shift + X` (or `Cmd + Shift + X` on Mac).
2. Search for `sonarqube`.
3. Finish the installation by selecting the **Install** button

Once installed, we recommended using [connected mode](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/setup) and setting up the [#sonarqube-mcp-server](#sonarqube-mcp-server "mention") with SonarQube Server or SonarQube Cloud to strengthen your AI integration with SonarQube.

#### Migrate extensions from VS Code

Cursor provides a workflow to [import your VS Code settings](https://cursor.com/docs/configuration/migrations/vscode), including your extensions.

If you were using connected mode or the [#sonarqube-mcp-server](#sonarqube-mcp-server "mention"), your SonarQube token will not be migrated but you will be prompted to reauthenticate any connections you created in VS Code.

{% hint style="info" %}
Cursor subscribers on their Enterprise plan should add SonarQube for VS Code to the list of allowed extensions. Please see the Cursor documentation to [Configure (your) allowed extensions](https://docs.cursor.com/en/account/teams/enterprise-settings#configure-allowed-extensions).
{% endhint %}

### SonarQube MCP Server

The SonarQube MCP Server is a Model Context Protocol (MCP) server that runs locally and enables a seamless connection between your AI agents and your SonarQube platform. The tools are designed to bridge the divide between productivity and quality. Please see the full details in the [SonarQube MCP Server](https://app.gitbook.com/o/2ibCvzwZt86Nlk2zloB7/s/xNksbUaDXyfRoTpHP0vQ/ "mention") documentation.

See the [Quickstart guide #Setup in Cursor](https://app.gitbook.com/s/xNksbUaDXyfRoTpHP0vQ/quickstart-guide#setup-in-cursor "mention") instructions in our SonarQube MCP Server documentation for full details.

#### Setup the SonarQube MCP Server

When you're using an AI-enabled IDE such as Cursor, Windsurf, or VS Code with Copilot enabled, and have already completed your [setup](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/setup "mention") in SonarQube for IDE with SonarQube Server or SonarQube Cloud, a quick select button is available.

* Select the <picture><source srcset="https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fr6Pesg2GVz7SeQGNl4hz%2Fmcp-dark-mode.png?alt=media&#x26;token=7ded2e19-d4ad-4017-a03d-42eee4abe3f4" media="(prefers-color-scheme: dark)"><img src="https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fgit-blob-0401b61efd30b446650d936aeba51a5fd7e33b62%2Fmcp-optimized.svg?alt=media" alt="" data-size="line"></picture> icon, **Configure MCP Server** from the **CONNECTED MODE** view window to use your connected mode credentials to start using the SonarQube MCP Server. The same workflow is available in the **AI AGENTS CONFIGURATION** view.

<div align="left"><figure><img src="https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2FV9bolpWxercO0dxqWUBf%2Fsq-vscode-mcp-automatic-setup-cursor.png?alt=media&#x26;token=d3a0f909-8578-41bf-806e-9e512fd54177" alt="Select the MCP Server icon and use your connected mode credentials to populate the MCP environment variables." width="375"><figcaption></figcaption></figure></div>

If you prefer to set up your MCP server manually, a detailed quickstart guide is available for [Quickstart guide #Setup in Cursor](https://app.gitbook.com/s/xNksbUaDXyfRoTpHP0vQ/quickstart-guide#setup-in-cursor "mention"). More information about the available tools can be found in the SonarQube MCP Server documentation, on the [Tools](https://app.gitbook.com/s/xNksbUaDXyfRoTpHP0vQ/tools "mention") page.

#### Configure your AI agent

The **AI AGENTS CONFIGURATION** view is only available when running an AI-enabled agent and offers two tools to help your AI agent engage with SonarQube (Server, Cloud).

* Select **Configure SonarQube MCP Server** to use your connected mode credentials to install the SonarQube MCP Server. You will be prompted to complete your [setup](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/setup "mention") if none exists.
* Available in Cursor, Kiro, and Windsurf: Select **Introduce SonarQube Rules File** to create explicit instructions for your AI-powered IDE to produce secure, reliable, and maintainable code.
  * The file provides SonarQube MCP Server instructions to your AI agent. As an example, it instructs the agent to disable SonarQube automatic analysis before starting code generation, and to enable it after the generation is complete. It also asks the agent to analyze changed files in batches, once the changes are done.

### Related pages

* [ai-codefix](https://docs.sonarsource.com/sonarqube-for-vs-code/ai-capabilities/ai-codefix "mention")
* SonarQube and [agents](https://docs.sonarsource.com/sonarqube-for-vs-code/ai-capabilities/agents "mention") in your IDE
* Getting started with other [ides](https://docs.sonarsource.com/sonarqube-for-vs-code/getting-started/ides "mention")
* [setup](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/setup "mention")
