# Source: https://docs.sonarsource.com/sonarqube-for-vs-code/ai-capabilities/agents.md

# AI agents

SonarQube for IDE’s code analysis workflow is enhanced by a set of tools designed to integrate with AI agents. These tools allow you to interact with AI agents in natural language to perform specific SonarQube-related tasks directly within your IDE. This integration streamlines your development process by bringing the power of SonarQube analysis into your AI-assisted conversations, helping you focus on and resolve code quality and security issues more efficiently.

### SonarQube MCP Server

The SonarQube MCP Server is a Model Context Protocol (MCP) server that runs locally and enables a seamless connection between your AI agents and your SonarQube platform. The tools are designed to bridge the divide between productivity and quality. Please see the full details in the [SonarQube MCP Server](https://app.gitbook.com/o/2ibCvzwZt86Nlk2zloB7/s/xNksbUaDXyfRoTpHP0vQ/ "mention") documentation.

Using SonarQube MCP Server together with the SonarQube for IDE plugin allows the MCP server to trigger analyses directly in the editor, just like regular on-the-fly analysis by SonarQube for IDE. This powerful combination helps AI agents deliver more reliable, maintainable, and secure code.

When you're using an AI-enabled IDE such as Cursor, Windsurf, or VS Code with Copilot enabled, and have already completed your [setup](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/setup "mention") in SonarQube for IDE with SonarQube Server or SonarQube Cloud, a quick select button is available.

* Select the <picture><source srcset="https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fr6Pesg2GVz7SeQGNl4hz%2Fmcp-dark-mode.png?alt=media&#x26;token=7ded2e19-d4ad-4017-a03d-42eee4abe3f4" media="(prefers-color-scheme: dark)"><img src="https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fgit-blob-0401b61efd30b446650d936aeba51a5fd7e33b62%2Fmcp-optimized.svg?alt=media" alt="" data-size="line"></picture> icon, **Configure MCP Server** from the **CONNECTED MODE** view window to use your connected mode credentials to start using the SonarQube MCP Server. The same workflow is available in the **AI AGENTS CONFIGURATION** view.

Once SonarQube MCP Server is configured in your AI Assisted IDE, select the **Create Instructions for AI** **agents** action (Cursor only) to generate a rules file in your workspace folder for the agent to use.

<div align="left"><figure><img src="https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fgit-blob-7f4dacaa9627569269caf237c91216c464d25d79%2Fsqvsc-mcp-server-create-instructions-for-ai.png?alt=media" alt="The Create instructions for AI agents action in SonarQube for VS Code."><figcaption></figcaption></figure></div>

This rule file contains instructions for the agent on how to effectively utilize SonarQube MCP Server. As an example, it instructs the agent to disable SonarQube automatic analysis before starting code generation, and to enable it after the generation is complete. It also asks the agent to analyze changed files in batches, once the changes are done.

### GitHub Copilot extension <a href="#github-copilot" id="github-copilot"></a>

SonarQube for VS Code includes tools for the GitHub Copilot extension in VS Code. The interactive tools come automatically with your [installation](https://docs.sonarsource.com/sonarqube-for-vs-code/getting-started/installation "mention") and are best accessed with the Copilot **Agent** mode enabled.

You can easily use SonarQube for VS Code’s tools within the GitHub Copilot extension. Simply call the SonarQube for IDE tools by name or ask Copilot to perform a SonarQube-related action using natural language. Either way, Copilot will recognize what you need and guide you by opening the right window or asking for any extra details.

#### SonarQube for IDE tools <a href="#sonarqube-for-ide-tools" id="sonarqube-for-ide-tools"></a>

* Security Hotspots
  * `#sonarqube_getSecurityHotspots`
  * Checks for security hotspots in your file. The tool takes a single file path as an argument.
* Exclude File or Folder from Analysis
  * `#sonarqube_excludeFiles`
  * Updates the SonarQube for IDE analysis settings to exclude files and folders using known [file-exclusions](https://docs.sonarsource.com/sonarqube-for-vs-code/using/file-exclusions "mention").
* Set up Connected Mode
  * `#sonarqube_setUpConnectedMode`
  * Copilot will walk you through the [setup](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/setup "mention") with SonarQube Server or Cloud. If you already have a shared setup, Copilot will open the UI to complete the process, or prompt you to choose Server or Cloud before beginning a new connection setup.
* Analyze File
  * `#sonarqube_analyzeFile`
  * Use this tool to analyze a file, including those you might have previously excluded.
