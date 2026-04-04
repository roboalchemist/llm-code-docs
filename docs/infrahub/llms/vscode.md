# Source: https://docs.infrahub.app/vscode.md

# VSCode Extension

Welcome to the comprehensive documentation for the Infrahub VSCode Extension. This extension transforms Visual Studio Code into a powerful development environment for working with [Infrahub](https://docs.infrahub.app), the open-source infrastructure automation platform.

## What is the Infrahub VSCode extension?[​](#what-is-the-infrahub-vscode-extension "Direct link to What is the Infrahub VSCode extension?")

The Infrahub VSCode Extension provides intelligent tooling that connects directly to your Infrahub servers, enabling you to develop infrastructure schemas, execute GraphQL queries, run Jinja2 and Python transforms, and manage branch-based workflows without leaving your IDE. It brings the power of Infrahub's graph database and version control directly into your development workflow.

## Documentation structure[​](#documentation-structure "Direct link to Documentation structure")

This documentation is organized following the [Diataxis framework](https://diataxis.fr/) to help you find exactly what you need:

### 🎓 Tutorials[​](#-tutorials "Direct link to 🎓 Tutorials")

**Learning-oriented** - Start here if you're new to the extension

* [Getting Started with Infrahub VSCode Extension](/vscode/tutorials/getting-started.md) - Complete walkthrough from installation to first query

### 📋 How-to guides[​](#-how-to-guides "Direct link to 📋 How-to guides")

**Task-oriented** - Practical steps for specific goals

* [How to Configure Multiple Infrahub Servers](/vscode/guides/configure-multiple-servers.md) - Set up dev, staging, and production environments
* [How to Execute GraphQL Queries](/vscode/guides/execute-graphql-queries.md) - Run queries with variables and branch selection
* [How to Run Transforms and Artifacts](/vscode/guides/running-transforms.md) - Execute Jinja2 and Python transforms with automatic command selection
* [How to Manage Branches](/vscode/guides/manage-branches.md) - Create, delete, and work with branches
* [How to use Infrahub Snippets](/vscode/guides/snippets.md) - Insert and customize Infrahub YAML and automation snippets

### 💡 Topics[​](#-topics "Direct link to 💡 Topics")

**Understanding-oriented** - Explanations and background

* [Understanding the Extension Architecture](/vscode/topics/extension-architecture.md) - Deep dive into how the extension works
* [Schema Validation and YAML Intelligence](/vscode/topics/schema-validation.md) - How intelligent editing and validation work

### 📚 Reference[​](#-reference "Direct link to 📚 Reference")

**Information-oriented** - Technical descriptions and specifications

* [Extension Commands and Settings Reference](/vscode/reference/commands-settings.md) - Complete list of commands, settings, and configuration options

## Quick start[​](#quick-start "Direct link to Quick start")

If you want to get up and running quickly:

1. **Install the extension** from the VSCode Marketplace
2. **Configure a server** in your VSCode settings
3. **Create a schema** file in your project
4. **Execute a query** to test your connection

For detailed instructions, see the [Getting Started tutorial](/vscode/tutorials/getting-started.md).

## Key features at a glance[​](#key-features-at-a-glance "Direct link to Key features at a glance")

### 🔗 Multi-server management[​](#-multi-server-management "Direct link to 🔗 Multi-server management")

Connect to multiple Infrahub instances simultaneously, perfect for working across development, staging, and production environments.

### 🌳 Visual tree views[​](#-visual-tree-views "Direct link to 🌳 Visual tree views")

Navigate your infrastructure configuration with intuitive tree views for servers, branches, and YAML structures.

### 📝 Intelligent Yaml editing[​](#-intelligent-yaml-editing "Direct link to 📝 Intelligent Yaml editing")

Get real-time validation, auto-completion, and go-to-definition support for your Infrahub schemas.

### ✂️ Snippets for automation and YAML objects[​](#️-snippets-for-automation-and-yaml-objects "Direct link to ✂️ Snippets for automation and YAML objects")

Quickly scaffold Infrahub transforms, scripts, generators, checks, and YAML objects using built-in VSCode snippets.

### 🚀 GraphQL integration[​](#-graphql-integration "Direct link to 🚀 GraphQL integration")

Execute queries directly from VSCode with variable support and formatted results display.

### 🔀 Branch management[​](#-branch-management "Direct link to 🔀 Branch management")

Create and manage branches for version-controlled infrastructure changes.

### 📊 Real-time status[​](#-real-time-status "Direct link to 📊 Real-time status")

Monitor server connections with live status updates in the VSCode status bar.

## Use cases[​](#use-cases "Direct link to Use cases")

The extension is designed for several key workflows:

* **Schema Development**: Design and validate infrastructure models with immediate feedback
* **Query Testing**: Develop and test GraphQL queries against live data
* **Branch Workflows**: Manage infrastructure changes across multiple branches
* **Multi-Environment Development**: Work seamlessly across different Infrahub environments
* **Infrastructure Automation**: Build automation workflows with validated schemas

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before using the extension, ensure you have:

* Visual Studio Code version 1.99.0 or higher
* Access to at least one Infrahub server (local or remote)
* Basic familiarity with YAML and GraphQL (helpful but not required)

## Getting help[​](#getting-help "Direct link to Getting help")

### Within the extension[​](#within-the-extension "Direct link to Within the extension")

* **Problems Panel** (`Ctrl+Shift+M`): View validation errors and warnings
* **Output Panel**: Check extension logs for debugging
* **Command Palette** (`Ctrl+Shift+P`): Search for Infrahub commands

### External resources[​](#external-resources "Direct link to External resources")

* **Infrahub Documentation**: [docs.infrahub.app](https://docs.infrahub.app)
* **Extension Repository**: [GitHub.com/opsmill/infrahub-vscode](https://github.com/opsmill/infrahub-vscode)
* **Issue Tracker**: [GitHub Issues](https://github.com/opsmill/infrahub-vscode/issues)
* **Community Support**: [Infrahub Discord](https://discord.gg/infrahub)

## Common tasks[​](#common-tasks "Direct link to Common tasks")

### First time setup[​](#first-time-setup "Direct link to First time setup")

Start with the [Getting Started tutorial](/vscode/tutorials/getting-started.md) for a complete walkthrough.

### Working with multiple environments[​](#working-with-multiple-environments "Direct link to Working with multiple environments")

See [How to Configure Multiple Servers](/vscode/guides/configure-multiple-servers.md) for setting up dev, staging, and production.

### Testing queries[​](#testing-queries "Direct link to Testing queries")

Learn query execution in [How to Execute GraphQL Queries](/vscode/guides/execute-graphql-queries.md).

### Understanding how it works[​](#understanding-how-it-works "Direct link to Understanding how it works")

Explore [Understanding the Extension Architecture](/vscode/topics/extension-architecture.md) for technical details.

## Contributing[​](#contributing "Direct link to Contributing")

We welcome contributions to both the extension and its documentation! Visit our [GitHub repository](https://github.com/opsmill/infrahub-vscode) to:

* Report bugs or request features
* Submit pull requests
* Improve documentation

## Version information[​](#version-information "Direct link to Version information")

* **Current Extension Version**: 0.0.2
* **Minimum VSCode Version**: 1.99.0
* **Recommended Infrahub Version**: 0.15.0+

## License[​](#license "Direct link to License")

The Infrahub VSCode Extension is part of the Infrahub project. See the [LICENSE](https://github.com/opsmill/infrahub-vscode/blob/main/LICENSE) file for details.

***

*Built with ❤️ by the [OpsMill](https://opsmill.com) team and the Infrahub community.*
