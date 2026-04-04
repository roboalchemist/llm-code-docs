# Source: https://docs.sonarsource.com/sonarqube-community-build/extension-guide/sonarqube-mcp-server.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/ai-capabilities/sonarqube-mcp-server.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/ai-capabilities/sonarqube-mcp-server.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/ai-capabilities/sonarqube-mcp-server.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/ai-capabilities/sonarqube-mcp-server.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/ai-capabilities/sonarqube-mcp-server.md

# Source: https://docs.sonarsource.com/sonarqube-server/ai-capabilities/sonarqube-mcp-server.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/ai-capabilities/sonarqube-mcp-server.md

# SonarQube MCP Server

{% hint style="info" %}
The SonarQube MCP Server is in Alpha release, see the [product-release-lifecycle](https://docs.sonarsource.com/sonarqube-cloud/appendices/product-release-lifecycle "mention") page for more information.
{% endhint %}

For complete details please see the [SonarQube MCP Server](https://app.gitbook.com/o/2ibCvzwZt86Nlk2zloB7/s/xNksbUaDXyfRoTpHP0vQ/ "mention") documentation.

### Overview <a href="#overview" id="overview"></a>

The SonarQube MCP Server is a [Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP) server that provides seamless integration with SonarQube Server or SonarQube Cloud for code quality and code security. It enables the analysis of code snippets directly within the agent context and allows you to retrieve information and perform actions on your SonarQube Server instance or SonarQube Cloud organization. Check the [SonarQube MCP Server #Prerequisites](https://app.gitbook.com/s/xNksbUaDXyfRoTpHP0vQ/#prerequisites "mention") for compatibility details.

Upon receiving a request from an MCP client, the SonarQube MCP Server calls the SonarQube Cloud or SonarQube Server API to perform actions:

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-6075b67bcbb29287b5c123c13be9d6e1098fbfad%2Fsonarqube-mcp-server-diagram.png?alt=media" alt="Overview of the SonarQube MCP Server setup."><figcaption></figcaption></figure></div>

### Setting up the SonarQube MCP Server <a href="#setting-up-the-sonarqube-server-with-docker" id="setting-up-the-sonarqube-server-with-docker"></a>

See the SonarQube MCP Server [Quickstart guide](https://app.gitbook.com/s/xNksbUaDXyfRoTpHP0vQ/quickstart-guide "mention") for the easiest way to get going.

### Tools <a href="#tools" id="tools"></a>

Once the SonarQube MCP server is connected, its tools become available. The current list of all tools available with the SonarQube MCP Server are listed on the [Tools](https://app.gitbook.com/s/xNksbUaDXyfRoTpHP0vQ/tools "mention") page.

For complete details please see [SonarQube MCP Server](https://app.gitbook.com/o/2ibCvzwZt86Nlk2zloB7/s/xNksbUaDXyfRoTpHP0vQ/ "mention")documentation.
